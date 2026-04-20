---
name: project-starter
description: >
  Explore a repo or empty project, align on product intent the code cannot reveal,
  compare the current state against AGENTS.md, and write a lean PROJECT_DIRECTION.md.
  For existing repos, also recommend how to bring the codebase closer to the desired
  structure and quality bar.
---

# Project Starter

Use this skill to align a project with its intended direction, not to produce a project-management plan.

This skill has two jobs:

1. Capture the product intent and taste that the code cannot reveal.
2. Help the repo move closer to the standards in `AGENTS.md`, whether the project is brand new or already messy.

This skill should complement `AGENTS.md`, not repeat it. Treat `AGENTS.md` as the universal operating policy. Use this skill to capture project-specific direction, non-obvious constraints, and intentional preferences.

## When To Use

- Starting a brand-new project
- Dropping into an existing repo that needs clearer direction
- Re-grounding the project after a substantial pivot
- Auditing a vibe-coded codebase before cleanup or continued feature work

## Core Principles

- Explore first. Read the repo before asking questions the code can answer.
- Ask only about intent, taste, constraints, priorities, and tradeoffs that cannot be reliably inferred from code.
- Ask in batches, not one question at a time. Group related questions so the user can answer several connected decisions in one pass.
- **Act as a technical co-founder, not a scribe.** Challenge scope creep, question choices that import complexity without a clear payoff, and push back on vague goals. When the user is unsure, recommend a concrete default and explain the tradeoff. Do not accept vague goals, overloaded terminology, or "maybe later" features that quietly force major architectural choices now.
- Keep the persistent doc lean. Do not store facts the agent can grep from the repo.
- Prefer directional truth over exhaustive planning. The output should guide future decisions, not become a requirements document.
- **When a later answer conflicts with an earlier decision, surface the conflict explicitly and resolve it before moving on or writing the direction doc.**

## Modes

### New Or Empty Project

- Use the interview to set direction before implementation starts.
- Resolve the product's reason for existing, the desired feel, major technical preferences, and any important guardrails.
- Recommend a simple starting shape that fits `AGENTS.md` without overdesigning the repo.

### Existing Project

- Explore the repo first.
- Compare the current codebase against `AGENTS.md`.
- Identify structural drift, duplication, unclear ownership, repeated bespoke UI, bad boundaries, or compatibility clutter.
- Ask only the questions needed to understand product intent and any non-obvious constraints that should guide cleanup.
- Recommend how to "deslop" the repo in a staged, practical way.

## Interview Areas

Use the following areas as a map, not a rigid script. Cover only what is useful for the project at hand. The goal is to extract the information the code cannot tell you.

### Why This Exists

- Why does this product exist?
- Who is it really for?
- What matters about it that the code cannot tell you?
- What is the main value or feeling it should create?

### Product Taste

- What should the app feel like?
- What visual or UX references fit it?
- What anti-references should be avoided?
- What level of polish, boldness, density, or simplicity is desired?
- What would make the product feel "wrong" even if it technically works?

### Guardrails

- Are there technical preferences or forbidden directions?
- Are there platform, implementation, or library choices the agent should respect?
- What should future changes preserve?
- What traps, mistakes, or recurring failure modes should the agent watch for?
- Where should the agent push back instead of taking the easiest local path?

## Existing Repo Exploration

If a repository already exists:

1. Read `AGENTS.md`, `PROJECT_DIRECTION.md`, `UBIQUITOUS_LANGUAGE.md`, `README`, and package manifests if present.
2. Inspect enough of the codebase to understand the main surfaces, stack, and current structure.
3. Compare the current implementation against `AGENTS.md`.
4. Note friction such as:
   - mixed-responsibility files
   - repeated local patterns that should be shared
   - feature logic living in pages or screens
   - global style dumps
   - shallow helper spray
   - unclear ownership
   - compatibility branches or silent fallbacks
   - tests coupled to implementation details
5. Ask the user only about the intent needed to judge what should be preserved, simplified, or reshaped.

## Decision Rules

- Keep the conversation focused on intent the code cannot reveal and on structural choices that affect future code quality.
- If the user is unsure, propose a reasonable default and keep moving.
- Do not write stack facts, current file structure, or feature inventory into the persistent doc if they can be discovered from code.
- If the project intentionally deviates from `AGENTS.md`, record that as a project-specific guardrail instead of restating the global rule set.

## Outputs

After the interview and exploration:

1. Write or update `PROJECT_DIRECTION.md` in the working directory using the template at `PROJECT_DIRECTION.template.md` only as a starting shape.
2. Keep `PROJECT_DIRECTION.md` lean and durable. It should read like a brief from the product owner to the agent, not like a plan, audit, or architecture dump.
3. Omit empty sections. Adapt the wording and structure to the project instead of forcing a rigid format.
4. If the session introduced new domain terms, changed the meaning of existing ones, or resolved terminology ambiguity, trigger the `ubiquitous-language` skill to write or update `UBIQUITOUS_LANGUAGE.md`.
5. For existing repos, also provide an in-chat alignment summary:
   - what currently matches the desired direction
   - where the repo drifts from `AGENTS.md`
   - the top cleanup or refactor opportunities
   - the recommended order of attack
6. For new or empty repos, also provide an in-chat bootstrap summary:
   - the intended product direction
   - the main technical and UX guardrails
   - the recommended starting shape
7. End by summarizing resolved direction, open questions, and next steps.

## Re-Running

When invoked again later:

1. Read the existing `PROJECT_DIRECTION.md`.
2. Preserve prior direction unless the user is intentionally changing it.
3. Ask only the questions needed to resolve the delta.
4. Update only the parts of the direction brief that materially changed.
5. Re-run repo exploration if code exists, because structural drift should be detected from fresh inspection rather than stored in the doc.
