---
name: plan-work
description: Capture an agreed direction as a spec or implementation tickets, or update existing work as decisions change. Use when asked to turn a conversation or plan into trackable work.
---

Preserve enough understanding for Marián and future agents to resume
the work after a gap: what matters, why, what is settled, and what comes next.

Use the conversation, relevant project context, and existing issues.
Check current repository reality where it affects the plan. Preserve
resolved decisions without repeating the interview; surface consequential
gaps or contradictions rather than filling them with assumptions.

Choose the output and granularity with Marián: one issue containing the
spec, a parent issue with implementation tickets, or updates to existing
work. Recommend the simplest structure that makes progress understandable.
A small change does not need a separate spec and ticket hierarchy.

Write for Marián as well as the implementing agent. Use plain language,
explain consequential technical choices, and make the intended outcome
easy to understand without reconstructing the original conversation.

Capture what the work needs:

- The problem, desired outcome, and why it matters.
- Agreed decisions, constraints, and useful rationale.
- Observable acceptance criteria and meaningful scope boundaries.
- Open questions or tentative ideas, clearly distinguished from requirements.
- References needed to recover deeper context.

Scale detail to the work. Describe behavior and responsibilities rather
than prescribing edits that assume today's file layout will remain.
Include technical specifics when they carry an agreed contract or
decision more accurately than prose.

When splitting work, prefer coherent, independently verifiable outcomes.
Use end-to-end slices where useful; let migrations, refactors, and other
work follow their actual dependencies. Avoid arbitrary ticket counts,
speculative preparatory work, and dependencies that merely impose an order.

Keep the overall direction and progress discoverable from the parent
issue when one exists. Give each ticket enough context to be understood
with its linked references.

GitHub Issues is Marián's default tracker. Follow project AGENTS.md
guidance for the authoritative repository and conventions, respecting
any explicit alternative. Resolve an ambiguous destination before
publishing. Create or update issues when requested; a drafting request
does not itself authorize publication.

When a project's tracking destination or non-obvious conventions are
established, record a concise pointer in its AGENTS.md or existing
work-tracking documentation if not already recorded.

When understanding changes, update the authoritative description so
current direction is clear. Retain useful discussion as history and
link related work rather than creating competing copies.

Feature-specific decisions can remain with the work. Use project-context
for decisions that become durable project guidance, linking to their
authoritative documents.

Finish with the created or updated work, its relationships, and the next
action or unresolved decision. Capturing a plan does not authorize its
implementation.
