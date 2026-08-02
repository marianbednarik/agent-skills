---
name: project-context
description: >
  Establish or refresh durable project context when Marian asks to document
  project direction, set up agent context, or update stale context. Capture only
  decisions future agents cannot reliably infer, and place each one in the
  narrowest useful instruction or document layer. Do not trigger merely because
  a project started, work finished, or context files are absent.
---

# Project Context

Capture durable information future agents need but cannot reliably infer from
the repository. Choosing where it belongs is part of the work.

## Choose The Layer

- **Root or nested `AGENTS.md`:** instructions that must apply automatically to
  every task in the repository or a particular subtree.
- **On-demand project documents:** narrative context that is relevant only to
  some work and should be read when the task calls for it.
- **A skill:** a reusable task-shaped behavior with a recognizable trigger.
- **Nothing:** information already clear from the repository, too temporary to
  preserve, or too weak to justify future context.

Do not place sometimes-relevant guidance into always-loaded instructions merely
because that is convenient.

Read the repository and existing context before asking questions. Where intent
remains unclear, ask grouped questions with your inferences and recommended
defaults so Marian can correct something concrete.

Create or update only documents that would materially improve future work. Use
the templates in this skill as flexible scaffolds, not schemas.

Document ownership:

- `PROJECT.md`: purpose, users, product taste, durable constraints, and reasons
  behind project-level decisions
- `DESIGN.md`: durable visual and interaction direction for a meaningful
  user-facing interface
- `ENGINEERING.md`: non-obvious architecture, chosen primitives, external
  systems, operations, contracts, and technical sharp edges
- `LANGUAGE.md`: project terminology and distinctions future agents could misuse

Keep the result lean and evergreen. Record decisions, constraints, conventions,
and reasons. Exclude plans, roadmaps, inventories, temporary state, obvious stack
facts, file trees, and details better read from the implementation.

Do not change always-loaded instructions or unrelated documents unless the
request clearly includes them. When refreshing context, update only what
actually changed and mention stale material outside the requested scope rather
than silently rewriting it.

Report what was captured, which layer it belongs to, and what remains unclear.

## Gotchas

- Creating no document is a valid result.
- Most projects do not need all four context documents.
- Do not copy template guidance into the finished artifact.
- Prefer code as the source of truth for exact tokens, versions, and values
  unless the exact value is itself a durable constraint.
- Do not duplicate the same fact across context layers.
