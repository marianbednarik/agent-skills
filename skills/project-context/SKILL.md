---
name: project-context
description: >
  Establish or refresh durable project context when the user asks to document
  project direction or update stale context. Create or revise lean PROJECT.md,
  DESIGN.md, ENGINEERING.md, or LANGUAGE.md only when they capture decisions
  future agents cannot reliably infer from the repository. Do not trigger merely
  because a project started, implementation or refactoring occurred, or context
  files are absent.
---

# Project Context

Capture the durable project context future agents need but cannot reliably infer
from the repository alone.

Inspect existing context documents and relevant repository evidence before asking
questions. Treat older, overlapping, or tool-specific documents as source
material, not structures that must be preserved.

Have a focused conversation where intent remains unclear. Ask grouped questions,
include recommended defaults, and state reasonable inferences so the user can
correct them instead of answering from scratch. For personal projects, infer the
project owner as the primary user when the available context supports it.

Act as a product-minded technical partner. Push back on vague direction,
overloaded terms, and decisions that create durable complexity without a clear
payoff.

Create or update only documents that would materially improve future work. Use
the matching template as a flexible scaffold: omit, merge, or rename sections
when that produces a clearer document. Italic template text is authoring guidance,
not content to copy into the finished document.

Document ownership:

- `PROJECT.md`: purpose, users, product taste, durable constraints, and reasons
  behind important project-level decisions
- `DESIGN.md`: durable visual and interaction direction, principles, and
  non-obvious conventions for a meaningful user-facing interface
- `ENGINEERING.md`: non-obvious architecture, chosen primitives, external
  systems, operations, commands, contracts, and technical sharp edges
- `LANGUAGE.md`: project-specific terminology, distinctions, relationships, and
  words future agents could misuse

Keep every document lean and evergreen:

- record durable decisions, constraints, conventions, and their reasons
- exclude current plans, next steps, roadmaps, inventories, and temporary state
- exclude stack facts, file structure, or behavior easily discovered from code
- do not duplicate `AGENTS.md` or another context document
- prefer the implementation as the source of truth for exact design tokens and
  other code-owned details unless an exact value is itself a durable constraint

Do not edit `AGENTS.md` or unrelated existing documents unless the user asks.
When refreshing context, update only documents whose durable information changed;
do not re-interview or rewrite everything by default. If context appears stale
outside the requested scope, mention it rather than changing it silently.

Before handoff, reread the result as a future agent. Remove anything quickly
inferable, duplicated, speculative, or included only because an older document
contained it.

End with what was captured or refreshed, which documents changed, what remains
unclear, and whether a separate implementation-planning session would help.
