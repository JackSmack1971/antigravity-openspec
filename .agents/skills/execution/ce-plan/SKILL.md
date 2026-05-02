---
name: ce-plan
description: Use when planning implementation of any multi-step feature, complex refactor, or system change. Triggers: "plan this feature", "create implementation plan", "how do we build X", any feature requiring 3+ implementation steps. Always plan when directly invoked — NEVER classify a direct invocation as not a planning task.
version: 1.0.0
user-invokable: true
allowed-tools: Read, Write, Edit, Bash
---
# ce-plan — Multi-Phase Implementation Planning

## Core Rule: DECISIONS NOT CODE
Plans capture: approach, boundaries, files, dependencies, risks, test scenarios.
Do NOT pre-write implementation code. Pseudo-code only if directional.
All file refs: repo-relative only. NEVER absolute paths.

## 6-Phase Workflow (never classify as "not a planning task" and abandon)

### Phase 0: Resume / Source / Scope
Check docs/plans/ for existing plan — resume if found.
Clarify scope via AskUserQuestion if ambiguous. One question at a time.
If "deepen" intent detected → fast-path to Phase 1 deepening.

### Phase 1: Context & Research
Read relevant codebase dirs. Identify patterns and constraints. Search Layer 1-2 (Rule 00).
Update findings.md with discoveries.

### Phase 2: Clarifying Questions
Identify unknowns. AskUserQuestion — one at a time; prefer single-select choices.

### Phase 3: Structure
Define implementation units (file-level). Map dependencies. Identify risks.

### Phase 4: Write Plan
Write to docs/plans/<feature-slug>.md.
Required sections: Overview, Implementation Units (repo-relative paths), Dependencies, Risks, Test Scenarios, Acceptance Criteria.

### Phase 5: Review & Confidence Check (GATE)
Review plan. Rate confidence 0–100.
confidence < 70 → return to Phase 1 with gap identification. Never handoff with low confidence.
Handoff: "Plan ready. Confidence: [N]%. Initiating /using-git-worktrees."

## Quality Gates
- [ ] All file refs are repo-relative (never absolute)
- [ ] Every implementation unit has acceptance criteria
- [ ] Confidence ≥ 70 before handoff to @apex-engineer
