---
name: diagnose
description: Investigate unexplained bugs, failures, or performance problems. Use when the cause is unclear and needs evidence before choosing a fix.
---

Build an evidence-backed explanation of the failure. Treat the reported
symptom as a starting point, not a diagnosis.

Establish what was expected, what happened, and the conditions that expose
the difference. Inspect enough of the implementation and surrounding system
to develop plausible explanations, including causes outside the place where
the error appears.

Consider credible alternative hypotheses before committing to a cause.
Explain the leading possibilities and what supports them. Scale exploration
to the uncertainty; avoid inventing alternatives when the evidence is clear.

Choose checks that distinguish between hypotheses. Use reproduction,
code tracing, logs, runtime inspection, targeted tests, or reversible
experiments as appropriate. Prefer the cheapest useful probe and be clear
about what its result would establish.

Let results change the investigation. Revise or discard hypotheses when
evidence contradicts them. An inconclusive check leaves uncertainty;
it does not confirm the preferred explanation.

Keep experimental changes controlled and distinguish them from accepted
fixes. Clean up temporary instrumentation and unsuccessful experiments.
When a fix is authorized, address the supported cause and verify the
original failure path.

A passing test or disappearing symptom is evidence, but does not by itself
establish the cause or completeness of a fix.

Explain what triggered the failure, how it propagated, and why the evidence
supports the conclusion. Distinguish confirmed causes from remaining
hypotheses. If unresolved, state what was learned and the next useful check.
