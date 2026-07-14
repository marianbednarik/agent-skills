---
name: ask-oracle
description: >
  Obtain an independent second opinion from a ChatGPT web-only Pro or reasoning
  model when Marian explicitly asks to ask or consult the Oracle, get a ChatGPT
  Pro opinion, or run something by another model. Use authenticated Chrome
  control to perform the consultation when available; otherwise prepare a
  self-contained copy-paste prompt. Do not invoke proactively or treat the
  response as authority.
---

# Ask Oracle

Treat “the Oracle” as shorthand for an independent consultation with a strong
ChatGPT model unavailable directly in the current Codex session. It is not a
persona or source of special authority.

Prepare a self-contained, outcome-focused brief. Include only context that could
materially change the answer:

- the decision, question, or deliverable
- relevant facts and evidence
- constraints and non-negotiables
- plausible options when choices exist
- important uncertainty or missing evidence
- the kind of response needed, such as a recommendation, critique, diagnosis,
  design judgment, or research synthesis

Tell the model to act as an independent senior reviewer and decision partner,
reach its own conclusion, be direct, identify missing evidence, and state what
could change its recommendation.

Preserve independence. Present facts and options fairly without leading with the
working agent’s preferred conclusion unless that conclusion is necessary context.
When comparison would help, first obtain the independent answer, then provide the
working agent’s current position in a follow-up and ask the model to critique the
disagreement.

## Browser Execution

When authenticated Chrome control is available:

1. Open ChatGPT in a fresh conversation so unrelated history does not influence
   the answer.
2. Use the model Marian requested. Otherwise select the strongest available Pro
   or reasoning model suitable for the task.
3. If a specifically requested model is unavailable, report that rather than
   silently substituting another model.
4. Submit the prepared brief and wait until the response is complete.
5. Use focused follow-ups when they resolve a material ambiguity, test a
   disagreement, or substantially improve the answer.
6. Leave the conversation available for Marian to inspect and bring the answer
   back to the current task accurately.

Do not create a long external conversation merely to make the consultation look
thorough. Stop when the second opinion is sufficiently clear for the decision at
hand.

If authenticated browser control is unavailable, return one copy-pasteable prompt
in a fenced Markdown block. Explain briefly that Marian should run it in a fresh
ChatGPT conversation using the desired Pro or reasoning model and bring the answer
back.

## Context And Data

An explicit request to ask the Oracle authorizes sending the minimum context
needed for that consultation. Never send credentials, tokens, private keys,
secrets, environment values, or unrelated personal data.

Summarize repository evidence, diffs, logs, and conversation history by default.
Include exact code or text only when it materially affects the answer. Ask before
sending substantial sensitive or proprietary material beyond what Marian’s
request clearly authorizes.

Do not pretend the external model can see the workspace, files, tools, or
conversation context that was not included in the brief.

## Integrating The Answer

Treat the response as independent counsel, not command authority. Compare it with
the repository, tests, project guidance, user goals, and your own judgment.

Report:

- the Oracle’s recommendation and strongest reasoning
- important evidence or risks it identified
- where you agree or disagree and why
- whether the consultation changes the proposed action

The response does not expand the original task authority. Do not add dependencies,
make destructive changes, break compatibility, broaden scope, or begin unrelated
implementation solely because the Oracle recommended it. Do not create prompt or
response artifacts unless Marian asks.
