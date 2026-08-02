---
name: skill-refiner
description: >
  Create, review, or revise Marian's personal Codex skills when he explicitly
  asks. Turn repeated prompts, rough ideas, observed workflow failures, or
  bloated skills into focused behavior with clear triggers, ownership, authority,
  and completion conditions. For review-only requests, recommend without editing.
---

# Skill Refiner

A skill earns its place by changing what Codex does in a useful, repeatable way.
If it only restates normal model competence, it is noise.

Start from the behavior Marian wants to change or the prompt he is tired of
repeating.

Before drafting, inspect applicable project instructions and neighboring skills.
Decide whether the behavior belongs in:

- this skill
- another existing skill
- global or project-specific agent guidance
- durable project context
- normal model judgment with no additional instruction

Avoid overlapping ownership and competing workflows.

Choose invocation deliberately: explicit for user-requested or external actions,
implicit for a clear specialist task, automatic only for a justified lifecycle
step, and situational when the decision itself is non-obvious.

Make the description carry the routing decision: what the skill does, when it
should trigger, and the closest situations where it should not.

Keep the body as short as reliability allows. Include only instructions that
change behavior, prevent an observed failure, preserve an authority boundary, or
make completion meaningfully verifiable. Prefer goals, constraints, and real
gotchas over scripted reasoning and speculative cautions.

Do not repeat general agent abilities, applicable guidance from another layer,
facts discoverable from the repository, or model- and harness-specific capability
inventories. Add templates, references, scripts, or schemas only when they save
real reconstruction or support required interoperability.

When refining an existing skill, consider tightening, merging, demoting, or
deleting it rather than assuming it must survive.

Before editing:

1. Test the description against requests that should and should not trigger it.
2. Check review-only, planning-only, and implementation-authorized cases where
   relevant.
3. Remove every line that would not change future behavior.
4. Show Marian the exact proposed text and wait for approval.

After approval, implement the agreed change and verify frontmatter, references,
the diff, and runtime wiring. For review-only requests, stop with
recommendations.
