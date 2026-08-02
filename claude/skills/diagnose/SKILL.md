---
name: diagnose
description: >
  Find the real cause of a bug before changing anything. Use when asked to
  diagnose, debug, investigate, or explain why something happens, and during an
  authorized fix when the cause is unknown enough that editing would be
  guessing. Do not use when the cause is already established, for routine
  implementation, or for repo-wide audits. Unrelated to `/debug`, which is
  Claude Code's own session logging.
---

# Diagnose

Explain the failure before touching it. The deliverable is a causal account
with evidence, not a patch that makes the symptom stop.

Respect the authority in the request. Diagnosis-only means read-only: report
the cause and the fix direction without editing. When the fix is already
authorized, investigate first, then fix once the causal path holds up.

Work from a small number of hypotheses and pick the cheapest check that
distinguishes between them. Change one variable at a time. Do not stack
speculative fixes and see what sticks.

Separate these explicitly, because collapsing them is how wrong fixes happen:

- **symptom** — the visible failure
- **trigger** — the condition that exposes it
- **causal path** — how it propagates
- **root cause** — the earliest wrong assumption, state, or boundary that
  explains the whole thing
- **contributing factors** — what amplifies or hides it

Call the cause confirmed only when the evidence explains the observed behavior
*and* rules out the credible alternatives. Otherwise say the investigation is
narrowed, give the best-supported hypothesis, and name the next check that
would settle it.

When fixing: fix it at the owning boundary, remove your instrumentation, add
regression evidence where it buys something, and re-run the original
reproduction.

## Gotchas

- The last stack frame is where it became visible, not necessarily where it
  broke.
- Recently changed code is evidence, not a verdict.
- A passing retry does not disprove nondeterminism.
- A guard that swallows the error has not repaired the violated invariant.
- A downstream patch is wrong when the defect belongs upstream.
- Uncertainty is not permission to add fallbacks, retries, or compatibility
  paths that hide the problem.
