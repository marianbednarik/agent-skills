---
name: test-strategy
description: >
  Decide what should be tested for a change and how much authority those tests
  should have. Use when planning or reviewing non-trivial behavior, choosing
  between automated tests and manual checks, handling failing tests, or avoiding
  useless implementation-detail coverage.
---

# Test Strategy

Decide how tests should support a change. Do not treat "write tests" as the automatic answer.

The behavior contract is the source of truth. Tests are executable witnesses for parts of that contract. If a test conflicts with the agreed behavior, classify the mismatch before changing code.

Before or during implementation, propose:

- the behavior contract worth protecting
- existing tests that should be trusted
- existing tests that may need updates because behavior intentionally changes
- new tests worth adding, if any
- what level to test at: integration, public API, UI flow, boundary/parser, state machine, or manual check
- what not to test because it would couple to implementation details

Prefer a tracer-bullet test when behavior is clear and important: one meaningful behavior through a public interface, then grow coverage only where it buys confidence.

Avoid tests that mostly verify mocks, selectors, private helpers, current file structure, or implementation shape.

When tests fail, classify before fixing:

- real regression: fix code
- intended behavior changed: update or remove the test with explanation
- implementation-detail coupling: rewrite the test around public behavior
- test setup drift: fix fixture/setup
- unclear contract: ask the user before changing code or test

End with a short recommendation: what to test, what to skip, what to run manually, and which failures should block the change.
