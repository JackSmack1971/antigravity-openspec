---
name: ship
description: Use when QA is complete to release changes. Requires /guard safety check. Chains /land-and-deploy and /canary.
---
# /ship — Release Workflow

## Source
Derived from: `workflows References Report.md`, Section 1 — Gstack Architecture Workflows, Workflow 3.

## Purpose
Executes the production release sequence: tests → safety gate → push → PR → deploy.
Imposes a **strict dependency on `/guard`** — ship cannot proceed without guard confirmation.
Integrates with `/land-and-deploy` and `/canary` for controlled rollout.

## Trigger Conditions
- `/review` completed (0 CRITICAL, 0 FAIL, all agents confidence ≥ 85)
- `/qa` completed (test suite green, SPEC.md acceptance criteria met)
- User explicitly approves ship

## Hard Dependencies (all must be satisfied before Step 1)
- ✅ `/review` output: PASS
- ✅ `/qa` output: PASS
- ✅ No active `/freeze` (freeze blocks ship unconditionally)

## Workflow Steps

### Step 1 — GUARD Gate
Invoke `/guard` skill → run pre-ship checklist (all 5 gates must pass). HALT if fails.

### Step 2 — SAST Gate
Run `.semgrep.yml` scan (or equivalent). **HALT** if any HIGH/CRITICAL findings are present.

### Step 3 — Full Test Suite
Run the full test suite. **HALT** if any failures occur.

### Step 4 — Fast Review
Run `/review` workflow in fast mode (skip browser QA).

### Step 5 — Release Execution
1. Push: `git push origin <branch>`.
2. PR: `gh pr create --title "<conventional commit>" --body "$(cat .agents/artifacts/actions.md)"`.

### Step 6 — Retrospective (`/retro`)
Chain to `/retro` (MANDATORY: Rule 05). No release is complete without a retrospective.
> Missing `/retro` = INCOMPLETE WORKFLOW. `check-complete.py` enforces this at session close.

## Guardrail Interrupts
- `/freeze` — blocks ship unconditionally until user lifts freeze
- `/guard` denial — ship aborted; blocking reason surfaced to user
- Test failure (Step 1) — hard stop; routes to `/ce-debug`
- Canary degradation — automatic rollback; user notified

## Quality Gates
- [ ] Full test suite green (Step 1) before any push
- [ ] `/review` artifact present and non-stale
- [ ] `/guard` confirmation received from user (not auto-approved)
- [ ] PR body references SPEC.md and review summary
- [ ] `/retro` invoked after ship — no exceptions
- [ ] L0 compliance: GOAL-DRIVEN — acceptance criterion from SPEC.md verified before ship
