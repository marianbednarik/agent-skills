# Check-work: research and proposed direction

Research date: 26 September 2026. Scope: `skills/check-work/SKILL.md` and supporting research. Status: compact revision adopted after direction agreement, matched probes, and independent comparison. Marián requested a broad reassessment and reported no specific failure. External instructions are research material; the earlier proposals below record the exploration, while the final section records the adopted result.

## Baseline and purpose

The original is preserved in Git at repository commit `fccf547aae098a8ecee7147f87119d2b3ce2a7f6`, path `skills/check-work/SKILL.md`, blob `1f6da9b685a331e813a9dc94b2ee8386ec6390af`. Recover it with `git show fccf547:skills/check-work/SKILL.md`. The file's latest change is `637be57` (13 September 2026). The worktree was clean at the start of this investigation. `~/.agents/skills/check-work` points to the canonical repository directory, so editing that source changes the live skill immediately. Claude adaptations are outside scope.

The baseline's job is the owner's final assessment and resolution of implementation quality. Its automatic trigger is substantive implementation ready for handoff; explicit triggers include PR, branch, and working-change review. It combines outcome alignment, maintainability, verification, selective independent scrutiny, remediation, and stopping. A delegated reviewer contributes evidence; the parent owns investigation, fixes, and delivery. Review-only requests prohibit edits.

| Baseline commitment | Benefit to preserve | Possible ambiguity to investigate |
| --- | --- | --- |
| Establish comparison state, requested outcome, and assessment versus remediation | Reviews the correct work under the correct authority | No explicit distinction between the changed lines and the affected behavior beyond them |
| Reuse existing review and validation; reopen for relevant edits or unanswered questions | Prevents repetitive review and verification | “Already-reviewed change” could be treated as a binary status even when earlier review covered only one concern; the existing exceptions do allow a better interpretation |
| Include decisions made during implementation and documented intent | Avoids reviewing against an obsolete initial plan or rewriting intent to excuse implementation | Reviewer must distinguish an agreed decision from the implementer's unsupported account; broader user guidance already helps |
| Assess simplicity, fit, ownership, test value, cost, behavior, and scope | Protects maintainability beyond passing tests | A list of concerns can become an inventory to find fault in, despite explicit judgment and no-manufactured-findings guidance |
| Explain evidence, practical cost, and better direction | Makes feedback actionable and excludes taste-based blockers | Stronger examples of evidence may help distinguish a demonstrated defect, a design tradeoff, and missing verification |
| Remove or improve tests that merely mirror implementation | Reduces tests that freeze incidental structure | A reviewer might mistake a meaningful interaction or compatibility contract for incidental structure |
| Fresh frontier reviewer where design/interaction warrants it; read-only; parent integrates | Independent scrutiny with clear ownership | Independence is a fresh perspective, not guaranteed accuracy; reviewer findings still need adjudication |
| Address worthwhile findings, recheck affected behavior, stop at material concerns | Closes the loop without indefinite polish | “Worthwhile” needs application to project maturity, practical benefit, and disruption, not another mandatory pass |

These are hypotheses about possible readings, not observed failures. Much of the desired behavior is already permitted or explicit. A longer skill is not automatically better.

### Neighboring responsibilities

- `diagnose` investigates an unexplained failure and discriminates among causes. Check-work can identify a suspicious path, but should not invent certainty or turn every review into an open investigation.
- `repo-health-audit` assesses accumulated maintenance opportunities across an area. Check-work stays with the requested change and its consequences; relevant unchanged callers may matter, unrelated pre-existing problems do not become remediation scope.
- `project-context` maintains durable intent. Check-work uses that intent as evidence, including later agreed decisions; it must not silently rewrite intent to make a change appear aligned.
- Global guidance already supplies project-proportionate rigor, maintainability, parent-owned implementation, fresh-context delegation, and concise reporting. The skill earns its place if it makes those principles operational at review/handoff, rather than merely repeating them.

## Public workflow comparisons

Sources below were inspected on the research date. Public branch links are moving snapshots; no external revision is pinned. They prescribe behavior, not demonstrated effectiveness.

| Source | Mechanism and intended use | What fits here | What to leave behind / limitation |
| --- | --- | --- | --- |
| [OpenAI Codex review-agent](https://github.com/openai/codex/blob/main/codex-rs/skills/src/assets/samples/review-agent/SKILL.md) | Read-only delegated review of a specified change; inspect complete diff and context, verify against tests/call sites, report discrete introduced issues with demonstrated affected paths; no findings is allowed | Ground behavioral concerns in a reachable scenario; inspect context beyond changed lines; tolerate a clean result | Its defect-first finding format does include meaningful maintainability, but does not own remediation or the whole delivery decision. Do not substitute an inline-comment contract for the parent workflow |
| [Superpowers requesting-code-review](https://github.com/obra/superpowers/blob/main/skills/requesting-code-review/SKILL.md) | Fresh reviewer with requirements and revision bounds; review required after major features, before merge, and after tasks in its subagent workflow | Independent context, clear comparison, technical pushback on mistaken findings | Mandatory repeated review can duplicate equivalent evidence; sample minor findings are not a universal quality bar |
| [Superpowers receiving-code-review](https://github.com/obra/superpowers/blob/main/skills/receiving-code-review/SKILL.md) | Verify feedback against the actual repository, compatibility needs, and decisions before applying it | Explicitly adjudicate the finding and the proposed remedy; preserve legitimate behavior even if simplification looks attractive | Extensive response scripts, blanket stopping on unclear items, and etiquette prohibitions add little to this skill |
| [Superpowers verification-before-completion](https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md) | Claims require freshly executed verification; distinguishes test, build, bug-fix, and requirements evidence | Match each completion claim to evidence that actually supports it | Requiring a new command in the current message would discard still-applicable evidence and conflict with the baseline's deliberate reuse. Review judgment is not reducible to a command |
| [b-mendoza review-pull-request](https://github.com/b-mendoza/agent-skills/blob/main/.agents/skills/review-pull-request/SKILL.md) | PR orchestrator partitions dimensions, delegates, adjudicates and deduplicates findings, verifies a local review artifact, then separately gates publication | Adjudication is distinct from finding generation; existing review threads can contain useful evidence | Many roles and explicit state contracts serve PR publication, not an ordinary local handoff. No present need for that machinery |

The most useful contrast is ownership: a read-only reviewer identifies concerns; check-work owns deciding what remains to establish or improve before handoff. Those functions can be distinguished within one compact skill without creating another skill or compulsory phase.

### Actual use and friction

A [Claude Code issue from 1 November 2025](https://github.com/anthropics/claude-code/issues/10785) reports false-positive recommendations despite anti-false-positive instructions and multiple agents, on version 2.0.31. It is a single short report, closed as not planned, with no independently verified examples in the inspected body. It illustrates a possible failure, not its frequency or current-model behavior. It supports testing adjudication; it does not establish that independent review is useless.

The worked examples in Superpowers show intended handoffs and responses, rather than recorded evaluations. The public PR orchestrator demonstrates how a workflow can handle comment duplication and publication, but inspecting its instructions does not establish the pipeline's precision or value. We should not import elaborate machinery based on apparent thoroughness.

## Professional methods and empirical evidence

| Primary source | What it establishes | Useful transfer and limits |
| --- | --- | --- |
| [Google review standard](https://google.github.io/eng-practices/review/reviewer/standard.html) | Prescribes improvement in code health while balancing progress; perfection and personal preferences are not approval requirements | Preserve broad quality judgment and stopping. This is an organizational practice, not measured validation of our prompt |
| [Google: what to look for](https://google.github.io/eng-practices/review/reviewer/looking-for.html) and [navigation](https://google.github.io/eng-practices/review/reviewer/navigate.html) | Reviews design, behavior, complexity, tests, and context; starts with overall purpose and important design before details | Follow the meaningful behavior and ownership connections. Do not turn its whole enterprise checklist or review authority into mandatory prototype process |
| [Bacchelli & Bird, ICSE 2013](https://sback.it/publications/icse2013.pdf) | Microsoft observations, interviews, comment analysis, and surveys identify understanding the change and its context as a central review challenge; defect detection is a strong motivation but review has broader outcomes | Give an independent reviewer the goal, constraints, and discoverable rationale. Freshness without enough context can produce shallow or wrong findings. Human organizational evidence does not measure LLM performance |
| [Beller et al., MSR 2014](https://azaidman.github.io/publications/bellerMSR2014.pdf) | Classifies over 1,400 actual review changes in two mature OSS projects; about 75:25 maintainability-related versus functional changes. Some comments are discarded and some fixes have no explicit comment | Bug-only counts miss much of review's observed output; finding count is a weak success metric. Maintainability here includes documentation, identifiers, and formatting, not only architecture; frequency of a change does not prove its value |
| [Bosu, Greiler & Bird, MSR 2015](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/bosu2015useful.pdf) | Author interviews distinguish useful feedback from false positives and out-of-scope requests; a classifier trained from ratings is then applied to about 1.5 million comments. Later iterations have a lower useful-comment proportion | Require practical consequence and scope fit; repeated comments are not automatically useful. Classifier estimates and correlations cannot justify a fixed pass limit or dismissal of late serious findings |
| [Sadowski et al., ICSE-SEIP 2018](https://sback.it/publications/icse2018seip.pdf) | Describes Google's lightweight review practice using large review logs plus interviews/survey; small changes, usually one reviewer, and quick iterations are characteristic | A broad review purpose need not imply many reviewers or elaborate process. Google's tooling and culture limit transfer to a personal agent workflow |
| [Google Testing Blog: change-detector tests](https://testing.googleblog.com/2015/01/testing-on-toilet-change-detector-tests.html?hl=ko_KR) and [Software Engineering at Google, chapter 13](https://abseil.io/resources/swe-book/html/ch13.html) | Explain brittle assertions copied from implementation and why state testing is generally preferred; identify legitimate interaction tests when call number/order matters or realistic alternatives are unavailable | Judge what a test protects, not its syntax or use of mocks. Preserve useful guarantees when replacing brittle tests. Do not infer that every call-order assertion or implementation-adjacent test is worthless |

The human-review studies support investigating context, maintainability, and practical usefulness. None establishes the best delegation frequency, prompt wording, model, or effort for Marián. The adapted mechanisms remain hypotheses to compare.

## Credible directions

1. **Keep the baseline.** Strongest case: it is already compact, tailored, proportionate, and explicitly evidence-aware. General agent capability may supply the details. This wins if probes show equal outcomes or a revision adds process without useful changes.
2. **Compact refinement within the existing role.** Preserve broad quality review, evidence reuse, selective independence, and parent remediation. Make affected-path inspection and finding adjudication clearer; treat simplification and test changes as decisions requiring concrete benefit. This is the provisional recommendation, subject to discussion and comparison.
3. **Reduce to a minimal handoff reminder.** Let global instructions own maintainability and delegation; retain only comparison scope, evidence reuse, outstanding concerns, and completion. This reduces duplicated guidance but may lose the reliable occasion for challenging unnecessary structure. Include a no-skill condition if investigating whether the skill earns its place.
4. **Separate broad owner assessment from a narrow reviewer contract.** Could help if repeated delegated reviews need a consistent defect-focused output. Costs another source of guidance and risks separating design from behavior too sharply. A paragraph distinguishing responsibilities may provide the same benefit.
5. **Mandatory specialist review pipeline.** Strongest case: explicit dimensions, adjudication, and coverage make repeated large PR review more consistent. Present evidence does not justify its overhead for this personal default; keep as a different workflow for a demonstrated need.

The proposed refinement is not “add more review.” It is to make the selected review answer a concrete unresolved question and to evaluate its suggestions before changing the work. Keep the baseline's explicit quality concerns unless comparisons show that compression preserves them.

### Concrete candidate mechanisms for discussion

These are proposed behavioral changes, not installed instructions or a full candidate:

- Inspect enough callers, consumers, state transitions, and existing guarantees to explain the consequences of the change. An unchanged file can be necessary evidence without becoming cleanup scope.
- For a suspected defect, establish the triggering condition, affected path, and consequence. For a maintainability finding, establish the concrete burden and why the remedy improves it in this project. A runnable reproduction is useful when needed, not mandatory for every sound code-based finding.
- Check evidence that could invalidate a finding or make the suggested fix worse before acting. Distinguish established defects, worthwhile design judgments, and unresolved verification gaps without requiring a new reporting taxonomy.
- Reuse prior evidence for the scope, state, and concern it actually covers. A previous correctness pass may leave an ownership question open; that warrants targeted scrutiny rather than restarting the entire review.
- Assess tests by the behavior or guarantee they protect. Removing a brittle test should not silently remove valuable coverage; improve it when the guarantee remains important.

Potential regression: adding these obligations could induce investigation of every speculative concern, excessive test work, or rigid scenario-writing. A candidate must preserve proportionality, room for judgment, evidence reuse, and a clear stopping condition. Several mechanisms are already implied by the baseline; a comparison may show no meaningful gain.

## Scenario comparisons

These are analytical walkthroughs, not executed probes or incidents reported by Marián. They describe distinctions to test rather than proven baseline failures.

| Scenario and available context | Strong baseline behavior | Proposed refinement / potential difference | Observable success and regression |
| --- | --- | --- | --- |
| A five-layer abstraction delivers a prototype's single export format; tests pass | Identify speculative flexibility and misplaced ownership; simplify coherently | Tie the maintenance concern to actual navigation, duplicated configuration, and unsupported variation; consider why each layer exists | Removes a demonstrated burden while retaining a useful boundary; fails if it demands an executable bug before allowing simplification or refactors for line count |
| A changed return value breaks an unchanged cache consumer; local tests pass | Behavior/scope and surrounding-code criteria allow finding the regression | Explicitly follow the changed contract to consumers and show the failing path | Reads the relevant consumer and verifies the consequence; fails if review only inspects the diff or expands into a repository audit |
| A test asserts write-before-notify order; documentation establishes this as a durability requirement | “Independently meaningful expectations” should preserve it | Ask which guarantee the assertion protects before labeling it a change detector | Retains or improves the test; fails if a cleanup removes the contract because it resembles implementation |
| A reviewer suggests removing a compatibility branch; a supported older runtime needs it | Parent's targeted investigation and project-fit criteria permit rejecting the suggestion | Explicitly examine the counterevidence and separate the concern from its suggested fix | Rejects mistaken removal with the runtime constraint; fixes only an independently supported issue |
| Earlier read-only review covered formatting; a new change crosses persistence and UI ownership | Unanswered-question exception permits further independent scrutiny | Match evidence to the concern, avoiding a binary “already reviewed” flag | Delegates or investigates the unresolved interaction; does not repeat the formatting pass |
| Same state has already had meaningful review and relevant tests; only the final report remains | Reuse evidence and stop | Preserve exactly this behavior | No redundant reviewer or rerun; accurately state what was verified |
| A wording-only README correction | Focused content check; no heavy review | Preserve exactly this behavior | No implementation checklist, unrelated test suite, or new reviewer |
| Agreed mid-task decision supersedes an older design note; review-only request | Review against the current agreement, surface stale context, make no edits | Preserve authority and distinguish the sources of intent | Does not “fix” code back to the obsolete design or edit documentation under review-only authority |

## Comparison plan after direction is agreed

If revising, apply skill-creator and writing-for-agents, draft outside the symlinked runtime path first, and compare with the preserved original. Use a small subset of the scenarios above implemented as isolated repositories with realistic requirements, docs, diff, tests, and prior-validation evidence. Give fresh agents ordinary task prompts; keep expected findings and evaluator criteria out of their briefs. Keep model, effort, fixtures, and unrelated instructions equal. Assess actual file reads, commands, findings, edits where authorized, and stopping behavior. Include at least one clean case and one case where the baseline should already do well.

Execution testing supplies the assigned guidance directly; it does not establish automatic discovery. A separate discovery test would expose only description and location and observe whether the agent loads the skill. If comparing minimal guidance or removal, include a no-skill condition under otherwise equal instructions. Avoid accidental loading of the globally symlinked baseline in that condition and disclose any harness limits.

A fresh GPT-6 Astra reviewer at high effort will compare original and candidate labeled A/B, with equivalent formatting, no conversation history, no preferred answer, and no indication of which is newer. Its text assessment is distinct from executed behavior. Compare strengths, losses, likely upgrades/downgrades, ambiguities, and preference if justified. Do not claim reliable improvement from a small synthetic sample.

## Initial exploration status (superseded by the decision below)

- Established: broad exploration; no user-reported defect; canonical Codex skill only; preserve the original; no commit, push, installation, or Claude synchronization requested.
- Completed: baseline/history/boundary inspection; primary-source research; fresh-context Luna high research on public workflows and reported friction; fresh-context Sol medium research on methods and empirical findings; parent inspection and synthesis of consequential sources.
- Provisional recommendation: retain the skill and its broad ownership role; test a compact refinement emphasizing concrete consequences, adjudication, and concern-specific reuse.
- Not yet done: direction agreement, candidate drafting, executed behavior comparison, discovery testing, independent A/B review, or runtime changes. The scenario table is analysis only.
- Open choice for Marián: keep the current approach, test the compact refinement, or investigate a much smaller reminder. Remaining empirical question: does more explicit evidence reasoning improve outcomes enough to justify the added guidance without reducing useful design judgment?


## Agreed direction and completed revision

On 26 September, Marián endorsed the proposed improvements and requested shorter, more direct guidance. He clarified two required workflows:

- Automatic review after completed work or useful completed slices, with timing and depth chosen by the agent. Small or simple work can be reviewed directly. More demanding work can use one or multiple independent reviewers with dimensions selected for the change, and further rounds when useful.
- Explicit review of a specified PR, remote branch, recent uncommitted diff, or other defined change. The agent resolves the scope and handles the depth of review, asking only when scope remains unclear.

Delegated reviewers should assess independently rather than inherit the implementer's conclusions. The parent hands over the selected review, then investigates and accepts or rejects feedback, owns authorized fixes, and avoids duplicating delegated work. These are settled requirements, not hypothetical extensions.

The adopted [canonical skill](../skills/check-work/SKILL.md) is 403 whitespace-separated words including frontmatter, down from 472 (about 15%). Paragraphs are no longer manually wrapped. Its automatic description covers completed work and useful checkpoints; explicit targets include PRs, branches, commits, and working diffs. It clarifies assessment/remediation authority near scope establishment, affected-path investigation, independent reviewer briefs, multiple reviewers and further rounds, counterevidence, meaningful test guarantees, and evidence reuse by state/scope/concern. Quality dimensions remain selectable rather than mandatory passes. No auxiliary runtime files or new skill were added.

Compression removes repeated process language and several examples from the quality checklist. Ownership and verification cost remain explicit, but examples such as oversized fixtures and specific UI tokens are left to judgment. This tradeoff is intentional: preserve decision criteria without an expanding inventory of concerns. The global delegation policy continues to own model choice.

### Independent text assessment

A fresh GPT-6 Astra agent at high reasoning effort compared A and B with equivalent paragraph formatting, no conversation history, no redesign rationale or preferred verdict, and a neutral statement of the two workflows. A was the candidate; B was the original. The reviewer preferred A and found no material blocker. It favored clearer triggers, early review-only authority, explicit fresh-context/multiple-reviewer delegation, affected paths, and counterevidence. It noted modest loss of concrete ownership, test-expectation, and review-machinery-cost examples.

The one recommended adjustment was to put evidence reuse before deciding on depth or delegation. That ordering change was applied before the behavioral probes, alongside explicitly naming verification cost. The final version is therefore not byte-identical to the blind-review candidate; these limited corrections received parent review rather than another independent round. This assessment is textual evidence, not a demonstration of better execution.

### Executed matched probes

All six runs used fresh GPT-6 Sol agents at medium effort. Each pair received equivalent isolated repositories, task wording, unrelated guidance, and permitted actions; only assigned skill guidance differed. Each had a private Git repository, standard-library Python code, project guidance, requirements, and relevant tests. No repository fixture contained the expected findings or redesign rationale. Execution pairs explicitly supplied the assigned skill path. The discovery pair exposed only its description and location, leaving loading to the agent.

Fixtures lived outside the repository under the local temporary directory `check-work-rethink-o5l2t6wj`; they are not a permanent test suite. The parent inspected resulting diffs and tool-call records in the agents' session logs, rather than relying only on final self-reports. Tool traces confirmed the assigned reads and commands described below. Both versions ran under the surrounding desktop agent harness; this was not a bare-model prompt experiment.

| Setup and ordinary task prompt | Baseline result | Candidate result | Assessment |
| --- | --- | --- | --- |
| Execution: “Check work on origin/export-streaming.” Local fetched refs identified a branch adding paging; README required workspace isolation and bounded paging. Unrelated working-tree notes were present. | Read assigned skill, project context, diff, and unchanged consumers. Reproduced a cross-workspace export leak; identified sorting all remaining rows before taking a page. Ran three existing passing tests; made no edits. | Read assigned skill and the same relevant context, reproduced the same leak, and reported the same paging-cost issue. Ran the same three tests; made no edits. | Equivalent useful findings and read-only scope. The baseline reproduction used the HTTP handler; the candidate used the export service. In-memory fixture findings establish allocation/sort overhead, not real database body-loading measurements. |
| Execution: “Finish the notification batching change and hand it back.” Working notes showed an implemented batch method and three passing tests. README required save-before-send and propagation of failures. | Read assigned skill, context, and tests. Replaced send-before-save batching with calls to the existing single-item method. Retained meaningful interaction assertions, added batch order/failure coverage, ran four passing tests and checked diff whitespace. | Same implementation correction and focused validation; four tests passed. Retained meaningful order assertions. | Same outcome, with modest test differences: baseline tested failure on the second item; candidate tested failure on the first. Both verified stopping and the failed item's save-before-send sequence. This is execution after loading, not proof of automatic skill discovery. |
| Discovery: “Correct the README command to match the CLI.” A one-line option spelling differed from the declared CLI option; project guidance required focused checks for docs changes. | Did not read the assigned skill. Changed only README, inspected `cli.py --help`, and checked the diff. | Read the assigned skill, then made the same README-only change, inspected CLI help, and checked the diff. | Revised description was consulted in this one small automatic-use case, with no extra reviewer or broad checks. Both outcomes were appropriate. This single observation does not establish reliable discovery. |

After the probes, the parent tightened “Review small or straightforward changes directly” to “Review directly when sufficient,” so small size cannot be read as a reason to skip needed independence. This narrow wording correction received direct review without rerunning the probes.

All six agents handled these small tasks directly, with no child reviewers or repeated rounds. The probes therefore do not validate autonomous selection of multiple reviewers, neutral delegated briefs in action, or later-round coordination. Those mechanisms received independent textual assessment and remain real-use uncertainties. Likewise, the branch refs were already local and the reviewed branch matched HEAD; this does not test fetching an inaccessible PR or reviewing a non-checked-out remote tip.

Local session identifiers, retained for evidence lookup:

- Blind text assessment: `01a0df48-8a81-7112-a384-144fa2fcd552`.
- Manual review, baseline/candidate: `01a0df4a-6483-7323-880e-c89f7f0b7554` / `01a0df4a-8435-70e2-8fb5-0fb0ece68a18`.
- Completion, baseline/candidate: `01a0df4a-a357-72f3-83f6-3ccd5cd49b0a` / `01a0df4a-c6b9-7b00-8af3-6e545f76515a`.
- Discovery, baseline/candidate: `01a0df4b-8915-7e00-82e6-367db14cd7e8` / `01a0df4b-b2e2-7181-a87a-f6c7728042c3`.

### Validation and stopping decision

The skill-creator structural validator passed using cached PyYAML through offline `uv run`; the system and bundled Python environments lacked PyYAML. No dependency download or project dependency change was necessary. Canonical-source equality against the preserved baseline was checked immediately before writing, and only the skill and this research sheet were changed. The global symlink exposes the revision immediately; no separate install, Claude synchronization, commit, or push was performed.

The evidence supports a shorter expression of the agreed workflow with no material regression in these probes. It does not establish more reliable defect detection or optimal review effort. Further synthetic polishing is not justified by the current results. Watch real use for premature stopping, unnecessary reviewer duplication, biased briefs, and loss of useful design/test judgment; change the skill only if concrete evidence warrants it.

## Real-use evidence and model-neutral rewrite (2026-09-29)

Marián questioned whether check-work is noise, since models already verify their own work, and asked for one skill set that works on both GPT-6 Astra and Opus 5.5 and can be shared with colleagues. This pass replaced synthetic probes with real session logs.

### Evidence from real use

Method: searched Codex logs (`~/.codex/sessions`) for tool calls that read `check-work/SKILL.md`, and Claude Code logs for Skill invocations. The catalog listed the skill in about 250 Codex sessions; 74 read it, 35 of them while editing the skill in this repository. That leaves 39 real Codex uses (2026-07-12 to 09-24, skill versions 277061f through 637be57) and 3 Claude uses of the retired Claude variant (ef0e59b). No real use of the 09-27 text exists. Three fresh-context Opus 5.5 agents (two with helpers) analyzed each run: trigger, review actions, findings, counterfactual, cost, and the user's next message. Subagent briefs are encrypted in Codex logs, so reviewer scoping is inferred from the parent's narration.

| Pattern | Observation |
| --- | --- |
| Independent reviewer on substantial code | Real findings in roughly 15 of 16 runs, about 35 defects in total, after tests had passed: hotseat deadlock, retained host authority after reconnect, wrong-card purchase, deck-card identity leak, retry to a nonexistent step, slug collisions, lost unsaved edits, and a deploy health check accepting a failure status. Follow-up rounds caught regressions introduced by earlier fixes at least four times. |
| Self-review by the implementer | About 25 of 40 passes found nothing, some in under 20 seconds; most re-ran suites that had just passed. Small real fixes occurred. The Claude variant never used reviewers: 4 small real defects and 6 simplifications across 3 sessions, 2–5 minutes each. |
| Document and admin work | Almost no value. Reviewers returned "no material findings"; one run injected review notes into an Excel deliverable, which the user asked to remove. Reviews of technical documentation against code did find real inaccuracies. |
| Rendered UI | In nearly every UI session the user's next message reported a visual defect the review missed. Some reports claimed correctness from code reading ("rendering path proven intact") while the bug persisted. |
| Independence | Every Codex reviewer was forked with the full parent history, including the implementer's verification claims; none was blind. Remote Codex PR review still found 1–4 further issues after local review in several sessions. |
| Process failures | The skill was re-read at the start of many turns (up to 16 times in one session) with a "review" after each small fix. Findings were mis-triaged (an animation deleted to resolve "exit can't animate", which the user reported minutes later) or silently dropped. Final reports often omitted what review had fixed ("Final Codex review found no issues" after four local fixes). Reviews widened scope, e.g. four rounds hardening an unrequested deploy script. |
| User reaction | No message commented on a review directly. Frustration concerned overall pace and fix–deploy–refix loops. |

Conclusion: the independent reviewer on substantial or risky code is the skill's real value; routine self-review adds little beyond ordinary verification. The previous description ("review completed work automatically, including useful checkpoints during development") invited the low-value mode, and omitted findings in reports hid the value from the user.

### Decisions

- Refocus on an independent review before handing back substantial or risky code, plus explicit PR/branch/commit/diff review on request.
- Reviewers start in fresh context, not forked, with requirements, diff, guidance, and suspected risk, but without the implementer's conclusions or verification claims.
- Exclude small fixes, bug-fix loops, and document and admin work.
- UI: check the running result when practical at reasonable cost, but do not require it; state what could not be observed. Marián's "I will do visual inspection" in hogwarts-battle-redux was a project-specific response to cost and tooling limits, not a standing rule.
- Each finding ends as fixed at its cause, reported, or rejected with a reason. Reports list findings, changes, declined items, and unverified areas.
- Remote or project-specific PR review stays in project guidance.
- Model-neutral wording: no model names, no personal name, no reference to personal global guidance, spec-only frontmatter.

Baseline before this pass: commit `6ae9adc`, SHA-256 `95b094b6342a9311a9643fef6e7fbec3355eb2fdc42d5191851f5c7bd83986f0`.

### Candidate tests (2026-09-29)

Fixture: a Python stdlib reservation service with an uncommitted change (release and 15-minute expiry) whose tests passed but which allowed cross-workspace release, double stock return, and confirmation after expiry. A second copy carried only a wrong README test command. Runs used each harness's real global setup and skill discovery: `claude -p` with Opus 5.5 at medium effort, `codex exec` with GPT-6 Astra at medium effort. Prompts: "Finish the reservation expiry and release change and hand it back." and "The test command in the README is wrong. Fix it."

| Run | Skill text | Result |
| --- | --- | --- |
| README fix, both models | first candidate | No skill use or reviewer; one-line fix and test run. |
| Change, Astra | first candidate | Read the skill, spawned a reviewer with `fork_turns: none`, and ran a second round after fixes. Found the three planted defects. Also added thread locking (unrequested) and tried to update issue #7. Short report. |
| Change, Opus | first candidate | Did not use the skill. It judged the change "small" from the description's "substantial". Fixed the three planted defects itself and reported honestly that no independent review ran. Negative quantities still drove stock below zero. |
| Change, Opus | revised | Used the skill. Its fresh reviewer's brief gave requirements, rules, the base commit, the checks already run, and suspected risk areas, with no verdict. The reviewer found negative-quantity and lazy-expiry defects; a second round found NaN quantities. The report covered findings, fixes, one decision for the user, declined pre-existing gaps, and what was unverified. About 2 minutes, $0.73 against $0.23 without review. |
| Change, Astra | revised | Same pattern as the first Astra run: fresh reviewer, "no actionable defects", thread locking added again, brief report without a declined or unverified section beyond runtime expiry. |

A blind GPT-6 Astra (high effort) comparison of the baseline (A) and first candidate (B), given owner requirements but not the log evidence, preferred A. It cited evidence reuse, completion criteria, separating actionable from speculative findings, and a delegation fallback. Its criticisms of B: the size exemption conflicted with requested reviews of small diffs and with risky one-line changes; "another round" conflicted with "do not re-review every fix"; the reviewer role was ambiguous; there was no fallback without subagents. The revision addresses each: a risk-based trigger in the description, an exclusion limited to automatic use, a re-review scoped to fixes that change behavior, "you are the reviewer" for others' changes, a fallback with disclosure, sharing of checks already run, and concrete-consequence and pre-existing-problem criteria. The revision received parent review and the two behavioral reruns above, not a second blind review.

Remaining uncertainty: one fixture, with one run per condition. The fixture is small enough that both models find the planted defects unaided. Astra's reports stay terse and it expands scope under "finish" prompts; that is an implementation-scope issue for global guidance rather than this skill. Watch real use for how often the risk trigger fires on routine UI work.

## Trigger-only description (2026-10-01)

Real use: in the first real session after the 09-29 rewrite (hogwarts-battle-redux, Opus 5.5, four issues merged), the agent never loaded the skill. It briefed two reviewers itself, then skipped re-review of behavior-changing fixes, dropped two findings silently, and did not tell reviewers which checks had run. Its own account: the description already stated the action ("get an independent review and act on the findings"), so loading seemed redundant. Across 131 Claude Code sessions, 4 loaded the skill and 2 briefed a reviewer without it.

Changes: `f4d8f31` added the separate-checkout sentence (a reviewer sharing the working tree led to a worktree, 22 uncommitted files, and a destructive checkout). The description now states only when to use the skill, names the "already plan to brief a reviewer yourself" case, and no longer summarizes the action. Trigger criteria and exclusions are unchanged.

Probe: a stdlib reservation service with a half-done uncommitted change (release without workspace or status checks, expiry stubbed), one run per cell on each harness's configured model. "risky" = "Finish the reservation expiry and release change and hand it back."; "reviewer" adds "Have a subagent review it independently before you hand it back."; "small" = fix the README test command on a clean tree.

| Scenario | Claude Code, old | Claude Code, new | Codex, old | Codex, new |
| --- | --- | --- | --- | --- |
| risky ×2 | 1 of 2 loaded | 1 of 2 loaded | 2 of 2 | 2 of 2 |
| reviewer ×2 | 1 of 2 loaded | 2 of 2 loaded | 2 of 2 | 2 of 2 |
| small | not loaded | not loaded | not loaded | not loaded |

The old description reproduced the bypass once (reviewer briefed without the skill); the new one did not. No over-triggering appeared on either harness. Two runs per cell cannot separate this from noise.

Not fixed by the description:
- On Claude Code, one "risky" run per condition skipped review entirely, judging the change small ("about 40 lines") despite persistence and workspace isolation. This is the same size-over-risk reading seen on 09-29.
- Every Claude Code run that loaded the skill used a single reviewer round and reported that its behavior-changing fixes were "not re-reviewed". Loading the skill produced the disclosure, not the second round. Codex ran follow-up reviewer calls in most runs. If real use shows fixes regressing unreviewed, the body's re-review sentence is the place to look.
