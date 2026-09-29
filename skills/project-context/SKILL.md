---
name: project-context
description: Keep a project's lasting knowledge in its repository - decisions and their reasons, constraints, domain terms, design direction, parts that must change together, and standing instructions for contributors and their agents. Use when something decided or learned should outlast the conversation, including in the middle of other work, or when project docs need creating, updating, or checking against the code.
---

Keep in the repository what a future contributor, or their coding agent, needs to make good decisions and cannot get from the code. They will not have this conversation, the user's personal setup, or your memory.

**Lasting, not perishable.** One failure is missing the lasting thing: a decision made in passing, in a PR thread, or in a closed issue; its reason; a constraint; a coupling such as lists in two places that must change together. The other is recording what goes stale and then misleads: build status, what is done or next, dates, counts and versions, values the code already holds, notes about this one piece of work. Ask whether a sentence will still be true after the next few changes. Write direction as direction ("exports keep integer cents"), not progress ("JSON export is not built yet"); leave status to the tracker and the code.

**At the strength agreed.** A rule in the repository instructs every future agent, so overstating it has a standing cost: a remark about one situation hardens into a blanket policy. Understating loses a real decision as a passing suggestion. Record what the user settled, in the scope they gave, with the reason when there is one. When someone would plausibly propose the alternative again, record what was rejected and why; that is what stops a decision from flip-flopping. Keep proposals, assumptions, and open questions visibly apart from decisions; do not invent reasons for existing choices.

**One home, reachable.** Keep each decision or rule in one place and point to it from elsewhere; restatements drift apart. When a decision or rule changes, rewrite it where it lives rather than appending an amendment or adding a contradicting rule elsewhere; version control keeps the history. Where a project keeps separate decision records, mark superseded ones and link their replacements. Entry points such as AGENTS.md and README should lead to what matters, saying when it matters.

Follow the project's existing layout. Where there is none, use these names so projects stay consistent, creating each only when it has content: `README.md` (what it is, how to start), `AGENTS.md` (agent instructions and routing), `PROJECT.md` (purpose, users, priorities, deliberate exclusions), `ENGINEERING.md` (technical choices, boundaries, constraints, and their reasons), `LANGUAGE.md` (domain terms and rules), and `DESIGN.md` (visual and interaction direction). Each file owns its kind of statement; the others link to it rather than restate it for their own reader. Do not restructure docs as a side effect.

**With the change.** Update context in the same change that makes it true, not in a later pass. When you touch an area, check nearby claims against the code: fix what is plainly out of date; when code and documented intent disagree without explanation, flag it rather than changing either side to match the other.

Make small context edits directly and mention them; ask only when the intent is unclear. Keep personal details, machine-specific setup, tool or model names, and your own standing instructions out of shared docs. Often nothing needs recording.
