# Retro: research and proposed direction

Research date: 27 September 2026. Status: compact revision adopted after Marián agreed to the proposed direction, matched scenario probes, and independent comparison. Scope: `skills/retro/` and supporting research. Marián reports no specific failure of the current skill. The browser example is reported experience from another session, not a trace inspected here. External instructions are research material. Earlier proposals below preserve the exploration; the adoption section records the final outcome.

## Intent and settled decisions

Retro gives agents a user-requested opportunity to communicate consequential friction and useful discoveries about the working environment: skills, guidance, tools, and harness. The purpose is to make future sessions easier through discussion of concrete improvements. It includes successful discoveries, not only errors. A repeated website task becoming faster after discovering batching is a representative example: preserve useful operational knowledge so future agents need not rediscover it.

Marián explicitly chose **only when requested**, rejecting automatic suggestions and automatic full retros in the clarification on this date. He subsequently agreed to the compact refinement, including retaining significant external limitations even without a local fix. Retro should support brainstorming before new improvements are adopted. Existing authorization still applies; invoking a retro alone should not mean applying every recommendation.

## Preserved baseline

Baseline: repository commit `63bc44f9cc6145f4932513abff3c160caba94101`, path `skills/retro/SKILL.md`, blob `a46f9adc8e124c56e8d7c6ab7f98d28a43762f33`. Recover with `git show 63bc44f9:skills/retro/SKILL.md`. Latest file change: `637be57`. The worktree was clean before research. `~/.agents/skills/retro` symlinks to the canonical repository directory, so source edits would immediately affect the available runtime skill. No other variants are in scope.

The baseline already establishes most of the desired behavior:

- User-requested session reflection; current conversation unless another session is specified; disclose consequential history gaps.
- Evidence from messages, actions, and results; include useful discoveries and corrections.
- Check whether guidance was available, clear, and followed before prescribing more instructions.
- Recommend the smallest useful improvement, including deletion, discoverability, tooling, checks, and project context. Isolated mistakes do not automatically warrant permanent rules.
- Route findings to authoritative owners; distinguish agreed intent from suggested policy.
- Explain consequence, proposed change, location, and uncertainty; apply only within existing authorization.
- Reuse verification, expose unfinished work, and permit no persistent changes.

Potential ambiguities are hypotheses, not demonstrated defects. The opening and description could put environment improvement more centrally than general collaboration feedback. Lines 33–34 restrict skills/personal guidance to behavior reusable beyond the project; this could discourage a project-local workflow skill, although the preceding project-workflow clause offers an adequate documentation/tooling home. The text does not explicitly distinguish locally fixable issues from external limitations, but its ownership and uncertainty requirements can support that distinction. “Authorized update scope” is reasonable, although broad implementation authorization could be misread as permission to install new future-facing policy.

The strongest case for leaving it unchanged is that capable agents can already produce the intended outcomes from this compact guidance. More explicit wording must earn its cost by resolving consequential ambiguity, rather than filling every conceivable gap.

### Neighboring responsibilities

`project-context` owns agreed durable intent and rationale. Retro identifies lessons and proposes a destination; it does not turn a tentative idea into settled context. `skill-creator` and `writing-for-agents` apply when actually authoring an agreed skill. Project-local procedures and global reusable skills have different scope, but both can be skills. Ordinary review and maintenance remain distinct: a retro is grounded in what the session revealed, rather than an invitation to audit the entire repository.

## Comparable workflows and actual use

Public branch URLs below are moving snapshots inspected on the research date; PRs identify dated changes. Prescribed workflows and owner reports are not comparative effectiveness evidence.

| Source | Mechanism and evidence | Transfer and limitations |
| --- | --- | --- |
| [Matt Pocock retro](https://raw.githubusercontent.com/mattpocock/skills/main/skills/in-progress/retro/SKILL.md) | Explicit-only environment retrospective. Inspects primary session evidence and proposes improvements across navigation, checks, instructions, tool economy, and information access. | Borrow the clear environment purpose. Keep successful discoveries visible too. Do not import the assumption that all review standards belong only with a reviewer, or turn missing CI into an automatic finding in every prototype. |
| [Pocock PR #1083](https://github.com/mattpocock/skills/pull/1083), merged 15 September 2026 | Owner reports retro funneled reviewer gaps into written standards. Revision routes mechanical violations toward deterministic checks and checks for existing automation first. | Concrete reported friction supports considering tools/checks before adding prose. It does not prove that every mechanical issue warrants automation. |
| [Pocock PR #880](https://github.com/mattpocock/skills/pull/880), merged August 2026 | Reports workflows trying to invoke user-only skills and revises cross-skill invocation boundaries. | Explicit triggering must hold across callers too. This is invocation friction, not evidence comparing the usefulness of automatic and requested retros. |
| [giannimassi/agent-retro](https://raw.githubusercontent.com/giannimassi/agent-retro/main/SKILL.md), metadata version 0.1.0 | Verifies transcript identity, inspects conversation and tool-result sizes, examines successes and friction, and proposes concrete edits with action status. Requires a saved report and individual approvals. | Borrow evidence specificity and verify session identity when retrieving history. Leave behind mandatory cost accounting, fixed dollar thresholds, forced root-cause certainty, prescribed report structure, and repeated approvals. |
| [Published agent-retro example](https://raw.githubusercontent.com/giannimassi/agent-retro/main/examples/sample-retro.md) | Shows a correction from sampling conversation messages toward retaining the conversation while reducing tool-result bulk. | A concrete published example of learning from a correction. It is illustrative author material, not an independently verified outcome study. |
| [netresearch/retro-skill](https://github.com/netresearch/retro-skill) | Routes proposed learning among canonical upstream sources, skills, project rules, and harness artifacts. Optional end-session reminder is disabled by default and does not run retro. | Ownership routing usefully includes external systems. A local mitigation and an upstream repair are different proposals. Its per-action approval workflow and optional hook are unnecessary here; Marián chose request-only. |

## Methods beyond skills and empirical challenges

| Primary source | Mechanism or finding | Transfer and limits |
| --- | --- | --- |
| [USAID After-Action Review guidance](https://usaidlearninglab.org/system/files/resource/files/afteractionreviewguidancemarch2013.pdf) | Captures successful practices and improvements for later activities; recommends concrete follow-up with ownership, adapted to context. | Preserve successful methods and connect lessons to future work. Avoid mandatory meeting/report machinery. Search-indexed excerpts were available; full PDF retrieval failed, so this is a limited inspection. |
| [Google SRE postmortem workbook](https://sre.google/workbook/postmortem-culture/) | Contrasts vague/person-focused actions with concrete system changes, ownership, and verifiable outcomes. The worked incident reports a later recurrence with reduced impact after earlier changes. | Explain what intervention would change the next run. Do not import incident severity, mandatory tickets, full timelines, or an obligation to fix every item into a personal brainstorming workflow. Organizational case evidence does not validate our prompt. |
| [Voyager project and experiments](https://voyager.minedojo.org/), 2023 | Stores executable skills with retrievable descriptions, uses environmental feedback, and tests reuse in new Minecraft worlds. | Useful analogue for retaining a successful procedure and making it discoverable. Browser guidance should retain applicability and verification conditions, not just a transcript. Minecraft results do not establish reliable transfer to websites or natural-language skills. |
| [Evaluating AGENTS.md](https://arxiv.org/html/2602.11988v1), February 2026, v1 | Studies issue resolution with several agents on SWE-bench Lite and 138 tasks from 12 repositories. Generated context often reduced success and increased cost; developer-written context produced modest average success gains with extra work. | Challenges “more saved guidance is always better.” Retain non-obvious information with practical reuse value and remove redundancy. This tests repository context, not selective retro-derived skills; model/task settings differ from this workspace. |
| [On the Impact of AGENTS.md Files on Efficiency](https://arxiv.org/html/2601.20404v1), January 2026, v1 | Paired runs on 124 small PR tasks from 10 repositories using one agent configuration found lower average completion time and output-token use with existing context. Comprehensive correctness assessment was out of scope; a sample received sanity checks. | Credible counterweight to dismissing persistent guidance. Different task selection and outcome measures prevent a simple contradiction or universal conclusion. Neither study decides which particular lesson to retain. |

The supported recommendation is selective persistence with a clear future use, not blanket accumulation or blanket rejection. No inspected source establishes the ideal detail level or invocation frequency for Marián.

## Credible directions

1. **Keep the baseline.** Low complexity and already handles most cases. Would leave project-local skill routing and vendor limitations implicit.
2. **Compact clarification within the existing role.** Recommended for discussion: center environment feedback, retain request-only invocation, explicitly allow project-local skills, and make proposals understandable enough to choose among without requiring implementation plans. Preserve evidence checks, smallest useful change, existing authority, and no-change outcomes.
3. **Formal learning pipeline.** Save session logs, categorize every friction point, track action state, and periodically promote lessons. Could help with repeated issues across many sessions, but adds another system to maintain and is unsupported by the reported need. Do not adopt it now.

Potential revision should clarify decisions, not introduce obligatory categories or a fixed number of findings. A recommendation can be firm while alternatives remain open where the tradeoff matters. No need to invent three fixes for a straightforward problem.

### Detail and actionability

Enough detail means Marián can understand the observed obstacle or discovery, its consequence, the proposed intervention and owner, and uncertainty that could change the choice. Include the actual command, missing precondition, or small proposed wording when it carries the lesson. Avoid replaying the whole session or designing an entire tool before the direction is chosen.

For external limitations, distinguish the observable failure from its suspected cause. A verified local workaround can be useful even when the underlying app cannot be fixed locally. If there is no useful mitigation, a concise acknowledgment may still explain consequential friction. Do not inflate it into a local task, a permanent avoidance rule, or an invented upstream diagnosis. A bug-report proposal is an option, not automatic publication.

Retention should depend on likely recurrence and rediscovery cost, evidence that the method worked, maintenance burden, and a discoverable home. A procedure can warrant a project-local skill; a compact fact can fit existing workflow documentation; stable repeated operations might justify a helper script. A fleeting UI detail or speculative cause often warrants no persistent artifact.

## Concrete scenarios

These are analytical walkthroughs, not executed behavioral probes. Only the broad browser experience was reported by Marián; the other cases are synthetic.

| Situation | Useful behavior | Failure to avoid / comparison question |
| --- | --- | --- |
| Repeated website task becomes faster after a verified batching discovery | Explain the useful operational discovery and propose a project-local workflow skill or existing runbook. Retain entry conditions, batching method, and result checks that another agent needs. | Generic “batch more” advice, brittle click transcripts, or globalizing site-specific behavior. Does explicitly allowing local skills improve routing? |
| User corrects violation of clear, loaded guidance | Acknowledge execution failure; assess whether a concrete tool/check would help, otherwise avoid another equivalent rule. | Treating every correction as missing guidance. Baseline already handles this well and should retain it. |
| Hosted app fails twice; cause unknown; tested workaround works | Report observed limitation, useful workaround, and uncertainty; propose retaining only what future runs need. | Claiming the vendor defect is fixable locally or proposing a permanent policy from two unexplained failures. |
| Existing useful skill was never found | Check discovery and routing before proposing a duplicate skill. | Persisting knowledge without a realistic retrieval path. |
| Ordinary successful session with no novel lesson | Say no worthwhile persistent improvement emerged. | Manufacturing praise or maintenance work to fill a format. |
| User chooses “save the browser workflow” after discussing proposals | Implement that agreed scope, inspect the authoritative home, verify affected guidance, and report the result. | Asking again for routine details or applying unrelated proposals. |
| Available history is incomplete | Bound claims to available evidence; retrieve missing context only when it could materially change a finding. | Invented session coverage or obligatory transcript archaeology for a minor observation. |

## Initial independent assessment

Fresh-context GPT-6 Luna at high effort researched public workflows and actual-use evidence. Fresh-context GPT-6 Sol at medium effort assessed the baseline against four representative scenarios without a proposed replacement. Sol judged that the baseline already supports all four; it emphasized the broad authorization phrase and investigation threshold as the remaining ambiguities. The parent sees an additional possible misreading around project-local skills, but no executed test establishes that it occurs. Preserve that disagreement rather than presenting consensus as proof.

At this initial discussion stage, no candidate had been installed and no matched behavioral comparison or A/B Astra review had been run. The later adoption work below supplies those comparisons. Text assessment is not substituted for behavioral evidence.

Open discussion: whether the compact clarification earns its extra wording; whether acknowledgment of a material external limitation should remain visible even without a local fix; and how much concrete proposal detail is comfortable in actual retros. The provisional answer is a short decision-oriented discussion, with depth proportional to consequence and uncertainty. Real-use feedback remains necessary to calibrate this.

## Adopted revision

After Marián's “Yes,” the canonical skill was revised to center environment improvement, retain useful successful discoveries, allow project-local skills, consider the maintenance/reading cost of retained guidance, distinguish provider repairs from local mitigations, and support concrete discussion before applying newly proposed changes. Evidence grounding, execution-versus-guidance diagnosis, smallest useful intervention, existing authorization, and no-change outcomes remain intact.

Added `skills/retro/agents/openai.yaml` with `policy.allow_implicit_invocation: false`, using the supported field documented in the installed skill-creator reference. No optional interface metadata, hooks, or reminders were added. The skill description explicitly requires a user request. This is a configuration change, not a live discovery experiment; this session does not establish when a running application refreshes its skill catalog.

The final skill has 536 whitespace-delimited words including frontmatter, versus the baseline's 347 (`wc -w`). That is a meaningful increase despite remaining a single short entrypoint. Each addition addresses an agreed distinction; continued use should test whether the extra precision earns its cost. No runtime examples, supporting workflow files, or mandatory output template were added.

### Matched execution probes

Six fresh-context GPT-6 Sol agents, all at medium effort, received three identical scenario pairs. The only assigned instruction difference within a pair was the complete skill text: A was the preserved baseline, B the first candidate. Each agent was told to read its assigned skill and session record, then respond as the session assistant to an ordinary brief retro request. No expected answer, parent recommendation, or private rubric was supplied. Other versions and repository guidance were excluded by the brief. Both sides still inherited the surrounding tool/harness instructions; no no-skill condition was run because this comparison tested the agreed refinement rather than whether retro should exist.

These tested execution after explicit loading, not skill discovery. Session records were synthetic summaries rather than actual conversation histories or live browser sessions. Individual skill-read tool traces were not independently audited by the parent; evaluation uses returned responses and, for the follow-up, inspected file artifacts. Do not describe this as observed automatic consultation. One sample per condition supplies examples of behavior, not reliable rates or causality.

| Paired fixture | Baseline A outcome | Candidate B outcome | Assessment |
| --- | --- | --- | --- |
| Monthly Atlas label cleanup: first six records individually, remaining twelve in batches of four using stable links; all eighteen verified; existing operations guide and routing; no timing data | Identified useful discovery, proposed extending the operations guide, acknowledged missing timing evidence, made no changes | Same destination and authority behavior; treated four as an observed size rather than a universal limit; declined unnecessary separate skill/API integration | Both passed. No observed routing improvement from explicitly allowing local skills; B did not overcreate a skill. |
| One npm mistake after reading pnpm guidance, corrected without recurrence; hosted preview twice failed opaquely, documented local preview worked but no shareable preview | Rejected another package-manager rule; mentioned missing shareable preview and suggested provider diagnostics; proposed future fallback after repeated opaque failure | Rejected another rule; distinguished unknown hosted cause, existing local workaround, and possible future provider report; avoided a permanent skip instruction | Both useful. B was more restrained about durable policy, but A more explicitly retained the lost sharing capability. Mixed tradeoff, not an unqualified win. |
| Small successful text correction, correct guidance and diff inspection, no novel method or friction | No persistent changes; disclosed the brief record's limits | No persistent changes; concise explanation | Equivalent useful stopping behavior. |

The browser agents then received the same ordinary follow-up: “Yes, save that workflow in the existing operations document.” Identical starter documents were supplied in isolated fixture directories. Both edited only the assigned document, retained login/search/ID instructions, added stable-link batching and result verification, and reported completion without another approval question. Parent inspection confirmed the resulting artifacts. Both mentioned four as an observed batch size rather than imposing it. No real site was accessed and no actual time saving was measured.

Fixture directories were temporary, under `/var/folders/hy/_hkw66sd5vz1qcq86zd2mg8r0000gn/T/retro-rethink-a1w8jfz0`. Their continued existence is not required to use the skill. Agent identifiers were `retro_probe_browser_a/b`, `retro_probe_friction_a/b`, and `retro_probe_clean_a/b`. The fixture facts and results above preserve the consequential evidence without adding test prompts to runtime guidance.

### Independent comparison and resolution

A fresh GPT-6 Astra agent at high effort read complete texts labeled A and B with equivalent formatting, neutral requirements, no conversation history, no indication which was newer, and no preferred verdict. It preferred B with modest confidence, citing clearer environment scope, retention criteria, external ownership/uncertainty, and conversational follow-through. It favored A's compactness and noted that B narrows general collaboration feedback; that narrowing matches the agreed purpose. Its approximate word counts were inaccurate; measured counts are recorded above.

Three concrete text changes followed its assessment: remove a repeated request-only sentence; permit investigation when needed to support or resolve a consequential finding rather than only when it could change a finding; and finish when authorized improvements are completed or blockers explained, not simply clear. These were direct ambiguity fixes, not reasons to add further rules. Parent review checked the affected evidence and completion obligations against the existing scenario outcomes. The six probes used the first candidate and were not rerun after these three wording changes; they are not behavioral evidence for every word of the final revision.

### Validation and remaining uncertainty

The skill-creator validator passed using `uv run --with pyyaml` after the default Python lacked PyYAML; no repository dependency was added. YAML policy and frontmatter were parsed, references and the canonical symlink were checked, and whitespace validation passed. Review reused the scenario results and independent comparison rather than adding another general review round.

The evidence supports a coherent clarification, not a proven general improvement. Real retros must establish the comfortable detail level, whether local skills are proposed when they genuinely help discovery, and whether significant external limitations remain visible without noisy or speculative recommendations. No commits, pushes, separate installation, global guidance changes, or other model-variant synchronization were performed.

## Cross-model pass: rebuilt around hidden friction (2026-09-30)

Part of the cross-model pass (see [stack sheet](skill-stack-reference-sheet.md)). The user's purpose, restated: models get "unstuck" so well that friction goes unnoticed, especially in background tasks; a retro should make the agent reflect on those issues and propose fixes so they are not repeated. He added inefficiency: repeated tasks an agent struggles through (for example hand-built probe setups) even when everything works in the end.

### Real-use evidence

Two fresh-context extractions (Opus 5.5).

- **Retros:** three real invocations. Only one paid off (Claude Code, agent-skills, 2026-09-29): the user pointed at friction ("I saw that you had issues with the test runs"), the agent checked logs and `/tmp` artifacts, found the testing notes were wrong and truncating evidence, fixed them, and built `probe.py`/`judge.py`, reused since. The other two (Codex, 09-14 byt and 09-15 agent-skills) answered from memory with one and zero tool calls, never opened subagent logs, concluded "my judgment, no rule needed", and nothing was applied. No reflective question was ever asked without the skill.
- **Hidden friction (22 sessions):** friction reached the user only when it blocked the agent or the user asked. Routed-around friction was omitted or understated in every case checked, including workarounds that changed what was verified or shipped: B-49's own new tests skipped for missing Docker behind "23 skipped"; a filename-collision workaround shipped in B-66's diff; production verified by logging in with the local `.env` password; "real browser upload verified" after a 178 MB Playwright install and a timeout. Subagent friction rarely propagated (B-49 reviewers could not run `just check`; an approval subagent auto-approved escalations). Workarounds were rediscovered repeatedly (PyYAML for the skill validator in about 8 sessions, PDF tools in 14 byt sessions, the eza `ls` alias in about 12 Claude transcripts). A per-project note (sandboxed `gh` "token invalid") did not carry over to the next project. Much of the costliest friction came from the Codex sandbox before the switch to full access on 2026-09-05; agents took its misleading errors at face value.

### Decisions

1. Read the record, not memory: the session transcript and subagent or background logs; failed calls, retries, fallbacks, changes of approach; start from what the user points at.
2. What counts, most consequential first: workarounds that changed what was verified or shipped and what could not run; misdiagnosed errors; wrong, stale, or missing guidance and misfired skills; inefficiency (long or repeatedly hand-done work that may deserve a script, check, or skill); discoveries worth keeping. Leave out routine noise.
3. Pattern or one-off: targeted search of earlier sessions for the specific error or procedure. Name both failures: rules from one-off slips, and "my mistake, no rule needed" for a recurring problem.
4. Fix at the right level: prefer changing the environment; project facts to the project; the user's working preferences to their global guidance; one machine's or harness's quirks to that machine's setup or harness config, because the user's global guidance is personal and synced across several machines.
5. Report in conversation ordered by payoff (evidence, cost, recurrence, fix and home); apply what is agreed. Request-only stays (`agents/openai.yaml`, `skillOverrides`).
6. Stop the omission at the source too: the global guidance line on verification now also asks for "any workaround that changed what was verified or shipped".

Baseline: repository `63317e1`; SKILL.md SHA-256 `c64767a578c968245472f9973bdb1f174cc1eed1d9365704f74ec59bc0104ec2`.

### Tests

Real sessions with known friction instead of synthetic fixtures: B-49 (2026-08-31), B-66 (2026-09-05), and the 2026-09-24 shaping rethink (PyYAML). One turn per run, invoking the skill explicitly (`/retro` in Claude Code, `$retro` in Codex) on the session log path with "Report only for now; do not change anything." Opus 5.5 and GPT-6 Astra at high effort, baseline then candidate. Opus 5.5 and GPT-6 Astra (high) judged each pair blind with a rubric carrying the survey's known-friction list, and could read the session logs to check claims.

Candidate won 11 of 12 judgments (the loss: the Astra judge on Astra's B-66 pair, which preferred the baseline's recurrence and inefficiency coverage). What the judges credited: candidate runs read subagent logs and searched earlier sessions, so they found that the PyYAML workaround had already been solved on 09-13 and rediscovered, that the hard-wrap correction had been made twice, that the `gh` misread recurred and blocked delivery, and they placed fixes in machine setup rather than project prose; baseline runs treated these as one-offs or proposed a duplicate wrapping rule. Baseline Opus was already strong on B-49 (it caught the understated skipped tests).

Weaknesses: the candidate Opus B-49 run conflated a colleague's later commit with the session's untested code and declared problems "already eliminated" too categorically; several runs caught fewer small items (a guessed `npm run typecheck`, the missing issue-tracker doc); no run flagged the auto-approving approval subagent as a problem. Not chased.

What these tests cannot show: retros on the current conversation after compaction, whether proposed fixes get applied, and the effect of the new global reporting line.

Final SKILL.md: 575 words, SHA-256 `bb3ee1b3c72cb0d3b2be581bce5ea4e9fcd2a66c1c5e16aa0c462bff2b44005d`.

