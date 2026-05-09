---
name: frontend-design
description: >
  Design, redesign, polish, or review frontend UI with a product-aware visual
  design point of view. Use for websites, landing pages, app screens, dashboards,
  forms, components, empty states, responsive behavior, visual polish, and UI
  quality problems where layout, typography, color, motion, copy, or interaction
  design matter.
---

# Frontend Design

Make the interface feel designed for this product, this user, and this surface
instead of reaching for generic AI defaults.

Read durable context before designing when present:

- `PROJECT.md` for audience, intent, product taste, and durable constraints.
- `DESIGN.md` for visual direction, components, tokens, and design guardrails.
- `LANGUAGE.md` for user-facing terms when copy or IA matters.
- `ENGINEERING.md` for technical constraints that affect UI implementation.

Do not create or refresh those files from this skill. If durable project context
is missing or stale enough to block good design, suggest `project-context` and
continue with clearly named assumptions when the current task can still move.

Start by identifying:

- the user-visible job this UI must do
- who uses it, in what physical or emotional context
- whether the surface is `product` or `brand`
- the owning component, route, design system, or local pattern
- the existing assets, tokens, and components that should shape the work

For screenshot-led redesigns, critique the current UI against the user-visible
job and project design context before editing. Name what is working, what is
fighting the workflow, and what direction the first pass should take. Unless the
user asks to plan first, make the first implementation pass and treat follow-up
screenshots as design input for iteration.

For new screens in an existing product, design from neighboring surfaces before
inventing. Reuse the app's established layout rhythms, navigation patterns,
components, tokens, copy style, and state patterns unless the new screen has a
real job those patterns cannot handle.

Treat `product` and `brand` differently.

For product UI, design serves repeated task completion: prefer clarity, density
where useful, familiar affordances, consistent component vocabulary, fast
feedback, restrained motion, and complete states. System fonts and quiet palettes
can be the right answer. Avoid landing-page drama, decorative motion, invented
controls, and display typography in labels, forms, tables, or operational flows.

For brand UI, design is part of the value: commit to a point of view, use
imagery or visual assets when the subject calls for them, shape the first
viewport intentionally, and make typography, color, rhythm, and composition feel
specific. Avoid centered template stacks, generic icon-card grids, timid palettes,
placeholder blocks where real imagery belongs, and fashionable editorial moves
that do not fit the brief.

Before choosing fonts, colors, layout, or motion, reject the obvious reflexes:
purple gradients, beige SaaS editorial, glass cards, nested cards, identical
feature grids, generic hero metrics, Inter-by-default, low-contrast gray text,
oversized rounded icon tiles, and decoration that does not serve the user.

Build from the project inward:

- reuse established components, tokens, icon sets, data-loading patterns, and
  form primitives
- keep feature styles with the owning feature or component
- add new visual primitives only when they solve a real repeated problem
- remove obsolete UI paths, placeholders, and one-off styling introduced during
  the change

Design the whole state model, not just the happy path: default, hover, focus,
active, disabled, loading, empty, error, success, long content, short content,
small viewport, wide viewport, keyboard use, touch use, and reduced motion where
motion exists.

Use screenshots as the preferred visual iteration loop when the user can provide
them or when browser automation would be brittle, such as authenticated apps,
browser extensions, native shells, or complex local setup. Ask for a screenshot
when rendered judgment matters and you cannot reliably inspect the UI yourself.
When browser access is cheap and appropriate, inspect the rendered UI across the
viewports that matter and fix visible defects before handoff.

When reviewing a screenshot or rendered UI, look first for hierarchy, alignment,
text overflow, overlapping elements, broken responsive behavior, weak focus or
contrast, inconsistent component vocabulary, awkward empty/loading/error states,
and anything that makes the surface look generic or accidental.

End UI work with a concise design readout: what direction you chose, how it fits
the project context, what states or viewports were checked, and what visual risks
remain.
