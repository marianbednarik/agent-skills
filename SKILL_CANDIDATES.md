# Skill Candidates

Source: local Codex sessions available under `~/.codex` as of 2026-04-20. The scan focused on Marian's messages, thread titles, and repeated workflows, not assistant/tool output.

This is a working backlog, not a commitment to build every skill.

## Strong Candidates

### Plan Executor

Trigger when Marian provides a detailed implementation plan, especially with "PLEASE IMPLEMENT THIS PLAN".

Purpose: execute an existing plan in small, reviewable steps instead of re-planning from scratch.

Useful behavior:
- Preserve the plan's intent unless there is a clear technical blocker.
- Split work into visible checkpoints.
- Verify each meaningful checkpoint with tests, typechecks, lint, or manual reproduction.
- Surface scope risks before expanding the plan.

Why: many past sessions start from a concrete plan and then need disciplined implementation rather than more ideation.

### Project Direction Refiner

Likely update to the existing `project-starter` skill rather than a new skill.

Purpose: help shape `PROJECT_DIRECTION.md`, `AGENTS.md`, and related docs without turning them into project-management bloat.

Useful behavior:
- Explore the repo first.
- Separate durable direction from transient implementation plans.
- Keep `AGENTS.md` lean and operational.
- Ask batches of focused questions when product intent is missing.
- Push back when the requested scope is too broad for a useful first version.

Why: several sessions revolve around project guardrails, repo direction, docs responsibility, and avoiding overbuilt initial scopes.

### Codebase Health Audit

Trigger when Marian asks to review, audit, inspect, find deficiencies, find dead code, or compare a repo against its own guidance.

Purpose: produce actionable findings before editing.

Useful behavior:
- Read project docs and current code.
- Prioritize concrete bugs, dead code, architecture drift, missing tests, and mismatches with `AGENTS.md`.
- Show findings before making broad cleanup changes.
- Recommend whether issues should become immediate fixes, backlog items, or doc changes.

Why: repeated review/audit sessions exist across multiple projects, often with a desire to learn from "vibe coded" deficiencies.

### Live App Debugger

Trigger when the task involves a visible UI bug, browser reproduction, screenshots, local dev servers, or "why does this not line up/work".

Purpose: make browser-based debugging systematic.

Useful behavior:
- Reproduce the issue before editing when possible.
- Use screenshots/browser state to form a concrete hypothesis.
- Patch the smallest likely cause.
- Re-check the same path after the fix.
- Report what was visually verified and what was only inferred.

Why: many long threads involve iterative UI/browser debugging, especially layout, command palette behavior, image loading, and app state issues.

### Product UI Iteration

Potential replacement for the old `frontend-design` skill, but tuned to Marian's actual workflow.

Purpose: improve existing app UI while respecting product direction and current architecture.

Useful behavior:
- Read existing product docs and UI before redesigning.
- Preserve established visual language unless explicitly rethinking it.
- Use screenshots or app inspection when available.
- Treat layout, hierarchy, interaction feel, and responsive behavior as first-class.
- Avoid generic "AI design" defaults.

Why: repeated UI sessions are not just "make it pretty"; they are product-specific iteration with strong opinions about direction, simplicity, and feel.

## Project Or Local Candidates

### Power Automate Extension Helper

Likely project-scoped, not global.

Purpose: capture PAX / Power Automate extension domain knowledge, including solution/flow navigation, command palette behavior, and Microsoft page quirks.

Why: a large share of long sessions center on `power-automate-extended`, but the domain is probably too specific for a global skill.

### Game UI / Card State Helper

Likely project-scoped to `hogwarts-battle-redux`.

Purpose: capture card game UI/state conventions, multiplayer authority assumptions, and layout constraints.

Why: repeated sessions involved card piles, player status, hand animation, multiplayer, and market/play-area layout.

### Slovak Academic Revision

Maybe global if this work continues; otherwise archive as a note.

Purpose: revise Slovak thesis/doc text according to review comments while preserving Marian's writing style.

Why: fewer sessions than coding work, but the workflow is distinct enough that a small writing skill could help.

## Existing Skills To Revisit

### `project-starter`

Main issue to refine: it should not lean too hard into project-management planning. It should help establish durable direction and boundaries for coding agents.

### `grill-me`

Main issue to refine: allow batches of related questions when that saves turns and token cost, instead of one question at a time by default.

### `hard-cut-policy`

Main issue to refine: decide whether it is a standalone skill or should be folded into project/codebase cleanup guidance.

### `tdd`

Main issue to refine: connect it to Marian's preference for human-testable checkpoints, not only automated red-green-refactor loops.

## Not Yet Worth A Skill

One-off app features, isolated bug fixes, and single-project implementation details should stay in project docs or local skills until they repeat across projects.

Do not create a broad "general coding" skill. Global skills should encode Marian-specific workflows that change how an agent behaves.
