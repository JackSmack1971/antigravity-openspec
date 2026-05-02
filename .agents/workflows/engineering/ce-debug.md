---
name: ce-debug
description: Triggered by bug reports. Executes: Reproduce failures → trace root cause → form/testable hypotheses → implement test-first fixes.
---
# /ce-debug — Systematic Debugging (Chain C)

## THE IRON LAW
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST.
Violating this law = symptom patching = guaranteed recurrence.

## Workflow Execution (Triggered by bug reports or test failures)

### Phase 1: Reproduce Failures
1. **Pitfall Audit:** Check `.agents/knowledge/pitfalls/` for known issues related to the current symptom.
2. **Repro:** Reproduce exactly (minimal repro case). Do not write any fix code yet.

### Phase 2: Trace Root Cause
1. Find working baseline example if available. Compare diff between working and broken.
2. Trace root cause. Gather evidence (logs, stack traces, instrumentation).
3. Document root cause in `findings.md` BEFORE proceeding.

### Phase 3: Form Testable Hypotheses
1. Form ONE falsifiable hypothesis about why the root cause occurred.
2. Write a minimal failing test BEFORE implementing a fix (Test-Driven Debugging).

### Phase 4: Implement Test-First Fixes
1. Apply single fix at the determined root cause (not the symptom).
2. Verify fix resolves the root cause and passes the newly written test.
3. 3+ failed fix attempts → question architecture → escalate to user.

## Defense-in-Depth
- Add 4-layer validation: Entry guards → Business Logic checks → Environment guards → Debug instrumentation.
- Condition-based-waiting: Replace ALL `sleep(N)` with `waitFor(condition)` polling loops to eliminate test flakiness.

## Post-Execution
- Proceed to `/ce-code-review`.
