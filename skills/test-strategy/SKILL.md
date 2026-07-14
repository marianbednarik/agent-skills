---
name: test-strategy
description: >
  Decide what evidence should protect behavior when the appropriate test level,
  coverage, or authority is not obvious. Use when the user asks what or how to
  test, automated and manual checks have meaningful tradeoffs, existing tests
  conflict with intended behavior, failures have ambiguous causes, or risky
  behavior lacks trustworthy evidence. Do not trigger merely because a change is
  nontrivial or tests need to be run.
---

# Test Strategy

Choose evidence that meaningfully supports the behavior being changed. Do not
treat “write tests” or test-driven development as automatic answers.

Establish the intended behavior contract from explicit user decisions,
authoritative project guidance, public or external contracts, acceptance
criteria, real user scenarios, and deliberate existing behavior that should be
preserved. Tests are executable evidence for parts of that contract; their
existence does not make every assertion permanently correct.

Choose evidence by risk:

- identify the behavior and plausible failure modes worth protecting
- inspect the relevant evidence that already exists
- select the lowest durable boundary that can prove the behavior
- add automation only where it buys repeatable confidence
- use manual, rendered, or environment-specific checks when they measure the
  result more meaningfully
- identify what must pass before the change is ready

Prefer a small number of high-value tests through public interfaces or meaningful
boundaries. One vertical tracer test can be enough to establish confidence before
adding cases for distinct risks. Do not add coverage merely to exercise lines or
freeze the current implementation shape.

Remain workflow-neutral:

- write a test first when it clarifies a stable contract or reproduces a regression
- add tests during or after implementation when the behavior is still being
  discovered
- use manual checks when automation would be brittle, misleading, or
  disproportionately expensive
- combine automated and manual evidence when they prove different aspects of the
  result

Avoid tests dominated by mocks, selectors, private helpers, file structure, or
other implementation details.

When a test fails, classify it before changing code or the test:

- **real regression:** fix the implementation
- **intentional behavior change:** update or remove the expectation with an
  explanation
- **implementation-detail coupling:** rewrite the test around public behavior
- **fixture or environment drift:** repair the setup rather than product code
- **flaky or nondeterministic behavior:** reproduce and isolate it; do not dismiss
  it because a retry passes
- **pre-existing unrelated failure:** establish that it is outside the change and
  report it
- **unclear contract:** obtain clarification before changing either side when the
  decision is consequential

A failure should block readiness when it shows requested behavior is broken,
preserved behavior regressed, a relevant contract no longer holds, or a risky
change lacks trustworthy evidence. An unrelated pre-existing failure need not
block the change, but it must be separated and reported. Passing tests are
evidence, not proof that the implementation is complete.

End with a concise recommendation covering what to automate, what to verify
manually, what not to test, and which evidence or failures should block the
change.
