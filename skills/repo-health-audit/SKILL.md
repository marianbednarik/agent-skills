---
name: repo-health-audit
description: >
  Audit a repository against Marian's coding standards and project direction.
  Use for repo-wide reviews of architecture, ownership, tests, duplication,
  state/data modeling, compatibility paths, UI/style drift, agent navigability,
  and maintainability, producing a prioritized report and recommended cleanup approach.
---

# Repo Health Audit

Audit the repo as something a future human or agent will need to understand, modify, and trust.

Explore before judging. Read relevant project docs (`AGENTS.md`, `PROJECT_DIRECTION.md`, `UBIQUITOUS_LANGUAGE.md`, README), package manifests, tests, and main code paths.

Look for friction, not enterprise checkboxes. Preserve intentional simplicity. Small repos do not need heavyweight structure just to look mature.

Review for:

- unclear concept ownership or parallel patterns
- large mixed-responsibility files
- shallow helper spray, vague `utils`, or modules that hide little
- duplicated local implementations
- optional-field soup, boolean flag piles, generic modes, or unclear state lifecycles
- compatibility shims, silent fallbacks, dual codepaths, or obsolete paths
- hand-rolled primitives where project-standard libraries or patterns exist
- global CSS drift or repeated feature styling patterns
- tests missing where behavior is important
- tests coupled to implementation instead of behavior
- dead code or confusing leftovers
- places where code, docs, and project direction disagree
- parts of the repo that are hard for a future agent to navigate safely

Do not assume every oddity is accidental. Call out likely deliberate tradeoffs and ask when intent is unclear.

Produce a report, not fixes by default. Treat the report as the start of a conversation: be opinionated, recommend what to tackle first, and ask targeted questions where intent may change the recommendation. Do not emit `::code-comment{...}` findings; repo-wide issues should stay in one coherent report.

Prioritize findings:

- P0: broken, dangerous, or blocking
- P1: high-impact correctness or maintainability issue
- P2: worthwhile cleanup/refactor
- P3: polish or opportunistic improvement

For each finding, include evidence, why it matters, recommendation, suggested first step, and whether it needs user confirmation.

End with what is already healthy, prioritized findings, recommended order of attack, questions or conversation topics, and what you would fix first.
