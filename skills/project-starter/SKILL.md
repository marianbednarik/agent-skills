---
name: project-starter
description: >
  Start or re-ground a project by exploring the repo, discussing product intent,
  and writing a lean evergreen PROJECT_DIRECTION.md with context future agents
  cannot infer from code. Use for new projects, major pivots, or under-documented
  repos; not for ordinary feature planning or implementation sequencing.
---

# Project Starter

Help the user capture the durable "why and vibe" of a project.

Explore first. Read the repo before asking questions the code can answer.

Have a focused conversation, but do not run a canned questionnaire. Ask grouped questions only where the project intent is unclear, and include your recommended default when a choice is open. For many personal projects, assume the primary user is the user unless they say otherwise.

Act as a product-minded technical partner. Push back on vague direction, scope creep, overloaded terms, and choices that create long-lived complexity without a clear payoff.

Write or update `PROJECT_DIRECTION.md` using `PROJECT_DIRECTION.template.md` as a starting shape. Keep it lean and evergreen:

- Capture product intent, taste, durable constraints, and non-obvious project preferences.
- Do not include current implementation plans, next steps, roadmaps, feature inventories, stack facts, or file structure.
- Do not repeat `AGENTS.md` or facts an agent can discover from the repo.
- If a hard-to-reverse decision is truly durable, capture the reason here instead of creating an ADR by default.

If the conversation reveals settled project-specific terminology, suggest using the `ubiquitous-language` skill. Do not force terminology work at project start when the language has not emerged yet.

End with a short summary of what direction was captured, what remains unclear, and whether a separate implementation-planning session should follow.
