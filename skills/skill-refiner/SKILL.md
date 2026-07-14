---
name: skill-refiner
description: >
  Create, review, or revise Marian's personal agent skills when he explicitly asks.
  Turn examples, rough ideas, repeated workflow pain, or existing bloated skills
  into behavior-first skills with clear ownership, trigger and authority
  boundaries, and only the guidance needed for reliable execution. For review-only
  requests, recommend changes without editing.
---

# Skill Refiner

Shape durable skills that make a future agent behave differently in a useful,
intentional way.

Start by identifying the behavior that should change. If the intended behavior,
trigger, or authority is unclear, discuss it before writing.

Before drafting, inspect applicable project instructions and neighboring skills.
Decide whether the behavior belongs in:

- this skill
- another existing skill
- global or project-specific agent guidance
- durable project context
- the model’s normal judgment without additional instruction

Avoid overlapping ownership or creating a second workflow for the same concept.

Choose the invocation model deliberately:

- explicit-only for user-requested capabilities or external actions
- implicit when the request clearly matches a specialist behavior
- automatic only for a justified lifecycle step
- situational when a decision itself is non-obvious

Front-load the YAML `description` with what the skill does, when it should trigger,
and important adjacent situations where it should not. Preserve Marian’s intent
and taste more than the source material’s structure.

Keep the body as short as reliability allows. Every instruction should change
behavior, prevent a demonstrated failure, define necessary authority, or make
completion verifiable. Prefer:

- outcomes and decision principles over scripted reasoning
- a few meaningful boundaries over repeated cautions
- explicit authority for review, implementation, or external action
- evidence and completion conditions over ceremonial workflow
- durable capability language over model-version-specific prompt hacks
- flexible scaffolds over rigid templates unless interoperability requires a
  schema

Extract the best idea from examples without inheriting their full workflow.
Avoid canned questionnaires, speculative abstractions, and artifacts that do not
materially improve future execution. Do not repeat general agent abilities,
applicable global guidance, or facts discoverable from the repository.

When a skill uses subagents, browser control, external services, or other special
capabilities, define only what normal agent judgment cannot safely infer:

- when the capability is warranted
- whether it may mutate state
- how work should be divided
- whether the parent must wait
- who owns synthesis and final judgment
- what fallback applies when the capability is unavailable

When refining an existing skill, decide whether to tighten it, split it, merge it,
demote behavior to another instruction layer, or delete it because the behavior
is not worth preserving.

Use standard skill hygiene:

- include a `SKILL.md` with valid `name` and `description` frontmatter
- add references, scripts, assets, or optional metadata only when they materially
  improve reliability or distribution
- keep referenced resources one hop from `SKILL.md` when practical
- do not add README, changelog, quick-reference, or process files inside a skill
  folder

Before finalizing:

1. Test the description against representative requests that should and should
   not trigger the skill.
2. Check planning-only, implementation-authorized, and review-only cases where
   relevant.
3. Reread the body as a future agent and remove anything that would not change
   its behavior.
4. Validate frontmatter, references, the resulting diff, and the repository’s
   canonical-source and runtime-wiring rules.

If the user requested review only, stop with recommendations. Once creation or
revision is authorized and material choices are resolved, implement and verify
the skill.
