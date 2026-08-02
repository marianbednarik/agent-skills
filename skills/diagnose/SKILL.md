---
name: diagnose
description: >
  Establish an evidence-backed cause for unexplained bugs, failures, or incorrect
  behavior before fixing them. Use when asked to diagnose, debug, investigate,
  find the root cause, or explain why something happens, and during an authorized
  fix when editing would otherwise be speculative. Do not trigger when the cause
  is already established, for routine implementation, repo-wide audits, or when
  only test authority is unclear.
---

# Diagnose

Explain the failure before changing product behavior. The result is a causal
account supported by evidence, not a patch that merely stops the symptom.

Respect the authority in the request. Diagnosis-only means read-only: report the
cause and fix direction without editing. When a fix is already authorized,
investigate first and implement once the causal path is sufficiently supported.

Establish what was expected, what happened, the conditions that expose it, and
whether it is reproducible. Inspect the owning boundary and gather evidence from
the relevant code, state transitions, data flow, callers, tests, logs, errors,
runtime behavior, and recent changes.

Work from a small number of plausible hypotheses. Prefer the cheapest safe check
that distinguishes between them, and change one investigative variable at a
time.

Separate:

- **symptom:** the visible failure
- **trigger:** the condition that exposes it
- **causal path:** how the failure propagates
- **root cause:** the earliest incorrect assumption, state, boundary, or behavior
  that sufficiently explains it
- **contributing factors:** conditions that amplify or obscure the cause

Call the root cause confirmed only when the evidence explains the observed
behavior and rules out the credible alternatives. Otherwise report the
investigation as narrowed, state the best-supported hypothesis, and identify the
next discriminating check.

When implementation is authorized, fix the problem at the owning boundary,
remove temporary instrumentation, add regression evidence where it buys
confidence, and verify the original reproduction path.

## Gotchas

- The final error or stack frame may only be where the failure became visible.
- Recently changed code is evidence, not automatic blame.
- A passing retry does not disprove nondeterminism.
- A guard that suppresses the error has not repaired a violated invariant.
- A downstream patch is insufficient when the defect belongs upstream.
- Uncertainty is not permission to add fallbacks or compatibility paths that
  hide the problem.
