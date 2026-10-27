---
name: codebase-audit
description: Use when the user asks what to clean up or improve in a codebase or area, wants a periodic cleanup pass, or asks whether the code is in decent shape. Not for reviewing one change or diagnosing one bug.
---

Find what in the codebase is worth removing, simplifying, or fixing, and turn it into work the user can approve and hand off. An audit is judged by what gets done afterwards, not by how much it lists.

## What to look for

Weight that serves no present purpose. It piles up fastest when agents write the code, and survives review because each piece looks reasonable alone. Most costly first:
- the same logic written again where a helper or rule already exists, or one rule implemented in several places;
- layers, options, and abstractions with no second use;
- error handling that swallows or papers over failures, and guards for states that cannot occur;
- state kept in two places;
- components that own too many responsibilities, and competing patterns for one job;
- dead paths;
- tests that are slow, brittle, or check implementation rather than behavior;
- repeated or blocking work on paths users hit;
- docs and agent guidance that contradict the code.

Prefer structural changes (delete, merge, collapse a layer, move a rule to its owner) over renames and rewording. Serious correctness or security problems found along the way go first in the report, but the audit is not a bug hunt.

## Two ways to get it wrong

Over-flagging proposes churn: uniformity for its own sake, fewer lines as the goal, splitting what is cohesive, merging what only looks alike, rigor beyond what the rest of the project has, style a linter could catch, theoretical risks, undoing a deliberate choice. Under-flagging calls a skimmed codebase "mostly fine", or lists cosmetic nits while the structural cost goes unnamed. Keep a finding only if the user would plausibly act on it. An audit that finds little is a good result when it comes from a real look; say so plainly.

## Scope

Follow the requested scope. For a whole codebase, orient first: what the project is for, its main parts, and where change happens; history, churn, and file size are leads, not findings. Then go deep where cost concentrates. Where independent agents are available, split a broad sweep by area, each with a fresh context; separate passes find more than one pass does.

## Verify before reporting

Read the project's recorded decisions first. Something that looks like slop may be a deliberate choice; raise it only if the cost is real enough to reopen the decision, and say which decision. Verify each finding against the code: follow callers and consumers before proposing removal or consolidation, and drop findings that rest on naming or assumption. Do not drop a real concern just because some uncertainty remains; state it. Where practical, confirm behavior by running the tests, the build, or the app. For performance, waste visible in the code is a finding; a claim that it matters to users is a hypothesis until measured, so name the measurement that would settle it.

## Report

Lead with the verdict: the codebase's state in a few sentences and the first move you recommend. Then the findings worth acting on, each ready to become an issue:
- what and where, and what it costs today;
- the evidence;
- the concrete change, and how to confirm behavior is unchanged or improved;
- effort and risk.

Propose the change yourself; defer only when it truly needs the user's input. Merge symptoms with one cause into one change, keep each change small enough to land on its own, and order by payoff against effort and risk. Say briefly what is solid and should be left alone, what you inspected, and what you did not. Write in the project's own terms. Report in conversation, with diagrams where they clarify structure; write a file only when the user wants to keep or share it.

## After the report

Changing code or creating issues waits for the user's go-ahead. End with a concrete proposal, such as which findings to file and which to start with, not an open menu. Once approved, file each approved change as an issue in the project's tracker, or implement it if asked.
