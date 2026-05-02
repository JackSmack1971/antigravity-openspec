---
name: ce-plan
description: Multi-phase planning workflow. Always triggered upon direct invocation to prevent abandonment, iterating through 6 phases.
---
# /ce-plan — Multi-Phase Planning

## Purpose
A multi-phase planning workflow that is always triggered upon direct invocation to prevent abandonment. It iterates through a strict sequence to generate a concrete implementation plan.

## Core Principles
- **Repo-relative paths only:** All references to files must use paths relative to the repository root.
- **Decisions-not-code:** Focus on architectural decisions and data flow, not writing the actual code implementation.
- **Output Artifacts:** Store generated plans in the `docs/plans/` directory.

## Planning Phases
The workflow MUST iterate through these phases sequentially:
1. **Phase 0 (Resume/Source/Scope):** Load context, determine the scope of work, and resume any prior state.
2. **Phase 1 (Context/Research):** Perform necessary repository searches, read required KIs, and gather deep context.
3. **Phase 2 (Questions):** Identify ambiguities and formulate clarifying questions if user input is needed.
4. **Phase 3 (Structure):** Define the architectural structure and module boundaries.
5. **Phase 4 (Write plan):** Write the detailed plan to `docs/plans/`.
6. **Phase 5 (Review/Confidence Check/Handoff):** Perform a final confidence check against `STRATEGY.md` and hand off to `/ce-work` for execution.
