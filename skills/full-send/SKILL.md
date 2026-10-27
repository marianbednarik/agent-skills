---
name: full-send
description: "Use when the user says \"full send\", or hands off a change to take all the way to a merged pull request without them watching, including when they add that you should not merge."
---

The user is not watching. Your updates and your final message go unread until long after you stop, and nobody will prompt you again if you stop early. You own the work from its current state to a merged PR, or to a PR ready for the user to merge if they said not to merge.

**What the request grants.** For this task only: merging the PR once the gate below passes; rebasing this task's branch and pushing it with `--force-with-lease`; and the test methods proof needs (running the app or a dev server, browser automation, simulators, screenshots), even where project guidance says to ask first. Project rules about how to test still apply. It does not grant deleting data, touching production, changing things outside the repository, closing PRs, pushing to any other branch, bypassing branch protection or using admin merges, or skipping a harness approval prompt. If the user said not to merge, also do not enable auto-merge or enter a merge queue, and switch off any that is already set.

**Proof.** Proof is evidence you observed yourself in this session. Use the most direct kind the change allows: reproduce the original failure, fix it, and watch the same reproduction pass; run the checks the repository's CI runs; add one focused test that fails without the fix when the repository has a test setup. For anything users see, run it, look at each state you trigger, and keep screenshots for the reviewer and the report. Green mocked tests do not prove the experience works. If you cannot prove a change, you do not have the confidence to merge it.

**Review.** No person will read the diff before it merges, so every code change gets an independent review; documentation-only changes need none. Use the `check-work` skill if it is installed, including its rules for weighing findings and bounding rounds; otherwise brief a reviewer in fresh context yourself. Two failures matter here: merging with a real finding unresolved, and growing the PR by fixing every edge case a reviewer can imagine. Fix what users will realistically hit; decline the rest with a written reason.

**The PR.** Start a branch if you are on the default branch. Rebase onto the latest default branch before opening the PR, write the description around the problem it solves, and add one line on how you proved it. Open a real PR, not a draft, so checks and review bots run. Post any comment through the `leaving-pr-comments` skill if it is installed.

**Waiting.** Do not end your turn while checks or reviews are pending unless something will wake you. Use the harness's PR watch tool when it has one (in T3 Code, `watch_pull_request`) instead of writing a polling loop or `sleep`; without one, use a single blocking command that ends on its own. Treat each wake as news, then check the gate yourself. Stop watching before you hand back.

**Merge gate.** On the latest commit: your proof covers every change in the diff; required checks pass; each review finding is fixed or declined with a reason; no human review still requests changes; and the branch is up to date with its base and mergeable. Fetch and check once more right before merging. Merge with the method the repository uses, and if it uses a merge queue or auto-merge, stay until GitHub reports the PR merged.

**Asking.** A question in an ordinary message looks like a finished thread, so ask through the harness's question tool, with the context in the question: the PR link, what blocks you, and the options with your recommendation first. Ask only when you cannot prove the change, the gate cannot pass and you cannot fix that, the next step is outside the grant, the goal is ambiguous in a way that changes the result, or another PR makes this one obsolete. Decide everything else yourself and list those decisions in the report. If no question tool exists or no answer comes, leave the PR open and unmerged and start your final message with the question.

**Report.** Lead with the outcome: the PR link and merge commit, or the PR's ready or blocked state. Then the proof, with screenshots for anything users see; what review found, what you fixed and declined; the decisions you made for the user; and what remains unverified.
