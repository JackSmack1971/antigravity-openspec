---
name: ce-plan
description: Multi-Phase Implementation Planner. Use for multi-step features, complex refactors, or system changes (3+ steps). Triggers: /ce-plan, "plan this feature", "create implementation plan", "how do we build X".
version: 2.0.0
user-invokable: true
allowed-tools: Read, Write, Edit, Bash
---
# ce-plan — Multi-Phase Implementation Planning

## Abbreviations (N-Grams)
* **IU**: Implementation Unit
* **AC**: Acceptance Criteria
* **CS**: Confidence Score
* **DP**: Discovery Plan

## Core Rules
- **DECISIONS NOT CODE**: Plan documents architectural decisions and boundaries, not implementation code.
- **Always Plan When Invoked**: NEVER skip Phases 0-3 when this skill is triggered.
- **Repo-Relative Paths ONLY**: All file references MUST be relative to the repository root (Rule 11).
- **Output Storage**: All plans MUST be stored in `docs/plans/` (created if missing).

## 6-Phase Workflow

### Phase 0: Resume / Scope
* Search `docs/plans/` for existing documents; resume if found.
* Read `task_plan.md` if it exists; if not, initialize with a clear goal statement.
* Clarify scope via AskUserQuestion if ambiguous (one question max).

### Phase 1: Context & Research
* Read relevant codebase directories and identify patterns.
* Check `.agents/knowledge/` for applicable Knowledge Items (KIs).
* Log discoveries into `findings.md`.

### Phase 2: Clarifying Questions
* Identify unknowns and surface 3-5 specific ambiguities.
* Present to user and await answers via AskUserQuestion.

### Phase 3: Structure
* Define component breakdown (using repo-relative file paths ONLY — Rule 11).
* Map dependencies and define interfaces between components.

### Phase 4: Write Plan
* Generate `docs/plans/<feature-slug>.md` with: Goal, Phases, File List, and Acceptance Criteria.
* Follow formatting in `examples/golden-plan.md`.

### Phase 5: Review & Approval (GATE)
* Present the generated plan to the user.
* GATE on explicit user approval before proceeding to any code generation.

## <ki_extraction> Strategy
* Execute `/retro` upon completion.
* Extract novel architecture decisions, constraints, or new patterns encountered into the Knowledge Item (KI) system.
