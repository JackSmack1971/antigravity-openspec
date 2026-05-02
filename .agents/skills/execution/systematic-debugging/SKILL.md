---
name: systematic-debugging
description: Use when encountering any bug, test failure, CI failure, unexpected behavior, or production incident. Triggers: error messages, test failures, "it's broken", "something is wrong", "why is X not working". MUST be invoked before ANY fix attempt — do not propose fixes before completing Phase 1.
version: 1.0.0
user-invokable: true
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---
# systematic-debugging

## THE IRON LAW
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST.
Violating this law = symptom patching = guaranteed recurrence.

## Red Flags (mandate return to Phase 1 immediately)
- "Quick fix for now" / "I know what the problem is" / "Just one more change"
- Proposing solution before Phase 1 evidence gathering is complete
- Making multiple simultaneous changes
- Applying fix without first writing a failing test

## 4-Phase Workflow (complete each phase before next — no skipping)

### Phase 1: Root Cause Investigation
Reproduce exactly (minimal repro case). Check recent changes: git log --oneline -10.
Gather evidence: logs, stack traces, instrumentation. Trace data flow backward from symptom.
Use find-polluter.sh for test isolation if test pollution suspected.
Output: root cause documented in findings.md before proceeding.

### Phase 2: Pattern Analysis
Find working baseline example. Compare diff between working and broken.
Map exact change that introduced regression.

### Phase 3: Hypothesis & Testing (Scientific Method)
Form ONE falsifiable hypothesis. Write minimal test BEFORE implementing fix.
Test hypothesis. If disproven: return to Phase 1 with new evidence.

### Phase 4: Implementation
Create failing test first (TDD). Apply single fix at root cause (not symptom).
Verify fix resolves root cause. Add Defense-in-Depth: 4-layer validation.
3+ failed fix attempts → question architecture → escalate to user.

## Defense-in-Depth (Post-Phase 4 Always)
Add 4-layer validation: Entry guards → Business Logic checks → Environment guards → Debug instrumentation.
Replace ALL sleep(N) with waitFor(condition) polling loops (eliminates test flakiness).

## Quality Gates
- [ ] Root cause documented in findings.md BEFORE any code change
- [ ] Single falsifiable hypothesis formed and tested before fix
- [ ] Failing test written BEFORE fix applied
