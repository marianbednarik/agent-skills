---
name: implementation-planner
description: >
  Shape and agree on an implementation direction in conversation. Use when
  Marian asks to brainstorm, compare approaches, challenge requirements, answer
  consequential questions, or settle a direction before or alongside
  implementation. Do not trigger merely because a direct implementation request
  is large or technically difficult.
---

# Implementation Planner

Reach an agreed direction at the level of detail the change actually warrants.
Marian should understand the important reasoning well enough to explain and
defend the result later.

Inspect relevant code, project guidance, tests, callers, and existing patterns
before asking questions the repository can answer.

Bring back:

- what the repository establishes or constrains
- the approach you recommend and why
- credible alternatives where a real tradeoff exists
- questions whose answers would materially change behavior, ownership,
  dependencies, compatibility, scope, or verification
- your recommended default for each question
- how the result would be verified
- important remaining uncertainty

Explain the reasoning behind boundaries and ownership choices, not merely the
implementation steps.

Keep the plan in conversation unless Marian asks for a durable artifact. Prefer
the smallest direction that resolves the material choices and leaves room to
learn.

Respect the authority in the request. Planning-only requests remain read-only
until implementation is approved. When Marian already asked to plan and
implement, continue once the direction is settled unless a newly discovered
consequential choice requires him. Planning never expands the requested scope.

## Gotchas

- Do not manufacture alternatives to look thorough.
- Do not turn the result into tickets or a file-by-file edit script.
- Do not ask for ceremonial approval when planning and implementation were
  already authorized together.
- If Marian asks to skip planning and implement a clear contract directly,
  stand down.
- Take pushback seriously instead of immediately adopting the last position
  stated.
