---
name: rethink-skill
description: Reassess an existing skill with evidence from real use, rewrite it if warranted, and test the result on every model family it must serve. Use for a substantial rethink of a skill's purpose or behavior, not routine wording edits or new skills.
---

Reach a direction for the target skill with the user, then revise it if warranted. Keeping it, shrinking it, removing it, and redesigning it are all valid outcomes. Treat the current text and the user's framing as hypotheses.

Start from purpose. Ask what the skill is for in the user's words and whether a capable model already does that without it. Read the canonical skill, its sheet under `research/`, and adjacent skills where ownership overlaps. If the text already serves its purpose, the work may only be making it model-neutral.

Get evidence from real use before building synthetic tests. Search the harness session logs for runs where the skill was actually loaded, not merely listed in the catalog, and for predecessor skills that did the same job. Delegate extraction to fresh-context agents with a neutral brief covering the trigger, what the agent did, the outcome, the cost, and the user's next message. How the user reacted after a skill ran is the strongest evidence of its value. Read [references/evidence-and-testing.md](references/evidence-and-testing.md) before searching logs or running probes.

Work the direction out in conversation: what the evidence shows, what it means for the skill, a recommendation, and questions with defaults. Research comparable skills and methods when the evidence leaves the direction open; extend the existing research sheet rather than redoing it.

Write for every model that will use the skill. Models drift in opposite directions, so name the failure on each side of a behavior rather than pushing one way. Use no model names or personal names, do not depend on personal global guidance, and keep frontmatter to Agent Skills spec fields. Put scope and risk triggers in the description, since that is all an agent sees before loading. Prefer steering and decision criteria over procedures.

Preserve the baseline (commit and hash) before editing. Test on each model family through normal discovery in its real harness: realistic prompts in isolated fixtures, baseline and candidate on the same scenarios, one condition changed at a time. Include a case where the skill should not fire. For conversational skills, script several turns that include pushback, "I don't know", and new information. Have judges from both model families compare pairs blind, with randomized labels and a rubric built from the agreed decisions. A blind text-only review is a separate, weaker signal. Fix concrete problems the tests reveal and rerun the affected scenarios; do not chase noise.

Record in the research sheet the real-use evidence, decisions, baseline, tests, results, and what synthetic tests cannot show. Report splits and losses honestly; small scripted samples cannot prove improvement. Canonical skill files are symlinked into the live harnesses, so edits take effect immediately. Commit or push only when asked.
