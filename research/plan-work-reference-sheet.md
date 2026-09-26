# plan-work rethink reference sheet

Research date: 2026-09-26. Status: agreed changes implemented and reviewed; validation complete. Earlier sections preserve the exploratory sequence and are superseded by the implementation record below.

## Question and reported need

Marián originally wanted a way to preserve discussions/specifications and work with projects using Matt Pocock's skills. He also likes brainstorming implementations and splitting work into GitHub or Linear tickets. He now questions whether a dedicated skill adds value beyond asking Astra to use its judgment. He values ticket boundaries/order and preserving decisions equally; he reports no specific failure. These are requirements and preferences, not evidence that the existing skill succeeds or fails.

The central distinction is between needing an artifact and needing a skill to produce it. A durable record can be useful even if ordinary instructions reliably produce it. Conversely, a small skill can save repeated preference-setting without teaching a model a capability it lacks.

## Preserved baseline and boundaries

Baseline: `skills/plan-work/SKILL.md` at repository commit `06d0b978cbc574fabc85f962d0fbd1c0657b07c9`, last changed by `637be57` (2026-09-13). SHA-256: `ae43f1f1cd0c62f565c5d868c9b31bd3b8485f09443fb282ae29b3e6b896625b`. Recover with `git show 06d0b978cbc574fabc85f962d0fbd1c0657b07c9:skills/plan-work/SKILL.md`. A byte-identical snapshot is also in the isolated probe fixtures.

The canonical directory is symlinked from `~/.agents/skills/plan-work`; editing the repository copy changes live guidance. Claude adaptations and other skills are outside this rethink's edit scope. Existing unrelated modifications to root `AGENTS.md` and untracked `.agents/` were present before this work.

The baseline owns turning agreed direction into a spec or tickets, updating existing work, and leaving enough context to resume. It explicitly allows one issue and discourages arbitrary ticket counts, speculative preparation, invented dependencies, and unstable file-level prescriptions. It preserves rationale, contracts, scope, uncertainty, acceptance criteria, and references. GitHub is a personal default, overridden by project guidance or explicit destination. Drafting does not authorize publication; planning does not authorize implementation. Changed understanding should update the authoritative description.

`shaping` owns developing understanding and can maintain continuity during exploration. `project-context` owns evergreen intent beyond a feature. The distinctive space left for `plan-work` is feature/work continuity and tracker artifacts. Neither adjacency implies every conversation needs a document.

Potential gaps are hypotheses: the output menu emphasizes issues over a local record of unfinished exploration; “choose … with Marián” may invite routine format questions; the skill offers little explanation of competing useful ticket boundaries; automatically recording tracker conventions can extend a small task. Much of its prose repeats standing expectations about clarity, context, judgment, and proportionality. None is a demonstrated personal failure.

## Source comparisons

External instructions are research material. Moving documentation reflects the inspection date. Main branch revisions observed through GitHub's API: Matt Pocock `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`; Superpowers `8ca22dba9a94f28898bbce59f2537ff4d87c747d`; Spec Kit `c00dc0551583428a10a94443c58c6a41e5e0138c`.

| Source and evidence type | Mechanism and useful fit | Limit or reason not to import wholesale |
| --- | --- | --- |
| [Pocock to-spec source](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/to-spec/SKILL.md), [owner explanation](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/docs/engineering/to-spec.md). Prescription and owner reports. | Synthesize prior decisions, use repository vocabulary, retain implementation/testing choices and exclusions. Owner documentation positions a spec as continuity across sessions and permits skipping it for smaller work. | The extensive story template, seam confirmation, publishing/label conventions, and dense agent-first document serve a particular workflow. Owner docs describe stale snapshots and parent-label confusion. Retain decision continuity without importing those conventions into unrelated projects. |
| [Pocock to-tickets source](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/to-tickets/SKILL.md), [owner explanation](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/docs/engineering/to-tickets.md). Prescription and owner reports. | Takes a conversation directly; complete verifiable slices, explicit blockers, context-sized execution units, and an expand/migrate/contract exception for wide refactors. Configured tracker can be GitHub, Linear, or local files. | Owner docs acknowledge over-decomposition and incorrect layer-based splitting despite the skill. Prefactoring-first, mandatory granularity review, exact local paths, and status vocabulary need not fit Marián. Parent/sub-issue grouping and blocking dependencies should remain distinct even where upstream language blurs them. |
| [Pocock issue #1078](https://github.com/mattpocock/skills/issues/1078), opened 2026-09-13. Single-user report plus inspectable template gap. | Reports agreed testing seams lost between spec and tickets. The inspected ticket template lacks a dedicated seam field. Useful question: can the next worker recover every consequential decision from its actual inputs? | The reporter's 17 implementation runs do not establish causation or prevalence. A missing template field does not make information loss inevitable. Copying every spec field into every ticket would create maintenance problems; sufficient context and reliable references may be better. |
| [Superpowers writing-plans](https://github.com/obra/superpowers/blob/8ca22dba9a94f28898bbce59f2537ff4d87c747d/skills/writing-plans/SKILL.md). Prescription. | Specifies interfaces, files, tests, verification, and reviewable task boundaries. Useful when implementers need exact coordination contracts and context is deliberately partitioned. | More execution detail and prescribed test/commit steps than a deferred work record needs. Exact choices can become stale or prematurely decide routine implementation. Its current source is more nuanced than older descriptions claiming every task must take 2–5 minutes. |
| [Spec Kit quickstart](https://github.github.com/spec-kit/quickstart.html). Official process prescription. | Separate spec, design, and tasks plus consistency analysis make disagreements across artifacts inspectable. Useful where several contributors depend on explicit contracts. | Multiple artifacts create their own synchronization work. Even its small-feature path is a substantial workflow. The existence of consistency tooling does not establish that this process is proportionate for personal prototypes. Borrow authoritative ownership, not the whole pipeline. |
| [Shape Up: Map the Scopes](https://basecamp.com/shapeup/3.3-chapter-12), [R&D mode](https://basecamp.com/shapeup/2.3-chapter-09). Practitioner method and experience. | Scopes emerge while building; organize around coherent finished portions. For novel products, spike key uncertainties before committing architecture and delivery scope. A saved direction and one learning step can be more accurate than a full backlog. | Basecamp's staffing, cycles, and appetite conventions need not fit a solo agent workflow. This supports conditional decomposition, not a blanket ban on upfront tickets. |
| [Linear conceptual model](https://linear.app/docs/conceptual-model). Official product concepts. | Issues track work; projects group an outcome. The artifact hierarchy can follow actual coordination needs. | Tracker structure does not determine useful engineering boundaries, nor require a project for every feature. |
| [SpecMine v3](https://arxiv.org/html/2608.25202v3), revised 2026-09-01. Primary empirical dataset paper. | Collects specifications and links to repository/PR artifacts; usefully distinguishes observable co-change from whether a spec actually guided implementation. | It does not compare planning skills against ordinary Astra requests. Artifact counts and adoption provide no causal evidence that this skill improves Marián's outcomes. |

Compatibility inference: existing Pocock-style projects may need their configured destinations, labels, identifiers, references, and execution prerequisites preserved. That is a project-specific contract to inspect, not a reason every personal planning request must recreate the upstream workflow. No reviewed source establishes superiority over a well-contextualized Astra request.

## Credible options

1. **Keep unchanged.** Already compact relative to workflow frameworks and sensibly permissive. Provides stable personal defaults across models. Cost: some redundant guidance and no demonstrated advantage yet.
2. **Keep a much smaller preference skill.** Preserve human-readable work continuity, simplest useful artifact, judgment about splitting, genuine dependencies, and an authoritative current record. Let the model supply ordinary planning competence. Cost: still another skill, and excessive compression might lose important exceptions.
3. **Remove it and use ordinary requests.** Lowest standing instruction burden; let task context drive artifacts and boundaries. Cost: preferences may vary between sessions/models, and requests may need occasional correction. Do not simply move the entire skill into global guidance.
4. **Use a reusable prompt rather than an auto-discovered skill.** Useful if invocation convenience is the main benefit. Cost: another asset and a manual selection step; no evidence this is necessary.

A heavier decomposition algorithm is justified only by a recurring failure or an execution system that needs a precise contract. Ticket count is a consequence of review, dependencies, learning, and handoffs—not a target or proxy for progress. No fixed number of tickets is proposed.

## Scenarios that distinguish the options

| Situation | Useful outcome and distinction to inspect |
| --- | --- |
| Agreed CSV import spanning later sessions | A few meaningful work units or one sufficiently bounded issue, preserving duplicate rules, shared validation, and rejected framework. Splitting should make progress verifiable without reopening decisions. |
| Search prototype with an unresolved approach | Save goal, privacy constraint, alternatives, and next comparison. Avoid presenting embeddings or a complete delivery backlog as settled. |
| Later correction to import semantics | Replace superseded requirements and adjust affected tickets; preserve rationale and unaffected constraints. An appended contradiction is not enough. |
| Small fix requested for immediate implementation | No separate planning artifact unless requested or independently useful. Existing implementation authorization survives planning. Analytical boundary case, not yet executed. |
| Existing upstream spec with an execution convention | Inspect the actual downstream inputs and preserve necessary references/contracts; do not require renaming documents or importing upstream rituals. Analytical case, not yet executed. |
| Wide mechanical migration | Split along real compatibility/dependency boundaries when needed; do not force UI-style vertical slices. Analytical case, not yet executed. |

## Evidence and decision record

Independent research: GPT-6 Luna/high inspected Pocock sources and reported friction; GPT-6 Sol/medium inspected complementary planning methods. Parent checked consequential upstream sources directly. Their opinions are not behavioral evidence.

Executed exploratory matched probes: two fresh GPT-6 Astra/medium contexts, identical personal guidance from `context/AGENTS.md` and two fictional user scenarios, with the baseline skill supplied to Y and no task-specific skill supplied to X. Neither had the rethink conversation or redesign rationale. Both received the same correction follow-up. Fixture/tool constraints prevented real tracker or implementation actions. Raw fixture and response files are under `/tmp/plan-work-rethink.7zOMiE` (`common.md`, `baseline.md`, `x-initial.md`, `y-initial.md`, `x-followup.md`, `y-followup.md`). Temporary files are local supporting evidence, not durable project guidance.

The feature fixture specified three CSV exports with differing headings; mapping, preview, shared create-book service validation, explicit saving of valid rows despite invalid rows, deduplication by ISBN only, no background jobs, a rejected generic framework, and undo only as a possibility. The user requested draft GitHub tickets for next week and let the agent choose a sensible split. The independent search fixture required local-only processing, left keyword/embedding/hybrid open, and requested a note for resuming next month; the agreed next evidence was a comparison of representative queries and notes, with collection/relevance judgments still unresolved.

The identical follow-up changed import semantics to save nothing if any row is invalid, retained preview, rejected a parent issue, and requested replacement drafts plus reasons for ticket boundaries. All other agreed constraints remained.

| Observation | No task-specific skill (X) | Baseline skill (Y) |
| --- | --- | --- |
| Initial decomposition | Three tickets: mapping/preview, shared validation, saving/deduplication. | Two tickets: mapping/validated preview, saving/deduplication. |
| Decision retention | Retained shared service, ISBN-only matching, no framework/jobs, deferred undo. | Retained the same consequential decisions. |
| Deferred search idea | Resumption note with open alternatives and evidence gathering; no invented chosen stack. | Same useful artifact; somewhat more explanation and explicit success-judgment uncertainty. |
| Correction | Replaced partial-save criteria, retained three tickets with a rationale, preserved other constraints. | Replaced partial-save criteria, retained two tickets with a rationale, preserved other constraints. |
| Boundary behavior | No publication, implementation, parent issue, or extra format interview. | Same. |
| Subtle save semantics | Enforced validation in the save path; distinguished invalid rows from unrelated storage failures; interpreted duplicate ISBN rows as skips. | Same. |

Parent assessment: both outputs were usable on the dimensions exercised. Two versus three tickets reflects a defensible granularity choice, not proof of superiority. Both inferred a nonblocking duplicate-skip policy, a plausible elaboration that still deserves attention when the actual domain contract is available. Neither run demonstrates durable retrieval or implementation success. The skill did not cause the hypothesized extra format interview in this sample. These are executed drafting probes with one sample per condition, not reliability estimates or proof of equivalence. They do not test shorter prompts, noisy real conversations, other models, live tracker operations, or longer gaps.

Independent comparison: a fresh GPT-6 Astra/high reviewer received the shared preferences/tasks and neutrally labeled conditions A (no additional task-specific instructions) and B (baseline body), without conversation history, redesign rationale, or a preferred conclusion. It separately assessed the text and inspected the single-run artifacts. The exact correction prompt was supplied in a follow-up after the reviewer flagged it as missing. The reviewer modestly preferred B's two-ticket split and clearer uncertainty, found both conditions competent, and recommended preserving the distinctive maintenance/decomposition guidance while removing repetition. It identified the same untested tracker-maintenance use case and plausible-but-inferred duplicate-skip behavior. This assessment is judgment, not an additional behavioral experiment. Raw review: `/tmp/plan-work-rethink.7zOMiE/review.md`.

Proposed direction for discussion: a much smaller preference skill for making work resumable. Its core would be choosing the simplest useful record; retaining decisions, rationale, constraints, and uncertainty; using meaningful verifiable work boundaries and genuine blockers when splitting helps; and revising the authoritative record as understanding changes. Ordinary technical planning remains a matter for agent judgment. Explicitly allow a note without a tracker, avoid routine format interviews when choice is delegated, and preserve project-specific tracker conventions. These are proposed responsibilities, not an implemented or behaviorally validated candidate.

The strongest alternative is removal and ordinary requests, especially for Astra-only one-shot drafting. That option performed competently here. Retention is justified by a desire for stable preferences and repeated work maintenance, not by evidence that Astra lacks planning ability. Keeping the baseline unchanged also remains reasonable: observed behavior was already proportionate, and wording concerns are largely hypothetical.

Open decision for Marián: whether that small reusable preference earns a named skill or whether ordinary requests are enough. No rewrite, deletion, live configuration change, commit, push, or installation has been performed. Baseline bytes were checked against both the isolated snapshot and the preserved Git revision. Research formatting was checked; no application tests apply to this research-only change.

## Follow-up: project context, decisions, and reading burden

Marián raised a more fundamental need: preserve direction and reasoning that code cannot reveal without requiring future agents to read a growing document archive. He wondered whether decisions and ADRs belong in plan-work because project-context is for evergreen understanding. This does not yet settle whether plan-work stays, changes, or is removed.

Local inspection corrects that premise: `project-context/SKILL.md` explicitly owns consequential choices/reasons (lines 17–19), relevant ADRs and single ownership (24–36), current versus superseded intent (38–46), and task-specific discovery pointers (52–54). `ENGINEERING.template.md` includes consequential decisions and optional links to decision records. `plan-work` already routes durable guidance toward project-context (59–61). Evergreen describes maintained relevance, not an exclusion of concrete decisions. Even a rule confined to one feature can deserve durable context if future changes need it.

Additional primary references inspected 2026-09-26:

- [Michael Nygard, Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions), 2011-11-15: short records preserve the context, choice, status, and consequences of significant decisions; superseded records remain identifiable. This is an original method description and early practitioner report, not an agent retrieval experiment. Borrow selective preservation of rationale and explicit status; do not require an ADR for every settled choice.
- [Matt Pocock domain-modeling source](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/domain-modeling/SKILL.md): glossary updates and selective ADR creation belong to domain modeling; documents are created when content exists. Its ADR threshold combines reversal cost, surprising behavior, and real alternatives. Its glossary-only CONTEXT.md has a narrower job than Marián's project-context skill. Importing that separation mechanically would obscure the existing ownership.

Proposed responsibility boundary, not an implemented change:

| Information need | Owner / usual home |
| --- | --- |
| Outcome, delivery scope, remaining uncertainties, decomposition and dependencies of current work | plan-work; issue, work note, or existing spec |
| Current intent or rationale that should constrain future decisions after this work ends | project-context; relevant evergreen section |
| Significant decision whose alternatives, consequences, or history deserve their own record | Optional ADR managed as project context, linked from the relevant current guidance |
| Where to find task-relevant guidance and active work | Short existing AGENTS routing; no separate mandatory index |

The skill handling a conversation can capture or update more than one artifact without the user manually invoking a chain. Ownership concerns where information is maintained, not which agent is allowed to write it. One conversation need not produce all artifact types. An existing issue can retain detailed history while a concise evergreen statement carries the lasting rule and reason; an ADR is optional when that is insufficient or the project already uses them.

Retrieval proposal: keep universal constraints and routing small; point from task/area to the relevant current section; follow its direct decision-history links only when needed to understand or reconsider that choice. Do not make every task read all evergreen docs or the ADR archive. A tiny file can remain one file; split when actual topics have different readers or tasks. A short navigation summary may point to an authoritative decision without reproducing an independently maintained account of it.

Lifecycle proposal: when an agreed choice becomes continuing guidance, preserve it while its rationale is available; check before closing the work that necessary future context is discoverable. Do not wait until shipping when the decision already governs other work. Distinguish agreed future direction from already-implemented behavior. Updating an existing documented rule belongs with an authorized change to that rule; this does not justify documenting every conversation or treating suggestions as agreements.

A fresh GPT-6 Sol/medium independently inspected both skills and templates. It confirmed that decisions/ADRs are already included, and identified the capture-to-maintenance handoff as a plausible gap. No actual missed-decision incident has been supplied. These are design proposals and a text assessment; neither retrieval nor lifecycle changes have been behaviorally tested. The next question is the shared capture/maintenance/discovery behavior, before selecting a heavier plan-work design. Neither runtime skill has been edited.

## Direction clarified: agent-led delivery with oversight

Marián wants agents to discover relevant context as needed and maintain useful documentation from discussions, exercising judgment about what deserves capture. He increasingly prefers agent-led delivery with his oversight; shaping remains a more tightly collaborative activity. Skills should supply small directional preferences and prevent meaningful mistakes rather than prescribe the full work process. This is a stated preference, not proof that current agents reliably perform every maintenance or retrieval task without guidance. The hypothesis that older agent limitations explain external workflow structure has not been established; repeatability, coordination, and artifact contracts can also explain it.

This changes the retention criterion: a skill should earn its place through distinctive judgment, personal preferences, or a consequential boundary, rather than because it names a normal activity an agent can perform. Under this preference, removing plan-work becomes a stronger candidate than preserving it mainly for general planning consistency. Existing probes support the feasibility of ordinary planning requests but do not establish reliable performance across real work.

Proposed organization: a small standing expectation for context discovery and maintenance applies during ordinary work; project-context supplies authoring guidance when maintaining durable intent; shaping owns collaborative exploration; ordinary task judgment chooses plans, tickets, and granularity. No mandatory sequence of skill invocations or document creation follows. Preserve settled intent and meaningful reasons, distinguish proposals from agreements, replace obsolete guidance, and make consequential reinterpretations visible while Marián can influence them. Routine maintenance should not require asking him to select a skill or document destination. If this direction is adopted, shared guidance should have one authoritative home rather than being copied into every skill.

No runtime changes are authorized by inference here: the discussion establishes design preferences, while the precise edits and the fate of plan-work remain to be settled. Existing instructions about editing canonical context first and separately authorizing live global configuration changes remain applicable.


## Agreed outcome and implementation

After the agent-led delivery proposal, Marián replied “Sounds good.” This authorizes retiring plan-work, refining project-context, and placing shared context-discovery/maintenance expectations in canonical personal guidance. The proposal does not authorize synchronizing live global guidance. The earlier no-change statements describe the exploration stages.

Implemented changes:

- Removed `skills/plan-work/SKILL.md` and its runtime discovery symlink. Ordinary task judgment now handles plans, ticket breakdowns, and work records.
- Added scope-bounded delivery ownership and a compact context-discovery/maintenance expectation to `context/AGENTS.md`. Preserved the actual GitHub Issues default with explicit project/user overrides, rather than migrating the old planning checklist.
- Refined `skills/project-context/SKILL.md` to cover lasting understanding during other work, carry feature-local decisions into relevant guidance when needed, distinguish future intent from implemented behavior, keep ADRs optional, and provide task-specific routing. The four existing templates remain optional and unchanged.
- Left root `AGENTS.md`, Claude assets, and `~/.codex/AGENTS.md` unchanged. The project-context skill edit is live through its existing symlink; the new shared standing guidance is canonical-only until a live sync is explicitly requested. Nothing was committed or pushed.

The old context and project-context files are recoverable from Git commit `06d0b978cbc574fabc85f962d0fbd1c0657b07c9`. Byte snapshots, proposed guidance packages, fictional repositories, and independent-review output are under `/var/folders/hy/_hkw66sd5vz1qcq86zd2mg8r0000gn/T/context-continuity-u46eqnb5`.

Executed matched comparison: two fresh GPT-6 Sol/medium contexts received identical fictional project files and user requests, with A assigned the proposed standing guidance/project-context and B assigned the old standing guidance/project-context/plan-work. Both prepared an existing CSV import work item for a future agent, then received the same clarification and tentative-background-import follow-up. A fresh GPT-6 Astra/high reviewer separately compared equivalently labeled A/B guidance without the conversation or a preferred verdict. This compares the agreed package change, not the isolated causal effect of one sentence or skill. Earlier Astra drafting probes were reused for ordinary planning competence.

| Observed behavior | Proposed package A | Baseline package B |
| --- | --- | --- |
| Work preparation | Updated existing item, used one item with internal breakdown, no parent or implementation. | Updated existing item, used one item, no parent or implementation. |
| Lasting intent | Updated ENGINEERING.md and explicitly distinguished current partial-write code from agreed future behavior. | Updated ENGINEERING.md, but phrased the target behavior as current behavior. Work item still identified code needing change. |
| Context consumption | Read routing, engineering, product, design, work item, and importer; listed ADR directory but did not read the unrelated search ADR. | Read the same project-content files; did not read the unrelated search ADR. |
| Unwarranted certainty | Added atomic rollback for storage failures as if it were agreed, beyond the explicit zero-writes-for-invalid-data requirement. | Made the same extension. |
| Correction and tentative idea | Removed added rollback semantics, updated both affected records, kept background imports out of this implementation. | Same. |

Neither run proves selective retrieval at scale. Both read broad context for a small task; neither created an ADR or extra context files. Both maintained context without a separate user request for a context skill, so this sample does not show a unique capture benefit from the new standing rule. The explicit future/current distinction in A is a useful observed difference, not a reliability estimate.

The observed inferred-requirement error prompted one narrow adjustment in project-context: do not record an inferred requirement as settled intent. One fresh Sol/medium rerun used identical original fixture inputs with this updated candidate (A2). It retained the narrower validation requirement without inventing storage-failure rollback semantics, clearly separated existing code from agreed future behavior, and produced two linked peer work items with acceptance criteria. This is a targeted additional sample, not a controlled estimate of the sentence's effect. Initial and follow-up A/B artifacts are retained separately under the temporary fixture root.

Independent text review preferred A's continuity, ownership, routing, and future/current wording. It recommended retaining a compact planning aid for acceptance criteria, meaningful work slices, work-record updates, and explicit publication/implementation boundaries. The parent retained the agreed retirement: those are useful activities, but omission of a checklist does not establish loss of capability, the behavioral probes remained competent in work preparation, and standing scope/authority requirements still apply. The actual tracker preference was preserved. No recurring planning failure was established to justify replacing the retired skill with another aid. This is a deliberate tradeoff to revisit if ordinary requests repeatedly lose scope, rationale, or useful boundaries.

Structure checks passed: skill-creator's validator, template link existence, removal of references to plan-work outside historical research, intact project-context symlink, and unchanged bytes for root and live global AGENTS files. The system Python lacked PyYAML; the validator ran successfully using an isolated `uv --with pyyaml` runtime without modifying repository dependencies.


Final disposition: the agreed package is complete. Independent review was applied as evidence rather than a requirement to retain a planning aid. The narrow post-review wording correction was checked with the targeted A2 execution and structural validation; no broader rewrite followed. Final validation confirmed unchanged unrelated root guidance, unchanged live global guidance, valid skill structure and template links, retired discovery symlink, and clean whitespace. Claude variants and templates were unchanged.

Real-use uncertainties remain: these small synthetic samples do not establish reliable automatic skill selection, selective retrieval in a large repository, behavior under noisier discussions, or performance across models. A brief instruction reduced neither need for judgment nor the possibility of inferring too much. Future changes should respond to observed friction, especially repeatedly lost rationale, invented commitments, or needless document reading; no further rules were added speculatively.


## Follow-up: terse entry-point testing

Marián questioned whether detailed test prompts were doing the work the skills should do, masking their contribution. The earlier prompts did supply consolidated decisions, explicit boundaries, and skill bodies; those runs tested preservation and execution more directly than discovery or spontaneous maintenance. Their comparison remains informative within those limits, but they should not support broader claims about ordinary terse requests.

A new matched exercise used two fresh GPT-6 Sol/medium agents. The only task request was “Please fix issue #14.” Identical small Python repositories contained an ordinary issue description, partial-import implementation, three initial unit tests, existing engineering rationale for partial saving, and AGENTS pointers to relevant documentation. Personal standing guidance and a skill catalog were supplied as setup. Agents chose whether to open skill bodies; project-context was not preloaded. P received old standing guidance, the old project-context description/body, and plan-work in the catalog. Q received current standing guidance and project-context, with plan-work absent. Both had identical copies of diagnose, check-work, writing-for-agents, and shaping available. Isolation instructions constrained filesystem/external actions but supplied no solution, documentation task, test design, or acceptance checklist.

The issue explained the desired result and reason: an invalid row should prevent all saves so the user can correct the CSV and retry. Keeping necessary task information in a discoverable issue is deliberate; a terse request should not require guessing missing product intent. This is still a well-organized, small synthetic project with explicit routing, not a large or messy repository. The surrounding agent harness and its metadata were not independently removable; the fixture catalogs were designated as the skill sources for both conditions.

Observed outcomes:

- Both implemented the same two-pass fix, added a regression test covering multiple invalid rows and a corrected retry, preserved manual creation behavior, updated ENGINEERING.md with the new behavior and rationale, and completed the local issue. Neither created extra documents or introduced broader rollback semantics.
- Both passed five independent parent-authored checks: valid import, late invalid row with pre-existing notes, early/multiple invalid rows, corrected retry, and unchanged manual validation. Those checks were outside the agent-visible fixtures; three failed on the preserved original code. Each agent's resulting four-test suite also passed.
- Both then received only “Would moving imports to the background help?” Each discussed responsiveness versus the validation problem and recommended retaining synchronous imports absent demonstrated delays. File hashes confirmed neither made further project edits during this exploratory turn.
- After both task turns, agents were asked to report what they had actually read, without opening more files. P reported reading check-work and writing-for-agents, but neither project-context nor plan-work. Q reported reading diagnose, check-work, project-context, and writing-for-agents, including consulting project-context before updating ENGINEERING.md. These skill-loading observations are agent self-reports, not independently captured tool traces.
- Both reported reading the issue, code, tests, AGENTS, and all three small project-context documents. Neither reported reading the unrelated search ADR. This is limited evidence of avoiding the archive, not proof of minimal context consumption.

Interpretation: terse entry-point testing provides more relevant evidence for agent-led delivery and autonomous context maintenance. The current package worked in this example, including reported spontaneous project-context selection. The baseline produced an equally successful outcome without that skill, so the experiment establishes neither superiority of the new package nor necessity of project-context for this task. No runtime instruction changes were made in response to these results.

Future comparisons should include terse user requests with realistic, discoverable project evidence and skill catalogs, without repeating the behavior being tested in the task prompt. Detailed handoffs remain useful as a separate test category. Evaluate artifact changes and task outcomes, record tool/skill discovery separately, and distinguish equivalent outcomes from demonstrated improvement. Vary projects and task shapes before making reliability claims.

Artifacts: `/var/folders/hy/_hkw66sd5vz1qcq86zd2mg8r0000gn/T/terse-continuity-p48tuhla` contains the paired Git fixtures, exact requests and condition mapping, original code, independent checks and outputs, initial diffs, and before-follow-up file hashes. Only this research record changed in the actual repository during the follow-up.


## Testing-method guidance updated

Marián requested incorporating the testing lesson into the project-local rethink-skill. Updated only its comparison section: match ordinary requests, include terse entry points for autonomous behavior, retain actual task requirements while excluding the evaluator's private rubric and coaching, distinguish discovery via catalog from direct skill-body execution, label harness/evidence limits, and include no-skill conditions when assessing necessity. Detailed handoffs remain valid when representative; the guidance does not require every test to be terse or every comparison to use both modes.

This is a focused correction grounded in the preceding experiments, not a new full rethink. A fresh GPT-6 Astra/high reviewer compared neutral A/B texts without history or a preferred result. It preferred the candidate, found no blocking issue, and suggested distinguishing private evaluation criteria from actual user requirements and avoiding an implied mandatory handoff condition. Both clarifications were incorporated. Validation covered skill structure, whitespace, and the narrow diff; the revised meta-procedure was not run recursively as a new behavioral experiment. The original text snapshot is under `/var/folders/hy/_hkw66sd5vz1qcq86zd2mg8r0000gn/T/rethink-testing-guidance-owxrdv6p/A.md`. No global installation, commit, or push was performed.


## Live activation

Marián subsequently requested making the shared guidance live and committing/pushing the work. Synchronized `~/.codex/AGENTS.md` from canonical `context/AGENTS.md` and verified byte equality. This supersedes the earlier canonical-only activation notes. The pre-existing root `AGENTS.md` edit remains outside this change; the revised project-local rethink-skill is included in the repository changes.
