---
name: full-send
description: "Use when the user says \"full send\", or hands off a change to take all the way to a merged pull request without watching, including when they add not to merge."
---

The user is not watching. Your updates go unread until after you stop, and nobody will prompt you again if you stop early. Own the work from its current state to a merged PR, or a ready-to-merge PR if asked not to merge.

## Authority

Granted for this task only:
- Merge the PR once the merge gate passes.
- Rebase this task's branch and push with `--force-with-lease`.
- Run the app, dev server, browser, or simulator needed to prove the change, even where project guidance says to ask first (project rules on how to test still apply).

Not granted: deleting data, touching production, changing anything outside the repo, closing PRs, pushing to any other branch, bypassing branch protection or using admin merge, or skipping a harness approval prompt. If asked not to merge, also keep auto-merge and merge queues off.

## Proof

Proof means evidence you observed yourself in this session:
- Reproduce the failure, fix it, and watch the same reproduction pass.
- Run the checks CI runs, and add a focused test that fails without the fix when the repo has tests.
- For UI changes, run the app, inspect each state you changed, and keep screenshots for review and the final report. Green mocked tests do not prove UI works.

If you cannot prove the change, do not merge it.

## Review

No human will read the diff before merge, so run the `council` skill on every code change (docs-only changes need none). Do not leave disputed findings unresolved when merging; fix what users will realistically hit, decline unrealistic edge cases and style nits with a one-line reason, or ask through the question tool if a serious concern remains open.

## PR and waiting

Branch off the default branch if needed, rebase onto its latest commit, and open a real PR (not a draft) whose description explains the problem, how you proved it, and includes the council review table when one ran. Use `leaving-pr-comments` for any PR comment.

Never end your turn while checks or reviews are pending unless a watch will wake you. Use `watch_pull_request` (or a single blocking command outside T3 Code), re-check the gate on each wake, and unwatch before handing back.

## Merge gate

On the latest commit:
- Proof covers every change in the diff.
- Required checks pass.
- Code changes had an independent review, with every finding fixed or declined with a reason.
- No human review requests changes.
- Branch is up to date with its base and mergeable.

Fetch and check once more right before merging. Use the repo's merge method; with auto-merge or a merge queue, stay until the host reports the PR merged.

## When to ask

A question in a normal reply looks like a finished thread. Use the harness's question tool with the PR link, blocker, and options (recommendation first), and ask only when:
- You cannot prove the change, resolve a serious review concern, or pass the gate.
- The next step is outside your authority grant.
- The goal is ambiguous in a way that changes the result.
- Another PR makes this one obsolete.

Decide everything else yourself and list those decisions in the report. If no question tool exists or no answer arrives, leave the PR open and start your final message with the question.

## Report

Lead with the outcome (PR link and merge commit, or ready/blocked state). Follow with proof and UI screenshots, what review found, fixed, and declined, decisions you made, and anything unverified.
