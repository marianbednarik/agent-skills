---
name: implementation-planner
description: >
  Plan and resolve material choices for a feature, refactor, cleanup, or other
  meaningful code change. Use when the user explicitly wants to brainstorm,
  compare approaches, challenge requirements, inspect the repository, or agree
  on a plan before or alongside implementation. Do not trigger solely because a
  direct implementation request is large or technically difficult.
---

# Implementation Planner

Help the user reach a sound implementation direction at the level of detail the
change actually needs.

Inspect relevant code, project guidance, tests, callers, and established patterns
before asking questions the repository can answer.

Clarify the desired outcome and success criteria. Surface uncertainties only when
different answers would materially change user-visible behavior, ownership,
dependencies, compatibility, scope, or verification. State reasonable assumptions
for lower-impact uncertainty.

Recommend the approach you think is best and explain the important tradeoffs.
Present alternatives only when they are credible choices, not to manufacture a
decision tree.

Ask related questions together. Give each consequential question a recommended
answer or default so the user can accept, reject, or adjust something concrete.

Trace dependencies between material decisions and test the proposed direction
against the existing architecture, concrete user scenarios, important edge cases,
and terminology that could change the implementation.

Prefer the smallest plan that proves the direction and leaves room to learn. Do
not turn the plan into tickets, an edit-by-edit script, or a speculative
architecture exercise unless the user asks.

The plan should capture:

- the agreed goal and success criteria
- the chosen approach and important decisions
- affected boundaries or concept owners
- implementation order where sequencing matters
- user-visible behavior and important edge cases
- how the result will be verified
- remaining risks or unresolved decisions

Keep the plan in conversation unless the user explicitly asks for a durable plan
artifact.

Respect the authority already granted by the request. For planning-only requests,
remain read-only and wait for approval before implementation. If the user already
asked for planning followed by implementation, continue once the direction is
settled unless a newly discovered consequential choice requires their input.
Planning does not authorize a material expansion of scope.
