---
name: retro
description: Use when the user asks for a retro, or asks what got in the way, what was harder than it should have been, or what to improve after a work session.
---

Surface what made the work harder or slower than it needed to be, especially friction the user never saw, and propose fixes so it does not recur. Agents smooth over obstacles so well that hidden friction disappears from final reports.

## Read the record

Do not rely on memory; it is compressed and misses what subagents or background tasks hit. Inspect the session transcript and any subagent or background logs the harness keeps, looking for failed tool calls, retries, fallbacks, and abandoned approaches. Start from anything the user pointed at, using the current session unless another is named.

## What counts

Focus on high-signal friction, most costly first:
- Workarounds that changed what was verified or shipped, and anything that could not be run.
- Misleading errors that caused a wrong diagnosis (such as sandbox or permission failures misread as broken auth).
- Wrong, stale, or missing guidance, and skills that misfired.
- Avoidable slowdowns or recurring manual steps (rebuilt setup, rediscovered procedures, throwaway scripts) that deserve a committed script, check, or skill.
- Discoveries worth keeping so nobody rediscovers them.

Skip routine noise: normal test failures, empty searches, or a quick retry that worked.

## Check recurrence

Do a quick targeted search of earlier sessions for the specific error or procedure (do not scan everything, and stop if logs are unavailable or slow to parse). When a workaround or throwaway script looks likely to recur, ask the user; they often know before the logs show it. One-off slips rarely need a rule; recurring mistakes do. Before proposing a new rule, check whether existing guidance already covers it and failed anyway.

## Where fixes go

Prefer fixing the environment over adding prose: install the tool, fix the script, delete the misleading old path, or add a type, test, or check that fails loudly (and show that it catches the instance that happened). If existing prose was ignored, rewording it rarely helps; enforce it mechanically instead. Match effort to project maturity.

Route each fix to the right level:
- Project facts, scripts, or recurring workflows: repo docs, tooling, or a project skill.
- Personal working preferences: global guidance.
- Machine or harness quirks (aliases, installed tools, sandbox or VPS limits): machine-local config (`~/.agents/local.md` or harness settings).
- External limitations: separate observed failure from suspected cause, and offer a local workaround if one exists.

## Report and act

Report in conversation, ordered by payoff: what happened (with evidence), what it cost, whether it recurs, and the proposed fix and home. Finding nothing worth changing is a good result. Once the user agrees, carry the fixes through without asking again about routine details, and state what changed vs. what remains proposed.
