---
name: skill-refiner
description: >
  Create, review, or revise Marian's personal Claude Code skills when he asks.
  Turn a repeated prompt, a rough idea, or a bloated existing skill into
  something that reliably changes behavior, with clear triggers and honest
  authority. For review-only requests, recommend without editing.
---

# Skill Refiner

A skill earns its place by changing what Claude does. If the instruction only
describes behavior Claude already produces, it is noise that costs context and
dilutes the instructions around it.

Start from the behavior that should change, and from what Marian was tired of
typing. Most of these skills exist to replace a prompt he retypes — that prompt
is the real specification.

## Does it belong here at all

Before writing, decide the layer:

- **a skill** — a task-shaped behavior with a recognizable trigger
- **a path-scoped rule** (`.claude/rules/` with `paths:`) — guidance that must
  be active while editing certain files
- **`CLAUDE.md`** — true for every task in a repo
- **auto memory** — something Claude should learn by working with him, not be
  told
- **nothing** — the model already does it

Overlapping ownership is worse than a missing skill. Check the neighbors, and
check what Claude Code already ships: `/code-review`, `/verify`, `/simplify`,
`/batch`, `/loop`, `/doctor`, plan mode. Duplicating a bundled behavior creates
a routing coin-flip.

## Writing it

The `description` is the routing decision — it is the only part loaded until
the skill fires. Lead with what it does and when it triggers, in the words
Marian would actually use, and name the adjacent situations where it should
*not* fire. `description` plus `when_to_use` truncates at 1,536 characters.

Keep the body short. Give goals and constraints; do not railroad with numbered
steps. Claude composes the procedure — it needs to know what "done" and "good"
mean, and where the boundaries are.

Include a **Gotchas** section wherever there is real failure data. It is the
highest-signal part of a skill. Grow it from observed failures rather than
imagined ones.

Cut anything that: restates general competence, repeats guidance already in
another layer, describes facts discoverable from the repo, or reads as caution
without a decision attached.

## Claude Code mechanics worth knowing

- The **directory name is the command**. In personal and project skills,
  frontmatter `name` is only a display label.
- Skill content is injected **once and persists for the session**, and is never
  re-read. Write standing instructions, not one-time steps.
- `disable-model-invocation: true` — only Marian can invoke it. Correct for
  anything with side effects or external reach.
- `user-invocable: false` — only Claude can. For background knowledge that is
  not a meaningful command.
- `disallowed-tools` removes tools while active — but do not use it on skills
  whose authority is conditional, or the authorized path breaks.
- `allowed-tools` pre-approves for the invoking turn only; it grants, it does
  not restrict.
- A skill is a folder. Scripts, references, and templates belong in it when
  they save reconstruction, and are read on demand.
- Personal skills live at `~/.claude/skills/<name>/`; symlinked directories are
  supported, which is how this repo stays the source of truth.

## Before finishing

Read the description against requests that should and should not trigger it.
Read the body as an agent that has never seen it and delete every line that
would not change what you do. Check that planning-only, implementation-
authorized, and review-only cases each land correctly.

If he asked for review only, stop at recommendations.

## Gotchas

- Do not port a skill's structure from another harness. Port its intent.
- Do not add README, changelog, or process files inside a skill folder.
- Length is not thoroughness. A skill that says four things well beats one that
  says twenty things adequately, because the four survive contact with a long
  session.
