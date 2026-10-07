---
name: check-work
description: Use before handing back or opening a PR for a code change that is large or risky (authorization, shared state, concurrency, persistence, deployment, public contracts), including when you already plan to brief a reviewer yourself, and when asked to review a PR, branch, commit, or diff. Not for automatic use on small low-risk fixes or on document and admin work.
---

Your own tests show the change does what you intended. This review exists to find what you did not think of: paths the tests never exercise, interactions across boundaries, and fixes that break something else. Re-reading your own work rarely finds these; a reviewer who approaches the change fresh often does.

Use it before handing back or opening a PR for a change that crosses module boundaries or touches authorization, shared state, concurrency, persistence, deployment, or a public contract, however few lines it has. For small low-risk changes, your normal verification is enough; do not re-review each fix in a bug-fix loop.

Establish what is being reviewed and against what: the agreed requirements, project guidance, and decisions made during the work. A request to review authorizes findings, not edits.

Start one or more reviewers in fresh context, not forked from this conversation. Prefer a model from a different family than your own when one is available; it shares fewer of your blind spots. Give them the requirements, the diff and its base, relevant guidance, where you suspect risk, and which checks already ran so they need not repeat them. Tell them they are the reviewer and that checking the running result stays with you. Leave out your judgment that the change is correct. Split focus across reviewers when the change is large. If you will keep editing while a review runs, give the reviewer its own checkout, such as a separate worktree; a reviewer sharing your working tree either blocks your edits or reads a moving target. If fresh reviewers are unavailable, review it yourself and say the review was not independent. When the user asks you to review someone else's change, you are the reviewer; add reviewers only if the change is large.

If another agent started you to review its change, you are the reviewer: do not start other agents, edit the checkout, or drive the running app or a browser. Run existing tests, or a scratch reproduction outside the checkout, when that settles a finding, and say what you could not check.

Look for findings with a concrete consequence: a reachable failure, an unmet requirement, or a real maintenance cost. Problems that existed before the change matter only when the change exposes or depends on them. Style preferences are not findings.

Decide each finding explicitly: fix it at its cause, report it, or reject it with a reason. Do not drop findings silently, remove the feature to make a finding disappear, or expand the change beyond what was agreed. When fixes change behavior, have what they touched reviewed again.

As the author, when the change affects what users see and you can check the running result at reasonable cost, do so; otherwise say what you could not observe.

Report what the review found, what you changed, what you declined and why, and what remains unverified. Do not claim something works because the code looks right. Finish when the requested scope is covered and worthwhile fixes are done.
