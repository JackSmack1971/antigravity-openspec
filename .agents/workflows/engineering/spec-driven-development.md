---
name: spec-driven-development
description: Spec-driven gated workflow for tracking a living document through project phases.
---
# Spec-Driven Gated Workflow

## Internal Pipeline
This workflow tracks a living document and enforces human review at each critical pivot.

### Phase 1: Specify
- Define assumptions and project scope.
- Generate 6-area specification (`SPEC.md`).
- **Gate**: Human review and approval required.

### Phase 2: Plan
- Break down `SPEC.md` into components and dependencies.
- Define architectural constraints.
- **Gate**: Human review of the implementation plan required.

### Phase 3: Tasks
- Generate atomic tasks with explicit acceptance and verification criteria.
- Maintain `task_plan.md` as the source of truth.
- **Gate**: Check-off tasks only after evidence is provided.

### Phase 4: Implement
- Execute implementation via incremental builds and TDD.
- Enforce the 2-Action Rule for status updates.
- Commit frequently to the repository.

## Triggers
- Triggered on any new project or significant feature request.
- Update `SPEC.md` immediately if scope changes.
