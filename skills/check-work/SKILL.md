---
name: check-work
description: Review implementation quality before handoff or on request. Use automatically when substantive implementation is ready to hand back, or when asked to review a PR, branch, or working changes.
---

Ensure the delivered implementation is coherent, maintainable, and supported
by useful evidence.

Establish the requested changes and comparison boundary, including the relevant
revision or working state, and whether assessment or remediation is requested.
Reuse evidence where it applies to that scope and state.

Start from the review and validation already performed and focus further work
on unresolved concerns. Do not repeat equivalent
self-review, spawn another reviewer for an already-reviewed change, or rerun
unchanged checks without a concrete reason. Relevant edits, changed
conditions, unreliable results, an unanswered question, or an explicitly
requested independent assessment can justify further review or targeted checks.

Review against the current agreed outcome, including decisions made during
implementation. Exclude unrelated pre-existing changes.

Include relevant documented project intent and decisions when assessing
alignment; surface unexplained discrepancies rather than changing the
documentation to fit the implementation.

Apply judgment to the concerns that matter:

- Smallest coherent implementation: unnecessary layers, speculative
  flexibility, redundant state, excessive indirection, and obsolete paths.
  Prefer removing complexity over compressing code.
- Fit with the project: inspect surrounding code for existing components,
  primitives, tokens, helpers, and conventions before accepting new ones.
  Evaluate deliberate departures on their merits.
- Ownership and duplication: repeated domain logic, competing representations,
  misplaced responsibilities, and changes scattered across owners.
  Share what represents the same concept without coupling unrelated behavior.
- Test value: plausible failures caught, independently meaningful expectations,
  resilience to implementation changes, and useful coverage beyond existing
  evidence. Remove or improve tests that merely mirror the implementation.
- Cost: avoidable runtime work, unnecessary test setup or waits, oversized
  fixtures, and expensive machinery whose cost exceeds its value.
- Behavior and scope: missing requirements, unintended behavior changes,
  unjustified additions, and important gaps in verification.

Use a fresh frontier reviewer when meaningful design decisions or interacting
behavior warrant independent scrutiny, applying the reuse criteria above.
Passing tests alone does not settle implementation quality. Scale review to
the change; routine documentation and mechanical edits need focused checks
appropriate to their content.

Follow global delegation guidance. Give the reviewer the agreed outcome,
relevant constraints, scope, completed validation, and applicable review
criteria. Keep it read-only. The parent owns targeted investigation of
findings, fixes, and integration; avoid duplicating the delegated review.

A finding should explain the evidence, practical cost, and a better direction.
Treat judgment calls as such. Do not manufacture findings or turn stylistic
preferences into blockers.

Address worthwhile in-scope findings before handoff, rechecking what the fixes
affect. Surface consequential choices that require Marián. Finish when the
requested outcome and material review concerns are resolved; avoid open-ended
polishing.

Report the outcome, material improvements, validation, and important remaining
uncertainty. For review-only requests, report findings without editing.
