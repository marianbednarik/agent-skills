# Delegation reference sheet

Research date: 2026-10-24. Scope: when the main agent in Claude Code or Codex should spawn subagents, for the Delegation section of `context/AGENTS.md` and delegation lines in skills.

## Decision

Work directly by default; delegate when it clearly pays: independent parallel tracks, broad sweeps whose raw output would otherwise sit in context, or a second opinion where another model's judgment matters (independent review of risky changes). Do not delegate work finishable in a handful of tool calls, chained steps, or work needing conversation history. The wording also names the opposite failure (serializing independent work), because the model families drift in opposite directions.

This replaces "delegate side work by default" (commits `487d7f4` through `95bec06`). Marián observed agents delegating too often; the sources below agree.

## Evidence

- Anthropic, "Building agents: When to fold subagents into your main agent loop" (2026-10-22, https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop). About API product agents, not interactive coding. Keep subagents for measurable context-bloat degradation, parallel tasks with discardable fresh context, or tool-selection or instruction conflicts. Handoffs return lossy summaries and add latency. Good splits: independent research paths, clean component boundaries, black-box verification.
- Anthropic prompting docs (live, checked 2026-10-24). Best practices: Opus 4.6 "might spawn them in situations where a simpler, direct approach would suffice"; sample: "Use subagents when tasks can run in parallel, require isolated context, or involve independent workstreams that don't need to share state." Opus 5 guide: "delegates to subagents more readily than prior models"; sample: "Do not delegate work you can finish yourself in a handful of tool calls, and do not use subagents to verify or double-check your own work." Also: remove routine "use a subagent to verify" instructions; they cause over-verification.
- Claude Code sub-agents docs (live): main conversation for back-and-forth, phases sharing significant context, quick targeted changes, or when latency matters; subagents for verbose output, tool restrictions, self-contained work returning a summary.
- OpenAI GPT-6 guide (live): pushes the other way for Astra, "if it could save time or improve quality", and says to tune delegation to the harness. Codex docs favor read-heavy exploration, tests, and triage for subagents; parallel writes with caution.
- Cognition: "Don't Build Multi-Agents" (2025-06-12) softened to "multiple agents contribute intelligence, writes stay single-threaded" (2026-04-22); reports clean-context review finding real bugs.
- Cursor (2026-09-23): removing prompts that strongly encouraged exploration subagents balanced usage.
- Li et al. preprint (2026-10-07, arXiv 2610.10263): Claude Code with concurrency fell 83% to 59% on sampled SWE-bench tasks with about 2x tokens; single run per condition, autonomous benchmarks. Not independently verified here.

Weak or missing evidence: cheap-model routing for code search, and cross-provider delegation in interactive coding, have no controlled comparison showing they beat direct work. The Haiku row is kept, limited to broad sweeps.

## Skill implications

- `check-work`: unchanged. Gated to large or risky changes; independent fresh-context review is the best-supported use.
- `codebase-audit`: unchanged. Splitting a broad sweep by area matches independent research paths.
- `shaping`: delegate fact-finding only when sizeable or splitting into independent questions.
