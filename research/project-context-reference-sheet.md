# Project-context reference sheet

Research date: 2026-09-27. Initial research was followed by an agreed compact revision; implementation and verification are recorded below. External guidance is evidence to assess, not adopted instructions.

## Request, evidence, and baseline

Marián considers project-context crucial. He wants lasting project knowledge to help both future agents and colleagues who fix or extend his projects, with little documentation bloat. He asks about CONTRIBUTING.md, README, document ownership and necessity, completeness of non-obvious guidance, Google's DESIGN.md convention, and composition with writing-for-agents. He reports no observed failure and has not tested the approach across all projects. These are desired outcomes and open questions, not authorization to adopt a particular document architecture.

Inspected all five canonical project-context files, root AGENTS.md, canonical personal context/AGENTS.md, writing-for-agents, shaping, and the relevant prior research in writing-for-agents-reference-sheet.md and plan-work-reference-sheet.md. Target files are preserved in Git at `8c68de0c1b3f9b1a1f3b0138e406bb068455b0f9`; the skill's last modifying commit is `397ea14`. The worktree was clean at research start. Exact target-file hashes are recorded below. The runtime directory `~/.agents/skills/project-context` symlinks to the canonical repository directory: future edits there would immediately affect the discovered source.

The baseline owns agreed durable intent, rationale, domain meaning, and interface direction, including decisions confined to a feature. It distinguishes assumptions and proposals from agreement, current implementation from agreed future direction, and unexplained divergence from deliberate change. It reuses existing document layouts, gives each decision one authoritative home, keeps delivery state in work records, makes ADRs optional, replaces superseded guidance, and routes agents to task-relevant current sections. Four templates are explicitly possible homes, not a required set. A no-edit outcome is allowed.

The strongest case for retaining the baseline is substantial: the desired anti-bloat mechanisms are already present, and no demonstrated failure demands more rules. Prior synthetic probes found competent context maintenance with both old and revised guidance; they do not establish unique benefit, reliable automatic discovery, or cross-project performance. See [prior context-continuity research](plan-work-reference-sheet.md) and [writing research](writing-for-agents-reference-sheet.md).

Potential gaps are textual hypotheses: named templates may anchor agents on creating files instead of extending existing docs; discovery explicitly names AGENTS.md but does not address a colleague arriving through README; contributor practices have no explicit role; an absolute reading of “cannot be reliably recovered from code alone” might omit a useful high-level map or consequential contract. The last concern is partly addressed already by the skill's allowance for contracts and constraints and by writing-for-agents. None is an observed incident.

## Source comparisons

Primary material inspected on the research date. Repository main revisions observed through GitHub's API: Google design.md `9bf8eae67128b6cc55ad9bf86665767deb4c11cd`; Google stitch-skills `0337446dadde6f8c94210444e2aa9d546126480f`; Matt Pocock skills `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`; Vercel AI `5d12eaa6caa193d3901cbab98a734403eb6bf622`. Documentation sites are moving sources; research papers below identify inspected versions.

| Source and evidence type | Mechanism and useful adaptation | Limit or reason not to import wholesale |
| --- | --- | --- |
| [GitHub README guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes). Product documentation. | README provides an entry point for purpose, use, getting started, help, and contribution links. Existing README sections can own small amounts of product context. | README need not become a full architecture or decision archive. A second PROJECT.md is useful only if deeper intent warrants separate reading. |
| [GitHub contributor guidelines](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors). Product behavior and recommendations. | GitHub surfaces CONTRIBUTING at issue/PR creation, the contribute page, repository overview, and sidebar. It can own the practical route to a contribution and link to deeper rationale. | The affordance helps discovery; it does not prove improved onboarding or require a substantial guide for occasional colleagues. A short README section can suffice. Do not invent governance, approval policies, or community machinery. |
| [Diátaxis](https://diataxis.fr/start-here/). Professional method. | Separates task-oriented how-to guidance from explanation and reference. Contributor workflow and architectural rationale answer different questions even when held in one small file. | Borrow reader-purpose distinctions, not four compulsory documentation trees or strict categorization of every paragraph. |
| [arc42 architecture decisions](https://docs.arc42.org/section-9/). Professional method. | Preserve significant decisions and rationale and avoid duplicating decisions already explained elsewhere. | No need to adopt the full architecture template. Existing evergreen guidance plus selective ADRs already serves this role. |
| [Matklad, ARCHITECTURE.md](https://matklad.github.io/2021/02/06/ARCHITECTURE.md.html), 2021-02-06. Maintainer experience and recommendation. | A stable, coarse map of important responsibilities and relationships can help contributors find where to work. This challenges an overly literal ban on information recoverable from code. | Its numerical effort comparisons are practitioner estimates, not controlled measurements. Avoid an exhaustive file tree; use ENGINEERING or an existing architecture page when a conceptual map materially helps. No extra ARCHITECTURE file is necessary by default. |
| [Pocock domain-modeling skill](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/domain-modeling/SKILL.md). Actual prescribed workflow. | Creates glossary and ADR files only when content exists, checks terminology against code, and applies a threshold to ADR creation. | Its glossary-only CONTEXT.md and three-part ADR threshold have narrower ownership than this skill. Importing them mechanically would lose useful evergreen rationale or rename established homes. |
| [Pocock owner account](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/docs/engineering/domain-modeling.md). Owner-reported friction. | Reports missed automatic invocation, glossary growth into a running spec, and historical decisions being missed outside the searched sources. Supports explicit purpose and source-aware retrieval. | These are reports about another skill, not measured failures of Marián's skill. Do not add a universal history search or compulsory invocation chain. |
| [Vercel ADR skill](https://github.com/vercel/ai/blob/5d12eaa6caa193d3901cbab98a734403eb6bf622/skills/adr-skill/SKILL.md). Actual contrasting workflow. | Makes constraints and decisions actionable and self-contained for implementation, includes discovery of existing conventions. | It treats ADRs as executable specifications with implementation plans, affected files, tests, and follow-up tasks. That intentionally combines responsibilities Marián previously separated. Do not import this heavier process into project-context. |
| [Google DESIGN.md specification](https://github.com/google-labs-code/design.md/blob/9bf8eae67128b6cc55ad9bf86665767deb4c11cd/docs/spec.md) and [README](https://github.com/google-labs-code/design.md/blob/9bf8eae67128b6cc55ad9bf86665767deb4c11cd/README.md). Format and tooling prescriptions. | Defines optional YAML tokens plus prose sections, including overview, color, typography, layout, elevation, shapes, components, and do/don't guidance. Provides a route to design interchange and tooling. | Format is alpha. Sections may be omitted; tokens are optional. Adoption does not inherently require duplicating tokens. If embedded tokens are adopted, the spec treats them as normative values, so ownership and synchronization must be intentional. |
| [Google design philosophy](https://github.com/google-labs-code/design.md/blob/9bf8eae67128b6cc55ad9bf86665767deb4c11cd/PHILOSOPHY.md). Design rationale and prescriptions. | Specific references, purpose, and meaningful constraints communicate more design intent than generic adjectives. This is useful for the existing DESIGN template. | Its emphasis on tokens as contextual rather than rendering requirements differs from the formal spec's normative-value language. Do not infer that prose can silently overrule a project's token source. Claims about generated quality are not a comparative evaluation of our template. |
| [Google Stitch design-md skill](https://github.com/google-labs-code/stitch-skills/blob/0337446dadde6f8c94210444e2aa9d546126480f/plugins/stitch-utilities/skills/design-md/SKILL.md). Concrete workflow example. | Retrieves designed screens and assets to produce semantic design guidance for further Stitch generation. | Requires a particular tool/workflow and extracts from observed UI. Observation alone does not establish agreed future design intent. Its existence does not make that extraction process part of this general context skill. |

Google's [responsive-token request #154](https://github.com/google-labs-code/design.md/issues/154) is evidence of requested format evolution, not a demonstrated failure in Marián's projects. The Google format can be a project-specific convention without becoming a global requirement. A prose-only adaptation is possible; the decision is whether consistent headings or actual interoperability offers enough benefit. Preserve the current template's interaction intent even if visual sections are aligned.

## Empirical evidence and limits

[Treude, Gerosa, and Steinmacher, Towards the First Code Contribution](https://arxiv.org/html/2404.18677v1), v1, 2024-04-29, uses a survey of about 100 practitioners, analysis, and validation interviews to study newcomer processes and information needs. It treats newcomers as new to a project, not necessarily inexperienced developers. The work supports attention to relevant information scattered across sources and differences in reader needs. It does not compare README/CONTRIBUTING layouts or validate an exact file set. Our inference: a competent colleague needs a usable route through existing knowledge, not generic programming instruction or every recorded decision up front.

[Gloaguen et al., Evaluating AGENTS.md](https://arxiv.org/html/2602.11988v1), v1, 2026-02-12, evaluates generated and developer-provided context using several agents on Python-heavy issue tasks. Generated context marginally reduced success on average and increased cost; developer-written context produced a small average success benefit with additional cost. The paper's body is more nuanced than a blanket “context hurts” reading of the abstract. Its documentation-removal experiment supports redundancy as a relevant factor. It does not evaluate long-term intent preservation or this skill.

[Lulla et al., On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents](https://arxiv.org/html/2601.20404v1), v1, 2026-01-28, instead finds lower runtime and output tokens with existing AGENTS.md on selected small PR tasks using one agent configuration. It does not comprehensively establish output correctness; task descriptions were generated from PR diffs. This is useful counterevidence to universal claims that context is overhead. Different tasks, selection, metrics, and setups prevent direct reconciliation into one effect estimate.

Together these studies justify testing what guidance contributes, not minimizing tokens regardless of lost meaning or prescribing a fixed documentation architecture. No measured improvement for the proposed changes is claimed.

## Provisional ownership map

This is a way to reason about ownership, not a mandatory file inventory. Existing authoritative locations take precedence. One file may serve several roles through short coherent sections; a brief entry-point summary can link to detailed authority without becoming an independent copy of the rules.

| Reader's question | Usual home | Boundary |
| --- | --- | --- |
| What is this, why would I use it, and where do I begin? | README | Introduce use and route contributors to relevant guidance; retain short product intent here when sufficient. |
| How do I make, check, and submit a change here? | CONTRIBUTING or README contribution section | Project-specific setup, validation expectations, contribution conventions, and routes to context. Link to canonical scripts/configuration instead of maintaining multiple command inventories. |
| What must an agent know on entry or for this area? | AGENTS.md / existing agent routing | Essential applicable instructions and task-sensitive pointers, including shared contribution guidance. Agent-only constraints stay here; contributor rules should not be discoverable exclusively here. |
| Which product outcomes and tradeoffs should changes preserve? | PROJECT or existing product/README sections | Purpose, users, priorities, deliberate exclusions, agreed direction. Separate only when meaningful deeper content exists. |
| Why are responsibilities and constraints arranged this way? | ENGINEERING or existing architecture guidance | Technical intent, stable conceptual map when useful, contracts, boundaries, reasons. Procedures belong with contributor/runbook guidance; exact changeable details stay in implementation sources. |
| What do the domain terms and rules mean? | LANGUAGE or an existing glossary/section | Non-obvious terminology, relationships, distinctions, domain invariants. Unnecessary for projects with no meaningful domain ambiguity. |
| How should the interface look and behave as it grows? | DESIGN or existing design-system/brand guidance | Visual and interaction intent, concrete references, constraints and rationale; link canonical components/tokens. Unnecessary where there is no relevant interface. |
| Why did we make this significant decision? | Current relevant section; optional ADR for substantial history | Keep current guidance discoverable; use records for context, alternatives and consequences when worth preserving. |
| What is being proposed or delivered now? | Issue, spec, work record | Scope, tasks, temporary status, exploration. Promote only agreed lasting understanding. |
| How do I operate or recover the system, or consult an API? | Existing runbook/reference documentation | Related knowledge may need routing, but project-context should not become a universal documentation generator. |

“All non-obvious guidance” cannot be guaranteed by filling templates. The better criterion is whether a future reader has the information needed to make the relevant change, understands consequential constraints, and can find the authoritative detail. For example, external-service assumptions, compatibility commitments, data-retention reasons, and unusual test setup may all matter, but belong according to their purpose rather than in a new generic bucket.

Single ownership also does not mean that every implemented fact must disappear from docs. A compatibility guarantee or high-level responsibility boundary can matter even when code demonstrates it. Conversely, a function inventory contributes little if search reveals the same thing immediately. README or CONTRIBUTING can reasonably show a runnable command for humans even though a script implements it; the goal is an authoritative procedure without conflicting copies, not eliminating every reference to executable behavior.

## Composition with writing-for-agents and shaping

The existing composition remains coherent. Project-context decides what lasting understanding deserves preservation, its certainty, ownership, and discovery. Writing-for-agents governs economical expression of agent-focused documents, preserving contracts, rationale, and non-obvious operational facts. Its current text explicitly respects primary document purpose and human readability. Agent readership does not turn a human contributor guide into agent-only prose. Shared technical rationale can remain concise and understandable without parallel human and agent copies.

README and CONTRIBUTING normally use ordinary clear contributor-facing language. Existing agent-focused context can remain compact while linking from those entry points. If colleagues become a primary audience for a particular context document, write to that purpose rather than deriving audience solely from its filename. No adjacent skill revision is currently established as necessary.

Shaping would own resolving a genuinely open product or collaboration decision. The invoked rethink-skill already provides collaborative exploration for this reassessment, so an additional mandatory shaping phase offers no clear benefit. No orchestration chain is proposed.

## Options for discussion

1. **Keep unchanged.** Credible because optionality, single ownership, no invented intent, and selective reading already cover much of the request. Lowest instruction cost; contributor discovery remains implicit.
2. **Compact clarification, provisionally recommended.** Preserve the core and explicitly recognize README/CONTRIBUTING as existing authoritative homes and human entry points. Include durable contributor expectations when relevant, without taking over all setup/reference authoring. Treat the four subjects as optional roles, strengthen concrete design intent, and allow the project's adopted DESIGN convention. Main risk: redundant wording or scope creep. A short clarification may be sufficient; no extra templates are yet justified.
3. **Broaden into a complete documentation-system skill.** Could own README, contribution setup, architecture, user docs, runbooks, design exports, and audits. Offers an explicit onboarding mandate but creates a much broader trigger and maintenance burden. Current evidence and project scale do not justify this direction.

The consequential open boundary is whether contributor readiness is part of this skill's success condition or a neighboring concern it routes to. Provisional recommendation: it should preserve and expose durable contribution knowledge when that is the work at hand, while ordinary implementation/documentation judgment handles routine command changes. An invocation to capture one product decision should not trigger a repository-wide onboarding audit.

Marián clarified that colleagues will mostly contribute through their own coding agents. This makes portability of project knowledge the primary sharing concern. Their agents cannot be assumed to have Marián's personal skills, global instructions, or past conversations. Project-specific constraints, rationale, and contributor expectations must therefore be discoverable and intelligible in the repository's own guidance. This does not require copying all his personal preferences or mandating his models, tools, or skill installation for collaborators. CONTRIBUTING remains a useful shared workflow home, but a second human-oriented copy of the technical context is not warranted. The existing writing-for-agents scope fits the clarified audience particularly well.

## Analytical scenarios and prospective comparison

These are walkthroughs, not executed behavioral probes. They specify observable distinctions for a later baseline/candidate comparison after a direction is agreed.

| Scenario | Useful outcome | Difference worth observing |
| --- | --- | --- |
| Tiny CLI with a good README, no UI, and three agreed product constraints | Update a README section and route where needed; avoid empty context documents. | Does naming four templates cause unnecessary files? |
| Colleague arrives to add an export mode; setup guidance lives only in AGENTS.md | Human entry point reaches runnable setup, verification, and relevant compatibility rationale. | Does contributor discovery improve without copying the rationale into CONTRIBUTING? |
| Existing docs/architecture.md and CONTRIBUTING already cover ownership and workflow | Preserve those owners, update only the affected rule and relevant links. | Does the skill create ENGINEERING.md solely to match its template? |
| UI has canonical CSS tokens and a brand guide; user agrees a density principle | Capture the principle and reason in the established home, retain tokens in their owner. | Does Google-style adoption create conflicting values or mistake existing UI for agreed intent? |
| Reversible refactor leaves intent and contributor workflow unchanged | No context change. | Does broader contributor scope provoke unrelated audits or documentation churn? |
| Code violates documented intent and a ticket suggests a possible future redesign | Investigate divergence; preserve the proposal as unsettled; update current intent only with evidence of a deliberate decision. | Does new onboarding/design wording weaken the baseline's strongest authority boundary? |
| Larger repo with many ADRs and area-specific guidance | Reach the current area rule and relevant decision history without traversing the archive. | Does human discoverability add useful routing rather than universal reading requirements? |
| Colleague's agent receives the repository and a brief feature request, without Marián's global guidance or skills | Discover project contribution expectations and relevant intent through repository entry points; respect them while making the change. | Does the authored documentation transfer enough understanding, or does success depend on the author's personal setup? |

A future test should use fresh matched contexts, realistic terse requests, discoverable evidence, and isolated repositories. Compare exact baseline with an agreed candidate while holding models, fixtures, and other instructions fixed. Test discovery separately from execution after loading, preserve follow-up corrections, and inspect artifacts/tool evidence. Include no-skill only if retention itself is at issue. An independent Astra/high A/B text review follows a real candidate; it would be premature to manufacture one for this research-only discussion.

The clarified audience adds a distinct downstream evaluation: have an incoming agent use the produced repository docs without project-context, writing-for-agents, or Marián's global guidance. Keep the recipient setup equivalent across baseline/candidate artifacts and disclose common harness instructions. This tests whether the outputs carry useful project knowledge, separately from whether the authoring agent knows how to maintain it. A dependency on privately installed skills should not be mistaken for successful sharing.

## Independent input and initial disposition

Fresh-context delegates: GPT-6 Luna/high investigated Google's format; GPT-6 Sol/medium researched contributor documentation; GPT-6 Sol/medium assessed the baseline and adjacent ownership. All were read-only and returned source references or local evidence. The parent inspected consequential source passages and retained uncertainty rather than treating reviewer agreement as validation. In particular, the formal Google spec explicitly makes YAML optional; token duplication is a conditional adoption risk, not a necessary consequence of compatibility.

Only this research sheet was added. No skill/template/global configuration changes, commit, push, or installation. No new behavioral tests were run: there is no agreed candidate yet. The next conversation should settle the narrow ownership boundary and whether DESIGN interoperability is an actual goal. Existing successful behavior remains the regression baseline.

## Preserved baseline hashes

At research start, all five files exactly matched the preserved Git revision above. These hashes identify that baseline, not the later revision.

| File | SHA-256 |
| --- | --- |
| `DESIGN.template.md` | `c5181fdc67d8eb5a754a5ea665eb1f03c23a4f3e0beaa41e431205a6053c5acc` |
| `ENGINEERING.template.md` | `d5239abc19eb9054c8de46ce892912f9ba40a2c9f636cbbf65bf8438c63c454f` |
| `LANGUAGE.template.md` | `9911f0ccb4ab38d2f67fb59423155ee751968123ee3ea20ae4d5bfe9f1483431` |
| `PROJECT.template.md` | `d6af2ebe0b734c27828bac206644ee8217b9d8e538d79a86fbc63aa491815d39` |
| `SKILL.md` | `7ef6bbdc86c875a32876b0979246932c4793d430dcd09d7c88dcfab75cd4b544` |

## Agreed direction and applied revision

Marián accepted the recommended boundary: “That does capture what I want. Evergreen docs holding intent and reasoning.” This authorizes the compact revision within project-context. Contributor readiness is supported through durable knowledge and appropriate entry points; the skill does not become a general documentation or onboarding audit.

The revision preserves all existing agreement/inference, current/future, authority, history, and optional-document boundaries. It explicitly recognizes README, CONTRIBUTING, and AGENTS roles while continuing to prefer the project's established layout. It includes contributors and their agents, asks that guidance stand without private conversations or personal skills, and clarifies the value of consequential implemented contracts and stable responsibility maps. It still avoids retelling implementation. No README or CONTRIBUTING template or mandatory file was added.

The ENGINEERING template now allows a concise explanation of how major responsibilities relate when that helps locate or assess a change. The DESIGN template asks for concrete references with reasons and useful examples or counterexamples, and respects an established design-document convention. Interaction intent and canonical token ownership remain intact. Google-specific schema, tooling, and dependencies were not adopted. PROJECT and LANGUAGE templates, writing-for-agents, and personal/global guidance were not changed.

The baseline skill contains 445 whitespace-separated words including metadata. The initial reviewed candidate contains 515; the final revision contains 525. The added content clarifies ownership and a consequential maintenance exception rather than prescribing a new process. Final SKILL.md SHA-256: `2daddc9e1525e88face0d77e31a187e4b3ec9a88852b6e84ba0c155e841eebb3`.

## Executed comparisons

Artifacts are under `/var/folders/hy/_hkw66sd5vz1qcq86zd2mg8r0000gn/T/project-context-rethink-6b897ln3`. They include baseline and candidate packages, neutral review packages, fixture repositories, initial author outputs, recipient implementations, parent checks, and results. A is the candidate; B is the baseline. These are isolated synthetic exercises, not real-world reliability estimates.

Four fresh GPT-6 Sol/medium author agents received two paired fixture tasks. They were explicitly assigned the corresponding project-context package plus identical writing-for-agents guidance; this tests execution after loading, not discovery. Original files, task prompts, model settings, and isolation instructions were equivalent within each pair. Only the project-context package differed. Agents were not given the research, a preferred output, or the evaluation rubric. All reported opening both assigned skill bodies; read reports are agent self-reports, not independent tool telemetry. Filesystem isolation was instructed rather than sandbox-enforced, and the host's common system/developer harness remained present.

| Exercise | Candidate A | Baseline B | Interpretation |
| --- | --- | --- | --- |
| “Capture the decisions in work/format-discussion.md in the project guidance.” Existing README, CONTRIBUTING, AGENTS, and docs/architecture.md; implemented CSV and agreed future JSON transfer behavior. | Updated architecture rationale, contributor fixture expectations, and AGENTS pointers. Preserved archive inclusion, collection order, IDs, integer cents, local-only export, and the future/current distinction. | Same appropriate owners and substantive preservation. | Neither created ENGINEERING or other unnecessary documents. No unique improvement observed. |
| “Capture the agreed interface direction from notes/interface-direction.md.” Static dispatch prototype with CSS tokens and settled visual/interaction direction. | Created concise DESIGN, linked from AGENTS and README; kept exact tokens in CSS and mobile cards undecided. | Created substantively equivalent DESIGN, linked from AGENTS; kept tokens and uncertainty correctly. | A added a human entry point. Both captured concrete intent and retained unimplemented interaction expectations. Neither reported opening the template, so this does not isolate the template edits' effect. |
| Follow-up to each UI author: reversibility ends when leaving the draft, not when confirming a visit. | Corrected DESIGN and source discussion note. | Corrected DESIGN. | Both authoritative guides reflect the correction; neither changed application code. Updating the old discussion note is a maintenance choice, not a material quality difference here. |

The parent inspected all initial diffs and new files. Both versions kept implementation and token files unchanged while authoring context. Neither promoted compressed exports or mobile cards into settled requirements. Successful equivalence supports retaining the baseline's mechanisms; it does not prove that the extra wording improves behavior reliably.

### Incoming-agent handoff

Two additional fresh Sol/medium agents received only copies of the authored repository docs and existing code, with source discussion notes omitted and no assigned authoring skills or personal guidance. Both received only the feature request “Add JSON export” plus identical isolation restrictions. They were instructed not to load installed skills or files outside their repository. The common host harness could not be removed, so this approximates rather than reproduces an arbitrary colleague's environment.

Both reported reading AGENTS, README, CONTRIBUTING, and architecture guidance. Both produced the same implementation, preserving archived records, IDs, original ordering, integer amounts, and Unicode text, with no remote operation. Both added an active/archived test fixture and updated README. Their two-test suites passed. Six additional parent checks passed for each: empty collection, archived/active retention, IDs/order/Unicode, integer cents, unchanged input, and unchanged CSV report behavior. This demonstrates usable transfer of the relevant intent in these fixtures, without showing a unique advantage for the revised skill.

Both incoming agents left architecture prose describing JSON as a future/unimplemented feature. This is an observed maintenance inconsistency, not a discovery failure or an A/B differentiator. Neither recipient had loaded project-context, so it cannot establish that either skill caused the omission or that editing the authoring skill would ensure maintenance by every future agent.

## Independent review and targeted correction

A fresh GPT-6 Astra/high agent compared packages A and B with equivalent formatting, no parent conversation or research, no newer/older labels, and no preferred verdict. It read all templates and the adjacent writing skill. It preferred A with moderate textual confidence for contributor discovery, portability, explicit implemented-contract allowance, and clearer document ownership. It found the extra guidance proportionate, the templates still optional, and no consequential loss. Possible rigid interpretation of conventional filenames was assessed as speculative because existing layout takes precedence. This review is separate from behavioral evidence.

A bounded follow-up asked that reviewer to assess the incoming agents' stale implementation status. It found an ambiguity shared by both versions: “implementation consistent with existing intent needs no context update” can conflict with the instruction to distinguish planned from implemented behavior. Completing an agreed feature changes the latter without changing intent. The final revision narrows the sentence: unchanged intent needs no intent rewrite, while affected planned/implemented distinctions should be refreshed. This is a textually justified clarification, not a claim to have fixed downstream maintenance without the skill. No universal maintenance boilerplate was added to generated docs.

A completion follow-up used the original author contexts, their respective captured guidance, and the incoming implementations. Both reopened their assigned skill; A received the final clarification while B retained the original. The request was “Finish the JSON export work.” This is a paired continuation with prior generated artifacts, not a new independently randomized comparison or a clean estimate of the added sentence's effect. Results and final validation follow below.

Both completion agents refreshed the architecture's implemented status, preserved transfer intent and the separate future re-import task, left the colleague's implementation/tests/README unchanged, and passed the existing tests and diff whitespace check. The final clarification was therefore exercised successfully, but the baseline also succeeded: no behavioral superiority is established for that sentence. The initial candidate and final candidate snapshots remain separate.

## Final validation and disposition

Applied skill-creator, writing-for-agents, and check-work to the authorized revision. Structural validation passed using `uv run --with pyyaml python /Users/marian/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/project-context`. Template links and the runtime symlink resolve; diff whitespace checks passed. The parent inspected author artifacts, both corrections, recipient code, independent checks, and completion updates. Unchanged templates and adjacent repository/personal guidance match Git HEAD. Only SKILL.md, DESIGN.template.md, ENGINEERING.template.md, and this research sheet changed in the real repository.

The agreed revision is complete. Existing symlinking makes the canonical skill revision available without a separate installation. No commit, push, runtime configuration synchronization, or other-model changes were performed. No unresolved material review finding remains.

Remaining uncertainty: automatic discovery was not tested; these small, orderly fixtures do not establish broad performance gains or behavior in a large/messy project. Both baseline and candidate produced largely equivalent useful outcomes. Incoming agents without the authoring skill successfully consumed the knowledge but left an implementation-status inconsistency. That gap is recorded for real-use observation rather than expanded into a mandatory maintenance process. The retained revision is justified by clearer agreed ownership and portability, supported by independent text assessment, without claiming measured superiority.

## Real-use evidence and model-neutral rewrite (2026-09-29)

Part of the cross-model pass (see [stack sheet](skill-stack-reference-sheet.md)). Marián felt the September revision still left room for improvement without naming a specific failure. This pass replaced textual hypotheses with evidence from real sessions and from the docs the skill produced.

### Evidence from real sessions

Fresh-context extraction (Opus 5.5) over every non-authoring session that loaded the skill: 9 Codex sessions (content-foundry, hogwarts-battle-redux, byt, a scratch directory) and 2 Claude Code sessions (hogwarts). None ran the September text; all predate `397ea14`/`bb685ea`, so this is evidence about the job, not the current wording.

- **The job in practice is "make the repo remember this."** Most hogwarts uses wrote agent workflow rules (PR and merge flow, running `gh` outside the sandbox, review etiquette) into README and AGENTS.md, often triggered by the user's dissatisfaction with agent behavior. The skill's stated scope (intent, rationale, language, design) did not cover this.
- **Agent-written rules overshot the user's intent and cost real work later.** A "Verify meaningful visual changes in the rendered app" rule in DESIGN.md drove expensive browser QA in later sessions; the user then said "I honestly don't need visual verification of changes at all". A written squash-merge rule contradicted what the user expected.
- **Ideals written as current fact.** A reviewer found ENGINEERING.md "overstates projection ownership and privacy"; the fix wrote implementation limits into the doc. Late additions in content-foundry drifted into slice status ("in this slice", "not part of this milestone").
- **Ceremony.** Agents proposed exact wording and waited; one ran a full PR cycle for a 3-line AGENTS.md note. User: "You can apply edits directly, we will review the diff after."
- **Placement flip-flop.** A Claude-only variant put design context in `.claude/rules/`; a Codex session removed it three days later as hidden from other agents. Resolved since by the shared skill set.
- Reactions to explicit uses were mostly approval (`LGTM`, `Agreed. Let's plan that out.`); complaints concerned delivery time and process, not doc content.

### Evidence from the docs themselves

Fresh-context audit (Opus 5.5 with four helpers) of seven repositories, about 90 claims checked against code: hogwarts-battle-redux (4/5 usefulness), b-hub (3), iphone-checker (3), power-automate-extended (3), smartfox (3, no code), iphone-viewer (2), helm (1, no code).

- **Intent survives; current-state claims rot.** No PROJECT.md was found wrong. Stale items are status, counts, and "what exists": "It is not installed yet" (it is), "bumped the schema to version 9" (code at 11), README and AGENTS.md disagreeing about what is built.
- **Plans written as built.** An ADR describes an unimplemented health check; LANGUAGE.md defines terms from a doc titled "(Proposed)"; DESIGN.md forbids ambient blobs that every page renders.
- **Copied values wrong from day one.** iphone-viewer DESIGN.md token frontmatter (radii, light-theme colors).
- **Restatement.** "Deleted = sold" six times across PROJECT, ENGINEERING, LANGUAGE in one repo; one b-hub rule about eight times across five ADRs. Safe only where restatements point to an owner (hogwarts). Splitting by lens (product/engineering/language) invites restating one rule in each.
- **Bulk passes go stale; docs shipped with the code stay current.** power-automate-extended and the iPhone repos were written in one pass and not touched again; hogwarts glossary edits ship with type changes and stay accurate.
- **Layout churn.** Four generations of doc layout across the repos, each a bulk migration; declared structure rules ("glossary and nothing else") were not kept.
- **Gaps.** Decisions made in PRs and closed issues never reached docs (hogwarts #126). Couplings and recurring changes were missing: adding an iPhone model (three times) touches two repos and a database select, recorded only in a code comment. The area under active work is least covered.
- **Leaks.** `ssh root@<ip>`, "cannot be fully inspected in Codex", a model name in AGENTS.md.

### Decisions

Agreed with Marián on 2026-09-29:

1. Rebuild the body around four two-sided tensions: lasting versus perishable, strength as agreed (over- and under-stating), one reachable home (scattered versus orphaned), and updating with the change (bulk passes versus missed decisions from PRs and issues).
2. Scope explicitly includes standing instructions for contributors and their agents, since that is how the skill is used; the strength rule matters most there.
3. Drop the four templates, but keep the file naming convention (`README.md`, `AGENTS.md`, `PROJECT.md`, `ENGINEERING.md`, `LANGUAGE.md`, `DESIGN.md`) as the default where a project has no layout, each file created only when it has content. Marián wants every project to share one shape so he can verify it at a glance, and named homes prevent single catch-all files. Duplication comes from files restating a rule for their own reader (iphone-checker), not from the names (hogwarts uses them and points instead), so the skill gives each file one kind of statement and has the others link.
4. No `docs/adr/` in the convention; it came from Matt Pocock's skills. Its core moves into the owning docs: a consequential decision carries its reason and, where someone would plausibly propose it again, the rejected alternative and why. A changed decision is rewritten where it lives, with version control as history, rather than appended as amendments chained across records (the b-hub failure) or left stale (the hogwarts failure). Projects that already keep decision records mark superseded ones and link replacements.
5. Do not adopt Matt Pocock's skills or conventions. Staying layout-neutral ("follow the existing layout") is enough to work in repos that use them, such as b-hub.
6. When touching an area, check nearby claims against the code; fix plain drift, flag unexplained divergence. Area only, not a repo-wide audit.
7. Make small edits directly and report them; keep personal, machine, and tool/model details out of shared docs.

Baseline: repository `490adf5`; SKILL.md SHA-256 `2daddc9e1525e88face0d77e31a187e4b3ec9a88852b6e84ba0c155e841eebb3` plus the four templates (removed in this revision).

### Tests

Fixtures (six small git repositories, under `/tmp/pc-probe`, not preserved) were built from the evidence above: a decision stated in passing during a code task that makes a glossary entry wrong (`motto-boundary`); a recurring change across three places (`model-coupling`); a complaint about agent behavior that conflicts with an existing DESIGN.md rule, then a refinement (`browser-check-rule`); a planned feature to implement, with a planted doc/code sort-order mismatch in the same area (`json-export`); a typo fix where the skill should not fire (`typo-fix`); and a new project described over three turns with a hedge, an "I don't know", and a late hard constraint (`new-project`). The first `motto-boundary` fixture used real licensed quotes as "our own" mottos, and Opus correctly refused; the fixture was replaced with original lines and the baseline rerun.

Each scenario ran through normal discovery on Opus 5.5 (`claude -p`) and GPT-6 Astra at medium effort (`codex exec`), baseline first, then the candidate. Judged transcripts included each repository's diff from the initial commit. Opus 5.5 and GPT-6 Astra at high effort judged every pair blind with randomized labels and a rubric built from the decisions.

Skill loading: Codex loaded project-context in 4 of 6 scenarios on the baseline and 5 of 6 on the candidate (`browser-check-rule` added); neither loaded it for `typo-fix`. Opus loaded it only for `new-project` in both conditions and handled the in-task cases competently without it, so its other pairs compare run-to-run variance, not the skill.

Verdicts over 24 judgments: candidate 9, baseline 8, tie 7. The judges agreed on direction in 9 of 12 pairs.

| Scenario | Opus runs | Astra runs | Note |
| --- | --- | --- | --- |
| new-project | candidate (both judges) | candidate (both judges) | Baseline Opus created PROJECT, AGENTS, and CLAUDE.md with repetition and a status line; baseline Astra wrote the owner's name, "there is no app implementation yet", and "not verified yet". Candidates used README plus a thin AGENTS.md. |
| browser-check-rule | baseline (both) | candidate (both) | All four runs edited the existing rule in place at the stated scope. Differences were small added clauses judged as over- or under-stating. The skill loaded only in the Astra candidate. |
| model-coupling | candidate (both) | baseline (both) | All four recorded the three-place coupling in ENGINEERING.md without dated history and declined a separate doc. The Astra baseline also added a pointer comment beside the model list. |
| motto-boundary | baseline (both) | baseline / tie | All runs fixed the glossary entry that caused the flip-flop. Differences were placement of one sentence. |
| json-export | split | tie | All runs turned "planned" into current intent. Opus flagged the sort mismatch in both conditions; Astra changed existing CSV ordering to match the doc in both. |
| typo-fix | tie | tie | No doc changes. |

Reading: the baseline was already competent on small fixtures, as in September. The clear gain is on new-project, where the template list and missing perishable/personal guidance showed; that is the scenario closest to how docs bloat in real repositories. The losses are small wording differences on pairs where the skill loaded in only one condition or in neither.

Two fixes followed and were rerun on Astra (`json-export`, `new-project`). "Your own standing instructions" was added to the leak list after a candidate Astra run copied a personal-guidance line ("Track requested implementation work in GitHub Issues") into README; the rerun did not. The divergence line changed from "rather than rewriting intent to match the code" to "rather than changing either side to match the other"; the rerun still changed CSV ordering to match the doc, disclosed in its report. This matches the scope expansion Astra showed in check-work probes and is left to global guidance rather than chased here.

Final SKILL.md: 485 words (baseline 525 plus four templates), SHA-256 `e347d12b905b74179c31c202d92a5b54803065cf806d7fb77a3a26882f1cb669`.

What these tests cannot show: whether agents notice lasting decisions over a long session, capture decisions made in PRs and issues, or keep docs current across many changes; whether the strength rule prevents overreaching workflow rules in practice; and whether dropping templates changes layouts in real new projects. Opus rarely self-loads the skill for in-task decisions in these fixtures; watch whether that holds in real use and whether missing decisions follow.

Follow-up after review: the first candidate named no files, and Marián asked to keep the naming convention. The one-line role list became the named default above. Rerun of `new-project` on both harnesses: both produced a short README linking onward, a routing AGENTS.md, and PROJECT.md owning intent and open questions, with no empty ENGINEERING, LANGUAGE, or DESIGN files. The Opus run noted that ENGINEERING.md would be created when the first technical choice is settled. Remaining restatement was a one-line summary of the defining requirement in AGENTS.md. The Astra PROJECT.md carried verification steps and a "not a verified result" note, which is mildly perishable. Not re-judged blind.

Second follow-up: `docs/adr/` dropped from the convention and its core distilled into the skill (decision 4). Rerun of `motto-boundary` on both harnesses: both moved the mottos, corrected the glossary entry that caused the original move, and recorded the reason ("our own jokes, not licensed game content"), which also works as the rejected-alternative note. Astra loaded the skill and put the rule in ENGINEERING.md beside the glossary fix. Opus did not load it and spread one idea across the glossary, ENGINEERING.md, and a code comment. Not re-judged blind.

Final SKILL.md: 563 words, SHA-256 `bb60c083cb342569f0a3c23bb241fd0c589def98f487d32720c09e2d36b059f9`.


Follow-up 2026-09-30: `writing-for-agents` was retired and its surviving guidance folded in as the "Written for the reader" paragraph; the description now names AGENTS.md and project skills. Evidence and tests are in the [writing-for-agents sheet](writing-for-agents-reference-sheet.md#cross-model-pass-retired-2026-09-30).
