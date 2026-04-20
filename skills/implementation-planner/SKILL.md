---
name: implementation-planner
description: >
  Plan a feature, refactor, cleanup, or meaningful code change before coding.
  Use when the user wants to brainstorm, inspect the code, challenge requirements,
  ask grouped questions with recommended answers, resolve tradeoffs, and agree on
  an implementation plan before explicitly approving implementation.
---

# Implementation Planner

Use this skill for the conversation before a non-trivial implementation.

Explore first. Read relevant code, docs, tests, and existing patterns before asking questions the repo can answer.

Restate the goal, surface ambiguity or risk, and propose concrete approaches with tradeoffs. Do not just ask what the user wants; recommend what you think the best answer is and explain why.

Ask grouped questions around the uncertainties that matter for this change. For each meaningful question, include your recommended answer/default so the user has something concrete to accept, reject, or adjust.

Walk the decision tree far enough to resolve dependencies between decisions. Stress-test the plan against the existing code, concrete user scenarios, edge cases, and terminology that could change the implementation.

Iterate until there is a shared plan. Prefer the smallest plan that proves the direction and leaves room to learn.

Keep the plan in chat by default. Avoid creating plan files unless the user asks, the work must span multiple sessions, or the plan is too large to safely keep in conversation.

The plan should cover the agreed goal, chosen approach, steps/checkpoints, verification, and remaining risks or open questions.

When the plan is ready, say so and wait for explicit user approval before implementing. Do not start coding just because the plan looks complete.
