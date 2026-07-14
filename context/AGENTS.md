Build code that a human maintainer would be happy to inherit. Prefer the right boundary over the smallest local diff, but scale the effort to the task.

Use this file as global engineering taste. Project and nested `AGENTS.md` files, project docs, tests, and coherent existing patterns override this file. When project style conflicts with this guidance, follow the project unless the task is to improve that style.

For nontrivial tasks, check for relevant project docs such as `PROJECT.md`, `DESIGN.md`, `ENGINEERING.md`, and `LANGUAGE.md`. Do not spend time hunting for docs that are not present.

## Task Scale

- For tiny mechanical changes, make the smallest safe edit, verify the obvious thing, and avoid architectural cleanup.
- For bug fixes, features, refactors, or cross-file changes, identify the user-visible behavior, owning module, existing patterns, relevant callers/tests, obsolete paths, and important behavior to verify before editing.
- For prototypes, spikes, or explicitly requested quick hacks, favor directness. Name the tradeoff and avoid hardening throwaway code prematurely.

## Code Shape

- Work with the repo's existing architecture when it is coherent. Do not create a parallel pattern for the same concept.
- Find the owner of a concept before editing. Model real concepts directly instead of spreading meaning across optional fields, boolean piles, generic modes, or repeated local logic.
- Read the boundary before changing it: exports, callers, tests, and established primitives.
- Prefer deep modules: small public interfaces hiding meaningful implementation. Avoid vague `utils`, shallow helper spray, and wrapper layers.
- First use can stay local. Second real use is evidence of a concept; extract toward the owning module or existing primitive, not a speculative abstraction.
- If new code only fits by expanding a large mixed-responsibility file, identify and recommend the better boundary before adding more responsibility.

## State And Data

- Keep one canonical internal shape. Normalize untrusted data only at boundaries: network, storage, browser/runtime APIs, and user input.
- Keep deterministic work in code: routing, retries, status handling, parsing, validation, and transforms should not depend on model judgment.
- Do not add compatibility shims, migration branches, silent fallbacks, dual codepaths, or legacy adapters unless the task is explicitly about compatibility, rollout, migration, or public API stability.
- For impossible internal state, fail loudly with a clear diagnostic. For untrusted boundary input, return a deliberate validation or recovery path.
- Delete obsolete code when it is proven obsolete by the change, tests, or project direction. Do not preserve old paths merely from anxiety.

## Change Discipline

- Reuse existing libraries and proven primitives already available in the project. Do not hand-roll another modal, dropdown, parser, state machine, or fetch/cache pattern when a good project-standard option exists.
- Keep global styles limited to tokens, reset, typography, and tiny utilities. Feature styles belong with the owning feature or component.
- Prefer small vertical changes that leave the repo cleaner than before. Avoid broad rewrites unless the current structure is the problem.
- When existing patterns conflict, choose the owner, newer path, or better-tested path. Do not average them into a hybrid.
- When ownership or architecture is ambiguous, state the assumption and recommended direction. Proceed when the choice is reversible and within scope; ask when it may remove valued behavior, add a dependency or layer, affect public behavior or compatibility, change ownership, or conflict with active work.

## Verification

- Test behavior worth preserving through public interfaces. Do not test implementation shape just to increase coverage, and do not weaken tests to fit the code.
- Prefer integration, boundary, and vertical-slice tests over mock-heavy, selector-heavy, private-helper tests.
- Refactors that preserve behavior should not require major test rewrites.
- Before finishing, run the most relevant available check when practical. If you cannot run it, state exactly what was not verified.
