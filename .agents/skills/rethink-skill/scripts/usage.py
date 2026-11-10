#!/usr/bin/env python3
"""Count real skill use in Claude Code and Codex session logs.

Without --skill, prints one row per skill: sessions that loaded it on each harness. With
--skill NAME, lists those sessions (date, harness, how it loaded, role, project, first user
message, log path) so they can be handed to extraction agents.

A load is a Skill tool call or a /name command in Claude Code, and a tool call reading
<name>/SKILL.md or an explicit <skill> mention in Codex. The catalog every session carries
is not counted. Roles: "sub" is a harness-spawned subagent; "delegated" is a Codex session
whose first message is a brief from another agent ("Act as the ... sub-agent"), which is
how T3 Code's delegated tasks appear. Sessions run under a temp directory are probes and
are skipped unless --include-tmp is given. Compressed Codex logs need the zstd binary.
"""
import argparse, collections, json, os, re, subprocess, sys
from pathlib import Path

SKILL_PATH = re.compile(r"skills/([a-z0-9-]+)/SKILL\.md")
SLASH = re.compile(r"<command-name>/([\w:-]+)</command-name>")
EXPLICIT = re.compile(r"<skill>\s*<name>([a-z0-9-]+)</name>")
BRIEF = re.compile(r"^Act as the [\w -]+sub-?agent")
TMP = ("/tmp/", "/private/tmp/", "/private/var/", "/var/folders/")


def text_of(content):
    if isinstance(content, str):
        return content
    return "\n".join(b.get("text", "") for b in content or [] if isinstance(b, dict) and "text" in b)


def claude_sessions(root, since):
    for path in root.glob("**/*.jsonl"):
        s = dict(harness="claude", path=str(path), date=None, cwd="", first="", loads={},
                 role="sub" if "subagents" in path.parts else "main")
        seen = set()
        for line in path.open(errors="replace"):
            if '"timestamp"' not in line:
                continue
            try:
                d = json.loads(line)
            except json.JSONDecodeError:
                continue
            s["date"] = s["date"] or d.get("timestamp", "")[:10]
            s["cwd"] = s["cwd"] or d.get("cwd", "")
            msg = d.get("message") or {}
            content = msg.get("content")
            if msg.get("role") == "assistant":
                for b in content if isinstance(content, list) else []:
                    if b.get("type") == "tool_use" and b.get("name") == "Skill" and b.get("id") not in seen:
                        seen.add(b.get("id"))  # some logs repeat lines
                        s["loads"].setdefault((b.get("input") or {}).get("skill", ""), "model")
            elif msg.get("role") == "user" and not d.get("isMeta"):
                text = text_of(content)
                m = SLASH.search(text)
                if m:  # a slash command expands the skill without a Skill tool call
                    s["loads"].setdefault(m.group(1), "explicit")
                elif text and not text.lstrip().startswith("<") and not s["first"]:
                    s["first"] = text
        if s["date"] and s["date"] >= since:
            yield s


def codex_lines(path):
    if path.suffix == ".zst":
        try:
            proc = subprocess.run(["zstd", "-dc", str(path)], capture_output=True)
        except FileNotFoundError:
            sys.exit("compressed Codex logs need the zstd binary on PATH")
        return proc.stdout.decode("utf-8", "replace").splitlines()
    return path.read_text(errors="replace").splitlines()


def codex_sessions(root, since):
    for path in list(root.glob("*/*/*/rollout-*.jsonl")) + list(root.glob("*/*/*/rollout-*.jsonl.zst")):
        date = "-".join(path.parts[-4:-1])
        if date < since:
            continue
        s = dict(harness="codex", path=str(path), date=date, cwd="", first="", loads={}, role="main")
        for line in codex_lines(path):
            if '"session_meta"' in line[:200] and not s["cwd"]:
                p = json.loads(line).get("payload") or {}
                s["cwd"] = p.get("cwd", "")
                if "subagent" in json.dumps(p.get("source")):
                    s["role"] = "sub"
            elif '"role":"user"' in line or '"role": "user"' in line:
                p = json.loads(line).get("payload") or {}
                if p.get("type") != "message":
                    continue
                text = text_of(p.get("content"))
                for name in EXPLICIT.findall(text):
                    s["loads"].setdefault(name, "explicit")
                if text and not text.lstrip().startswith(("<", "# AGENTS.md")) and not s["first"]:
                    s["first"] = text
            elif "SKILL.md" in line and '_call"' in line:
                p = json.loads(line).get("payload") or {}
                # function_call in older logs, custom_tool_call (named exec) in newer ones
                if str(p.get("type", "")).endswith("_call"):
                    for name in SKILL_PATH.findall(json.dumps(p)):
                        s["loads"].setdefault(name, "model")
        if s["role"] == "main" and BRIEF.match(s["first"].lstrip()):
            s["role"] = "delegated"
        yield s


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--since", default="0000-00-00", help="YYYY-MM-DD; sessions that started earlier are skipped")
    p.add_argument("--skill", help="list the sessions that loaded this skill")
    p.add_argument("--all", action="store_true", help="count every skill seen, not only this repository's")
    p.add_argument("--include-tmp", action="store_true", help="keep sessions run under a temp directory (probes)")
    p.add_argument("--claude-root", default="~/.claude/projects")
    p.add_argument("--codex-root", default="~/.codex/sessions")
    args = p.parse_args()

    repo = Path(__file__).resolve().parents[4]
    own = {d.name for base in ("skills", ".agents/skills") for d in (repo / base).glob("*/")}
    sessions = [*claude_sessions(Path(args.claude_root).expanduser(), args.since),
                *codex_sessions(Path(args.codex_root).expanduser(), args.since)]
    if not args.include_tmp:
        sessions = [s for s in sessions if not (s["cwd"] + "/").startswith(TMP)]
    for s in sessions:  # a synced or plugin copy counts as the skill it copies
        s["loads"] = {name.split(":")[-1]: how for name, how in s["loads"].items()}

    if args.skill:
        for s in sorted(sessions, key=lambda s: s["date"]):
            if args.skill in s["loads"]:
                first = " ".join(s["first"].split())[:70]
                print(f"{s['date']} {s['harness']:<6} {s['loads'][args.skill]:<8} {s['role']:<9} "
                      f"{Path(s['cwd']).name[:28]:<28} {first}\n    {s['path']}")
        return

    counts = collections.defaultdict(collections.Counter)
    for s in sessions:
        for name, how in s["loads"].items():
            if args.all or name in own:
                counts[name][f"{s['harness']} {s['role']}"] += 1
                counts[name][f"{s['harness']} explicit"] += how == "explicit"
    cols = ["claude main", "claude sub", "claude explicit", "codex main", "codex delegated", "codex sub", "codex explicit"]
    print(f"{len(sessions)} sessions since {args.since}; 'explicit' counts are included in the role columns")
    print(f"{'skill':<22}" + "".join(f"{c:>17}" for c in cols))
    for name in sorted(counts, key=lambda n: -sum(counts[n].values())):
        print(f"{name:<22}" + "".join(f"{counts[name][c]:>17}" for c in cols))
    for name in sorted(own - set(counts)):
        print(f"{name:<22}" + "".join(f"{0:>17}" for _ in cols))


if __name__ == "__main__":
    main()
