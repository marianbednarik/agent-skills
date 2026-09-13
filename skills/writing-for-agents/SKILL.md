---
name: writing-for-agents
description: Write or refine documentation primarily intended for agents, including skills, agent instructions, and project-context references. Use when authoring these materials; human-facing tickets, PR descriptions, and commit messages retain Marián's human communication style.
---

Optimize for reliably understood information per token.

Write for an agent that already understands general technical concepts.
Use precise terminology, compact statements, and explicit relationships.
Omit conversational framing, generic explanations, repeated summaries,
and instructions that add nothing beyond applicable existing guidance.

Preserve information that changes decisions: intent, constraints,
ownership, rationale, exceptions, and non-obvious operational facts.
Compression should remove redundancy, not distinctions or reasons
needed to apply the guidance correctly.

Let the document's purpose govern its content. A writing style does not
expand what belongs in a document: evergreen project context still
captures durable understanding, while procedures and implementation
references serve their own purposes.

Structure for selective reading. Keep closely related rules and caveats
together. Use headings, lists, tables, or compact examples when they
make relationships easier to retrieve and apply.

Keep essential guidance at the point of use. Move substantial conditional
detail behind references that explain when to read them. Avoid splitting
short, coherent material merely to create more files.

Maintain one authoritative home for each fact or instruction. Reference
existing sources rather than copying them. Prefer inspecting code,
configuration, or tooling over documenting readily discoverable state;
record what those sources cannot explain.

For behavioral instructions, make the relevant trigger, scope, authority,
and completion conditions clear where they affect execution. Prefer
outcomes and decision criteria over a fixed sequence unless ordering
or exact steps materially affect correctness.

For descriptive context, distinguish settled intent, constraints, and
rationale. Preserve the project's established terminology and resolve
material ambiguity rather than disguising it with confident wording.

Include examples when they clarify a subtle distinction or prevent a
likely misreading. Avoid exhaustive catalogues of hypothetical cases.

When revising, remove obsolete or conflicting guidance and consolidate
duplication. Check references and preserve meaningful exceptions.
A shorter document is useful only if it remains accurate and actionable.

Apply this style to the agent-facing artifact. Explain the resulting
changes to Marián in the usual clear, human-facing language.
