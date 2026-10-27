---
name: check-work
description: Use before handing back or opening a PR for a code change that is large or risky (authorization, shared state, concurrency, persistence, deployment, public contracts), including when you already plan to brief a reviewer yourself, and when asked to review a PR, branch, commit, or diff. Not for automatic use on small low-risk fixes or on document and admin work.
---

Your own tests show the change does what you intended. This review exists to find what you did not think of: paths the tests never exercise, interactions across boundaries, and fixes that break something else. Re-reading your own work rarely finds these; a reviewer who approaches the change fresh often does.

Use it before handing back or opening a PR for a change that crosses module boundaries or touches authorization, shared state, concurrency, persistence, deployment, or a public contract, however few lines it has. For small low-risk changes, your normal verification is enough; do not re-review each fix in a bug-fix loop.

Establish what is being reviewed and against what: the agreed requirements, project guidance, and decisions made during the work. A request to review authorizes findings, not edits.

Start one or more reviewers in fresh context, not forked from this conversation. Prefer a model from a different family than your own when one is available; it shares fewer of your blind spots. Otherwise use one at least as capable as your own. Give them the requirements, the diff and its base, relevant guidance, where you suspect risk, which checks already ran so they need not repeat them, and, for changes users see, screenshots of each state you checked so they can judge the look as well as the code. Tell them they are the reviewer and that checking the running result stays with you. Leave out your judgment that the change is correct. Split focus across reviewers when the change is large. If you will keep editing while a review runs, give the reviewer its own checkout, such as a separate worktree; a reviewer sharing your working tree either blocks your edits or reads a moving target. Have a reviewer in a worktree check out your branch detached: git lets a branch be checked out in only one worktree, so an attached checkout stops you switching back to the branch to apply fixes. If fresh reviewers are unavailable, review it yourself and say the review was not independent. When the user asks you to review someone else's change, you are the reviewer; add reviewers only if the change is large.

If another agent started you to review its change, you are the reviewer: do not start other agents, edit the checkout, or drive the running app or a browser. Run existing tests, or a scratch reproduction outside the checkout, when that settles a finding, and say what you could not check.

Look for findings with a concrete consequence: a reachable failure, an unmet requirement, or a real maintenance cost. Problems that existed before the change matter only when the change exposes or depends on them. Style preferences are not findings.

Decide each finding explicitly: fix it at its cause, report it, or reject it with a reason. Do not drop findings silently, remove the feature to make a finding disappear, or expand the change beyond what was agreed.

Judge each finding's weight yourself, whatever severity the reviewer gave it. Thorough reviewers list every path they can imagine, and fixing everything listed grows the change one cheap-looking guard at a time. Fix what breaks the intended use or what users will realistically hit. Decline the rest in one line, as a follow-up if it is worth keeping: races that need millisecond timing, inputs nobody sends, small performance costs, extra compatibility, and tests or guards the requirements do not need. Prefer the fix that deletes or narrows code; if review grew the diff, cut it back. The opposite failure is agreeing just to end the loop: keep a real finding open until it is fixed or you can show why it does not apply.

Run another round only when a fix changed behavior or a real finding is still open. Give that reviewer the earlier findings with what happened to each (fixed, declined and why, disputed with evidence), and ask it to check those and the changed code rather than review everything again. Stop after two rounds, or four when the change touches authorization, stored data, or concurrency; a round with only minor findings ends the loop early. Findings still disputed at the end go to the user with both sides in a few lines; running out of rounds is not approval.

As the author, when the change affects what users see and you can check the running result at reasonable cost, do so and show the user screenshots of what you checked; otherwise say what you could not observe.

Report how many rounds ran, what the review found, what you changed, what you declined and why, and what remains unverified. Do not claim something works because the code looks right. Finish when the requested scope is covered and worthwhile fixes are done.
