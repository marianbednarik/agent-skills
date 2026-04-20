---
name: hard-cut-policy
description: >
  Enforces a canonical-current-state-only code policy for products with no external installed user base.
  Apply this skill whenever writing, reviewing, or refactoring application code — especially when the task
  involves state management, data loading, persistence, configuration parsing, or any path that could
  plausibly diverge based on "old" vs "new" state shapes. Trigger aggressively: if there's any chance
  a compatibility shim, migration bridge, fallback path, dual-behavior branch, or silent adapter might
  be introduced (even "temporarily"), consult this skill first. Also apply when reviewing diffs for
  cleanup, when a user says "just add a fallback for now", or when deciding whether to delete vs preserve
  old-state handling code.
---

# Hard-Cut Policy

This app has **no external installed user base**. There are no users in the wild running old versions
that need seamless migration. Optimize aggressively for a single, clean, current-state implementation.
Long term maintainability is a core priority. If you add new functionality, first check if there is shared logic that can be extracted to a separate module. Duplicate logic across multiple files is a code smell and should be avoided. Don't be afraid to change existing code. Don't take shortcuts by just adding local logic to solve a problem.

---

## The Core Rule

**One canonical codepath. Full stop.**

Do not introduce — and actively delete — any of the following unless explicitly asked:

- Compatibility bridges or adapters for old local state shapes
- Migration shims (inline or standalone)
- Fallback paths that silently handle legacy formats
- Dual-behavior branches (`if (isOldFormat) ... else ...`)
- "Temporary" second paths left in for convenience
- Compact adapters that paper over a state schema change

---

## Preferred Patterns

| Instead of... | Prefer... |
|---|---|
| Silent fallback to default on bad state | Fail fast with a clear diagnostic |
| Auto-migration on load | Explicit recovery instructions to the user/developer |
| `isLegacy` guard branches | Delete the old path entirely |
| "We'll clean this up later" | Clean it up now, or don't merge it |

---

## When Temporary Compatibility Code Is Justified

Occasionally a narrowly scoped transition or debugging need genuinely requires a second path.
This is the exception, not the norm. If you introduce it anyway, the **same diff must include**:

1. **Why it exists** — what specific transition/debug need requires it
2. **Why the canonical path is insufficient** — what would break without it and why that can't be fixed now
3. **Exact deletion criteria** — the observable condition that means it can be removed (e.g., "after task #123 is complete", "once all dev machines have migrated", "after next deploy")
4. **Tracking reference** — the ADR, ticket, or task that owns its removal

If any of these four items are missing, the code should not be merged.

---

## Default Stance on Existing Compatibility Code

When you encounter old-state compatibility code during refactors or reviews:

> **Delete it. Don't carry it forward.**

If deletion reveals a real problem (e.g., something breaks), that's signal — fix the root cause rather
than reinstating the shim.

---

## Diagnostic Voice

When writing error handling for invalid or unexpected state, prefer explicit over silent:

```
// Good
throw new Error(
  `Unexpected state shape: expected { version: 2, items: [...] }, got ${JSON.stringify(state)}. ` +
  `Clear local storage and reload to reset.`
);

// Bad
const items = state.items ?? state.data?.items ?? [];  // silent compat fallback
```

The goal: a developer (or you, in a future session) should immediately know *what broke*, *why*, and
*what to do about it* — not silently limp along on stale assumptions.

---

## Checklist Before Shipping Code

- [ ] Does this introduce any branch that handles an "old" state shape?
- [ ] Is there any `?? fallback` that exists to paper over a schema mismatch?
- [ ] Is there any code path that only exists for a prior version of the data model?
- [ ] If yes to any of the above: is it explicitly justified with all four required annotations?

If the answer to the last question is no, revert or refactor before proceeding.