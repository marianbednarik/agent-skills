---
name: project-context
description: Create or maintain durable project intent, technical rationale, domain language, and design direction. Use when capturing or revising lasting project understanding, including during other work.
---

Preserve agreed understanding that helps future agents make good decisions and cannot be reliably recovered from the code alone. A decision confined to one feature can still matter to future work.

Read relevant existing guidance, conversation, and implementation. Distinguish settled intent, assumptions, and open questions; ask where missing intent affects the work. Do not invent reasons for existing choices, treat a suggestion as agreement, or record an inferred requirement as settled intent.

Reuse the project's documentation layout and keep each decision authoritative in one place. Follow existing routing such as CONTEXT-MAP.md and consult decision records relevant to the area. The templates offer possible homes, not a required document set:

- [PROJECT.md](PROJECT.template.md): purpose, users, product priorities, and deliberate scope boundaries.
- [ENGINEERING.md](ENGINEERING.template.md): technical intent, responsibilities, consequential choices and reasons, infrastructure constraints, and boundaries future changes should respect.
- [LANGUAGE.md](LANGUAGE.template.md): domain terms, distinctions, relationships, and rules.
- [DESIGN.md](DESIGN.template.md): visual and interaction intent and principles for extending the interface.

Capture enough rationale to guide future choices. Keep decisions in the relevant evergreen section by default. Use a separate decision record when substantial rationale or history warrants one, or the project follows that convention; link it from the relevant current guidance. Include technical specifics that express agreed contracts or constraints. Leave schemas, file layouts, commands, and exact design tokens to their existing sources of truth.

Keep delivery scope, tasks, progress, and unresolved exploration with the work record. Carry lasting decisions into project guidance while the agreed reasoning is available, linking the work when its history helps. Distinguish agreed future direction from implemented behavior when the difference affects current work.

When understanding changes:

- Implementation consistent with existing intent needs no context update.
- A deliberate change to durable intent updates its authoritative description.
- An unexplained disagreement between code and intent needs investigation or clarification; do not rewrite intent merely to match implementation.

Replace superseded guidance so current direction is clear, retaining useful history where the project maintains it. Mark superseded decision records and point to their replacements.

Make context discoverable through short pointers that say when it matters, using the project's AGENTS.md or existing routing. Point to relevant sections and current decisions so agents can read for their task without traversing the archive. Keep universally applicable constraints easy to find; leave detailed rationale in its authoritative home. Create or split documents only when useful content and distinct reading needs justify it.

Briefly report what understanding changed and any consequential uncertainty. No edits or new documents may be needed.
