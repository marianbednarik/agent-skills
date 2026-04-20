# AGENT.md

## Goal

Optimize for human readability, clear ownership, and one clean current-state implementation. Prefer the right boundary over the smallest local diff.

Use this file as the universal operating policy. Use `PROJECT_DIRECTION.md` for project-specific intent and `UBIQUITOUS_LANGUAGE.md` for canonical domain terms.

## Operating Rules

- Work with the repo's existing architecture when it is coherent. Do not create a parallel pattern for the same concept.
- Keep one owner per concept. Entrypoints, routes, pages, and screens should compose; they should not become the home for reusable business logic or repeated UI behavior.
- Prefer a few deep modules with small public interfaces over many shallow helpers, wrappers, or `utils`.
- First use can stay local. Second real use must trigger extraction into a shared primitive, pattern, or domain module.
- Validate and normalize untrusted data only at boundaries: network, storage, browser/runtime APIs, and user input.
- Inside the app, keep one canonical internal shape. Do not add compatibility shims, migration branches, silent fallbacks, or dual codepaths unless explicitly requested.
- When internal state is invalid, fail loudly with a clear diagnostic and recovery guidance instead of silently adapting.
- Keep global styles limited to tokens, reset, typography, and tiny utilities. Feature styles belong with the owning feature or component.
- For interaction-heavy UI, reuse existing primitives or proven headless primitives instead of hand-rolling the same behavior twice.
- Delete or replace obsolete code as part of the change. Do not leave known structural cleanup for later.

## Before Coding

Answer these before writing code:

1. What user-visible behavior is changing?
2. Which module should own it?
3. What existing code already covers a similar concept?
4. Is this the first instance or the second real use?
5. What old code should be deleted or replaced?
6. What 1-3 behaviors are important enough to test?

If these answers are fuzzy, stop and propose a better boundary before implementing.

## Align On Direction When

Pause and confirm direction if the change has multiple reasonable homes or meaningfully changes product shape.

- Check with the user before moving a concept into a new shared owner when there are multiple plausible owners.
- Check with the user before promoting a feature-local pattern into a cross-feature primitive, pattern, or domain abstraction.
- Check with the user before simplifying by removing, merging, or hard-cutting behavior the user may still value.
- Check with the user before introducing a new top-level dependency, framework pattern, or architectural layer.
- Check with the user before deleting or restructuring code that may conflict with active in-progress work.
- Do not stop for routine cleanup when the direction is obvious: local splits within the same owner, second-use extraction into an established pattern, renames, file moves, dead-code deletion, or internal simplification that preserves behavior.
- When escalating, present the decision, the recommended direction, the main tradeoff, and what becomes simpler afterward.

## Testing

- Test behavior through public interfaces.
- Prefer a tracer-bullet test first, then grow coverage in vertical slices.
- Favor integration and boundary tests over selector-heavy, mock-heavy, or helper-level tests.
- If behavior did not change, refactors should not require major test rewrites.

## Pause And Refactor When

- A file becomes large and mixed-responsibility.
- A page or screen starts owning multiple workflows or interaction modes.
- A component grows many booleans, state cells, or branches.
- A second modal, form, card shell, dropdown, or normalization path appears.
- New code only fits by appending to the nearest large file.

## Absolute Bans

- No giant mixed-responsibility files by default.
- No duplicate local implementation of an existing pattern.
- No feature-specific additions to a global CSS dump.
- No speculative abstractions for hypothetical future reuse.
- No implementation-detail tests as the main form of coverage.
- No compatibility code without explicit approval and clear deletion criteria.
