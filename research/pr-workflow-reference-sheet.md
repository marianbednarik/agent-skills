# PR workflow reference sheet

Research date: 2026-10-27. Scope: what to take from Theo Browne's [tstack](https://github.com/t3dotgg/tstack) (commit `92e38e2`, 2026-10-27, MIT), a public set of PR-workflow skills for Claude Code and Codex. Result: new `full-send` and `leaving-pr-comments` skills, a bounded review loop and reviewer screenshots in `check-work`, and two lines in `context/AGENTS.md`.

## Evidence from real use

- Marián's repositories are solo: 100 merged PRs across five repos, no human or bot reviewers on recent ones, private repos without branch protection. CI exists in some (PAX `ci.yml`). No open PRs.
- About 34 of his session messages are just "merge" or "lgtm, merge": he reads the result, then approves. On 2026-10-25 he asked for PAX PRs to merge automatically once check-work and the reviewer agree, "but no doom loops and 6 review rounds and getting stuck on small edgecases". PAX `AGENTS.md` already encodes that as standing project policy.
- An unattended run already works without a skill: "Work on issue #191 please. Get it to a merged PR." produced a test that fails without the fix, a check in the loaded extension, an independent review, and a merge after CI (PR #198, 2026-10-13).
- His account of the loop: GPT-family reviewers find real problems but also nitpick and raise edge cases nobody will hit (millisecond races); Opus as the author tends to fix whatever is listed, so the loop grows the PR. He observed agents writing their own PR polling loops instead of using T3 Code's `watch_pull_request`. He reviews UI by screenshots rather than running the app.
- At work he leaves PR comments, and agent-written comments have gone out sounding like him. His work machine installs this skill set.

## tstack, skill by skill

| tstack skill | Decision | Why |
| --- | --- | --- |
| `full-send` / `full-stop` | Adapted as one explicit-only `full-send`; "don't merge" is a mode, not a second skill | Matches the "lgtm, merge" pattern. Kept: an explicit grant of what the phrase authorizes and what it does not, proof as evidence observed in this session, the merge gate, asking through the question tool because a plain-message question looks like a finished thread, listing decisions in the report. Left: the mandatory chain to sol-loop, file-pr and babysit-pr. |
| `sol-loop` | Ideas folded into `check-work` | Round budget with an exception for risky areas, the author triaging severity rather than trusting the reviewer's label, declining edge cases in one line, cutting a diff that review grew, and handing the next round the earlier findings with outcomes. Left: hardcoded model, telegraphic style, procedural steps. |
| `leaving-pr-comments` | Adapted | Useful on the work machine. Made host-neutral (plain-quote fallback where GitHub alerts do not render) and tightened. |
| `babysit-pr` + `pr-wait` | Left; one idea kept | No review bots, and T3 Code's watcher covers CI. Kept "use the watch tool, never write a polling loop" in global guidance and `full-send`. Revisit `pr-wait` if Greptile, Macroscope, or CodeRabbit is added, or for waiting outside T3 Code. |
| `council` | Left | Multi-model reviews are already asked for ad hoc and work; global delegation guidance covers routing. |
| `file-pr` | Left | His PR titles already lead with the problem; `full-send` carries the one line that matters. |
| `takeover`, `modernize` | Left | Solo work, no stale PRs. `modernize` (MODERNIZE / REWORK / CLOSE disposition) is the one to revisit if old PRs pile up. |

## Authoring lessons

Taken: positive, scoped permission grants that override a project's ask-first rules for one task; harness-specific failure knowledge that a capable model will not predict (unread questions, stopping while checks run); scripts for mechanical work that prose handles badly (`pr-wait`); a number where models drift (review rounds).

Not taken: phrase-trigger descriptions on model-invocable skills. tstack's `full-stop` was widened to fire on "a closing 'Full stop.' that reads like emphasis", which lets ordinary English start an autonomy grant; here such skills are explicit-only (`disable-model-invocation`, `allow_implicit_invocation: false`). Also not taken: model names in skills, and skills that require other skills. Naming a harness tool as an example, and handing a step to another skill with a fallback, are now allowed by the root `AGENTS.md` writing rules.

## Not tested

No probes: Marián judged that synthetic prompts cannot carry the context in which these skills matter, and that real use is the test. Watch in real use: whether `full-send` stops early or ends a turn while checks run; whether the two-round budget leaves real regressions unreviewed (earlier Claude Code runs used one round even when fixes changed behavior, see [check-work](check-work-reference-sheet.md)); whether agents actually use `watch_pull_request` after the global line; whether screenshots reach both the reviewer and the user.
