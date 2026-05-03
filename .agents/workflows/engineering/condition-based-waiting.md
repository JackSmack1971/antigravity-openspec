---
name: condition-based-waiting
description: Implementation level routine to eliminate test flakiness by replacing sleeps with polling loops.
---
# Condition-Based Waiting (Flakiness Elimination)

## Purpose
An implementation-level routine designed to eliminate test flakiness and race conditions caused by arbitrary timing assumptions.

## Procedure
1. **Identify arbitrary waits:** Locate any instances of `sleep(N)`, `setTimeout(..., N)`, or arbitrary timeouts in tests or asynchronous logic.
2. **Define predicate:** Identify the exact state or DOM condition that the code is waiting for (e.g., "element is visible", "database row is updated").
3. **Replace with polling loop:** Implement a `waitFor(condition)` function that polls for the predicate at tight intervals (e.g., every 50ms) with a maximum safety timeout.
4. **Validation:** Ensure the test now fails immediately upon the safety timeout or passes instantly when the condition is met, removing all non-deterministic arbitrary delays.
