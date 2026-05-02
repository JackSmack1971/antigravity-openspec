---
name: spec-driven-development
description: Use when starting any new feature, significant codebase change, or when asked to implement something without clear written requirements. Triggers: "build X", "implement Y", "add Z", new project kickoff, implicit or assumed requirements detected in task description.
version: 1.0.0
user-invokable: true
allowed-tools: Read, Write, Edit
---
# spec-driven-development

## Core Principle
Code without a spec is guessing. SPEC.md is the single source of truth before any implementation.

## 4-Phase Gated Workflow

### Phase 1: Specify (GATE: Human Approval)
Create SPEC.md with all 6 sections:
1. Objective + measurable success criteria (numbers, not feelings)
2. Features + user stories (Given [context] / When [action] / Then [outcome])
3. Tech stack + explicit dependency versions
4. Architecture decisions + alternatives considered + rationale
5. Boundaries: Always do / Ask-first / Never do
6. Verification: test acceptance criteria + evidence format (screenshot / test output / etc.)

GATE: Human MUST review and approve SPEC.md. NO Phase 2 without approval.

### Phase 2: Plan (GATE: Human Review)
Decompose spec → components + dependencies.
Identify risks. Map to existing codebase patterns.
GATE: Human reviews plan before Phase 3.

### Phase 3: Tasks
Convert plan → atomic tasks. Each task: acceptance criteria + verification method.
Commit tasks.md to repo.

### Phase 4: Implement
Execute via @apex-engineer. TDD. Incremental. 2-action rule active.

## Anti-Rationalization Table
| Rationalization | Reality | Correct Action |
|---|---|---|
| "Simple task, no spec needed" | Simple ≠ no spec | Write minimal SPEC.md |
| "Requirements are obvious" | Implicit = future bugs | Externalize all assumptions |
| "Spec will change" | Write current-best-known | Delta via ADDED/MODIFIED/REMOVED |

## Quality Gates
- [ ] SPEC.md exists and human-approved before any code written
- [ ] All 6 sections present with verifiable criteria
- [ ] Specification enforces L0 Foundational Rules (THINK BEFORE CODING, GOAL-DRIVEN)
