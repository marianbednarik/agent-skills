---
name: council
description: "Use when the user says \"council\", or asks for a multi-model review or second opinion from multiple models on a PR, diff, plan, or hard problem."
---

Get independent judgment from fresh reviewers, catch what you missed, and act on what matters without turning review into a loop or scope creep.

## Before starting

If the change is not yours (for example reviewing a colleague's or upstream PR), review only: report findings without editing files, pushing commits, or modifying the PR description.

For your own code change, fix known issues, address outstanding PR comments, and run relevant checks first. Give the council the updated implementation, not half-finished work. Skip fixes to code the user wants to discard or rethink.

## Picking delegates

- **In T3 Code:** Call `orchestrator_capabilities`, then use `delegate_task` in parallel from the trusted trio, each on its own provider: the latest **Opus** (Claude), **Sol** (Codex), and **Neon** (Antigravity) at high reasoning effort (or the nearest level offered). Skip your own model family so you get the other two independent families without spending extra usage on your own provider, unless the user explicitly names members to run. If a needed member is unavailable, report it instead of silently substituting.
- **Outside T3 Code** (Claude Code Desktop, Codex Desktop): Start 1 or 2 fresh-context subagents on the available harness, using your judgment on whether a second angle is worth the tokens (for example correctness and edge cases vs. architecture and simplicity). If no subagent tool is available, review it yourself and note that the review was not independent.

## Running the review

Give each delegate the request, diff or material, relevant guidance, and screenshots for UI changes. Keep review delegates read-only, and leave out your own verdict.

Do not wait idle. As each result arrives, check its findings against the code right away. Never edit files while a delegate is still reading the same checkout. If you need to work in parallel, commit a checkpoint first and start delegates with worktree isolation (`isolation: "worktree"` in T3 Code), since a new worktree holds only committed state.

## Weighing findings and rounds

Triage every finding yourself regardless of the reviewer's severity label. Fix real bugs, unmet requirements, and issues users will realistically hit. Decline unrealistic edge cases, style preferences, and unnecessary guards in one line. Prefer fixes that delete or narrow code, and fight scope creep.

For code reviews, ask each delegate for a score out of 10 and count each full pass as one round. Run another round only if fixes changed behavior or a real finding stayed open, handing delegates the earlier findings and what happened to each (fixed, declined, or disputed). Stop after 2 rounds (4 only for auth, stored data, or concurrency); a round with only minor findings ends early. Escalate still-disputed findings instead of looping.

## Reporting results

If the work is your own PR and the PR is open, put the score table in the PR description (edit the description; do not post a comment for it). Otherwise put it in your final reply, along with what was fixed, declined, and left disputed.

```markdown
## Council review

Rounds: 2

| Delegate | Round 1 | Round 2 |
| --- | --- | --- |
| Opus | 7/10 | 9/10 |
| Sol | 8/10 | 10/10 |
```

If a delegate gives no score, write `no score`. Do not invent one.
