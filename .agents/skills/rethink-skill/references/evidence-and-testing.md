# Evidence and testing reference

Operational facts learned on 2026-09-29. Verify CLI flags against `--help` if a command fails; harness versions change.

## Finding real use in session logs

Shell note: `ls` and `grep` may be aliased (eza, ugrep). Use `/bin/ls` and `command grep`.

**Codex**: `~/.codex/sessions/YYYY/MM/DD/rollout-*.jsonl`, one JSON object per line.
- Line 1 is `session_meta`. `payload.cwd` gives the project; `payload.source` contains `subagent` for spawned agents. Many files are subagents or forks of one conversation, so group them by parent.
- `type: "response_item"` with `payload.type`:
  - `message`: `payload.role` is user or assistant; text is in `payload.content[].text`.
  - `function_call`: `payload.name` plus `payload.arguments`. Often `exec_command`, or JavaScript calling `tools.exec_command(...)`.
  - `function_call_output`
- Implicit skill use is a tool call that reads `<skill>/SKILL.md`. Every session's catalog lists every skill path, so grepping for the path alone is noise; filter to `function_call` lines.
- Explicit invocation is a user message containing `<skill><name>NAME</name>`.
- Subagent briefs (`spawn_agent` message) are encrypted. `fork_turns` shows whether a subagent inherited the conversation (`all`) or started fresh (`none`).
- Files reach tens of MB. Extract with `jq` rather than reading whole files.

**Claude Code**: `~/.claude/projects/<escaped-cwd>/<session-id>.jsonl`.
- Skill use: an assistant `message.content[]` item with `type == "tool_use"`, `name == "Skill"`, and `input.skill`.
- Subagent transcripts live under `<session-id>/subagents/`.

Fresh-context extraction agents need: the skill's purpose, the file list, the format notes above, the questions to answer per session, and a request for a per-session table plus at most 10 aggregate bullets with quoted evidence. Do not include the expected conclusion.

## Running probes

Both harnesses load the live global skills, which are symlinks to this repository. Run baseline and candidate sequentially: baseline runs first, then edit the canonical file and run the candidate. Keep fixtures under `/tmp`, identical except for the condition under test.

**Claude Code**
- New session: `claude -p "<prompt>" --session-id <uuid> --output-format stream-json --verbose --permission-mode bypassPermissions < /dev/null`, run from the fixture directory.
- Later turns: `--resume <uuid>`.
- Without `< /dev/null` a warning line precedes the JSON, so filter with `command grep '^{'`.
- The reply is `.result` on the `type == "result"` line. Tool use appears in `type == "assistant"` lines.

**Codex**
- New session: `codex exec -m <model> -C <dir> -s workspace-write --skip-git-repo-check --json "<prompt>" < /dev/null`.
- The first line carries `thread_id`.
- Later turns: `codex exec resume <thread_id> -m <model> --skip-git-repo-check --json "<prompt>"`, run from the fixture directory.
- The final reply is the last `item.completed` event whose `item.type` is `agent_message`.
- Subagent calls and briefs appear only in the session file under `~/.codex/sessions`.

**Blind judges**
- Codex: `codex exec -m <model> -c model_reasoning_effort=high -s read-only ...`
- Claude: `claude -p "<prompt>" --output-format json < /dev/null | jq -r .result`
- Give each judge a rubric built from the agreed decisions. Randomize A/B per pair and keep the key outside the prompt.

## What synthetic tests miss

- Small fixtures are often solvable without the skill.
- Scripted users never answer questions, which penalizes question-asking styles.
- Drift over long sessions, out-of-sight work, recording decisions too early, and fit with the user's real preferences only show in real use. Say so when reporting.
