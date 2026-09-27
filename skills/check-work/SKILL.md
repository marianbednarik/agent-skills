---
name: check-work
description: Review completed work automatically, including useful checkpoints during development, or review a specified PR, branch, commit, or working diff on request.
---

Check that the work meets the agreed outcome, is coherent and maintainable, and has useful verification evidence.

Establish the requested scope, comparison base and reviewed state, and whether review or remediation is authorized. Resolve the target from available context; ask when consequential ambiguity remains. Review-only requests authorize findings, not edits.

Review against current agreed requirements, project guidance, and decisions, including changes agreed during implementation. Investigate unexplained discrepancies rather than rewriting intent to fit the work. Follow affected behavior into relevant callers, consumers, and state transitions; exclude unrelated pre-existing problems.

Reuse review and validation that still apply to the state, scope, and concern. Use targeted checks or further reviewer rounds for changed behavior, unresolved questions, unreliable evidence, or an explicitly requested independent assessment. Neither an earlier review nor a fresh reviewer is a blanket assurance.

Choose the depth and dimensions that matter: correctness, completeness, security, project standards, ownership, simplicity, runtime and verification cost, and test value. Inspect existing patterns before accepting new ones; assess deliberate departures on their merits. Seek the smallest coherent implementation, removing unnecessary indirection, duplicated concepts, redundant state, and obsolete paths without coupling unrelated behavior. Judge tests by the guarantees and plausible failures they protect; improve brittle tests without losing meaningful coverage. Passing checks alone does not establish quality.

Review directly when sufficient. Delegate when independent scrutiny would help, using one or more fresh-context, read-only reviewers with complementary scopes as useful. Follow global delegation guidance. Give them the agreed outcome, constraints, comparison boundary, source references, and existing evidence, without your conclusions or a preferred verdict. Let them inspect the work independently; do not duplicate their review. The parent evaluates findings and owns fixes and integration.

Ground findings in evidence and practical consequence: a reachable failure path, unmet requirement, or concrete maintenance cost. Check what could invalidate a concern or make its proposed remedy worse before acting. Distinguish defects, design judgments, and verification gaps; do not manufacture findings or promote stylistic preferences into blockers.

When remediation is authorized, address worthwhile in-scope findings and recheck what fixes affect. Surface consequential choices requiring Marián. Finish when the requested scope is covered and worthwhile authorized fixes are complete; explain any material concern that cannot be resolved. Avoid open-ended polishing. Report findings or improvements, relevant validation, and important remaining uncertainty.
