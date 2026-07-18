---
name: check-work
description: >
  Post-implementation quality review. Automatically use after completing a
  feature, bug fix, refactor, or other nontrivial code change, before final
  handoff. Also use when asked to assess whether an implementation is ready.
  Do not trigger for planning, diagnosis, repo-wide audits, or tiny mechanical
  edits.
---

# Check Work

Switch from builder mode to reviewer mode before handing implementation work
back to the user.

Establish the review scope from the requested outcome and the work performed.
Inspect the working tree, staged and untracked files, and the branch diff against
the relevant base when needed. Read applicable project guidance and exclude
unrelated pre-existing changes.

First judge the implementation against the user-visible goal, project
conventions, existing architecture, and behavior worth preserving. Look for
correctness problems, missing behavior, scope drift, architecture or style
drift, obsolete paths, and important validation gaps.

Then perform a deliberate simplicity pass. Seek the smallest coherent final
implementation, not the smallest diff or lowest raw line count. A slightly wider
edit at the concept owner is better when it reuses an established path,
collapses parallel logic, or removes code made obsolete by the change.

Challenge every added abstraction, helper, wrapper, branch, state field, file,
dependency, fallback, or compatibility path. It should serve a current
requirement or an established project boundary. Look especially for speculative
generality, defensive handling of impossible internal states, one-use
indirection, duplicated paths, and comments compensating for unclear code.

Treat line count and file growth as review signals, never targets. Explicit
cases, tables, tests, generated code, and inherently detailed behavior may
justify many lines. Terse code that hides concepts, ownership, or state is not
simpler.

Treat a behavior-preserving simplification as material when it removes a concept,
path, dependency, or meaningful future change cost. Do not block completion for
code golf, personal syntax preferences, or broad cleanup unrelated to the
change.

Run the strongest relevant validation that is practical. Treat passing checks as
evidence, not a substitute for inspecting the changed behavior or implementation
shape. State exactly what could not be run or verified.

When the active harness supports subagents, use one fresh read-only reviewer if
any of these apply:

- the change crosses meaningful ownership boundaries or interacting layers
- it affects persistence, migrations, public contracts, authentication,
  permissions, security, concurrency, destructive behavior, or compatibility
- it substantially restructures or removes an existing implementation path
- it introduces substantial new structure or indirection relative to the
  behavior gained
- it changes a multi-step user flow or several interacting states
- validation is weak or incomplete for the risky behavior
- it touches unfamiliar critical code where independent scrutiny would
  materially improve confidence

Do not delegate solely because a diff has many lines. Skip delegation for
coherent, localized changes with strong validation.

Give the reviewer the user-visible goal, review scope, relevant constraints, and
suspected risk areas. Ask it to report evidence-based findings about correctness,
missing behavior, architecture drift, validation gaps, and whether a smaller
coherent final implementation is available. The reviewer must not edit files,
alter working state, or invoke this skill recursively.

Wait for the reviewer before final handoff. While it works, you may gather
objective validation evidence, but do not duplicate the delegated review or hand
off early.

Treat the reviewer report as input, not authority. Verify its findings yourself.
The main agent owns the final synthesis, any authorized fixes, and the handoff.

Use the review as an internal completion gate, not a ceremonial verdict. When
implementation is authorized, fix safe in-scope issues and rerun affected checks.
A simplification may touch more lines than the original patch when it removes
concepts or parallel paths while preserving the agreed behavior. Do not expand
into unrelated cleanup or cross consequential boundaries in behavior,
dependencies, compatibility, or ownership without authorization. If completion
depends on missing authority, a user decision, external state, or unavailable
critical evidence, state the concrete blocker or limitation.

After implementation, lead with the delivered outcome. Include only information
that materially helps the user understand or trust the result:

- review-driven improvements, especially meaningful simplifications
- validation performed, its result, and the behavior it supports
- important behavior that remains unverified
- remaining risk, blocker, or required user action

Omit empty sections, routine review narration, and a readiness label. Do not
repeat the diff as a file-by-file changelog.

For a review-only request, report findings without editing. If the user
explicitly asks for a readiness decision, answer with `ready`, `ready with
caveats`, or `not ready`, followed by the concrete evidence, caveats, or blockers
that make the distinction useful.
