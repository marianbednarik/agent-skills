# Agent Skills Workspace

This repository is the source of truth for Marian's reusable agent assets:
personal skills, reusable context, and prompt patterns.

Files in this repository are authored content, not automatically active
instructions. Follow a stored skill only when the user invokes it or the current
task explicitly requires editing or testing that skill.

## Skill Sets

`skills/` is the primary skill set for Codex and the main source for ongoing
skill development. Its skill directories are symlinked into `~/.agents/skills`.

`claude/skills/` contains secondary Claude Code adaptations. They are retained
as model-specific artifacts and may offer useful comparative wording, but they
are not authoritative for Codex. Do not mechanically synchronize either set
into the other.

Edit repository copies rather than runtime symlinks. Changes to one model's set
do not imply equivalent changes to the other.

## Instruction Sources

Canonical reusable Codex guidance lives under `context/`. Edit the repository
copy first. Sync a live runtime file such as `~/.codex/AGENTS.md` only when the
user explicitly asks for the live configuration to change.

Claude Code reads the root `CLAUDE.md`, which imports this file. Global Claude
guidance is deliberately separate from Codex guidance.

## Working Style

Keep skills small and behavior-focused. Give each skill a clear trigger,
authority boundary, and distinct owner. Add supporting files only when they
materially improve execution.

Keep `AGENTS.md` files focused on durable intent, non-obvious setup, and source
of truth. Do not use them as long project documentation.
