---
name: codebase-audit
description: Use when the user asks what to clean up or improve in a codebase or area, wants a periodic cleanup pass, or asks whether the code is in decent shape. Not for reviewing one change or diagnosing one bug.
---

Find what is worth deleting, simplifying, or fixing structurally, and turn it into concrete work the user can approve. An audit is judged by what gets done afterward, not how long the list is.

## What matters most

Focus on weight that serves no present purpose and structure that makes every change harder than it should be (especially agent-accumulated sprawl where each piece looked fine alone):
- Duplicated rules, competing patterns for one job, components owning too many responsibilities, or state stored in two places.
- Single-use abstractions, pass-through wrappers, dead paths, and guards for impossible states.
- Swallowed errors, types or data shapes that allow invalid states, validation scattered through core logic, or dependencies violating layering.
- Hidden couplings (changes that must touch several files with nothing enforcing it) and outdated patterns that invite bad copy-paste.
- Repeated or blocking work on user-facing paths, brittle implementation-coupled tests, and docs or agent guidance that contradict the code.

Prefer structural fixes (delete, merge, collapse a layer, move a rule to its owner) over renames or rewording. Put serious correctness or security bugs first if found, though this is not a bug hunt.

## Calibration

Keep a finding only if the user would plausibly act on it. Skip style a linter could catch, theoretical risks, rigor beyond the project's maturity, uniformity for its own sake, splitting cohesive code, merging things that only look alike, undoing a deliberate choice, or working layouts that just look unfamiliar.

On the other side, do not skim and call a messy area "mostly fine", or fill the report with nits while missing structural cost. Finding little after a real look is a good result; say so plainly.

## How to inspect

Follow the requested scope. For a whole repo, orient first on purpose, main parts, and churn hotspots (churn and file size are leads, not findings), then go deep where cost concentrates. For a broad sweep, split by area across fresh-context subagents.

Read recorded project decisions first so you do not flag a deliberate choice without a real reason to reopen it. Verify every finding against actual callers and consumers before proposing removal or consolidation, and run tests or the build where practical. Drop findings that rest on naming or assumption, but keep real concerns even when some uncertainty remains (state it). Flag visible code waste directly, and mark user-facing performance impact as a hypothesis unless measured.

## Report and next steps

Report in conversation (write a file only if asked). Lead with a short verdict on the codebase's state and the first move you recommend.

List only findings worth acting on, merged by root cause, small enough to land individually, and ordered by payoff against effort and risk. For each:
- What and where, and what it costs today.
- Concrete evidence.
- Proposed change and how to verify behavior.
- Effort and risk.

Note briefly what is solid and should stay alone, plus what you inspected and skipped. Do not edit code or file issues until approved; end with a concrete proposal of which findings to file or tackle first. Once approved, file each approved change as an issue in the project's tracker, or implement it if asked.
