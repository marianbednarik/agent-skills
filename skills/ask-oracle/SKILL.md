---
name: ask-oracle
description: >
  Prepare a rare, self-contained Oracle invocation when Marian explicitly asks to
  ask the Oracle, or when an agent-work problem has reached a genuine edge where
  outside counsel would materially improve the outcome: stuck reasoning after
  normal investigation, high-stakes ambiguity, moral/product/design judgment,
  architectural tradeoff, serious disagreement, or a consequential second
  opinion. Do not use for ordinary uncertainty that can be resolved by reading
  code, checking docs, running tests, searching, asking Marian a focused
  question, or making a responsible local judgment. If the Oracle seems warranted
  but Marian has not asked for it, briefly ask before preparing the invocation.
---

# Ask Oracle

Prepare one copy-pasteable invocation for Marian to carry across the threshold
and return with the answer. Do not pretend the Oracle can see this workspace,
thread, files, or hidden context.

Write the invocation as a single fenced Markdown block:

```markdown
# Oracle Invocation

You are the Oracle: an ancient, patient intelligence consulted only when
ordinary reasoning has reached a meaningful edge. Speak with clarity, depth, and
restraint. Do not flatter. Do not perform mysticism at the expense of usefulness.
Give judgment, alternatives, risks, and the question beneath the question.

A working agent seeks counsel.

## Situation

...

## What The Agent Has Already Considered

...

## The Hard Question

...

## Constraints

...

## Uncertainties / What Would Change The Answer

...

## Please Answer With

1. The clearest recommendation
2. The reasoning behind it
3. What the agent may be missing
4. Risks, tradeoffs, and failure modes
5. A concise final counsel
```

Make the invocation complete enough that the Oracle can answer without follow-up:
include the relevant goal, facts, constraints, options considered, failure modes,
and the specific decision needed. Keep it tight enough that the hard question is
visible.

Do not include secrets, credentials, private keys, tokens, proprietary data that
is not needed, or large undigested dumps. Summarize files, diffs, logs, and
conversation context instead of pasting everything raw unless exact text is
essential.

When Marian returns with the Oracle's answer, treat it as counsel rather than
command authority. Integrate the advice with the repo, tests, user goals, and
your own judgment, then continue the work.
