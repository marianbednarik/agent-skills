---
name: check-work
description: Use before handing back or opening a PR for a code change that is large, or that touches authorization, shared state, concurrency, persistence, deployment, or a public contract however few lines it changes, including when you already plan to brief a reviewer yourself; and when asked to review a PR, branch, commit, or diff. Not for automatic use on small changes outside those areas, or on document and admin work.
---

Your own tests show the change does what you intended. This review finds what you did not think of: paths the tests never exercise, interactions across boundaries, and fixes that break something else. Re-reading your own work rarely finds these; a reviewer who approaches the change fresh often does.

## What to review against

Establish what is being reviewed and against what: the agreed requirements, project guidance, and decisions made during the work. A request to review authorizes findings, not edits. When the user asks you to review someone else's change, you are the reviewer; add reviewers only if the change is large.

A finding needs a concrete consequence: a reachable failure, an unmet requirement, or a real maintenance cost. Problems that existed before the change matter only when the change exposes or depends on them. Style preferences are not findings.

## Starting reviewers

Start one or more reviewers in fresh context, not forked from this conversation. Prefer a model from a different family than your own, since it shares fewer of your blind spots; otherwise one at least as capable as yours. Split focus across reviewers when the change is large. If no fresh reviewer is available, review it yourself and say the review was not independent.

Give each reviewer:
- the requirements, the diff and its base, and relevant guidance;
- where you suspect risk, and which checks already ran so it need not repeat them;
- for changes users see, screenshots of each state you checked, so it can judge the look as well as the code;
- its role: it is the reviewer, and checking the running result stays with you.

Leave out your judgment that the change is correct.

If you will keep editing while a review runs, give the reviewer its own worktree with your branch checked out detached. A reviewer sharing your working tree blocks your edits or reads a moving target, and an attached checkout locks the branch so you cannot switch back to it to apply fixes.

## If you are the reviewer

If another agent started you to review its change, do not start other agents, edit the checkout, or drive the running app or a browser. Run existing tests, or a scratch reproduction outside the checkout, when that settles a finding, and say what you could not check.

## Weighing findings

Decide each finding explicitly: fix it at its cause, report it, or decline it with a reason. Do not drop findings silently, remove the feature to make a finding disappear, or expand the change beyond what was agreed.

Judge each finding's weight yourself, whatever severity the reviewer gave it. Thorough reviewers list every path they can imagine, and fixing everything listed grows the change one cheap-looking guard at a time. Fix what breaks the intended use or what users will realistically hit. Decline the rest in one line, as a follow-up if it is worth keeping:
- races that need millisecond timing, and inputs nobody sends;
- small performance costs and extra compatibility;
- tests or guards the requirements do not need.

Prefer the fix that deletes or narrows code; if review grew the diff, cut it back. The opposite failure is agreeing just to end the loop: keep a real finding open until it is fixed or you can show why it does not apply.

## More rounds

Run another round only when a fix changed behavior or a real finding is still open. Give that reviewer the earlier findings with what happened to each (fixed, declined and why, disputed with evidence), and ask it to check those and the changed code rather than review everything again. Stop after two rounds, or four when the change touches authorization, stored data, or concurrency; a round with only minor findings ends the loop early. Findings still disputed at the end go to the user with both sides in a few lines; running out of rounds is not approval.

## Report

When the change affects what users see and you can check the running result at reasonable cost, do so; otherwise say what you could not observe. Report how many rounds ran, what the review found, what you changed, what you declined and why, and what remains unverified. Finish when the requested scope is covered and worthwhile fixes are done.
