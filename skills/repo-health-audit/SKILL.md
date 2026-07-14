---
name: repo-health-audit
description: >
  Audit repository-wide structural health against project direction and applicable
  engineering guidance. Use when the user explicitly asks for an architecture,
  maintainability, technical-debt, ownership, testing, state-modeling, UI
  consistency, documentation, or agent-navigability audit. Produce an
  evidence-based prioritized report and cleanup direction. Do not use for current
  diff review, a single bug diagnosis, or routine implementation validation.
---

# Repo Health Audit

Assess the repository as something future maintainers and agents must be able to
understand, change, and trust.

An audit-only request is read-only. Do not edit, format, clean up, or create a
report file unless the user explicitly authorizes remediation or requests a
durable artifact. Return the report in conversation by default.

Map the repository before judging it. Read applicable project guidance,
manifests, tests, main entry points, and representative code paths. Preserve
intentional simplicity; a small repository does not need heavyweight structure
merely to resemble a mature enterprise system.

Evaluate the dimensions that matter for this repository:

- **direction:** agreement between product intent, documentation, code, and
  current behavior
- **ownership:** clear concept owners, module boundaries, and absence of competing
  patterns
- **state and data:** canonical shapes, lifecycles, contracts, validation, and
  external boundaries
- **change cost:** duplication, tangled responsibilities, obsolete paths,
  compatibility branches, and risky coupling
- **evidence:** whether tests and validation protect important behavior without
  freezing implementation details
- **interface coherence:** consistency of UI patterns, states, styling, and
  accessibility conventions where relevant
- **operations:** understandable deployment, migrations, external systems,
  recovery paths, and operational constraints where relevant
- **navigability:** whether a future maintainer or agent can find context, owners,
  commands, and verification paths

Be explicit about coverage. State what was inspected, what was sampled, and what
material areas were not examined. Distinguish directly verified findings from
inferred patterns. Do not claim repository-wide prevalence from one example; use
additional searches, counts, or representative evidence when prevalence matters.

Support material findings with concrete files, symbols, behavior, or command
evidence. When an oddity may be deliberate, state the likely interpretation,
explain its cost or risk, and identify what depends on user intent. Put targeted
questions at the end unless uncertainty prevents a responsible assessment.

When the active harness supports subagents, use a small number of read-only
subagents only when the repository contains independent domains whose evidence
would otherwise overload the main context. Map the repository first, give each
subagent a bounded non-overlapping area, and ask for evidence rather than a
complete competing audit. Wait for every requested result, verify important
findings, identify cross-cutting causes, and own the final synthesis. Do not
delegate merely because the repository has many lines.

Prioritize findings:

- **P0:** dangerous, broken, or actively blocking
- **P1:** high-impact correctness, ownership, or maintainability problem
- **P2:** valuable structural cleanup
- **P3:** opportunistic polish

Priority should reflect impact, risk, and change cost rather than aesthetic
dislike.

For each finding, include:

- priority and concise title
- concrete evidence
- impact on behavior, trust, or change cost
- recommended direction
- material uncertainty or required user decision

End with:

1. overall verdict, audit scope, and coverage limits
2. healthy foundations worth preserving
3. prioritized findings
4. cross-cutting causes or themes
5. recommended cleanup sequence based on leverage, dependencies, risk, and
   ability to verify
6. open decisions that could change the recommendation

Do not invent a numerical health score. If the user also authorized remediation,
establish the cleanup scope from the findings before editing and preserve any
approval boundary around behavior, dependencies, compatibility, or ownership.
