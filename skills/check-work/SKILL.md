---
name: check-work
description: >
  Post-implementation readiness review. Automatically use after completing a
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

Judge the implementation against the user-visible goal, project conventions,
existing architecture, and behavior worth preserving. Look for correctness
problems, missing behavior, scope drift, architecture or style drift, obsolete
paths, unnecessary complexity, and important validation gaps.

Run the strongest relevant validation that is practical. Treat passing checks as
evidence, not a substitute for inspecting the changed behavior. State exactly
what could not be run or verified.

When the active harness supports subagents, use one fresh read-only reviewer if
any of these apply:

- the change crosses meaningful ownership boundaries or interacting layers
- it affects persistence, migrations, public contracts, authentication,
  permissions, security, concurrency, destructive behavior, or compatibility
- it substantially restructures or removes an existing implementation path
- it changes a multi-step user flow or several interacting states
- validation is weak or incomplete for the risky behavior
- it touches unfamiliar critical code where independent scrutiny would
  materially improve confidence

Do not delegate solely because a diff has many lines. Skip delegation for
coherent, localized changes with strong validation.

Give the reviewer the user-visible goal, review scope, relevant constraints, and
suspected risk areas. Ask it to report evidence-based findings about correctness,
missing behavior, architecture drift, test gaps, and avoidable complexity. The
reviewer must not edit files, alter working state, or invoke this skill
recursively.

Wait for the reviewer before declaring readiness. While it works, you may gather
objective validation evidence, but do not duplicate the delegated review or hand
off early.

Treat the reviewer report as input, not authority. Verify its findings yourself.
When this review follows an implementation request, fix safe in-scope issues and
rerun affected checks. When the user requested review only, report findings
without editing. The main agent owns the final verdict.

End with:

- readiness verdict: `ready`, `ready with caveats`, or `not ready`
- material findings and how they were resolved
- validation performed and its result
- important behavior that was not verified
- remaining risks or required next action

Use `ready` only when the implementation matches the requested behavior, the
change is coherent and in scope, relevant validation has passed, and no known
material finding remains unresolved.
