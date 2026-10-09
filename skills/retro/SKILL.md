---
name: retro
description: Look back over a work session, including its background and subagent work, for friction the agent worked around, work that took far longer than it should or keeps being redone, and wrong or missing guidance, then propose fixes so future sessions do not repeat them. Use only when the user asks for a retro or asks what issues came up.
disable-model-invocation: true
---

Surface what made the work harder or slower than it needed to be, especially what the user never saw, and propose fixes so it does not happen again. Capable agents route around obstacles so smoothly that the friction disappears from their final report, and background work has no one watching at all. That hidden friction is what a retro is for.

**Read the record, not your memory.** Your recollection of a long session is compressed, and you never saw what subagents or background tasks struggled with. Go back through what happened: the session transcript and any subagent or background logs the harness keeps, and within them the failed tool calls, retries, fallbacks, and changes of approach. Start from anything the user points at. Use the current session unless another is named.

**What counts,** most consequential first:
- workarounds that changed what was verified or what shipped, and anything that could not be run;
- misleading errors that led to a wrong diagnosis, such as a sandbox or permission failure read as broken auth or a missing tool;
- guidance that was wrong, stale, or missing, and skills that misfired;
- inefficiency: work that took far longer than it needed, or a task done by hand that keeps coming back (setup rebuilt each time, a procedure rediscovered), which may deserve a script, a check, or a skill;
- useful discoveries worth keeping so no one has to rediscover them.

Leave out routine noise: expected test failures, a search that found nothing, a quick retry that worked.

**Pattern or one-off.** Check whether the same obstacle or task came up before by searching earlier sessions for the specific error or procedure; do not read them all. A one-off slip does not justify a permanent rule, but "my mistake, no rule needed" is the wrong verdict when the same thing keeps happening. Before proposing guidance, check whether existing guidance already covers it and why it did not help.

**Fix at the right level.** Prefer changing the environment over adding instructions: install the missing tool, fix the script, correct the wrong line, write the helper the task keeps needing. Put each fix where the next agent who needs it will find it:
- the project's facts, workflows, and recurring procedures: its docs, tooling, or a project skill;
- the user's own working preferences: their global guidance;
- one machine's or harness's quirks (shell aliases, installed tools, sandbox behavior): fix the machine or that harness's configuration, not guidance that other machines or people read.

For a limitation outside local control, keep what failed separate from what you suspect caused it, and offer a local mitigation if one exists.

**Report and act.** Present findings in conversation, ordered by payoff: what happened, with the evidence; what it cost; whether it recurs; and the fix and where it goes. Keep to what is worth acting on; finding nothing worth changing is a fine result. Apply what the user agrees to, carry agreed fixes through without asking again about routine details, and say what changed and what remains a proposal.
