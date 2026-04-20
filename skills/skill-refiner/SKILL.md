---
name: skill-refiner
description: >
  Create or revise Marian's personal agent skills by turning examples, rough ideas,
  repeated workflow pain, or existing bloated skills into concise behavior-first
  skills with strong trigger descriptions and minimal body guidance.
---

# Skill Refiner

Use this skill to shape skills for Marian's personal agent workflow.

Start by identifying the behavior that should change when a future agent loads the skill. If that behavior is unclear, discuss it before writing.

Prefer lean, opinionated skills:

- Make the YAML `description` do the discovery work. It should clearly say when the skill should trigger.
- Keep the body short. Future agents need guidance, not a script.
- Preserve the user's intent and taste more than the source skill's structure.
- Extract the best idea from examples; do not inherit their bloat.
- Avoid canned questionnaires, rigid categories, and artifacts unless they clearly improve future agent behavior.
- Prefer grouped questions with recommended defaults when clarification is needed.
- Do not repeat general agent abilities or facts the agent can discover from the repo.

Borrow good default skill hygiene:

- Every skill needs a `SKILL.md` with `name` and `description` frontmatter.
- Add references, scripts, or assets only when they materially improve reliability or avoid repeated work.
- Keep reference files one hop from `SKILL.md` and load them only when needed.
- Do not add README, changelog, quick-reference, or process docs inside a skill folder.

When refining an existing skill, decide whether to:

- tighten it in place
- split it into separate skills
- merge it with another skill
- demote it to project-local guidance
- delete/archive it because the behavior is not worth preserving

Before finalizing, reread the skill as if you were a future agent in a real project. Ask: would loading this make me act differently in the intended way? If not, rewrite until the answer is yes.
