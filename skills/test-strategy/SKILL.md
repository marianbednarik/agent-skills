---
name: test-strategy
description: >
  Decide what evidence should protect behavior when the appropriate test level
  or authority is genuinely unclear. Use when Marian asks what or how to test,
  automated and manual checks have meaningful tradeoffs, existing tests conflict
  with intended behavior, or risky behavior lacks trustworthy evidence. Do not
  trigger merely because implementation is nontrivial or tests need to be run.
---

# Test Strategy

Choose the smallest body of evidence that meaningfully supports the behavior
being changed. Tests are evidence for a contract, not automatic authority over
that contract.

Establish the intended behavior from explicit decisions, project guidance,
public contracts, acceptance criteria, real user scenarios, and deliberate
existing behavior worth preserving.

Choose evidence by risk:

- identify the behavior and plausible failures worth protecting
- inspect relevant evidence that already exists
- use the lowest stable boundary that can prove the behavior
- automate where repeatability buys confidence
- use manual, rendered, or environment-specific checks when they measure the
  result more honestly
- identify which evidence should block completion

Prefer a small number of high-value tests over broad coverage or duplicated
cases. Do not freeze implementation details through private helpers, selectors,
file structure, or excessive mocking.

Remain neutral about when tests are written. Write one first when it clarifies a
stable contract or reproduces a regression; add evidence later when the behavior
is still being discovered.

When a test fails, determine whether it represents a real regression, an
intentional behavior change, implementation-detail coupling, fixture or
environment drift, nondeterminism, an unrelated pre-existing failure, or an
unclear contract before changing either the code or the test.

Passing tests do not prove the implementation is complete. Unrelated failures do
not automatically block it, but they must be separated and reported.

Recommend what to automate, what to verify manually, what not to test, and which
evidence should block the change. Keep the recommendation in conversation unless
Marian asks for an artifact.
