---
name: check-work
description: >
  Review the current implementation before handoff by inspecting changed files,
  checking the diff against Marian's coding standards, running relevant validation
  commands, fixing safe issues, and reporting readiness.
---

# Check Work

Switch from builder mode to reviewer mode.

Review the current changes by default, not the whole repo. Inspect `git status`, diffs, untracked files, relevant project docs, and `AGENTS.md`.

Check for AI-code failure modes:

- wrong concept owner or parallel pattern
- optional-field soup, boolean flag piles, generic modes, or invalid states made easy
- giant mixed-responsibility files
- duplicate local implementations
- shallow helper spray instead of a deeper module
- compatibility shims, silent fallbacks, dual codepaths, or legacy adapters
- defensive guards hiding impossible states
- global CSS drift or hand-rolled UI primitives where project-standard primitives exist
- weakened, mock-heavy, selector-heavy, or implementation-detail tests
- obsolete code left behind
- behavior that no longer matches the agreed plan or user-visible goal

Run the strongest relevant validation commands you can discover: formatter checks, lint, typecheck, tests, build, focused smoke checks, or app-specific verification.

Fix safe issues immediately. Stop and ask before broad rewrites, behavior changes, risky cleanup, or anything that would change the agreed plan.

For concrete issues tied to specific changed lines, emit Codex review findings using `::code-comment{...}` so the user can select findings later. Keep broader architectural or process concerns in the normal summary instead of forcing them into line comments.

End with:

- readiness verdict: ready, ready with caveats, or not ready
- any unfixed `::code-comment{...}` findings for concrete file/line issues
- what changed during review
- commands run and results
- what was inspected but not executed
- remaining risks
- recommended next action if anything is not ready
