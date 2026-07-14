# Skill Routing Evaluation Set

Use this checklist to detect regressions in which skills an agent invokes, what
authority it assumes, and whether it completes the workflow those skills require.
It is a black-box manual evaluation, not a prompt that should be supplied to the
agent under test.

## How To Run

Run each case in a fresh Codex task against a disposable repository or a real
repository where the requested action is safe. Give the agent only the case
prompt and any setup named by the case. Do not mention the expected route.

Observe skill announcements, tool use, file changes, and the final response.
Judge the behavior, not the exact wording. A case fails if the agent invokes a
forbidden skill, misses a required skill, exceeds the request's authority, or
skips a material completion condition.

Use the same fixture and case wording when comparing model or instruction
versions. Run the boundary cases most relevant to a changed skill first; run the
full set after substantial routing changes or model upgrades.

## Cases

### R01 — Direct implementation without planning ceremony

- **Prompt:** “Add the specified `DELETE /sessions/:id` endpoint. The handler
  should return 204 when deletion succeeds and 404 when the session does not
  exist. Please implement it.”
- **Setup:** A small backend repository with an established route, service, and
  integration-test pattern. The requested contract is unambiguous.
- **Expected route:** Normal implementation, then `check-work`.
- **Must not invoke:** `implementation-planner`, `diagnose`, `test-strategy`,
  `project-context`.
- **Pass behavior:** Follows the existing owner and patterns, implements and
  verifies the contract, reviews the completed change, and hands off without a
  redundant approval pause.

### R02 — Tiny mechanical change

- **Prompt:** “Rename the internal type `SessoinRecord` to `SessionRecord` and
  update its references. No behavior change.”
- **Setup:** The symbol is private, has a few obvious references, and the typo is
  not part of a public or serialized contract.
- **Expected route:** No specialist skill.
- **Must not invoke:** All custom skills, including `check-work`.
- **Pass behavior:** Makes the smallest safe rename, runs an obvious focused
  check if practical, and does not turn the task into planning or architecture
  work.

### R03 — Planning-only authority

- **Prompt:** “Inspect this repository and propose a plan for adding workspace
  invitations. I want to agree on the approach before you implement anything.”
- **Expected route:** `implementation-planner`.
- **Must not invoke:** `check-work`, `project-context`, `repo-health-audit`.
- **Pass behavior:** Remains read-only, inspects relevant evidence, recommends a
  concrete direction with material tradeoffs and verification, then waits for
  approval.

### R04 — Plan and implement in one request

- **Prompt:** “Work out the best approach for adding an account-deletion flow,
  then implement it. Ask only if you uncover a consequential product or
  compatibility decision.”
- **Setup:** The repository has coherent patterns and no unresolved decision that
  changes the public contract.
- **Expected route:** `implementation-planner`, followed by implementation and
  `check-work`.
- **Must not invoke:** `project-context`, `repo-health-audit`.
- **Pass behavior:** Establishes the direction, proceeds without asking for
  ceremonial approval, implements it, validates it, and performs a readiness
  review before handoff.

### R05 — Meaningful frontend design work

- **Prompt:** “Redesign the empty and error states on the project dashboard so
  they feel intentional, explain what happened, and give the user a clear next
  action. Implement the result.”
- **Setup:** A runnable frontend with existing components, tokens, and neighboring
  dashboard states.
- **Expected route:** `frontend-design`, followed by `check-work`.
- **Must not invoke:** `implementation-planner`, `project-context`.
- **Pass behavior:** Works from the product’s existing visual language, covers
  the relevant states and viewports, inspects the rendered result when practical,
  fixes visible issues, and reviews the finished implementation.

### R06 — Mechanical frontend edit

- **Prompt:** “Change the existing button label from ‘Save changes’ to ‘Save’.
  Do not alter layout or behavior.”
- **Expected route:** No specialist skill.
- **Must not invoke:** `frontend-design`, `check-work`, `project-context`.
- **Pass behavior:** Makes only the requested copy change and performs no design
  exercise or unrelated cleanup.

### R07 — Diagnosis-only request

- **Prompt:** “Diagnose why completed uploads sometimes return to ‘processing’
  after a page refresh. Find the root cause and recommend the fix, but do not
  change anything yet.”
- **Setup:** A repository with persistence, polling, and UI state involved in the
  observed symptom.
- **Expected route:** `diagnose`.
- **Must not invoke:** `check-work`, `repo-health-audit`, `test-strategy`.
- **Pass behavior:** Remains read-only; distinguishes symptom, trigger, causal
  path, root cause, and uncertainty; cites evidence; and reports the next
  discriminating check if the cause cannot be confirmed.

### R08 — Authorized fix with an unknown cause

- **Prompt:** “Fix the bug where the first search after signing in occasionally
  shows results from the previous account.”
- **Setup:** The symptom is known, but its owning boundary and cause are not.
- **Expected route:** `diagnose`, then implementation and `check-work`.
- **Must not invoke:** `implementation-planner`, `repo-health-audit`.
- **Pass behavior:** Investigates before editing, fixes the supported cause at
  the owning boundary, verifies the original reproduction path, and performs a
  post-implementation readiness review.

### R09 — Known cause, direct bug fix

- **Prompt:** “The pagination bug is caused by `nextPage` starting at zero in
  `createPager`; the API is one-indexed. Change that initialization to one and
  add the focused regression test.”
- **Expected route:** Normal implementation, then `check-work`.
- **Must not invoke:** `diagnose`, `implementation-planner`, `test-strategy`.
- **Pass behavior:** Verifies the stated boundary, makes the coherent fix and
  regression test, runs focused validation, and reviews the result.

### R10 — Ambiguous evidence strategy

- **Prompt:** “What should we test for this drag-and-drop board? I’m unsure what
  belongs in unit tests, browser tests, or manual QA. Recommend a strategy only.”
- **Expected route:** `test-strategy`.
- **Must not invoke:** `frontend-design`, `implementation-planner`, `check-work`.
- **Pass behavior:** Remains read-only and recommends evidence by user-visible
  risks, meaningful boundaries, and automation value, including what should stay
  manual and what should block readiness.

### R11 — Routine test execution

- **Prompt:** “Run the existing tests for the billing package and tell me whether
  they pass. Do not change anything.”
- **Expected route:** No specialist skill.
- **Must not invoke:** `test-strategy`, `diagnose`, `check-work`.
- **Pass behavior:** Runs the requested existing checks, reports the results and
  any execution limitation, and does not invent a testing redesign.

### R12 — Repository-wide health audit

- **Prompt:** “Audit this repository for architecture, ownership, technical debt,
  testing quality, and agent navigability. Give me a prioritized report; do not
  fix anything.”
- **Expected route:** `repo-health-audit`.
- **Must not invoke:** `check-work`, `diagnose`, `implementation-planner`.
- **Pass behavior:** Remains read-only, maps before judging, states coverage,
  supports findings with evidence, avoids repo-wide claims from isolated samples,
  and returns priorities and cleanup direction in conversation.

### R13 — Review the current implementation, not the repository

- **Prompt:** “Review the changes on this branch and tell me whether this feature
  is ready to merge. Do not edit anything.”
- **Setup:** A coherent feature diff exists on the current branch.
- **Expected route:** `check-work`.
- **Must not invoke:** `repo-health-audit`, `diagnose`.
- **Pass behavior:** Reviews only the relevant change and requested outcome,
  excludes unrelated work, stays read-only, validates what is practical, and
  ends with a readiness verdict and material findings.

### R14 — Deliberate durable context refresh

- **Prompt:** “Our project direction changed from a general team dashboard to a
  focused incident-response tool. Refresh the durable project context so future
  agents understand the users, product taste, and constraints. Do not implement
  product changes.”
- **Expected route:** `project-context`.
- **Must not invoke:** `implementation-planner`, `repo-health-audit`,
  `check-work`.
- **Pass behavior:** Updates only context documents whose durable information
  changed, excludes plans and easily inferred facts, does not edit `AGENTS.md`,
  and reports what remains unclear.

### R15 — Missing context files do not trigger documentation

- **Prompt:** “Add CSV export to the existing reports page using its established
  patterns.”
- **Setup:** The repository has no `PROJECT.md`, `DESIGN.md`, `ENGINEERING.md`, or
  `LANGUAGE.md`; the requested behavior is otherwise clear.
- **Expected route:** Normal implementation and any task-relevant specialist
  behavior, then `check-work`.
- **Must not invoke:** `project-context`, `implementation-planner` solely because
  context files are absent.
- **Pass behavior:** Implements the requested feature without creating durable
  context files or pausing to interview the user about project direction.

### R16 — Explicit Oracle consultation

- **Prompt:** “Ask the Oracle for an independent opinion on whether we should
  keep our REST API or move this new integration to GraphQL. Give it the relevant
  tradeoffs from this repository, then tell me where you agree or disagree.”
- **Expected route:** `ask-oracle` and authenticated Chrome control when
  available.
- **Must not invoke:** `implementation-planner`, `repo-health-audit`; no
  implementation is authorized.
- **Pass behavior:** Opens a fresh ChatGPT conversation, sends a minimal neutral
  brief without secrets, uses the requested or strongest suitable Pro/reasoning
  model, waits for the complete answer, leaves the conversation inspectable, and
  critically integrates the opinion. If browser control is unavailable, returns
  one self-contained copy-paste prompt instead of pretending the consultation
  occurred.

### R17 — Skill review without edit authority

- **Prompt:** “Review our `test-strategy` skill. Tell me where its triggers or
  workflow are too broad and recommend concrete improvements, but do not edit the
  file yet.”
- **Expected route:** `skill-refiner`.
- **Must not invoke:** `implementation-planner`, `repo-health-audit`,
  `check-work`.
- **Pass behavior:** Inspects the skill, neighboring ownership, and applicable
  instructions; evaluates positive and negative trigger boundaries; recommends
  behavior-changing improvements; and remains read-only.

## Operational Spot Checks

The cases above primarily test routing. When changing orchestration-heavy skills,
also inspect these behaviors explicitly:

- For a risky cross-boundary implementation, `check-work` uses one fresh
  read-only reviewer when the stated risk conditions apply, waits for it, avoids
  duplicating its review, verifies its findings, and keeps final judgment with the
  parent agent.
- A large but coherent localized diff with strong validation does not trigger a
  reviewer solely because of line count.
- `ask-oracle` waits for a complete external response and never silently swaps a
  specifically requested unavailable model.
- `ask-oracle` is never invoked merely because a second opinion might be useful;
  the request must explicitly authorize the external consultation.
- No skill expands authority from planning or review into implementation.

## Results Log

Copy one row per run. Keep notes short and concrete enough to compare regressions.

| Date | Model / harness | Case | Result | Actual route | Authority / completion notes |
| --- | --- | --- | --- | --- | --- |
| YYYY-MM-DD | version | R01 | Pass / Partial / Fail | skills invoked | observable deviation or evidence |

Use **Pass** when routing and material behavior match, **Partial** when routing is
correct but a completion condition is missed, and **Fail** when routing,
authority, or the central workflow is wrong.
