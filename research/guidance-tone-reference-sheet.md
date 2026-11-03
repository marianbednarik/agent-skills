# Guidance tone reference sheet

Scope: tone, personality, praise, and humor in `context/AGENTS.md` and `context/chat.md`.

## Trigger (2026-11-03)

A viral X post (Peter Steinberger, 2026-11) offered eight "SOUL.md" rules for the OpenClaw assistant: strong opinions with no "it depends", delete corporate-sounding rules, ban "Great question" openers, mandatory one-sentence brevity, natural humor, call out dumb moves, swearing when it lands, and a closing "assistant you'd want at 2am" line. Marián brainstorms with agents and wanted to know whether any of it would make them better to talk to. He wants less praise, not more, and swears himself.

## Decisions

Opus 5.5 and an independent GPT-6.1 Sol review (high effort, given the material without Opus's verdict) agreed item by item:

- Already covered in a better form: opinions (`chat.md` "Recommend a direction when the evidence supports one. Otherwise explain what the choice depends on"; the blanket ban invites faked confidence), calling things out ("Disagree plainly"), openers (`chat.md` skips preambles), brevity ("short by default"; an absolute collides with "enough to explain the approach to a colleague").
- Rejected: "delete corporate rules" (style is not purpose; nothing in the files is handbook filler) and the 2am line (no behavioral target; invites a companion persona).
- Adopted in `chat.md` only: humor and occasional swearing, not forced and not used for praise, plus drafted text matching its audience so swearing stays out of emails. The post's example "that's fucking brilliant" is intensified praise, the opposite of the target, so the line gives no examples. Agent output reaches colleagues through PRs, tickets, and commits, so `context/AGENTS.md` gets neither.
- Adopted in `chat.md`: skip praise and flattery, judge ideas on merit, and don't disagree just to seem independent. Both failures are named because an anti-glazing rule alone can overcorrect into invented objections. Sol proposed "be warm and direct"; "warm" was dropped as a one-direction push.
- Rejected: a global brainstorming line ("develop possibilities before pushing for a decision"); the shaping skill already owns this ("settling too early", "let unusual ideas develop before ranking them").

## Screen: anti-flattery line in `context/AGENTS.md`

Candidate (B): the `chat.md` anti-flattery line, placed before "Disagree plainly" in Working together. Baseline (A): `context/AGENTS.md` at `d5aa2ad`.

Method: 4 cases (a sound idea to swap a hand-rolled Postgres queue for pg-boss; a flawed Rust rewrite before a demo at 50 requests a day; a correct user correction of `prices.sort()`; a mixed idea of giving ops people the Supabase table editor instead of an admin UI) x 2 conditions x Opus 5.5 (`claude -p --setting-sources local`, no tools, guidance via `--append-system-prompt`) and GPT-6.1 Sol (`codex exec` with a temporary `CODEX_HOME` whose `AGENTS.md` was the condition) x 2 runs. Isolation was partial: Codex still saw globally installed skills. Two blind judges (Opus 5.5, GPT-6.1 Sol) compared each A/B pair in random order for flattery count, forced objections, calibration (1 to 5), and preference.

| Condition | Flattery phrases | Forced objections | Mean calibration | Preferred | Mean words |
| --- | --- | --- | --- | --- | --- |
| A | 0 | 2 | 4.47 | 13 | 305 |
| B | 0 | 1 | 4.59 | 9 | 309 |

Ties: 10 of 32 verdicts. The baseline never glazed: no "great idea" on the sound case, and the correction case opened with a plain "You're right" (or nothing) in both conditions. All three forced objections were single judge calls on Claude runs.

Decision: no change to `context/AGENTS.md`; there is no glazing for the line to fix. Revisit if real sessions show praise or "You're absolutely right" returning, for example after a model change. The `chat.md` lines are untested; watch whether humor reads as a performed persona and whether the anti-flattery line produces contrarian replies.
