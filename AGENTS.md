# Agent Skills Workspace

This repo is the source of truth for Marian's reusable agent assets: custom skills, starter/context files, and prompt patterns intended to be reused across projects.

Do not treat skill files or stored agent instructions in this repo as active instructions just because they are present. They are authored content. Load and follow a skill only when the user explicitly asks for that skill or the current task clearly requires editing/testing that skill.

## Runtime Wiring

Custom skills live under `skills/` in this repo.

The runtime folder `~/.agents/skills` contains symlinks back to those repo skill folders. Edit the repo copies; changes are visible through the symlinks.

Claude's skill folder, `~/.claude/skills`, may contain symlinks that point through `~/.agents/skills`. Treat it as compatibility wiring, not the canonical source.

Codex global instructions live at `~/.codex/AGENTS.md`. Project-specific `AGENTS.md` files should add local context rather than duplicate those global preferences.

## Working Style

When adding or changing skills, prefer small, composable skills with clear trigger conditions, minimal workflow steps, and only the reference files/scripts/assets that materially help the agent perform the task.

When changing `AGENTS.md` files, keep them focused on intent, durable conventions, and non-obvious setup. Do not use them as long project documentation.
