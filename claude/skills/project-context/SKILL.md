---
name: project-context
description: >
  Capture or refresh durable project context that an agent cannot infer from
  the code, and put each piece in the layer that loads it at the right time.
  Use when Marian asks to document project direction, set up a project's agent
  context, or refresh stale context after the direction changed. Do not use
  merely because a project is new, work just finished, or context files are
  missing.
---

# Project Context

Capture only what a future agent cannot work out from the repository, and put
it where it will load when it is needed and stay out of the way when it is not.

Marian's standing constraint: he does not want everything injected into every
conversation. A backend task should not carry his color preferences. Choosing
the layer is most of this skill's value.

## Choose the layer

- **`CLAUDE.md` (repo root)** — only what is true for every task in this repo.
  Usually a handful of lines: what this is, the commands that are not obvious,
  and one line naming the on-demand docs below. Keep it under ~30 lines. If
  something here only matters sometimes, it belongs in a rule.
- **`.claude/rules/*.md` with `paths:`** — guidance that must be *active while
  editing* a particular kind of file, and absent otherwise. Frontend taste
  scoped to `src/**/*.tsx`, API conventions to `src/api/**`, migration cautions
  to `**/migrations/**`. This is the layer that solves the "why am I carrying
  this right now" problem; reach for it first.
- **On-demand docs** — `PROJECT.md`, `DESIGN.md`, `ENGINEERING.md`,
  `LANGUAGE.md`. Narrative context read when a task calls for it, not loaded at
  startup. Name them in `CLAUDE.md` so they are discoverable, but do not
  `@`-import them; an import loads the whole file every session and defeats the
  point.
- **Auto memory** — leave it alone. It is Claude's own notes from working with
  him. Do not hand-author it, and do not duplicate into a doc something that is
  already being learned there.
- **Nothing** — the honest answer for most candidate facts.

## Writing it

Read the repo and any existing context before asking anything. Ask grouped
questions with your inferences stated, so he corrects rather than composes.

Use the templates in this folder as scaffolds, not schemas — omit, merge, or
rename sections when that reads better. Italic text in them is authoring
guidance, not content.

Document ownership when these docs are warranted:

- `PROJECT.md` — purpose, users, product taste, durable constraints, and the
  reasons behind project-level decisions
- `DESIGN.md` — durable visual and interaction direction for a real interface
- `ENGINEERING.md` — non-obvious architecture, chosen primitives, external
  systems, operations, contracts, sharp edges
- `LANGUAGE.md` — project terms an agent could misuse, and the distinctions
  they encode

Every entry records a decision, constraint, or reason. No roadmaps, no current
state, no dependency inventories, no file trees, no restating the stack.

When refreshing, update only what actually changed. If something looks stale
outside the requested scope, say so rather than rewriting it.

End with what changed, which layer each thing landed in, and what is still
unclear.

## Gotchas

- The most common mistake is putting a sometimes-relevant rule in `CLAUDE.md`
  because it was easier than scoping it. Scope it.
- Do not create the four documents by default. Most projects need one or two,
  and some need none.
- Prefer the implementation as the source of truth for exact tokens, versions,
  and values — unless the exact value is itself the constraint.
- Do not edit `CLAUDE.md` or unrelated docs beyond what he asked for.
