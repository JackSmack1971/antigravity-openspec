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

## Core Rule: DECISIONS NOT CODE
Capture approach, boundaries, files, dependencies, risks, test scenarios.
Use pseudo-code solely for directional clarity.
Format all file references relative to the repository root.

## 6-Phase Workflow

### Phase 0: Resume / Scope
* Search `docs/plans/` for existing documents; resume if found.
* Clarify scope via AskUserQuestion if ambiguous (one question max).
* Fast-path to Phase 1 if "deepen" intent detected.

### Phase 1: Context & Research
* Read relevant codebase directories.
* Identify patterns and constraints inline (e.g., must match existing state-management approach, strict typing requirements).
* Log discoveries into `findings.md`.

### Phase 2: Clarifying Questions
* Identify unknowns.
* Execute AskUserQuestion (single question, prefer single-select choices).

### Phase 3: Structure
* Define IUs (file-level).
* Map dependencies.
* Identify risks.

### Phase 4: Write Plan
* Generate `docs/plans/<feature-slug>.md` using `resources/plan-template.md`.
* Required sections: Overview, IUs (repo-relative paths), Dependencies, Risks, Test Scenarios, AC.
* Follow formatting in `examples/golden-plan.md`.

### Phase 5: Validate & Handoff (GATE)
* Execute deterministic black-box validation: `python .agents/skills/execution/ce-plan/scripts/validate-plan.py docs/plans/<feature-slug>.md`
* Parse exit code. If CS < 70, return to Phase 1.
* On success: Output "Plan ready. CS: [N]%. Initiating /using-git-worktrees."

## <ki_extraction> Strategy
* Execute `/retro` upon completion.
* Extract novel architecture decisions, constraints, or new patterns encountered into the Knowledge Item (KI) system.
