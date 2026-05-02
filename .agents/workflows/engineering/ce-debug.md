---
name: ce-debug
description: Use for systematic debugging of reported bugs or test failures.
---
# /ce-debug — Systematic Debugging (Chain C)

## THE IRON LAW
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST.
Violating this law = symptom patching = guaranteed recurrence.

## 4-Phase Workflow (complete each phase before next — no skipping)

### Phase 1: Root Cause Investigation
1. **Pitfall Audit:** Check `.agents/knowledge/pitfalls/` for known issues related to the current symptom.
2. Reproduce exactly (minimal repro case).
3. Trace root cause. Gather evidence (logs, stack traces, instrumentation).
4. Document root cause in `findings.md` BEFORE proceeding.

### Phase 2: Pattern Analysis
1. Find working baseline example. Compare diff between working and broken.
2. Map exact change that introduced regression.

### Phase 3: Hypothesis & Testing
1. Form ONE falsifiable hypothesis.
2. Write minimal test BEFORE implementing fix.

### Phase 4: Implementation
1. Apply single fix at root cause (not symptom).
2. Verify fix resolves root cause.
3. 3+ failed fix attempts → question architecture → escalate to user.

## Defense-in-Depth
- Add 4-layer validation: Entry guards → Business Logic checks → Environment guards → Debug instrumentation.
- Condition-based-waiting: Replace ALL `sleep(N)` with `waitFor(condition)` polling loops to eliminate test flakiness.

## Post-Execution
- Proceed to `/ce-code-review`.
