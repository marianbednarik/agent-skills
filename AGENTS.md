# Agent Skills Workspace

This repository is the source of truth for Marian's reusable agent assets: personal skills, global guidance, and the research behind them. One set serves both Codex (GPT) and Claude Code. `research/` holds reference sheets with the evidence and rejected alternatives behind skills and guidance; read the matching sheet, if there is one, before changing what it covers.

Reusable assets in `skills/` and `context/` are authored content, not automatically active instructions. Follow a stored skill only when the user invokes it or the current task explicitly requires editing or testing that skill.

## Runtime wiring

On macOS and Linux, `install.sh` links runtime paths to the repository, so edits are live immediately; re-run it when skills are added or removed or the shared settings in `context/` change. Edit repository copies, not runtime paths. The Hetzner VPS (`agent` user, T3 Code over T3 Connect) runs it hourly from cron, which also pulls. On Windows, where links need admin rights, `install.ps1` copies the same assets (plus `~/.claude/CLAUDE.md` and `~/.copilot/copilot-instructions.md`) and must be re-run after changes; GitHub Copilot reads skills from `~/.agents/skills/`.

| Asset | Codex | Claude Code |
| --- | --- | --- |
| `skills/*` | symlinked into `~/.agents/skills/` | symlinked into `~/.claude/skills/` |
| `context/AGENTS.md` | `~/.codex/AGENTS.md` symlinks to it | `~/.claude/CLAUDE.md` imports it |
| `context/codex-config.toml`, `context/claude-settings.json` | merged into `~/.codex/config.toml` | merged into `~/.claude/settings.json` |
| `.agents/skills/*` (project-local) | discovered directly | `.claude/skills/*` symlinks to it |
| Explicit-only invocation (hides the description from the model, so only `$name` or `/name` triggers it) | `agents/openai.yaml` in the skill | `disable-model-invocation: true` in frontmatter (Copilot reads it too) |

`context/chat.md` is the shared chat-tailored counterpart of `context/AGENTS.md` for ChatGPT and claude.ai. Paste it manually into each service's personal instructions or preferences; keep shared preferences aligned with `context/AGENTS.md` while preserving differences between chat and agent work.

Do not export project-local skills to the global set unless requested.

## Vendored skills

`skills/frontend-design` is Anthropic's skill, copied verbatim from `anthropics/claude-plugins-official` (`plugins/frontend-design/skills/frontend-design`, commit `44490cc`, 2026-09-01) so Codex can use it too; keep the Claude plugin of the same name disabled. Do not edit it here. To update, diff upstream against the copy and re-copy `SKILL.md` and `LICENSE.txt`, then bump the commit above.

## Writing for both models

Skills and guidance must work on both current model families and be shareable with colleagues:

- No model names in skills; per-harness settings belong in harness config. A harness's tool may be named as an example beside the generic instruction ("the harness's PR watch tool, such as T3 Code's `watch_pull_request`") when agents otherwise improvise around it.
- The description says when to load the skill, not what it does: the situations or phrases that call for it, and a boundary only where a neighboring request could misfire. An agent that reads a summary of the action thinks it already knows the skill and skips it ([check-work sheet](research/check-work-reference-sheet.md#trigger-only-description-2026-10-01)). For a skill triggered by a phrase, name the phrase and keep the skill model-invocable; explicit-only skills never see the phrase.
- A skill may hand a step to another skill by name, with a fallback for when it is not installed, so each skill still works when shared alone. Do not build mandatory chains.
- Name the failure to avoid and the target, rather than pushing in one direction; the models drift in opposite ways.
- Shared skills refer to "the user", not Marian, and must not depend on his personal global guidance.
- No em dashes in skills or guidance; use a comma, colon, semicolon, parentheses, or a new sentence. Vendored skills keep their upstream text.
- Keep `SKILL.md` frontmatter to Agent Skills spec fields so skills stay portable. The exception is `disable-model-invocation`, which Codex ignores. Quote any value that contains `: `.

## Working style

Keep skills small and behavior-focused: steering and reasoning prompts, not prescribed flows. Give each skill a clear trigger, authority boundary, and distinct owner. Add supporting files only when they materially improve execution.

Keep `AGENTS.md` files focused on durable intent, non-obvious setup, and source of truth. Do not use them as long project documentation.
