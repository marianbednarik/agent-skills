---
name: check-work
description: >
  Review completed implementation work before handoff. Automatically use after
  finishing a feature, bug fix, refactor, or other nontrivial code change, and
  when asked whether an implementation is ready. Do not trigger for planning,
  diagnosis, repo-wide audits, or tiny mechanical edits.
---

# Check Work

Before handing implementation back, stop building and read the work that
actually exists. Marian should not have to ask whether it can be simplified;
assume he would, and answer that first.

Establish the scope from the requested outcome and the relevant diff or working
tree. Exclude unrelated pre-existing changes.

Ask, and act on the answers:

- Does the implementation satisfy the requested behavior, including easy-to-miss
  states and preserved behavior?
- Is there a smaller coherent result: parallel paths that should be one path,
  one-use indirection, unnecessary wrappers, speculative branches, or defensive
  handling of impossible internal states?
- Does the change live at the right owner and follow the project's coherent
  patterns, or did it invent a second pattern for the same concept?
- Did it make another path, abstraction, dependency, or comment obsolete?
- Do the tests protect meaningful behavior, or merely add volume and freeze the
  implementation?
- What relevant validation has actually proved the result?

## Independent Review

When subagents are available, use one fresh read-only reviewer when independent
scrutiny would materially improve confidence, especially when the change:

- affects a high-consequence boundary such as persistence, migrations, public
  contracts, authentication, security, concurrency, destructive behavior, or
  compatibility
- crosses meaningful owners or layers, restructures or removes an existing path,
  introduces substantial structure or indirection, or changes interacting states
- touches unfamiliar critical code or lacks strong validation for its risky
  behavior

Skip delegation for coherent, localized work with strong validation. Diff size
alone is not a reason to delegate.

Give the reviewer the user-visible goal, review scope, relevant constraints, and
suspected risks. Ask for evidence-based findings about correctness, missing
behavior, architecture drift, validation gaps, and whether a smaller coherent
implementation is available. The reviewer must not edit files, alter working
state, or invoke this skill recursively.

Wait for the reviewer before handoff. While it works, gather objective validation
if useful, but do not duplicate the delegated review. Treat its report as input,
not authority: verify material findings yourself. The main agent owns any
authorized fixes, final synthesis, and handoff.

Fix safe in-scope issues and rerun the checks affected by those fixes. Do not
cross a consequential boundary in behavior, dependencies, compatibility, or
ownership without authorization.

Report the delivered outcome, material improvements made during review,
validation and what it supports, important unverified behavior, and any
remaining risk or required user action. Omit routine review narration and
file-by-file changelogs.

For review-only requests, report findings without editing.

## Gotchas

- Seek the smallest coherent implementation, not the smallest diff or lowest
  line count.
- Do not turn personal syntax preference or unrelated cleanup into a blocker.
- Passing checks are evidence, not a substitute for reading the implementation.
- Use a readiness label only when Marian explicitly asks for a readiness
  decision.
