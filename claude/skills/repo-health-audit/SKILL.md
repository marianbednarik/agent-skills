---
name: repo-health-audit
description: >
  Assess a whole repository's structural health and return a prioritized
  report. Use when Marian explicitly asks what he should improve about a
  project, or for an architecture, tech-debt, ownership, testing, or
  agent-navigability audit — typically to bring an older or vibe-coded project
  up to current standards. Do not use for reviewing the current diff, a single
  bug, or routine validation.
---

# Repo Health Audit

Judge the repository as something a future maintainer — human or agent — has to
understand, change, and trust.

Read-only unless remediation is explicitly authorized. Report in conversation;
do not write a report file unless asked.

Map before judging: project docs, manifests, entry points, tests, and
representative code paths. Preserve intentional simplicity — a small project
does not need enterprise scaffolding to be healthy.

Look at whichever of these actually matter here: agreement between stated
intent and real behavior; clear concept owners versus competing patterns for
the same thing; canonical data shapes and where untrusted input is validated;
change cost from duplication, tangled responsibilities, and dead compatibility
paths; whether tests protect behavior or freeze implementation details; and
whether someone landing cold can find the commands, owners, and verification
paths.

Be explicit about coverage: what you read, what you sampled, what you did not
open. Distinguish what you verified from what you inferred.

Prioritize by impact and change cost, not by aesthetic preference:

- **P0** dangerous, broken, or blocking
- **P1** real correctness, ownership, or maintainability problem
- **P2** worthwhile structural cleanup
- **P3** opportunistic polish

Each finding: what it is, the concrete evidence, what it costs, and the
recommended direction. End with the healthy foundations worth keeping, the
cross-cutting themes behind the individual findings, and a cleanup sequence
ordered by leverage and risk.

## Gotchas

- One example is not a prevalence claim. Count or search before saying
  "throughout the codebase".
- An oddity may be deliberate. Say what it would cost if it stays and what
  depends on his intent, rather than declaring it wrong.
- No numerical health scores.
- Do not quietly start fixing things because a finding looked easy.
