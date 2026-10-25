#!/bin/sh
# Links the shared skills and global guidance for Codex and Claude Code on
# macOS and Linux, and merges the shared Claude Code settings. Links point into
# this checkout, so later edits and pulls are live without re-running; re-run
# when skills are added or removed, or the shared settings change.
#
#   ./install.sh
#
# Pulls the repository first. Existing links are replaced; real files and
# directories in the way are left alone with a warning. Links to skills removed
# from the repository are deleted.

set -eu
repo=$(cd "$(dirname "$0")" && pwd)

git -C "$repo" pull --ff-only -q 2>/dev/null || echo "warning: git pull failed; installing the current checkout." >&2

link() { # link <source> <target>
  if [ -L "$2" ] || [ ! -e "$2" ]; then
    mkdir -p "$(dirname "$2")"
    ln -sfn "$1" "$2"
    echo "  linked   $2"
  else
    echo "  skipped  $2 (exists and is not a link)" >&2
  fi
}

# Codex reads ~/.agents/skills; Claude Code reads only ~/.claude/skills.
echo "Skills"
for root in "$HOME/.agents/skills" "$HOME/.claude/skills"; do
  for skill in "$repo"/skills/*/; do
    link "${skill%/}" "$root/$(basename "$skill")"
  done
  for entry in "$root"/*; do
    case $(readlink "$entry" 2>/dev/null) in
      "$repo"/skills/*) [ -e "$entry" ] || { rm "$entry"; echo "  removed  $entry"; } ;;
    esac
  done
done

# Codex links the guidance file; Claude Code imports it so ~/.claude/CLAUDE.md
# can hold machine-specific notes below the import.
echo "Guidance"
link "$repo/context/AGENTS.md" "$HOME/.codex/AGENTS.md"
claude_md="$HOME/.claude/CLAUDE.md"
import="@$repo/context/AGENTS.md"
if grep -qs "^@.*/context/AGENTS\.md" "$claude_md"; then
  echo "  ok       $claude_md"
elif [ -e "$claude_md" ]; then
  echo "  skipped  $claude_md (add the line: $import)" >&2
else
  printf '%s\n%s\n' "<!-- Canonical source: $repo/context/AGENTS.md (shared with Codex). Edit it there. -->" "$import" > "$claude_md"
  echo "  wrote    $claude_md"
fi

# Claude Code also writes settings.json itself, so merge the shared keys in
# rather than linking; the repository owns those top-level keys, the rest stay.
echo "Claude settings"
python3 - "$repo/context/claude-settings.json" "$HOME/.claude/settings.json" <<'PY'
import json, os, sys
shared_path, target = sys.argv[1:]
with open(shared_path) as f:
    shared = json.load(f)
try:
    with open(target) as f:
        current = json.load(f)
except FileNotFoundError:
    current = {}
except ValueError:
    sys.exit(f"  skipped  {target} (not valid JSON)")
merged = {**current, **shared}
if merged == current:
    print(f"  ok       {target}")
else:
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w") as f:
        json.dump(merged, f, indent=2)
        f.write("\n")
    print(f"  merged   {target}")
PY
