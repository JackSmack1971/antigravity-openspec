---
name: backward-root-cause-tracing
description: Data flow extraction process starting from symptom back to original trigger.
---
# Backward Root-Cause Tracing

## Purpose
A deterministic data flow extraction process to trace a bug from its visible symptom back to its exact origin in the code.

## Procedure
1. **Start from symptom:** Identify the exact output, error message, or behavior that is failing.
2. **Trace backward through call chain/stack:** Follow the execution path in reverse, identifying the sequence of functions and data transformations that led to the symptom.
3. **Add instrumentation/logs:** Insert temporary logging or debugging instrumentation at each level of the stack to observe state changes.
4. **Identify original trigger:** Pinpoint the exact line of code or data input where the state first became corrupted.
5. **Integration:** This workflow seamlessly integrates with the `find-polluter.sh` script to isolate state leakage across test suites.
