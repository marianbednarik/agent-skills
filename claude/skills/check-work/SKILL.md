---
name: check-work
description: >
  Self-review before handing back a nontrivial implementation. Use
  automatically after finishing a feature, bug fix, or refactor, and when asked
  whether something is ready. Do not use for tiny mechanical edits, planning,
  diagnosis, or repo-wide audits.
---

# Check Work

Before handing back, stop building and read what you actually wrote. Marian
should not have to ask "can this be simplified?" — assume he would, and answer
it first.

Ask, and act on the answers:

- Does this do the thing he asked, including the parts that are easy to skip?
- Is there a smaller coherent version? Parallel paths that should be one path,
  a helper used once, a wrapper around a thing that needed no wrapper, a branch
  for a state that cannot happen.
- Should any of this be extracted, or merged into an existing owner instead of
  living beside it?
- Is it consistent with how this repo already does this, or did you invent a
  second pattern?
- Did the change make something else obsolete that is still sitting there?
- Are the tests the few that protect real behavior, or did you pad?

Fix what is safe and in scope, then rerun what the fix affects. Flag anything
that needs his decision instead of deciding it yourself.

Report the outcome, not the process: what it does now, what you changed on
review, what you ran and what it proved, what is still unverified, and any
remaining risk. No file-by-file changelog, no readiness label unless he asked
for one.

## Gotchas

- Smallest coherent implementation, not smallest diff. A wider edit at the
  concept owner that deletes a parallel path is the smaller result.
- Line count is a signal, never a target. Explicit cases and real tests earn
  their lines; terse code that hides state does not.
- Do not expand into unrelated cleanup you noticed along the way. Mention it.
- For a review-only request, report and do not edit. Use `/code-review` when he
  wants the deep multi-agent pass.
