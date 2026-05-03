---
name: autoplan
description: Use when a new feature or complex task is requested. Triggers the full Power-Chain A sprint pipeline.
---
# /autoplan — Full Sprint Pipeline (Chain A)

## Source
Derived from: `workflows References Report.md`, Section 1 — Gstack Architecture Workflows, Workflow 1.
Cross-ref: `Vertical Stack Analysis.md` § Power-Chains, Chain A.

## Purpose
Orchestrates the complete feature build sprint from CEO review through ship and retrospective.
Chains multiple specialist roles with mandatory user sovereignty checkpoints between phases.
Agent MUST NOT skip phases or merge checkpoints under time pressure.

## Trigger Conditions
- New feature request received
- Complex task requiring multi-phase coordination
- User invokes `/autoplan` explicitly

## Prerequisite
- `SPEC.md` does NOT yet exist for this feature (if it does, start at Step 3)
- `task_plan.md` initialized (see Rule 02)

## Workflow Steps

### Step 1 — CEO Review (`/plan-ceo-review`)
Strategic framing before any engineering begins.
```
Invoke /plan-ceo-review:
- Define: target problem, success metric, user impact, strategic fit
- Output: CEO-approved STRATEGY.md or brief framing doc
```
> **User Sovereignty Checkpoint #1**: Present strategy summary. Wait for explicit approval before proceeding.

### Step 2 — Design Review
Validate UI/UX and architecture approach before committing to implementation path.
```
- Review proposed design/architecture for: feasibility, constraints, edge cases
- Identify dependencies and integration risks
- Output: design decisions documented in task_plan.md Phase 1
```
> **User Sovereignty Checkpoint #2**: Confirm design direction. No coding until approved.

### Step 3 — Spec (`/spec`)
Generate the 6-area specification document.
```
Invoke /spec:
1. Clarify objective, features, tech stack, boundaries
2. Generate SPEC.md (6 areas: objective, commands, structure, style, testing, boundaries)
3. Save to repo root
4. Human reviews + approves SPEC.md
```
> **User Sovereignty Checkpoint #3**: Human MUST approve SPEC.md. Gate is mandatory.

### Step 4 — Engineering Review
Pre-implementation technical deep-dive by eng persona.
```
- Review SPEC.md for: technical feasibility, architecture decisions, data flow
- Identify implementation risks, security constraints, test requirements
- Output: eng review notes appended to findings.md
```

### Step 5 — DX Review
Developer experience validation of API surface, tooling, and docs.
```
- Review proposed interfaces and commands for ergonomics
- Flag usability issues, missing error messages, doc gaps
- Output: DX notes appended to findings.md
```

### Step 6 — Implementation (`/ce-plan` → build)
```
Invoke /ce-plan (Phases 0–5):
- Phase 0: Resume/Source/Scope
- Phase 1: Context/Research
- Phase 2: Questions
- Phase 3: Structure
- Phase 4: Write plan to docs/plans/
- Phase 5: Review/Confidence Check/Handoff

Then: invoke /using-git-worktrees (workspace isolation)
Then: incremental implementation with TDD
```

### Step 7 — Code Review (`/ce-code-review`)
3-persona parallel quality gate.
```
Invoke /ce-code-review:
- CORRECTNESS sub-agent: logic, off-by-one, null propagation, race conditions
- SECURITY sub-agent: SQL injection, trust boundaries, OWASP Top-10
- MAINTAINABILITY sub-agent: readability, coupling, test coverage gaps
- If any FAIL → route to /ce-debug → fix → re-review
- All PASS (≥85 confidence) → proceed
```

### Step 8 — PR Review (`/review`)
```
Invoke /review:
- Detect branch/plan
- Diff analysis → slop scan → critical checks
- Specialist dispatch (parallel) → fix-first → verification
```

### Step 9 — QA (`/qa`)
```
- Run full test suite
- Validate acceptance criteria from SPEC.md
- Confirm no regressions
```
> **User Sovereignty Checkpoint #4**: QA sign-off required before ship.

### Step 10 — Ship (`/ship`)
```
Invoke /ship:
- Run tests + /guard safety check
- Push branch + open PR
- /land-and-deploy (if applicable)
```

### Step 11 — Retro (`/retro`)
```
Invoke /retro (MANDATORY — Rule 05 enforces this):
- Extract KI deltas (Pitfall | Playbook | Context | Reference)
- Write to knowledge/ store
```

## Guardrail Interrupts
- `/freeze` — halts entire pipeline; requires explicit user resume
- `/guard` — safety confirmation gate (required before any push/deploy)
- 3-Strike Escalation — if 3+ failures in any step, HALT and surface to user

## Quality Gates
- [ ] CEO/strategy review completed before spec
- [ ] SPEC.md human-approved before implementation
- [ ] `/ce-code-review` all personas PASS (≥85 confidence)
- [ ] `/guard` executed before push
- [ ] `/retro` chained after `/ship` — no exceptions (Rule 05)
- [ ] L0 compliance: THINK BEFORE CODING — intent in comments before any implementation
