---
name: implementation-planner
description: >
  Agree on an approach in conversation before writing code. Use when Marian
  wants to think something through, hear options, be asked questions, or sign
  off on a direction first — "let's plan this", "what are the options", "how
  would you approach", "before you implement". Also use for a change whose
  shape is genuinely undecided. Do not use when the contract is already
  specified, for tiny mechanical edits, or for pure research questions.
---

# Implementation Planner

Reach an agreed direction through conversation. Marian wants to understand the
system well enough to explain and defend it later — not just approve a diff.

Do not enter plan mode. Plan mode writes the plan to a file and gates on
approval to exit it; this skill is deliberately conversational and leaves no
artifact. Keep the plan in the conversation unless Marian asks for a document.

Read the code first. Questions the repository can answer are not questions.

Then bring back, at the level of detail the change actually warrants:

- what you found and what it constrains
- the approach you recommend, and why that one
- real alternatives where they exist, with the tradeoff that separates them
- the questions where his answer changes the work — grouped, each with your
  recommended default so he can accept, adjust, or reject something concrete
- how the result will be verified
- what you are still unsure about

Explain the reasoning behind boundaries and ownership choices, not just the
steps. That reasoning is the deliverable as much as the plan is.

Once the direction is settled, implement it. Planning does not authorize
expanding scope; a newly discovered consequential choice comes back to him.

## Gotchas

- Do not manufacture alternatives to look thorough. One recommendation with a
  clear reason beats three options with no opinion.
- Do not stop at "here's the plan, shall I proceed?" when he already asked you
  to plan *and* implement. Ceremony he did not request is friction.
- Do not turn the plan into tickets, a file-by-file edit script, or a
  speculative architecture exercise.
- If he pushes back on the recommendation, take the position seriously rather
  than immediately folding to the last thing said.
