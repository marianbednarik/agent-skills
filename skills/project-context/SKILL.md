---
name: project-context
description: Use when writing, updating, or auditing project docs, AGENTS.md, or project skills, or mid-task when a lasting decision, constraint, domain rule, or coupling should be recorded in the repository.
---

Record in the repository what a future contributor or agent needs to make good decisions and cannot read from the code. Often nothing needs recording.

## Keep what lasts

Record durable intent: settled decisions and their reasons, rejected alternatives that someone would plausibly re-propose, constraints, domain rules, and couplings (things that must change together).

Leave out anything that goes stale: progress, status ("not built yet"), dates, counts, versions, notes about one task, and values already visible in code. Write direction as direction ("exports keep integer cents"), not status.

## Match the strength

Every rule in a repo steers every future agent. Do not harden a one-off remark into a blanket policy, and do not soften a real decision into a vague hint. Record the exact scope the user settled, keep open questions and proposals visibly separate from decisions, and never invent reasons for existing code.

## Put it in one place

When a type, test, or check can enforce a rule, prefer enforcing it there and keep prose for the reason and judgment.

Keep each rule in one authoritative home and link to it elsewhere. When a decision changes, rewrite it in place instead of appending amendments (git keeps the history); in separate decision records, mark superseded ones and link their replacements. Entry points (`AGENTS.md`, `README.md`) should lead to what matters and say when it matters. Respect existing doc layouts; if none exist, create files only when they have real content:
- `README.md`: what it is, how to run it
- `AGENTS.md`: agent instructions and routing to other docs
- `PROJECT.md`: purpose, users, priorities, deliberate exclusions
- `ENGINEERING.md`: technical choices, boundaries, constraints, and why
- `DESIGN.md`: visual and interaction direction
- `LANGUAGE.md`: domain terms (only when the domain needs a glossary)
- `BACKLOG.md`: open tasks and progress (only when the project has no remote issue tracker; drop completed items once done)

## Writing and updating

Write so a newcomer (human or agent) can follow it without this conversation. Cut padding, code walkthroughs, and file inventories; also avoid cramming several rules into one sentence. State goals, reasons, and judgment points rather than checklists (use steps only when order matters). Do not hard-wrap prose, and keep personal, machine-specific, or tool/model details out of shared repo docs.

Update docs in the same change that makes them true. When touching an area, fix plainly stale claims; if code and documented intent disagree without explanation, flag it instead of silently rewriting either side. Make small doc edits directly and mention them; ask only when intent is unclear.
