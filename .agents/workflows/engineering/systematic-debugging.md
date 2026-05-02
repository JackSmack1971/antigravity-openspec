---
name: systematic-debugging
description: Triggered by bug reports. A strict diagnostic mechanism preventing unverified patching (4-Phase Debugging Procedure).
---
# /systematic-debugging — Systematic Debugging (Chain C)

## THE IRON LAW
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST.
Violating this law = symptom patching = guaranteed recurrence.

## Workflow Execution (4-Phase Debugging Procedure)

### Phase 1: Root Cause Investigation
1. **Pitfall Audit:** Check `.agents/knowledge/pitfalls/` for known issues related to the current symptom.
2. **Repro:** Reproduce exactly (minimal repro case). Do not write any fix code yet.
3. **Trace:** Execute the Backward Root-Cause Tracing sequence to find the original trigger.

### Phase 2: Pattern Analysis
1. Find a working baseline example if available.
2. Compare diff between working and broken to identify failure patterns.
3. Document root cause and patterns in `findings.md` BEFORE proceeding.

### Phase 3: Hypothesis and Testing
1. Form ONE falsifiable hypothesis about why the root cause occurred.
2. Write a minimal failing test BEFORE implementing a fix (Test-Driven Debugging).

### Phase 4: Implementation
1. Apply a single fix at the determined root cause (not the symptom).
2. Verify the fix resolves the root cause and passes the newly written test.
3. **Architectural Trigger:** 3+ failed fix attempts MUST trigger an architectural query and escalate to the user.

## Post-Execution
- Apply Defense-in-Depth Validation.
- Proceed to `/ce-code-review`.

