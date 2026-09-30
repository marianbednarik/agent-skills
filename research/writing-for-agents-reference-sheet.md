# Writing-for-agents reference sheet

**Status: retired 2026-09-30; its surviving guidance lives in `project-context`. See [Cross-model pass: retired](#cross-model-pass-retired-2026-09-30).**

Research date: 2026-09-27. Scope: reassess and refine the existing documentation-writing skill. External instructions are research material, not adopted authority.

## Agreed purpose and scope

Marián reports a recurring authoring problem: agents produce unnecessarily prose-heavy documentation and restate information readily recovered from code. His initial report of no issues concerned the existing skill, not the absence of that underlying problem. This is owner-reported experience; no real-use trace was supplied to establish when the skill was loaded or whether it failed.

Keep the skill, centered on selective content and economical expression. Each passage should contribute useful understanding. Omit general tutorials, obvious implementation walkthroughs, redundant file inventories, repeated summaries, and copied changeable details. Preserve intent, rationale, ownership, consequential constraints, contracts, exceptions, domain meaning, and non-obvious operational facts. Code implementing a contract does not remove the value of stating its significance for future changes. Useful navigation pointers still earn their place.

The primary scope is creating or revising agent-focused documentation: skills, AGENTS.md, specs, and project context. Primary purpose and established role determine style, rather than exclusive readership. Agent-focused project context can be compact and technically dense while remaining understandable to Marián. Ordinary communication with him, PR descriptions, and commit messages retain clear human-facing prose.

Marián explicitly asked to leave subagent briefs out, trusting the agent's general capabilities. Remove briefs, handoffs, task-brief examples, and recipient-specific briefing guidance from this skill. This is a scope decision, not an empirical claim about what reinforcement learning guarantees. Do not add a negative briefing policy to the runtime instructions.

## Ownership and composition

`project-context` decides what durable understanding to preserve, whether it is agreed, and its authoritative home. `writing-for-agents` guides how selectively and economically agent-focused documentation expresses that understanding. Both preserve rationale, distinctions, and uncertainty; neither requires parallel human and agent copies.

Both can apply to PROJECT.md, ENGINEERING.md, LANGUAGE.md, DESIGN.md, and agent-focused decision records. For AGENTS.md, the writing skill applies to authoring its instructions; project-context also applies when preserving lasting understanding or routing to its authoritative location. Routine operational instructions do not automatically need project-context. A refactor consistent with existing intent may need no context update. An unexplained code/intent discrepancy requires investigation before rewriting intent. Specs and work records retain their own purpose; concise writing does not promote task status or undecided proposals into durable guidance.

`skill-creator` owns packaging and structural validation. This writing skill does not decide to delegate, expand authorization, create extra documents, or impose a documentation architecture. No other skill or global guidance was modified.

## Baseline and applied revision

Canonical file: `skills/writing-for-agents/SKILL.md`. Original repository HEAD: `63bc44f9cc6145f4932513abff3c160caba94101`; original skill's last commit: `637be57`. Original file SHA-256: `d04fcb4021587fb62b33e25c6d4b4d72a873b19573953b70aec1b785a58d3170`. Exact original is preserved below.

The original was 355 whitespace-separated words including metadata. It already preserved decision-relevant information, respected document purpose, supported selective reading and references, and excluded human-facing communications. Earlier revisions in this review overemphasized audience classification and expanded into briefs and handoffs. A blanket “shared writing” exclusion was misleading for primarily agent-facing project context that Marián also reads. Those intermediate decisions are superseded by the agreed purpose above.

The final revision centers the content-selection test, retains contracts even when implemented in code, assumes technical competence without assuming local knowledge, and preserves the original's useful structure and source-of-truth principles. It contains 344 whitespace-separated words. SHA-256: `b3785e2f8963f5cd5bfd470b39e6762fab3c28b65a2f26a0bd497fa2ada40462`.

The runtime directory `~/.agents/skills/writing-for-agents` symlinks to the canonical directory, so the edit changes the live source without a separate installation. Implicit selection remains at its default; no openai.yaml was needed. No commit, push, or other model variant synchronization was requested.

## Source comparisons

Sources inspected directly on 2026-09-27. Upstream Matt Pocock repository main revision observed through GitHub API: `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`; latest commit touching the skill: `321658273cb1d20b76026717d027d505790106d4` (2026-08-19). Moving documentation below reflects the inspection date.

| Source and evidence type | Useful mechanism | Adaptation and limits |
| --- | --- | --- |
| [Matt Pocock skill](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/productivity/writing-for-agents/SKILL.md). Authored prescriptions. | Task-sensitive pointers, nearby rules and caveats, conditional references, completion criteria, pruning repeated or discoverable information. | Most already present. Preserve these without importing its taxonomy, aggressive use of compressed “leading words,” or broad rule covering anything an agent reads. Those mechanisms are not comparative evidence of reliable improvement. |
| [Pocock owner overview](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/docs/productivity/writing-for-agents.md). Owner rationale and reported friction. | Warns that requests to streamline can remove useful behavior; recommends judging deleted information by its effect. Describes broader use in specs, tickets, runtime prompts. | Supports preserving meaning over length. Its own discovery is narrower than manual use. It says there is no automated evaluation, so the explanation does not establish causal results. Its broad audience boundary conflicts with Marián's clarified default. |
| [Anthropic context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), 2025-09-29. Provider guidance and engineering experience. | Use enough specific information to guide behavior without brittle scripts; minimize irrelevant context, retain essential detail, retrieve conditional material when needed. | Reinforces the existing density principle. Compact does not mean shortest. General model knowledge does not imply shared local context. Does not validate any exact wording or compression target here. |
| [LongLLMLingua](https://aclanthology.org/2024.acl-long.91/), ACL 2024. Primary empirical research; abstract inspected. | Query-aware prompt compression can reduce tokens while improving performance on evaluated long-context tasks. | Evidence that information selection matters, not that manually telegraphic specs work better. Different algorithms, models, and tasks; no transfer of benchmark gains to this skill. Do not adopt a numerical compression target or imply a measured efficiency improvement. |
| [Michael Nygard: Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions), 2011-11-15. Professional method plus early author experience report. | Preserve decision context, status, consequences, and reasons so later readers can judge changes. | Supports the strongest case for readable shared docs and the baseline's preservation of rationale. Borrow the distinction between accepted and proposed intent; leave ADR format, mandatory files, and human prose requirements to document purpose. |
| [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills). Product documentation. | Names/descriptions precede body loading; implicit selection matches descriptions; implicit invocation defaults to enabled. | The local skill has no explicit-only policy. Improve scope in metadata; do not add redundant configuration. Automatic selection is available, not guaranteed on every relevant task. |
| [OpenAI: Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra), 2026-09-11. Provider recommendations. | Keep discovery discriminating; avoid overbroad descriptions and unnecessary procedural scaffolding. | Supports a small revision and no additional runtime files. Does not establish that removing this personal preference skill would preserve its behavior. |

## Alternatives and decisions

- **Keep the original:** credible because no loaded-skill failure was observed and its core already fits. The revised content filter makes the reported problem more explicit and fixes the audience ambiguity explored in discussion.
- **Remove the skill and rely on standing guidance plus project-context/skill-creator:** credible given overlap, and included in the final behavioral comparison. The synthetic result does not demonstrate a unique skill benefit. Marián nevertheless chose to retain a targeted reminder against a recurring authoring problem across documentation types.
- **Move all guidance into global instructions:** not pursued; the user prefers normal clear prose globally with a focused skill for agent documentation.
- **Broaden to all text an agent consumes or prescribe subagent brief structure:** rejected by the agreed scope. Agent readership alone does not change a human-facing artifact's purpose.
- **Aggressively minimize length or require a special syntax:** rejected. Accurate decision support, useful navigation, explicit contracts, and necessary rationale outweigh cosmetic brevity.

## Behavioral evidence

These are small synthetic probes, not reliable estimates of discovery, efficiency, or real-world performance. All test agents were fresh GPT-6 Sol instances at medium reasoning, without conversation history or preferred outputs. The surrounding host developer context remains common to every condition; these are not standalone model evaluations. Filesystem isolation was instructed, not sandbox-enforced. The parent inspected generated artifacts. Reports of skill reads are agent self-reports, not independent read telemetry.

### Earlier audience-focused probes

Fixtures remain under `/tmp/writing-for-agents-review-20260927/`. A baseline/early-candidate pair produced fresh-agent briefs from identical partial-import notes. Both preserved constraints, local terminology, and undecided retries. A second baseline/intermediate-candidate pair produced a shared design note for a colleague, an agent handoff, and a PR draft from identical CSV-export notes. Both preserved semantics, scope, and validation limits while keeping human-facing outputs readable. Agents chose whether to read the exposed skill; all reported doing so.

Neither pair established an improvement. The shared design fixture was explicitly colleague-facing; it did not resolve how primarily agent-focused project context should read. Briefing tasks are now outside the selected scope and do not validate the final revision.

### Documentation-content comparison: original / revised / no writing skill

Fixture root: `/var/folders/hy/_hkw66sd5vz1qcq86zd2mg8r0000gn/T/writing-docs-review-5aotsvf6/`. Conditions: X = original writing skill; Y = revised candidate before three small review clarifications; Z = no writing skill. Each received the same `project-context` skill, standing preference for compact agent documentation, and task: update AGENTS.md and ENGINEERING.md for the importer and decisions in notes.md. Skill bodies were explicitly assigned for execution; this does not test automatic discovery. The only guidance difference was the writing skill condition.

Each fixture contained a short Python importer, prose-heavy existing guidance, and meeting notes. Existing docs explained basic Python, listed functions and fields, copied a changeable batch-size value, and described stale all-or-nothing behavior. Notes specified partial success and its user rationale, original zero-based error indexes as a compatibility contract, all-invalid results, oversized-batch rejection before writes and its reason, offline/local persistence semantics, a deferred duplicate-ID proposal, and temporary review status. Exact limits and required fields remained inspectable in code.

Parent inspection of all six edited files found:

- All three conditions removed generic explanations, obvious function walkthroughs, stale behavior, and copied batch-size/required-field values.
- All preserved partial-success rationale, successful input order, original error indexing, all-invalid semantics, upfront size rejection, and offline/local persistence meaning.
- All added useful task-sensitive pointers in AGENTS.md and kept temporary review status out of durable context.
- X and Y noted that duplicate-ID behavior remains undecided and linked its work record; Z omitted that proposal. None promoted it to an agreed feature.
- All produced understandable compact documentation and ordinary human-facing explanations. No material regression or unique advantage of the revised skill was observed.

The no-skill condition also had project-context and the user's standing writing preference. Its success shows that those can be sufficient on this fixture; it does not establish consistent performance across all authoring tasks. Retaining the skill follows the user's recurring experience and preferred ownership, without claiming measured superiority.

## Independent assessments

An earlier fresh Astra/high comparison favored the initial candidate's audience and recipient clarifications; that review assessed an intermediate scope now superseded. A fresh Sol/medium comparison of project-context and writing-for-agents found compatible ownership and identified “shared writing” as the principal ambiguity.

For the final content-focused revision, fresh GPT-6 Astra/high reviewed the exact original and candidate labeled A/B with equivalent formatting, neutral requirements, no history, and no preferred verdict. It preferred B for its actionable content filter, contract exception, uncertainty distinctions, and human-readable agent documentation. It found no briefing prescriptions. Three recommendations were applied: retain file inventories that provide navigation value; keep instruction scope explicit; preserve established terminology. These narrow clarifications were structurally checked; the behavioral probes used the preceding candidate and were not rerun. Textual review is distinct from behavioral evidence.

## Validation and remaining uncertainty

The canonical target was checked against its pre-edit snapshot before applying the revision. Structural validation uses `uv run --with pyyaml python /Users/marian/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/writing-for-agents`; system Python lacks PyYAML, so an isolated uv environment avoids changing repository dependencies. Final skill validation and `git diff --check` passed; the runtime symlink and absence of briefing/handoff guidance were also checked. Unrelated retro work is outside scope and remains untouched.

Automatic invocation frequency and incremental benefit remain unmeasured. Future useful evidence is an ordinary documentation task where prose or recoverable implementation detail persists despite the skill, or a case where aggressive omission loses an important contract or rationale. Inspect what guidance was actually loaded before expanding the instructions. Do not turn every plausible edge case into another rule.

## Preserved baseline

```markdown
---
name: writing-for-agents
description: Write or refine documentation primarily intended for agents, including skills, agent instructions, and project-context references. Use when authoring these materials; human-facing tickets, PR descriptions, and commit messages retain Marián's human communication style.
---

Optimize for reliably understood information per token.

Write for an agent that already understands general technical concepts.
Use precise terminology, compact statements, and explicit relationships.
Omit conversational framing, generic explanations, repeated summaries,
and instructions that add nothing beyond applicable existing guidance.

Preserve information that changes decisions: intent, constraints,
ownership, rationale, exceptions, and non-obvious operational facts.
Compression should remove redundancy, not distinctions or reasons
needed to apply the guidance correctly.

Let the document's purpose govern its content. A writing style does not
expand what belongs in a document: evergreen project context still
captures durable understanding, while procedures and implementation
references serve their own purposes.

Structure for selective reading. Keep closely related rules and caveats
together. Use headings, lists, tables, or compact examples when they
make relationships easier to retrieve and apply.

Keep essential guidance at the point of use. Move substantial conditional
detail behind references that explain when to read them. Avoid splitting
short, coherent material merely to create more files.

Maintain one authoritative home for each fact or instruction. Reference
existing sources rather than copying them. Prefer inspecting code,
configuration, or tooling over documenting readily discoverable state;
record what those sources cannot explain.

For behavioral instructions, make the relevant trigger, scope, authority,
and completion conditions clear where they affect execution. Prefer
outcomes and decision criteria over a fixed sequence unless ordering
or exact steps materially affect correctness.

For descriptive context, distinguish settled intent, constraints, and
rationale. Preserve the project's established terminology and resolve
material ambiguity rather than disguising it with confident wording.

Include examples when they clarify a subtle distinction or prevent a
likely misreading. Avoid exhaustive catalogues of hypothetical cases.

When revising, remove obsolete or conflicting guidance and consolidate
duplication. Check references and preserve meaningful exceptions.
A shorter document is useful only if it remains accurate and actionable.

Apply this style to the agent-facing artifact. Explain the resulting
changes to Marián in the usual clear, human-facing language.
```

## Cross-model pass: retired (2026-09-30)

Part of the cross-model pass (see [stack sheet](skill-stack-reference-sheet.md)). Marián named no specific failure; his guess was agents including content that does not belong, such as implementation or plan details.

### Real-use evidence

Two fresh-context extractions: the Codex sessions that loaded the skill, and 18 recent sessions in both harnesses where agents wrote agent-facing docs. Claude Code evidence is thin (two sessions).

- **Loads.** Codex loaded the skill in 6 sessions (two further matches were catalog noise), none on the 2026-09-27 text; four ran the older Pocock-derived version. Claude Code never loaded it through discovery. Marián never commented on doc style after a load; the one approval ("Lgtm", smartfox AGENTS.md) was on a rewrite whose gain was content, not style.
- **Dominant failure is content selection, almost all Codex:** plan, status, and verification notes in lasting docs ("No application stack has been installed on the server by this work", "accepted in B-70 refinement on 2026-09-07"); ticket IDs as the organizing device (b-hub ADR-0007: 43 references); code restated then drifting ("Tests are never typechecked… Deliberate", later false; hook and component names in a glossary); harness mechanics in always-loaded guidance (`fork_turns`, model slugs). The worst ticket and status bloat came from sessions with neither skill loaded, several via `grill-with-docs` (already retired from the personal set; left as is).
- **Missing content:** the project's purpose and scale (smartfox "suck ass for what we want this repo to be for", helm template AGENTS.md, b-hub over-engineering because "five friends" was buried).
- **Style, both directions, fewer cases:** over-specification (tables and checklists after "I would not create a checklist", a 9-line rule for "improve this a bit"), crammed multi-clause rules (byt), hard-wrapped lines (two corrections). Long chatty prose had little in-window evidence.
- **The skill did not prevent these:** sessions that loaded it still produced `fork_turns`, the tables, hard wraps, and crammed rules.
- Marián rarely reviews doc content beyond "LGTM"/"merged", so bloat accumulates unless the writing agent catches it.

### Decisions

1. Retire `writing-for-agents`. `project-context` (rebuilt 2026-09-29 around lasting vs perishable, strength, and one home) already owns most of it.
2. Fold what survives into `project-context` as one paragraph, **Written for the reader**: length fits the content, with the failure named on both sides (padding, code walkthroughs, file or symbol inventories vs crammed rules and conversation-only shorthand); a newcomer can follow it; instructions give goal, reason, and where judgment is needed rather than checklists, with steps only where order matters; no hard-wrapped prose. The description now names AGENTS.md and project skills.
3. Writing global skills loses its dedicated skill; this repository's `AGENTS.md` ("Writing for both models") and `rethink-skill` cover it.

Baseline: repository `b5b63c5`; writing-for-agents SKILL.md SHA-256 `b3785e2f8963f5cd5bfd470b39e6762fab3c28b65a2f26a0bd497fa2ada40462`; project-context SKILL.md `bb60c083cb342569f0a3c23bb241fd0c589def98f487d32720c09e2d36b059f9`. The runtime symlinks in `~/.claude/skills` and `~/.agents/skills` were removed.

### Tests

Six fixtures (under `/tmp/wfa-probe`, not preserved), built from the evidence: `deploy-docs` (user states deployment facts mixed with status, a ticket for next week, and a tested restore; second turn adds backups), `agents-md` (plumbing-only AGENTS.md plus kickoff notes; second turn adds a scope-limited UI rule), `small-rule` ("pull first… just something simple"), `run-felt` (feature with a domain rule, "update docs as needed"), `copy-skill` (turn call notes with perishable details into a project skill; second turn "is it as short as it can be without losing anything?"), and `pace-fix` (bug fix; no doc work expected).

Baseline was both skills as they stood; candidate was folded `project-context` alone. Each ran through normal discovery on Opus 5.5 and GPT-6 Astra at medium effort. Opus 5.5 and GPT-6 Astra at high effort judged every pair blind, with randomized labels and a rubric built from the decisions, on transcripts plus repository diffs.

Skill loading: baseline Codex loaded writing-for-agents in all 5 doc scenarios (with project-context in 3); baseline Opus loaded it for `agents-md` and `copy-skill` only. Candidate Opus loaded project-context for `deploy-docs` and `copy-skill`; candidate Codex for 4 of 5 doc scenarios, not `copy-skill`. Neither loaded anything for `pace-fix`.

Verdicts over 24 judgments: candidate 14, baseline 4, tie 6.

| Scenario | Opus runs | Astra runs | Note |
| --- | --- | --- | --- |
| deploy-docs | candidate (both) | baseline / tie | Candidate Opus dropped the B-84 status, dates, and restore log. Astra wrote "As of… 2026-09-30, the background worker is not configured… B-84" and the dated restore in both conditions despite loading project-context. |
| agents-md | candidate (both) | split | Baseline Opus added "Current state: … not set up yet" and rules the user never set. Candidate Opus moved content into PROJECT.md and ENGINEERING.md and deleted `notes/kickoff.md` (reported); judges called the split slightly more structure than needed but preferred it. Both Astra runs copied personal global guidance ("Track requested work in GitHub Issues", verification rules) into project AGENTS.md. |
| copy-skill | candidate (both) | candidate (both) | Baseline Astra copied "Jana… on leave until end of October" and the note date into the skill; candidate did not, without loading any skill. |
| small-rule | candidate (both) | candidate (both) | All four were one line; differences are wording noise. |
| run-felt | candidate / tie | baseline (both) | Candidate Astra added a README code example restating the API, and also ran check-work on a small change. |
| pace-fix | tie | tie | No doc changes. |

Reading: retiring the skill cost nothing measurable and the folded paragraph did not hurt; the clear wins are Opus runs where project-context loaded, and the Astra `copy-skill` win came without any skill loaded, so part of the margin is run variance. Neither condition stops Astra writing status the user states directly into deployment docs, although project-context names that failure; not chased with more wording. No fixes were rerun.

What these tests cannot show: long-session drift, docs accumulating across many changes, whether Codex self-loads project-context when writing skills in real use, and whether hard wraps disappear (few runs wrapped in either condition).

Final project-context SKILL.md: 656 words, SHA-256 `0b93ddb2c25d7bba01165c7db5ccc83f487c2b070a0bdeef78ca407d9db451ef`.
