---
name: chain-c-debug
description: Root-cause-first debug and patch pipeline. Iron Law enforced: no fix without root cause. Slash command: /chain-c or /ce-debug
---
# Chain C: Debug & Patch Pipeline

## Constitutional Entry Rule
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST.
Any attempt to skip to fix before Phase C1 completion → HALT + restart from C1.
"I know what the problem is" = red flag. Verify before acting.

## Sequence

### C1: Root Cause Investigation (systematic-debugging Phase 1)
@apex-engineer: invoke systematic-debugging skill.
Reproduce bug exactly (minimal repro case).
git log --oneline -10 → identify recent changes.
Gather: logs + stack traces + instrumentation output.
Trace data flow / call stack backward from symptom.
Use find-polluter.sh for test pollution isolation if needed.
Output: root cause documented in findings.md. MANDATORY before C2.

### C2: Pattern Analysis (systematic-debugging Phase 2)
Find working baseline. Compare diff between working and broken.
Map exact regression point.

### C3: Hypothesis & Test (Scientific Method)
Form ONE falsifiable hypothesis.
Write FAILING TEST for hypothesis before any code change.
Run test: if disproven → return to C1 with new evidence.

### C4: Fix Implementation (systematic-debugging Phase 4)
TDD: failing test already written → implement minimal fix at ROOT CAUSE.
Apply single change. Verify fix resolves root cause + all tests pass.
Defense-in-Depth: add 4-layer validation (Entry → Logic → Env → Debug).
Replace sleep() with waitFor(condition) throughout affected test files.
3+ failed attempts → HALT → escalate to user with: root cause + attempts + recommendation.

### C5: Fix Review Gate: STRICT_MODE
@apex-reviewer: /ce-code-review on fix diff.
CORRECTNESS sub-persona must PASS (confidence ≥ 85).
Fix is clean → proceed.

### C6: Pitfall KI Extraction (mandatory)
Document failure pattern in .agents/knowledge/pitfalls/<domain>_<timestamp>.md.
/retro → KNOWLEDGE SUBAGENT → ensure pitfall KI promoted.

## Success Criteria
Root cause documented + failing test written before fix + fix verified + /ce-code-review PASS + Pitfall KI extracted.

## Failure Handling
3-strike: HALT. User receives: root cause summary + all 3 fix attempts + recommended escalation path.
