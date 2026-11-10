# Evidence and testing reference

Operational facts learned on 2026-09-29; log formats rechecked on 2026-11-10. Verify CLI flags against `--help` if a command fails; harness versions change.

## Finding real use in session logs

Start with `scripts/usage.py`: it counts the sessions that loaded each skill on both harnesses, and `--skill NAME` lists them with their log paths for extraction. If its counts look wrong (a skill in daily use showing zero), a log format has changed again: check the notes below against a recent log, fix the script, and update the notes.

Shell note: `ls` and `grep` may be aliased (eza, ugrep). Use `/bin/ls` and `command grep`.

**Codex**: `~/.codex/sessions/YYYY/MM/DD/rollout-*.jsonl`, one JSON object per line. Codex compresses older logs to `.jsonl.zst` and keeps them; read those with `zstd -dc`. Searching only `*.jsonl` finds a handful of recent sessions and looks like no use.
- Line 1 is `session_meta`. `payload.cwd` gives the project; `payload.source` contains `subagent` for agents Codex spawned itself. Many files are subagents or forks of one conversation, so group them by parent.
- `type: "response_item"` with `payload.type`:
  - `message`: `payload.role` is user or assistant; text is in `payload.content[].text`.
  - tool calls: `custom_tool_call` named `exec`, with JavaScript calling `tools.exec_command(...)` in `payload.input`. Logs from before October 2026 use `function_call` with `payload.arguments`.
  - their outputs: `custom_tool_call_output` or `function_call_output`.
- Implicit skill use is a tool call that reads `<skill>/SKILL.md`. Every session's catalog lists every skill path, so grepping for the path alone is noise; filter to tool-call items.
- Explicit invocation is a user message containing `<skill><name>NAME</name>`.
- Tasks another harness delegated through T3 Code (`delegate_task`) are ordinary sessions here, not subagents: `payload.source` is `vscode`, the working directory is a T3 worktree, and the first user message is the brief, opening with "Act as the review sub-agent for this task." or another role. The reviewers a Claude Code author started are found this way, not under Claude Code's `subagents/`.
- Subagent briefs (`spawn_agent` message) are encrypted. `fork_turns` shows whether a subagent inherited the conversation (`all`) or started fresh (`none`).
- Files reach tens of MB. Extract with `jq` rather than reading whole files.

**Claude Code**: `~/.claude/projects/<escaped-cwd>/<session-id>.jsonl`.
- Skill use: an assistant `message.content[]` item with `type == "tool_use"`, `name == "Skill"`, and `input.skill`. A skill synced from claude.ai appears as `anthropic-skills:<name>`.
- A skill invoked as `/name` is expanded without a `Skill` tool call. It appears as a user message containing `<command-name>/name</command-name>`; counting only tool calls misses every explicit use.
- Some logs repeat lines; count a tool call once by its `id`.
- Subagent transcripts live under `<session-id>/subagents/`.
- Logs are deleted 30 days after their last change unless `cleanupPeriodDays` is raised in the settings, and the cleanup runs when the `claude` CLI starts, including the `claude -p` runs that probes make. Collect Claude Code evidence before running probes, and record the counts in the research sheet, since they cannot be reproduced later.

Fresh-context extraction agents need: the skill's purpose, the file list, the format notes above, the questions to answer per session, and a request for a per-session table plus at most 10 aggregate bullets with quoted evidence. Do not include the expected conclusion.

## Running probes

Both harnesses load the live global skills, which are symlinks to this repository. Run baseline and candidate sequentially: baseline runs first, then edit the canonical file and run the candidate. Keep fixtures under `/tmp`, identical except for the condition under test.

Use the scripts rather than hand-rolling runners; `--help` documents inputs. Both use each harness's configured default model unless `--claude-model` or `--codex-model` is given; choose the model in harness config, not per run.
- `scripts/probe.py`: for explicit-only skills, put the invocation in the turn (`/name` for Claude Code, `$name` for Codex) and run each harness separately with `--harness`; a slash-invoked skill is expanded without a `Skill` tool call, so the summary shows no load, and its session transcript under `~/.claude/projects/` confirms it. Runs each scenario's fixed turns on both harnesses in parallel. Writes clean transcripts for judges, raw per-turn logs, and a summary of reply length and skills loaded per turn. Check that summary: a probe proves nothing if the skill never loaded.
- `scripts/judge.py`: runs judges in the process's working directory; launch it from a clean fixture copy when judges should check claims against the code. Blind pairwise judging of two condition directories by judges from both families, with randomized A/B per pair and the key kept outside the prompt. Write the rubric from the agreed decisions; the script appends the verdict format.

Harness facts the scripts depend on, for when a CLI changes:
- Claude Code: `claude -p ... --session-id <uuid>` then `--resume <uuid>`, `--output-format stream-json --verbose`, stdin from `/dev/null` (otherwise a warning line precedes the JSON). The reply is `.result` on the `type == "result"` line; skill loads are `Skill` tool_use items.
- Codex: `codex exec ... -C <dir> --json` (the first line carries `thread_id`), then `codex exec resume <thread_id> ...` from the same directory. `-C` resolves relative to the process cwd, so pass absolute paths. The reply is every `agent_message` item in the turn joined in order; Codex may split one reply into several items. Skill loads are `command_execution` items reading a `SKILL.md`. `-o <file>` writes the final message, which suits single-turn judges. Subagent briefs appear only in `~/.codex/sessions`.

## What synthetic tests miss

- Small fixtures are often solvable without the skill.
- Scripted users never answer questions, which penalizes question-asking styles.
- Drift over long sessions, out-of-sight work, recording decisions too early, and fit with the user's real preferences only show in real use. Say so when reporting.
