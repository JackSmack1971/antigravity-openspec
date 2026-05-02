---
name: chain-a-feature-build
description: Full feature build pipeline. Spec → Plan → Isolate → Build → Review → Security → QA → Ship → Retro. Slash command: /chain-a
---
# Chain A: Feature Build Pipeline

## Sequence (invoke in order — no skipping)

### A1: PM Discovery (if product context unclear)
@apex-pm: /chain-d-pm-discovery → OST → approved opportunity → hand off to @apex-planner.
Skip if SPEC.md context already clear.

### A2: Spec Gate: Human Approval
@apex-planner: invoke spec-driven-development skill.
Generate SPEC.md (6 sections). Save to repo root.
GATE: Human approval of SPEC.md required. No Phase A3 without explicit approval.

### A3: Implementation Planning
@apex-planner: invoke ce-plan skill (Phase 0–5).
Output: docs/plans/<feature>.md. Confidence ≥ 70 required.

### A4: Workspace Isolation
@apex-engineer: invoke using-git-worktrees skill.
Worktree created, gitignored, baseline tests confirmed passing.

### A5: TDD Implementation
@apex-engineer: build in worktree. TDD: failing test first, then implementation.
React code: react-best-practices skill active (CRITICAL rules first).
2-action rule active: progress.md updated every 2 tool ops.

### A6: Code Review Gate Gate: STRICT_MODE
@apex-reviewer: /ce-code-review — 3-persona parallel.
All 3 personas: verdict=PASS, confidence ≥ 85, zero slop.
FAIL → @apex-engineer + /chain-c-debug loop. Max 3 review iterations.

### A7: Security Gate Gate: STRICT_MODE
@apex-security-officer: /chain-b full run.
STRIDE + Attack Tree + Mitigations (score ≥ 0.8) + SAST CI/CD committed.
HOLD if any artifact incomplete.

### A8: Browser QA
@apex-reviewer: invoke agent-browser skill on staging URL.
Snapshot → interact → verify acceptance criteria from SPEC.md.
Bug found → /chain-c-debug → return to A8.

### A9: Ship Gate: STRICT_MODE
/guard confirmation before git push / merge to main.
GitHub MCP: create PR with description linking SPEC.md + plan + review findings.

### A10: Retro (mandatory)
/retro → KNOWLEDGE SUBAGENT → KI extraction → promote to .agents/knowledge/.

## Success Criteria
SPEC.md approved + all acceptance criteria verified + PR created + /retro KI extracted.

## Failure Handling
Any gate failure → log in task_plan.md. 3-strike → HALT + user escalation.
