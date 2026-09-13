---
name: repo-health-audit
description: Assess accumulated code quality and structural health, and recommend worthwhile maintenance. Use when asked to audit a repository or area for improvement, rather than review a completed change or diagnose a specific bug.
---

Help Marián decide what deserves maintenance attention, why it matters,
and how confidently it can be improved.

An audit authorizes investigation and reporting. Implement changes only
when remediation is also requested.

Ground the assessment in the project's intent, maturity, and existing
decisions. Follow the requested scope. For a broad audit, use development
hotspots and representative code paths to find where complexity is
accumulating; expand exploration as the evidence warrants.

Look for practical friction: scattered responsibilities, competing
patterns, repeated domain logic, unnecessary abstractions, obsolete paths,
inconsistent use of shared UI foundations, and tests whose value does
not justify their complexity or runtime. Treat these as leads, not a
checklist every project must satisfy.

Explain how a finding affects understanding, change cost, consistency,
or confidence in the system. Assess existing patterns on their merits.
Preserve deliberate simplicity and useful foundations; fewer lines or
more uniform code are not sufficient reasons for a refactor.

Support findings with concrete examples and file references. Check
prevalence before describing something as a repository-wide pattern.
Make coverage and important gaps visible. Distinguish observed problems
from hypotheses about their causes or solutions.

For each worthwhile finding, explain the practical cost, recommended
direction, expected benefit, and relevant effort, risk, or uncertainty.
Distinguish confidence in the finding from confidence in the proposed fix.

Organize recommendations around the maintenance decision:

- Address soon: consequential problems, especially patterns ongoing
  development is spreading.
- Improve now: well-supported improvements with modest effort and
  limited disruption.
- Explore first: promising directions that need further investigation
  or a design decision.

Recommend a starting point and explain dependencies that affect the
order of work. Group symptoms with a shared cause when that produces
a more coherent improvement. A useful audit may find little to change.

For a substantive audit, create an HTML report outside the repository
unless another destination or format is requested. Use before-and-after
diagrams where they clarify responsibilities, relationships, or flow.
Keep observations and proposed structures visibly distinct, and pair
visuals with concise explanations and source references.

A small, focused audit can stay in conversation. In either format,
make the recommendation easy to find and the reasoning understandable
without requiring Marián to inspect every referenced file.
