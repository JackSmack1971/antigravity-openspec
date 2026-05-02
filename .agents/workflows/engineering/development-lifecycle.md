---
name: development-lifecycle
description: The full agentic development lifecycle from definition to release.
---
# Full Development Lifecycle (Agentic)

## Sequence
The lifecycle follows a deterministic path of specialized skills, each with its own gates:

1. **DEFINE** (`/spec`)
   - Invoke `spec-driven-development` skill.
   - Output: Human-approved `SPEC.md`.

2. **PLAN** (`/plan`)
   - Invoke `planning-and-task-breakdown` skill.
   - Output: `task_plan.md` and atomic tasks.

3. **BUILD** (`/build`)
   - Invoke `incremental-implementation` + `test-driven-development` skills.
   - Output: Functional code passing local tests.

4. **VERIFY** (`/test`)
   - Invoke `verification` skill.
   - Output: Evidence of correctness (logs, screenshots, test results).

5. **REVIEW** (`/review`)
   - Invoke `code-review-and-quality` skill.
   - Output: PR review artifact with 0 critical/fail findings.

6. **SHIP** (`/ship`)
   - Invoke `release-management` skill (chains `/guard`).
   - Output: Pushed code and opened PR.

## Contextual Activation
Skills automatically activate by context through the sequence. The agent must check the current state (e.g., `task_plan.md`) to determine the active phase.
