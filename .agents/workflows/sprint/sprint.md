---
name: sprint
description: Use to understand or enforce the overall sprint lifecycle. The canonical Think-Plan-Build-Review-Test-Ship-Reflect loop. Guardrails /freeze and /guard can interrupt any phase.
---
# /sprint — Overall Sprint Lifecycle (Think-Plan-Build-Review-Test-Ship-Reflect)

## Source
Derived from: `workflows References Report.md`, Section 1 — Gstack Architecture Workflows, Workflow 4.
Cross-ref: `Vertical Stack Analysis.md` § Power-Chains (all 5 chains), Chain A (Feature Build).

## Purpose
The canonical top-level sprint governance model. Defines the mandatory phase sequence for any
non-trivial feature, enforced via routing rules in AGENTS.md. Each phase maps to a registered
workflow or guardrail command. No phase can be re-ordered or skipped.

## Sprint Phase Map

```
[THINK]          [PLAN]              [BUILD]           [REVIEW]
/office-hours → /plan-ceo-review → /spec + /ce-plan → implementation
     ↓
[TEST]           [SHIP]              [REFLECT]
/qa           → /ship              → /retro
```

## Detailed Phase Sequence

### Phase 1 — THINK: `/office-hours`
```
Trigger: user brings a product problem, user request, or opportunity
Purpose: unstructured exploration + framing before committing to a plan

- Discuss the problem space openly
- Identify: core user pain, strategic fit, rough scope
- Output: problem statement + initial framing (informal, not a plan yet)
- If PM-discovery needed: chain to /discover → opportunity-solution-tree
```
> Not a planning session — no commitments, no spec. Pure thinking.

### Phase 2 — PLAN: `/plan-ceo-review`
```
Trigger: office-hours outputs a clear problem statement
Purpose: CEO/strategy review to align on approach before engineering begins

- Define: target problem, success metric, user impact, resource estimate
- Review: strategic fit, priority vs. backlog, risk assessment
- Output: approved STRATEGY.md or framing brief
- Gate: User Sovereignty Checkpoint — explicit approval required
```
> No engineering begins until this gate passes.

### Phase 3 — PLAN: `/spec` + `/ce-plan`
```
/spec:
- Generate 6-area SPEC.md (objective, commands, structure, style, testing, boundaries)
- Human reviews + approves — MANDATORY gate (Rule 01)

/ce-plan (Phases 0–5):
- Multi-phase implementation planning
- Output: implementation plan in docs/plans/
- Includes: component breakdown, dependencies, acceptance criteria
```

### Phase 4 — BUILD: Implementation
```
- Invoke /using-git-worktrees (workspace isolation on dedicated branch)
- Incremental implementation following SPEC.md
- TDD: write failing tests first, implement to pass, refactor
- 2-Action Rule: update progress.md every 2 tool operations (Rule 02)
- If blocked 3+ times: invoke 3-Strike escalation (Rule 00)
```

### Phase 5 — REVIEW: `/review`
```
Invoke /review:
- Detect branch + load plan context (/browse dependency)
- Diff analysis → slop scan → critical checks (SQL, trust boundaries)
- Parallel specialist dispatch: CORRECTNESS + SECURITY + MAINTAINABILITY agents
- Fix-First loop (auto or ask)
- Verification: 0 CRITICAL, 0 FAIL, confidence ≥ 85
```

### Phase 6 — TEST: `/qa`
```
- Full test suite run
- Validate all SPEC.md acceptance criteria
- Confirm no regressions from fix-first loop
- Output: QA sign-off artifact
- Gate: User Sovereignty Checkpoint — QA approval before ship
```

### Phase 7 — SHIP: `/ship`
```
Invoke /ship:
- Final test run
- /review confirmation (non-stale)
- /guard safety check (MANDATORY human gate)
- Push branch + open PR
- /land-and-deploy (if applicable)
- /canary rollout (if high-risk)
```

### Phase 8 — REFLECT: `/retro`
```
Invoke /retro (MANDATORY — Rule 05 enforces — check-complete.py monitors):
- Compare plan vs. implementation → identify deltas
- Classify: Pitfall | Playbook | Context | Reference
- KNOWLEDGE SUBAGENT: distill → write to knowledge/ store
- Quality gate: actionability + uniqueness + density ≥ 0.8
- Output: "KI extracted: [title] | Type: [type] | Trace: [6-char ID]"
```

## Guardrail Interrupts (can interrupt ANY phase)

| Guardrail | Effect | Resume Condition |
|-----------|--------|-----------------|
| `/freeze` | Halts entire pipeline immediately | Explicit user `/unfreeze` command |
| `/guard` | Safety confirmation gate (required at ship) | User confirms: "yes" |
| 3-Strike Escalation | Halts current phase; surfaces to user | User provides direction |
| `/careful` | Adds review layer to next destructive op | Cleared after single op |

## Phase Gating Summary

| Gate | Phase | Who Approves |
|------|-------|-------------|
| Strategy approval | After PLAN (CEO review) | User |
| SPEC.md approval | After PLAN (/spec) | User (Rule 01) |
| QA sign-off | After TEST | User |
| /guard confirmation | At SHIP | User (mandatory) |
| /retro completion | After SHIP | Automated (check-complete.py) |

## Quality Gates
- [ ] Every phase executed in order — no skipping
- [ ] All User Sovereignty Checkpoints received explicit approval
- [ ] `/freeze` state checked at each phase boundary
- [ ] `/retro` invoked after `/ship` — monitored by `check-complete.py`
- [ ] L0 compliance: GOAL-DRIVEN — SPEC.md acceptance criteria verified before SHIP phase
