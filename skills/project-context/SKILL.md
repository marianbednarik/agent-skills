---
name: project-context
description: >
  Establish or refresh durable project context after project start, substantial
  implementation, refactors, product pivots, or design changes by reading the
  repo, interviewing the user where intent cannot be inferred, and writing lean
  PROJECT.md, DESIGN.md, ENGINEERING.md, or LANGUAGE.md only when those docs
  would materially help future agents.
---

# Project Context

Help the user capture or refresh the durable context future agents need but cannot reliably infer from code alone.

Explore first. List the repo's Markdown docs, then read the ones that look like durable product, design, engineering, domain-language, planning, or architecture context before asking questions the repo can answer. Treat tool-specific and older docs as source material for this skill's outputs, not as structures to preserve or files to clean up. Do not edit `AGENTS.md` or other existing docs unless the user asks; if docs look stale, overlapping, or superseded after the refresh, mention that in the final response.

Have a focused conversation, but do not run a canned questionnaire. Ask grouped questions only where intent, design direction, technical constraints, or terminology are unclear. Include your recommended default when a choice is open. For many personal projects, assume the primary user is the user unless they say otherwise.

Act as a product-minded technical partner. Push back on vague direction, scope creep, overloaded terms, and choices that create long-lived complexity without a clear payoff. State inferred assumptions so the user can correct them instead of making them answer from scratch.

Always write or update `PROJECT.md` using `PROJECT.template.md` as a starting shape. Keep it lean and evergreen:

- Capture project intent, taste, durable constraints, and non-obvious project preferences.
- Do not include current implementation plans, next steps, roadmaps, feature inventories, stack facts, or file structure.
- Do not repeat `AGENTS.md` or facts an agent can discover from the repo.
- If a hard-to-reverse decision is truly durable, capture the reason here instead of creating an ADR by default.

Treat italic explanatory text in the templates as authoring scaffolding; leave it out of final project docs unless the wording itself is genuinely useful content.

Write or update `DESIGN.md` using `DESIGN.template.md` only when the project has a meaningful user-facing interface. Follow Google's DESIGN.md alpha format: optional YAML frontmatter for real machine-readable tokens, then `##` sections in canonical order. Omit irrelevant sections, but keep the exact heading names and order for sections included. Avoid fake precision; use exact token values only when they are already settled or directly observed.

Write or update `ENGINEERING.md` using `ENGINEERING.template.md` only when there are non-obvious technical facts a good agent could still miss, repeatedly rediscover, or get wrong from code alone. Capture decisions, external systems, operations, commands, and project-standard primitives; avoid dependency inventories, file trees, and obvious stack facts.

Write or update `LANGUAGE.md` using `LANGUAGE.template.md` only when project-specific terminology has clearly emerged. Capture canonical terms, aliases to avoid, and important relationships; clarify terminology ambiguity with the user before writing assumptions into the doc. Skip generic programming terms unless the project gives them domain-specific meaning.

When refreshing an existing project, compare current docs against the repo and the user's stated changes. Update only the docs whose durable context changed; do not re-interview from scratch unless the existing docs are missing, thin, or clearly stale.

Before handoff, reread the produced docs as a future agent. Remove facts that are merely implementation inventory, quickly inferable from code, duplicated across docs without a distinct purpose, or included only because they appeared in an older document. Keep external contracts, product decisions, project conventions, sharp edges, and reasons the code alone would not explain.

End with a short summary of what was captured or refreshed, which docs were changed, what remains unclear, and whether a separate implementation-planning session should follow.
