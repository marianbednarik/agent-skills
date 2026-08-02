Build code that a human maintainer would be happy to inherit, and scale the
effort to the task.

Treat these as personal defaults, not project law. Project and nested
`AGENTS.md` files, project documentation, tests, and coherent existing patterns
take precedence. For nontrivial work, read only the project context relevant to
the task.

- Prefer one coherent owner, canonical shape, and implementation path over
  parallel patterns or scattered local logic.
- Model real concepts at their owning boundary. Avoid speculative abstractions,
  shallow wrappers, and indirection that does not reduce meaningful change cost.
- Keep deterministic system behavior in code. Normalize untrusted data at
  external boundaries rather than carrying uncertainty through the system.
- Do not add compatibility shims, silent fallbacks, dual paths, or migration
  branches unless compatibility or rollout is part of the actual requirement.
- Reuse coherent project primitives, but do not preserve a weak pattern merely
  because it already exists.
- Delete code and paths made obsolete by the change when their obsolescence is
  supported by the project direction, implementation, or tests.
- Favor direct solutions for prototypes and small tasks. Do not harden
  throwaway work prematurely.
- Verify the behavior that matters through the most useful available evidence.
  State important gaps when something could not be verified.
