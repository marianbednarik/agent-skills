---
name: writing-for-agents
description: Create or revise agent-focused documentation, including skills, AGENTS.md, specs, and project context. Remove unnecessary explanation and restatements of code while preserving decision-relevant meaning. Human-facing communication retains the default clear prose.
---

Optimize for useful information per token. Write for a technically competent agent: use precise, established terminology, compact statements, and explicit relationships. Omit conversational framing, general tutorials, repeated summaries, and explanations that add no project-specific understanding.

Before adding descriptive detail, ask what it contributes beyond readily inspecting code, configuration, or tooling. Omit obvious function walkthroughs, file inventories that add no navigation value, and copied implementation details. Preserve explicit contracts, consequential constraints, and non-obvious operational facts when they guide future work, even if code currently implements them. Reference the authoritative source for exact, changeable details.

Preserve intent, rationale, ownership, exceptions, and meaningful distinctions. General technical knowledge does not supply project-specific context. Keep enough reasoning to guide future decisions; distinguish settled intent, assumptions, and open questions without inventing missing reasons. Compression must not change the meaning or remove necessary qualifications.

Let the document's purpose govern what belongs in it. Respect existing ownership and authoritative sources; a writing pass does not expand scope or turn task details into durable project context. Remove obsolete or conflicting guidance and consolidate duplication when revising.

Structure for selective reading. Keep related rules and caveats together. Use paragraphs, lists, tables, or examples where they convey relationships efficiently; avoid exhaustive hypothetical catalogues. For instructions, retain the triggers, scope, authority boundaries, and completion conditions that affect execution. Prefer decision criteria over fixed sequences unless ordering matters.

Keep essential guidance at the point of use. Move substantial conditional detail behind references that say when to read it; verify those references. Avoid splitting short, coherent documents merely to create more files.

Apply this style according to the document's primary purpose, including agent-focused project context Marián also reads. Compact technical writing should remain understandable to him. Respect the requested audience and format; explain changes to Marián in the usual clear prose. A shorter document is useful only if it remains accurate and actionable.
