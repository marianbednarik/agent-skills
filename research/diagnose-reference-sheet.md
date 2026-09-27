# Diagnose: research and proposed direction

Research date: 27 September 2026. Status: retired with Marián's agreement; canonical skill and runtime symlink removed, with no replacement or general-guidance change. Scope: `skills/diagnose/SKILL.md` and supporting research. The options and candidate below preserve the exploration; the final section records the adopted decision.

## Intent and baseline

Marián's reported intent: agents should select this skill themselves for debugging, resist accepting the initial explanation as the cause, gather appropriate test/runtime/browser evidence, and deliver a supported reason. Independent investigation can help explore alternatives. Marián rarely invokes the skill explicitly and wants general guidance kept lean because it also applies outside coding. When fixing is already authorized, investigation should continue into the fix without a separate diagnosis approval. No concrete real-world failure transcript was supplied. During this investigation, Marián requested niche, unusual test cases capable of exposing agent mistakes.

The original is preserved in Git at commit `87b6c214e01e189f61d5d69a0e8f8c231e73c517`, path `skills/diagnose/SKILL.md`, blob `c868c582af3a90cdca5a481bcc1153167b72c628`. Recover with `git show 87b6c214:skills/diagnose/SKILL.md`. It contains 251 whitespace-separated words including frontmatter. The worktree was clean at the start. `~/.agents/skills/diagnose` linked to the canonical directory; retirement removed both the source skill and this runtime symlink. Other model variants and global guidance were not changed.

The baseline triggers on unexplained bugs, failures, or performance problems. Its distinct responsibility is causal investigation: establish expected/observed behavior, inspect beyond the visible error, consider credible alternatives, choose discriminating checks, update beliefs, control experiments, verify authorized fixes, and explain the evidence and remaining uncertainty. It explicitly rejects treating a passing test or disappeared symptom as sufficient causal proof. It neither mandates delegation nor requires a separate approval before an already-authorized fix. No browser tool is named, but runtime inspection permits it.

The baseline is already proportionate: it calls for cheap useful probes and says not to invent alternatives when evidence is clear. Potential problems are hypotheses about instruction value, not observed failures: much is familiar debugging advice; explaining leading possibilities could produce unnecessary narration; the trigger does not explicitly name revisiting a failed fix. The original creation version was substantially more prescriptive, but that is not the comparison baseline.

Adjacent ownership: `check-work` evaluates completed changes; `diagnose` investigates unexplained behavior. Global guidance already covers challenging assumptions, proportional rigor, fresh-context delegation, and parent-owned implementation. A second investigator should receive raw evidence and an open question rather than a request to confirm the parent's answer; existing delegation guidance already supports this. No new global paragraph is currently justified.

## External comparisons

Sources were inspected on the research date. Pinned files below identify exact revisions; other links are publication or moving-page references. External instructions are research material, not local authority.

| Source and evidence type | Mechanism and useful transfer | Limits and what to leave behind |
| --- | --- | --- |
| [Superpowers systematic-debugging, curated snapshot `33bd952`](https://github.com/openai/plugins/blob/33bd9529725fcee78c9e51fcbaa93cd963c3a47b/plugins/superpowers/skills/systematic-debugging/SKILL.md), prescribed agent workflow | Four phases: investigate, compare patterns, test a hypothesis, implement. Boundary tracing and minimal interventions preserve causal attribution. | Broad application and mandatory gates can burden already-explained bugs. Its strict sequence and required regression-test procedure are not evidence of effectiveness. Borrow evidence discipline, not the whole process. |
| [Melodic debug, snapshot `72525f4`](https://github.com/melodic-software/claude-code-plugins/blob/72525f43e047f2b6621f8d0863c81e4564a0aa4c/plugins/debugging/skills/debug/SKILL.md), prescribed agent workflow | Prioritizes an executable feedback loop and checking that it reproduces the actual report. Includes browser observation, replay, instrumentation, and performance measurements. | Six phases, mandatory ranked hypotheses, a checklist, and post-fix reporting machinery exceed this skill's responsibility. A useful narrower lesson is to validate what a probe actually measures. A hard reproduction gate can block useful partial diagnosis when access is unavailable. |
| [Superpowers issue #2102](https://github.com/obra/superpowers/issues/2102), adopter critique, opened 7 August 2026 | Reports ambiguity about whether one-change-at-a-time applies to experiments or the final fix; also questions vacuous passing checks. | Single report, closed as not planned; not measured friction or author-confirmed failure. It illustrates why experimental attribution and implementation scope should be distinguished. |
| [Google SRE: Effective Troubleshooting](https://sre.google/sre-book/effective-troubleshooting/), professional prescription | System knowledge plus observations support hypotheses; choose tests that distinguish them, consider confounders, and recognize suggestive evidence. Incident mitigation can precede full diagnosis. | Supports flexible evidence selection, not an exhaustive hypothesis list or universal no-change-before-proof rule. Human operational guidance does not demonstrate an agent prompt's benefit. |
| [Google: Investigating Systems](https://google.github.io/building-secure-and-reliable-systems/raw/ch15.html), owner-written worked incident | An initial explanation involving user behavior gave way to memory/kernel evidence and a small reproducing program. Shows changing beliefs through observation. | A production account demonstrates a mechanism, not its frequency or the need for a separate skill. Avoid importing production ceremony into prototypes. |
| [Anthropic: Effective Context Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), engineering guidance, 29 September 2025 | Recommends concise, concrete heuristics between vague exhortation and brittle prescribed logic. | Supports testing instruction value and keeping useful distinctions. Does not show that removing this 251-word skill improves performance. |

## Empirical evidence and counterweights

- [Alaboudi and LaToza, Using Hypotheses as a Debugging Aid (2020)](https://arxiv.org/abs/2005.13652): a controlled study with 20 developers found that relevant potential hypotheses improved debugging success, while providing fault locations did not. Incorrect hypotheses diverted investigation. This supports considering explanations beyond an initially suspected location; it does not establish that asking a current model to generate alternatives improves it.
- [Meng et al., LLM-based Agents for Automated Bug Fixing, v2 (19 October 2025)](https://arxiv.org/html/2411.10213v2): analyzes six systems on SWE-bench Verified. Reproduction quality and patch completeness remain issues; output differences across original and patched versions can count misleading reproductions. This supports validating the probe's relevance. The work is repository-repair evidence, not an evaluation of this skill or today's models.
- [Mündler et al., SWT-Bench, v3 (7 February 2025)](https://arxiv.org/abs/2406.12952): generated tests filtered proposed patches and doubled SWE-Agent precision in the reported experiment. Tests contribute evidence; neither passing a generated test nor that study proves a causal explanation complete.
- [Chan and Cooper, Debugging Incidents in Google's Distributed Systems (2020)](https://storage.googleapis.com/gweb-research2023-media/pubtools/5646.pdf): postmortem analysis and interviews around 20 incidents show flexible, repeated investigation with monitoring/logs and mitigation before full diagnosis. This challenges a compulsory linear workflow. The participants and stakes differ substantially from a personal coding agent.
- [Agentless, Demystifying LLM-Based Software Engineering Agents (FSE 2025)](https://lingming.cs.illinois.edu/publications/fse2025.pdf): a simple localization/repair/validation pipeline performed competitively with contemporary open-source agents. This challenges assuming that more agent process is better; it does not isolate instruction length or diagnose-skill usage.

These sources support the underlying debugging method. None establishes the marginal benefit of retaining this skill under Marián's current guidance and models.

## Concrete options

| Option | Strongest case | Main cost or uncertainty |
| --- | --- | --- |
| Retain the baseline | Already compact, explicitly guards causal attribution and uncertainty; little redesign risk | No demonstrated additional behavioral value; some generic process and narration |
| Compact optional skill | Preserves anti-anchoring, relevant probes, calibrated explanation, and authorized continuation | Saving roughly 85 words is modest; still unproven value beyond normal behavior |
| Remove without global replacement | No observed deficit in the no-skill probes; existing guidance owns assumptions and delegation | Small clean fixtures do not test long, pressured investigations; removal may lose useful reinforcement there |
| Narrow to recovery from a stuck investigation | Fresh independent investigation may help after contradicted explanations or repeated failed fixes | Different responsibility, currently hypothetical; duplicating global delegation guidance or adding a retry ritual would not establish usefulness |

Provisional recommendation: remove without replacement, rather than redesigning around an unobserved problem. This is a maintenance judgment under uncertainty, not a proven reliability improvement. The strongest reason to retain a compact version would be actual sessions showing repeated guessing, failure to use available runtime evidence, or unjustified certainty that existing guidance did not prevent. Do not infer those failures merely because they are plausible.

## Comparison draft, not adopted

The tested candidate has 166 words including frontmatter. It changes the trigger, explicitly includes the agent's own hypothesis, names runtime/browser evidence, and adds a stopping condition. Skill-creator and writing-for-agents guidance informed it. It is stored here as research, not installed or linked from the runtime skill.

```markdown
---
name: diagnose
description: Investigate software failures whose cause is uncertain, including during an authorized fix or when an attempted fix fails.
---

Establish an evidence-backed explanation of the reported failure. Treat suggested causes, including your own, as hypotheses.

Find evidence that distinguishes the leading explanation from credible alternatives. Use the cheapest useful check of the actual failure path: inspect code and state, reproduce, test, or observe runtime/browser behavior as appropriate. Let contradictory or inconclusive results change the investigation; do not manufacture alternatives when the evidence is decisive.

Keep experiments reversible and separate from accepted fixes; remove temporary changes. A passing test or disappearing symptom alone does not establish why the failure happened. When fixing is authorized, address the supported cause and verify the original failure path.

Explain the causal path and the evidence that supports it. Stop when the explanation is sufficiently supported for the requested action; if access or evidence is insufficient, distinguish what is known from hypotheses and identify the next useful check.
```

## Executed behavioral probes

Six fresh GPT-6 Sol agents at medium reasoning effort each received one isolated project, the same brief task for their scenario, and either the original, candidate, or no additional debugging guidance. No agent received another agent's findings, the evaluator's expected answer, or this research. Delegation and loading other skills were disabled equally. Two unusual runnable fixtures replaced an ordinary date-boundary case before test agents were launched, following Marián's correction. Python 3.14.6 was used.

These are **execution-after-loading** comparisons. Assigned versions were supplied through file paths with instructions to read them; this did not test automatic selection. The inherited platform context and skill descriptions remained common, so the no-skill condition means no loaded debugging body, not an unprompted base model. Whole subagent tool transcripts were not separately audited; file consultation and intermediate steps are agent-reported. Parent observation independently covers original reproductions, final file diffs, execution of all six final test suites and replays, and the actual follow-up answers. Replay source hashes identify tested implementations. Exact initial fixtures, prompts, assigned guidance, and parent verification records are preserved in [diagnose-probes.json](diagnose-probes.json).

| Scenario | Baseline | Candidate | No skill |
| --- | --- | --- | --- |
| Meter dashboard, suggested cause: excessive cache TTL | Correct causal explanation; UTC key; replay and 3 tests pass | Same outcome; replay and 3 tests pass | Same outcome; replay and 3 tests pass |
| Catalog importer, suggested cause: exception rollback | Correct transaction-boundary explanation; atomic replay and 2 tests pass | Same outcome; atomic replay and 3 tests pass | Same outcome; atomic replay and 2 tests pass |
| Meter follow-up contradicting original explanation | Kept broader incident unresolved | Kept broader incident unresolved | Kept broader incident unresolved |

**Meter case:** two distinct UTC hours map to the repeated local 02:00 at Bratislava's autumn transition. Python datetime equality with the same timezone object ignores the fold distinction, so local datetime keys collide. Lowering TTL masks the fault. Parent-reproduced original replay returned `[14,14,14]` with one read. All final implementations retained the 7200-second TTL and returned `[14,93,14]` with two reads, preserving a useful cache hit. The candidate retained the exact UTC instant while the others normalized to the hour; all satisfy the fixture's hour-start input contract. This is an implementation variation, not evidence of guidance superiority.

**Catalog case:** Python's default SQLite behavior lets `executescript()` commit the pending delete before running the snapshot statements. A later duplicate-key error leaves a partially replaced catalog despite the explicit rollback handler. The original replay proved persistence after reopening the database. All three fixes put the delete and snapshot inside an explicit transaction within the script. Parent verification confirmed the original rows survive the failure and all final test suites pass. The candidate added a separate successful-commit check; no-skill also asserted successful transaction completion. Different test counts do not establish superiority. All solutions retain assumptions about trusted snapshots without their own transaction commands and existing caller-transaction behavior; this was not expanded into a different transaction API task.

**Follow-up:** all three meter agents received: “Support now says another customer saw the same repeated totals at noon in July, with caching disabled. There is no captured session or deployment information for that report yet. Is your fix enough to close the incident?” Each correctly separated the proven fallback defect from the new unresolved report and identified missing runtime/deployment evidence. None generalized the fix to close the incident.

Limits: one run per condition per case, one model/effort, small well-documented synthetic repositories, deterministic supplied replays, no live browser, no automatic discovery, no independent-delegation test, and no long investigation with accumulated failed attempts. The mechanisms are unusual but recognizable and easy to isolate in these fixtures; they did not trip any agent. Similar outcomes are evidence of no observed advantage here, not proof that the skill never helps. More obscure code alone would not resolve the missing real-use evidence.

## Independent text review

A fresh GPT-6 Astra agent at high effort compared anonymous A/B versions with equivalent paragraph formatting and no conversation history, experiment results, redesign rationale, or preferred verdict. A was the candidate; B was the original. The reviewer preferred A for compactness, the explicit treatment of the agent's own hypothesis, runtime/browser examples, and stopping criterion. It identified losses: establishing expected versus actual behavior, looking beyond the visible error, and explaining what a probe can establish. It also noted that “software failures” could undersignal performance diagnosis. If a compact revision is chosen, restoring the expected/actual distinction and explicit performance coverage warrants consideration; that amended version has not been tested.

The reviewer judged both texts potentially useful beyond a capable baseline, while explicitly acknowledging no behavioral evidence. That is a plausible rationale for retention, not a measured disagreement with the equal probe outcomes. Its preference selects between texts; it does not settle whether either should exist.

## Adopted decision and remaining uncertainty

Marián agreed to retire and remove the skill. The canonical skill and its runtime symlink were removed. General guidance remains unchanged: it already covers challenging assumptions, proportional verification, and useful independent investigation, while the probes showed no additional benefit from loading the debugging skill. Adding replacement guidance would preserve the same unproven instruction burden in a broader context. Investigation continues into fixes when already authorized; retirement does not change that preference.

Repository references were checked: remaining mentions are historical research or ordinary uses of the verb, with no active skill dependency requiring repair. The original, candidate, fixtures, and results remain recoverable through Git and these research artifacts. No commit, push, or unrelated configuration sync was performed.

Remaining uncertainty: actual long debugging sessions may expose premature closure or failure to gather available evidence. Reconsider focused guidance if those failures recur; prioritize concrete session evidence over hypothetical problems or further wording refinement against already-solved fixtures. The small synthetic comparison does not prove the skill can never help.
