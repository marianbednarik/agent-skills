Build code that a human maintainer would be happy to inherit. Prefer the right boundary over the smallest local diff.

Use this file as universal coding taste. Use `PROJECT.md` for project intent, `DESIGN.md` for design and frontend guidance, `ENGINEERING.md` for non-obvious technical context, and `LANGUAGE.md` for project-specific terms, when those files are available.

## Code Shape

- Work with the repo's existing architecture and idioms when they are coherent. Do not create a parallel pattern for the same concept.
- Find the owner of a concept before editing. Model real concepts directly instead of spreading meaning across optional-field soup, boolean flag piles, generic modes, or repeated local logic.
- Prefer deep modules: small public interfaces that hide meaningful implementation. Avoid shallow helper spray, wrapper layers, and vague `utils`.
- First use can stay local. Second real use is evidence of a concept; extract it into a shared primitive, pattern, or domain module.
- YAGNI means no speculative abstractions, not permission to duplicate a real pattern that already exists.
- If new code only fits by appending to a large mixed-responsibility file, pause and propose a better boundary.

## State And Data

- Keep one canonical internal shape. Normalize untrusted data only at boundaries: network, storage, browser/runtime APIs, and user input.
- Do not add compatibility shims, migration branches, silent fallbacks, dual codepaths, or legacy adapters unless explicitly approved.
- When invalid internal state appears, fail loudly with a clear diagnostic and recovery guidance instead of silently adapting.
- Delete or replace obsolete code as part of the change. Do not preserve old paths "just in case."

## Change Discipline

- Before coding, identify the user-visible behavior, the owning module, existing related patterns, the first-use vs second-use status, obsolete code to remove, and the important behaviors to verify.
- Reuse existing libraries and proven primitives already available in the project. Do not hand-roll another modal, dropdown, parser, state machine, or fetch/cache pattern when a good project-standard option exists.
- Keep global styles limited to tokens, reset, typography, and tiny utilities. Feature styles belong with the owning feature or component.
- Prefer small vertical changes that leave the repo cleaner than before. Avoid broad rewrites unless the current structure is the problem.
- Escalate when a change has multiple plausible owners, introduces a new architectural layer or dependency, removes behavior the user may value, relies on inferred product intent, or conflicts with active work. Recommend a direction when escalating.

## Testing

- Test behavior worth preserving through public interfaces. Do not test implementation shape just to increase coverage, and do not weaken tests to fit the code.
- Prefer tracer-bullet tests and vertical slices: one meaningful behavior, minimal implementation, then the next behavior.
- Favor integration and boundary tests over selector-heavy, mock-heavy, or helper-level tests.
- Refactors that preserve behavior should not require major test rewrites.

## Defaults To Avoid

- Giant mixed-responsibility files.
- Duplicate local implementations of an existing pattern.
- Feature-specific additions to global CSS dumps.
- Speculative abstractions for hypothetical reuse.
- Defensive guards that hide impossible states instead of exposing broken assumptions.
- Tests that mostly verify mocks, private helpers, selectors, or current file structure.
