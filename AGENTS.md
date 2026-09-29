# Agent Skills Workspace

This repository is the source of truth for Marian's reusable agent assets: personal skills, global guidance, and the research behind them. One set serves both Codex (GPT) and Claude Code.

Reusable assets in `skills/` and `context/` are authored content, not automatically active instructions. Follow a stored skill only when the user invokes it or the current task explicitly requires editing or testing that skill.

## Runtime wiring

Edits to canonical files are live immediately in both harnesses. Edit repository copies, not runtime paths.

| Asset | Codex | Claude Code |
| --- | --- | --- |
| `skills/*` | symlinked into `~/.agents/skills/` | symlinked into `~/.claude/skills/` |
| `context/AGENTS.md` | `~/.codex/AGENTS.md` symlinks to it | `~/.claude/CLAUDE.md` imports it |
| `.agents/skills/*` (project-local) | discovered directly | `.claude/skills/*` symlinks to it |
| Explicit-only invocation | `agents/openai.yaml` in the skill | `skillOverrides` in `~/.claude/settings.json` |

Do not export project-local skills to the global set unless requested.

## Writing for both models

Skills and guidance must work on both current model families and be shareable with colleagues:

- No model names in skills; per-harness settings belong in harness config.
- Name the failure to avoid and the target, rather than pushing in one direction; the models drift in opposite ways.
- Shared skills refer to "the user", not Marian, and must not depend on his personal global guidance.
- Keep `SKILL.md` frontmatter to Agent Skills spec fields so skills stay portable.

## Working style

Keep skills small and behavior-focused: steering and reasoning prompts, not prescribed flows. Give each skill a clear trigger, authority boundary, and distinct owner. Add supporting files only when they materially improve execution.

Keep `AGENTS.md` files focused on durable intent, non-obvious setup, and source of truth. Do not use them as long project documentation.
