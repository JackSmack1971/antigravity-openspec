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

### Step 1 — Final Test Run
```bash
# Run the full test suite one final time on the ship-ready branch
# Purpose: catch any last-minute regressions from fix-first loop
<run project test command>
```
> If tests fail: **HALT** — route back to `/review` → `/ce-debug`. Do NOT proceed.

### Step 2 — `/review` Confirmation
```
- Confirm /review summary artifact exists (from prior step)
- Confirm: 0 CRITICAL findings, 0 FAIL findings
- Confirm: all 3 specialist agents returned PASS with confidence ≥ 85
- If review is stale (> since last commit): re-run /review before proceeding
```
> Stale review = no ship. Always review against final diff state.

### Step 3 — `/guard` Safety Check (MANDATORY)
```
Invoke /guard:
- Surface to user: {branch, files_changed, lines_changed, PR target}
- Display: destructive ops in diff (deletes, schema migrations, env changes)
- Require explicit user confirmation: "Confirm ship? [yes/no]"
- If NO: abort — return to user with blocking reason
- If YES: proceed to Step 4
```
> **User Sovereignty Checkpoint**: `/guard` is the final human gate before any push.
> This step CANNOT be skipped, auto-approved, or rationalized away under time pressure.

### Step 4 — Push Branch
```bash
git push origin <branch-name>
```
> Only after `/guard` confirmation. Never force-push without explicit user instruction + `/guard`.

### Step 5 — Open Pull Request
```
- Create PR: {title from SPEC.md objective, body from review summary + SPEC.md}
- Assign reviewers (if team context available)
- Link: SPEC.md, task_plan.md, review summary artifact
- Label: feature | fix | security | chore (match change type)
```

### Step 6 — `/land-and-deploy` (if applicable)
```
Invoke /land-and-deploy when:
- Auto-merge is configured AND PR checks pass
- OR user explicitly requests immediate deploy after merge

Sequence:
- Merge PR (squash preferred for feature branches)
- Trigger deploy pipeline
- Monitor deploy status until: success | failure
- If failure: /canary rollback or alert user
```

### Step 7 — `/canary` (if applicable)
```
Invoke /canary for staged rollout when:
- Change is high-risk (schema migration, new infra, breaking API change)
- User requests progressive traffic shifting

Sequence:
- Deploy to canary slice (e.g., 5% traffic)
- Monitor error rate + latency for canary window
- If healthy: promote to 100%
- If degraded: rollback canary → surface alert to user
```

### Step 8 — `/retro` (MANDATORY — Rule 05)
```
Invoke /retro immediately after successful ship:
- Extract KI deltas (Pitfall | Playbook | Context | Reference)
- Write to knowledge/ store
- Log: "Retro complete: [KI count] KIs extracted | Trace: [6-char ID]"
```
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
