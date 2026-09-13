---
name: project-context
description: Establish or refresh durable project intent, technical rationale, domain language, and design direction. Use when asked to set up, capture, or update project context.
---

Preserve agreed understanding that helps future agents make good decisions
and cannot be reliably recovered from the code alone.

Read relevant existing documents, conversation, and implementation. Distinguish
settled decisions from assumptions and open questions. Ask where missing intent
matters; do not invent reasons for choices merely because they exist in code.

Use these document roles by default:

- PROJECT.md: project identity, purpose, users, product priorities, and
  deliberate scope boundaries.
- ENGINEERING.md: technical intent, ownership boundaries, available
  infrastructure, consequential choices and their reasons, and constraints
  that affect future proposals.
- LANGUAGE.md: agreed domain terms, distinctions, relationships, and rules.
- DESIGN.md: visual and interaction intent, including character, hierarchy,
  density, motion, feedback, and principles for extending the interface.

Respect an established documentation layout. If CONTEXT.md owns the glossary,
maintain it instead of introducing LANGUAGE.md. Follow CONTEXT-MAP.md when
present and consult relevant existing ADRs. Keep each decision authoritative
in one place.

Record decisions and enough rationale to guide future choices. Include
technical specifics when they express durable constraints or ownership;
leave current schemas, file layouts, commands, inventories, and exact design
tokens to their existing sources of truth.

Keep decisions in the appropriate evergreen document by default. Use a
separate decision record when its history or substantial rationale warrants
one, or when the project follows that convention. Link rather than duplicate.

When refreshing context, distinguish:

- Implementation consistent with existing intent: no update needed.
- A deliberate change to durable intent: update its authoritative document.
- An unexplained disagreement between code and intent: surface and resolve it.

Do not rewrite intent merely to make an implementation appear consistent.
Replace superseded guidance so current direction is clear, preserving useful
history where the project maintains it.

Use the templates as flexible scaffolds. Create documents and sections only
where they carry useful information. Keep template instructions, temporary
plans, progress reports, and unresolved speculation out of the finished docs.

Make the documents discoverable through concise, task-specific pointers in
the project's AGENTS.md. Reuse existing routing and keep content in its
authoritative document rather than copying it into always-loaded guidance.

Report what understanding was captured or changed and what remains unresolved.
A refresh that requires no edits is a valid result.
