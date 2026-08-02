---
name: repo-health-audit
description: >
  Assess a repository's structural health and return a prioritized report. Use
  when Marian explicitly asks what to improve across architecture, ownership,
  maintainability, technical debt, state modeling, testing, documentation, UI
  consistency, operations, or agent navigability. Do not use for reviewing the
  current diff, diagnosing one bug, or routine implementation validation.
---

# Repo Health Audit

Judge the repository as something future maintainers and agents must be able to
understand, change, and trust.

An audit request is read-only unless remediation is explicitly authorized.
Return the report in conversation unless Marian asks for a durable artifact.

Map the repository before judging it. Read applicable project context,
manifests, entry points, tests, and representative code paths. Preserve
intentional simplicity; a small repository does not need heavyweight structure
merely to look mature.

Evaluate the dimensions that matter here: alignment between stated direction and
implementation, concept ownership, state and data boundaries, competing
patterns, change cost, obsolete paths, evidence quality, interface coherence,
operations, and navigability.

Be explicit about coverage. Distinguish what was verified from what was inferred.
Do not generalize from one example when prevalence matters; search, count, or
sample enough evidence to support the claim.

Prioritize by impact and change cost:

- **P0:** dangerous, broken, or blocking
- **P1:** substantial correctness, ownership, or maintainability problem
- **P2:** worthwhile structural cleanup
- **P3:** opportunistic polish

For each material finding, explain the evidence, its cost, the recommended
direction, and any decision that depends on Marian's intent.

End with the healthy foundations worth preserving, the cross-cutting causes
behind the findings, and a cleanup sequence ordered by leverage, dependency,
risk, and ability to verify.

## Gotchas

- Do not invent a numerical health score.
- Do not present an aesthetic preference as a structural defect.
- An oddity may be deliberate; explain its cost and the intent it depends on.
- Do not quietly start fixing findings from an audit-only request.
