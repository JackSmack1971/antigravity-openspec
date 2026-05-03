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
- If `SPEC.md` exists, verify it against `STRATEGY.md` (Step 1) before proceeding.
- `task_plan.md` initialized (see Rule 02).
- If a new project is requested, ensure `using-git-worktrees` (Step 8) handles initialization.

## Workflow Steps

### Step 1 — Strategy + Plan Check
1. Read `STRATEGY.md` if it exists.
2. Read `task_plan.md` if it exists.

### Step 2 — office-hours Diagnostic (`/office-hours`)
Run the `/office-hours` diagnostic (5-question YC frame) to ensure problem/risky-assumption alignment.
> **User Sovereignty Checkpoint #1**: Present reframed problem + highest-leverage action. Wait for explicit approval.

### Step 3 — Feature Proposal
Generate a formal feature proposal based on the diagnostic.
> **User Sovereignty Checkpoint #2**: HALT until proposal is approved.

### Step 4 — Spec (`/spec`)
1. Load `spec-driven-development` skill.
2. Generate `SPEC.md` (6 core areas).
3. Save to repo root.
> **User Sovereignty Checkpoint #3**: Human MUST approve SPEC.md. HALT until approved.

### Step 5 — Engineering Review
Pre-implementation technical deep-dive by eng persona.
```
- Review SPEC.md for: technical feasibility, architecture decisions, data flow
- Identify implementation risks, security constraints, test requirements
- Output: eng review notes appended to findings.md
```

### Step 6 — DX Review
Developer experience validation of API surface, tooling, and docs.
```
- Review proposed interfaces and commands for ergonomics
- Flag usability issues, missing error messages, doc gaps
- Output: DX notes appended to findings.md
```

### Step 7 — Engineering Plan (`/ce-plan`)
Invoke `/ce-plan` to generate `docs/plans/<feature>.md`.
> **User Sovereignty Checkpoint #4**: HALT until eng plan is approved.

### Step 8 — Worktree Setup (`/using-git-worktrees`)
Auto-trigger `/using-git-worktrees` to create an isolated development branch and workspace.
Log: "Plan complete. Branch ready. Awaiting implementation."

### Step 9 — Code Review (`/ce-code-review`)
3-persona parallel quality gate.
```
Invoke /ce-code-review:
- CORRECTNESS sub-agent: logic, off-by-one, null propagation, race conditions
- SECURITY sub-agent: SQL injection, trust boundaries, OWASP Top-10
- MAINTAINABILITY sub-agent: readability, coupling, test coverage gaps
- If any FAIL → route to /ce-debug → fix → re-review
- All PASS (≥85 confidence) → proceed
```

### Step 10 — PR Review (`/review`)
```
Invoke /review:
- Detect branch/plan
- Diff analysis → slop scan → critical checks
- Specialist dispatch (parallel) → fix-first → verification
```

### Step 11 — QA (`/qa`)
```
- Run full test suite
- Validate acceptance criteria from SPEC.md
- Confirm no regressions
```
> **User Sovereignty Checkpoint #5**: QA sign-off required before ship.

### Step 12 — Ship (`/ship`)
```
Invoke /ship:
- Run tests + /guard safety check
- Push branch + open PR
- /land-and-deploy (if applicable)
```

### Step 13 — Retro (`/retro`)
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
