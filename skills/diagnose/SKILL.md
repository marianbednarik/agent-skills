---
name: diagnose
description: >
  Establish an evidence-backed root cause for unexplained bugs, failures, or
  incorrect behavior before recommending or implementing a fix. Use when the user
  asks to diagnose, debug, investigate, find the root cause, or explain why
  something happens, and during an authorized fix when the cause remains unknown
  enough that editing would be speculative. Do not trigger when the cause is
  already established, for routine implementation, repo-wide audits, or when only
  test authority needs classification.
---

# Diagnose

Determine what is actually failing and why before changing product behavior.

Respect the authority in the request. For diagnosis-only requests, remain
read-only and report the cause and fix direction without editing. When the user
already authorized a fix, investigate first, then implement once the causal path
is sufficiently supported. Do not use uncertainty as permission to add guards,
fallbacks, retries, or compatibility paths that merely hide the symptom.

Establish the observed behavior:

- what was expected
- what actually happened
- the conditions that trigger it
- whether it is reliably reproducible
- the affected user-visible behavior or external contract

Inspect the owning boundary and gather direct evidence from relevant code, state
transitions, data flow, logs, errors, tests, callers, runtime behavior, and recent
changes. Ask for clarification only when expected behavior or a user-only fact
would materially change the investigation.

Form a small number of plausible hypotheses. Prefer the cheapest safe check that
would distinguish between them. Change one investigative variable at a time, and
do not make several speculative fixes before learning which explanation is
correct.

Distinguish:

- **symptom:** the visible failure
- **trigger:** the condition that exposes it
- **causal path:** how the failure propagates through the system
- **root cause:** the earliest incorrect assumption, state, boundary, or behavior
  that sufficiently explains the failure
- **contributing factors:** conditions that amplify or obscure the primary cause

Do not mistake correlation for cause. In particular:

- the last error or stack frame may only be where the failure became visible
- recently changed code is evidence, not automatic blame
- a passing retry does not disprove flakiness or nondeterminism
- a defensive guard that suppresses the error does not repair a violated invariant
- a downstream patch is not sufficient when the defect belongs to an upstream
  owner

Call a root cause confirmed only when the evidence explains the observed behavior
and rules out the most credible alternatives. If reproduction or access is
insufficient, report the investigation as narrowed rather than presenting a
hypothesis as fact. State the next discriminating check that would increase
confidence.

When implementation is authorized, fix the problem at the owning boundary with
the smallest coherent change. Remove temporary instrumentation, preserve relevant
behavior, add or update regression evidence where it buys confidence, and verify
the original reproduction path.

End with:

- observed behavior and reproduction status
- root cause or best-supported hypothesis
- causal evidence and alternatives ruled out
- confidence and remaining uncertainty
- contributing factors
- recommended fix or next discriminating check
- what was not verified
