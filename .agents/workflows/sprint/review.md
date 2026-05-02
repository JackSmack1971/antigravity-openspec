---
name: review
description: Use for PR review and final verification before ship. Triggered on any branch containing changes.
---
# /review — PR Review + Fix Loop

## Source
Derived from: `workflows References Report.md`, Section 1 — Gstack Architecture Workflows, Workflow 2.

## Purpose
Systematic PR review pipeline with parallel specialist dispatch and fix-first resolution.
Maintains strict dependency on `/browse` skill for contextual memory retrieval.
Every step must produce evidence before the next step begins (Rule: verification evidence required).

## Trigger Conditions
- Any branch containing changes awaiting review
- Post-implementation gate before `/ship`
- Explicitly invoked by `/autoplan` pipeline at Step 8
- User invokes `/review` directly on a branch

## Dependency
- **Required**: `/browse` skill loaded for contextual memory retrieval (plan/spec cross-reference)
- **Required**: Branch must exist and be diffable against base

## Workflow Steps

### Step 1 — Detect Branch + Plan
```
- Identify current branch name and base branch
- Load task_plan.md → read active phase + acceptance criteria
- Load SPEC.md → read verification evidence requirements
- Cross-reference: does the diff address SPEC.md objectives?
```
> If `task_plan.md` missing: invoke restore-context before proceeding.

### Step 2 — Diff Analysis
```
- Run: git diff <base>..<branch> --stat        # summary
- Run: git diff <base>..<branch>               # full diff
- Categorize changes: feature / fix / refactor / test / docs / config
- Flag: any unexpected files in diff (scope creep signal)
```

### Step 3 — Slop Scan
```
Scan for low-quality patterns:
- Placeholder text left in code (TODO without ticket, FIXME, HACK)
- Debug artifacts (console.log, print(), debugger, breakpoints)
- Dead code (unreachable branches, unused imports)
- Hard-coded values that should be config
- Missing error handling on IO/network calls
```
> Any slop found → log to findings.md → route to fix-first (Step 6).

### Step 4 — Critical Checks (SQL + Trust Boundaries)
```
Security-critical inspection:
- SQL injection surface: raw string interpolation in queries
- Trust boundary violations: user input reaching privileged ops without validation
- Hardcoded credentials, tokens, API keys in diff
- Unescaped output (XSS vectors)
- Missing auth/authz on new endpoints
- Unsafe deserialization patterns
```
> Any CRITICAL finding → **HALT** → present to user immediately (User Sovereignty).

### Step 5 — Specialist Dispatch (Parallel Agents)
```
//parallel — invoke three specialist sub-agents simultaneously:

[CORRECTNESS agent]
- Mental execution of changed code paths
- Off-by-one errors, null propagation, race conditions
- Logic correctness vs. SPEC.md acceptance criteria
- Returns: {verdict: PASS|FAIL|WARN, confidence: 0-100, findings: []}

[SECURITY agent]
- OWASP Top-10 scan on changed surface
- STRIDE threat model on new trust boundaries
- Returns: {verdict: PASS|FAIL|WARN, confidence: 0-100, findings: []}

[MAINTAINABILITY agent]
- Readability, coupling, cohesion
- Test coverage gaps vs. changed lines
- Documentation completeness
- Returns: {verdict: PASS|FAIL|WARN, confidence: 0-100, findings: []}
```
> Deduplicate overlapping findings across the three agents before Step 6.

### Step 6 — Fix-First (Auto or Ask)
```
For each finding (sorted: CRITICAL → FAIL → WARN):
  IF fix is unambiguous + non-destructive:
    → auto-apply surgical fix
    → log to progress.md: "Auto-fixed: [finding ID] — [change summary]"
  ELSE IF fix requires design decision:
    → present options to user (AskUserQuestion)
    → wait for explicit choice before applying
  NEVER apply ambiguous fixes silently
```
> Re-run Steps 3–4 after fixes to confirm resolution.

### Step 7 — Verification
```
- Confirm all CRITICAL and FAIL findings resolved
- Run test suite: confirm no regressions introduced
- Validate diff scope: no unintended files changed
- Confirm SPEC.md acceptance criteria met
- Generate review summary:
  {files_changed, lines_added, lines_removed, findings_fixed, warnings_remaining}
```
> Hand off to `/qa` → `/ship` only when: 0 CRITICAL, 0 FAIL, confidence ≥ 85 on all agents.

## Quality Gates
- [ ] `/browse` skill loaded before Step 1 (contextual memory active)
- [ ] SPEC.md and task_plan.md consulted in Step 1
- [ ] All CRITICAL findings presented to user before auto-fixing anything
- [ ] Parallel specialist dispatch completed (3 agents, all returned)
- [ ] Fix-First loop ran to zero CRITICAL + FAIL
- [ ] Final test suite green before handoff
- [ ] L0 compliance: SURGICAL EDITS — fix only what review surfaces, zero opportunistic refactoring
