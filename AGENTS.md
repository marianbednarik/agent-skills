# Agent Skills Workspace

This repository is the source of truth for Marian's reusable agent assets:
personal skills, reusable context, and prompt patterns.

Reusable assets in `skills/` and `context/` are
authored content, not automatically active instructions. Follow a stored skill
only when the user invokes it or the current task explicitly requires editing
or testing that skill.

`.agents/skills/` contains project-local skills discovered by Codex for work in
this repository. Keep their canonical files there; do not export them to the
global skill set unless requested.

## Skill Sets

`skills/` is the primary skill set for Codex and the main source for ongoing
skill development. Its skill directories are symlinked into `~/.agents/skills`.

Edit repository copies rather than runtime symlinks.

## Instruction Sources

Canonical reusable Codex guidance lives under `context/`. Edit the repository
copy first. Sync a live runtime file such as `~/.codex/AGENTS.md` only when the
user explicitly asks for the live configuration to change.

## Working Style

Keep skills small and behavior-focused. Give each skill a clear trigger,
authority boundary, and distinct owner. Add supporting files only when they
materially improve execution.

Keep `AGENTS.md` files focused on durable intent, non-obvious setup, and source
of truth. Do not use them as long project documentation.
