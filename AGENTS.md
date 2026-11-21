# Agent Skills Workspace

This repository is the source of truth for Marian's personal agent assets: skills, global guidance, harness settings, and the research behind them. One set serves Codex, Claude Code, Antigravity, and GitHub Copilot across macOS, Linux, and Windows. `research/` holds reference sheets with the evidence and rejected alternatives behind skills and guidance; read the matching sheet, if there is one, before changing what it covers.

Reusable assets in `skills/` and `context/` are authored content, not automatically active instructions. Follow a stored skill only when the user invokes it or the current task explicitly requires editing or testing that skill.

## Runtime wiring

On macOS and Linux, `install.sh` links runtime paths to this repository, so edits are live immediately; re-run it when skills are added or removed, shared settings in `context/` change, or `~/.agents/local.md` changes (Codex and Antigravity also need a re-run after `context/AGENTS.md` edits on machines that have `~/.agents/local.md`, since they get a generated combined file). Edit repository copies, not runtime paths. The Hetzner VPS (`agent` user, T3 Code over T3 Connect) runs `install.sh` hourly from cron, which also pulls.

On Windows, where links need admin rights, `install.ps1` copies the same assets (including `~/.copilot/copilot-instructions.md` and `~/.gemini/`) and must be re-run after changes; GitHub Copilot reads skills from `~/.agents/skills/`.

Machine-local constraints (such as VPS hardware, firewall, and sudo limits) live outside this repository in `~/.agents/local.md` on that machine only, so personal infrastructure never leaks onto the work laptop. When `~/.agents/local.md` exists, `install.sh` imports it in `~/.claude/CLAUDE.md` and writes combined `~/.codex/AGENTS.md` and `~/.gemini/AGENTS.md` files, and `install.ps1` appends it to all four guidance files.

| Asset | Codex | Claude Code | Antigravity |
| --- | --- | --- | --- |
| `skills/*` | symlinked into `~/.agents/skills/` | symlinked into `~/.claude/skills/` | symlinked into `~/.gemini/config/skills/` |
| `context/AGENTS.md` | `~/.codex/AGENTS.md` symlinks to it (or combines with `~/.agents/local.md`) | `~/.claude/CLAUDE.md` imports it (and `~/.agents/local.md` if present) | `~/.gemini/AGENTS.md` symlinks to it (or combines with `~/.agents/local.md`) |
| `context/codex-config.toml`, `context/claude-settings.json` | merged into `~/.codex/config.toml` | merged into `~/.claude/settings.json` | none |
| Explicit-only invocation (hides the description from the model, so only `$name` or `/name` triggers it) | `agents/openai.yaml` in the skill | `disable-model-invocation: true` in frontmatter (Copilot reads it too) | none |

`context/chat.md` is the chat-tailored counterpart of `context/AGENTS.md` for ChatGPT and claude.ai. Paste it manually into each service's personal instructions; keep shared preferences aligned with `context/AGENTS.md` while preserving differences between chat and agent work.

`skills/shaping` is also uploaded to claude.ai as a personal skill, for chat. Upload it again after editing it; nothing syncs that copy. claude.ai syncs its skills into Claude Code as `anthropic-skills:<name>`, which would list shaping twice, so `context/claude-settings.json` switches the synced copy off. Use the prefixed name there: a bare `shaping` key switches off both copies.

## Vendored skills

`skills/frontend-design` is Anthropic's skill, copied verbatim from `anthropics/claude-plugins-official` (`plugins/frontend-design/skills/frontend-design`, commit `44490cc`, 2026-09-01) so Codex can use it too; keep the Claude plugin of the same name disabled. Do not edit it here. To update, diff upstream against the copy and re-copy `SKILL.md` and `LICENSE.txt`, then bump the commit above.

## Authoring skills and guidance

These are Marian's personal skills, not a public library. They can rely on `context/AGENTS.md` and name T3 Code or harness tools directly when that prevents improvisation.

- Keep skills short and concrete (roughly 200 to 500 words). Prefer short imperative paragraphs (1 to 3 sentences) and flat bullets for distinct rules over dense multi-clause essays.
- Write down what a model would otherwise get wrong: authority boundaries, harness quirks, caps, and output formats. Skip textbook engineering advice models already follow.
- Avoid pinning minor model version numbers that rot; name model families (Opus, Sol, Neon) when routing matters.
- Descriptions say when to load the skill, not what it does: situations, phrases, and boundaries where a neighboring request could misfire. An agent that reads a summary of the action thinks it already knows the skill and skips it ([check-work sheet](research/check-work-reference-sheet.md#trigger-only-description-2026-10-01)). Phrase-triggered skills must stay model-invocable.
- No em dashes in skills or guidance; use a comma, colon, semicolon, parentheses, or a new sentence. Vendored skills keep their upstream text.
- Keep `SKILL.md` frontmatter to Agent Skills spec fields (plus `disable-model-invocation`, which Codex ignores). Quote any value that contains `: `.
- Add supporting files only when they materially improve execution. Keep `AGENTS.md` files focused on durable intent, non-obvious setup, and source of truth.
