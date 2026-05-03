---
name: freeze
description: Emergency circuit breaker to halt all agent operations. Triggers on "freeze", "halt", "stop everything", "emergency stop".
version: 1.0.0
---

# freeze — Emergency Circuit Breaker

## Purpose
Provides a mechanism to immediately cease all autonomous actions in the event of an error, loop, or unexpected behavior.

## Execution Procedure
1. **Immediate Halt**: Cease all tool use and command execution immediately.
2. **State Capture**: Write the current session state and last known status to `progress.md`.
3. **Freeze Report**: Generate a `FREEZE_REPORT.md` at the repository root containing:
   - **Last Action**: Exactly what the agent was doing when frozen.
   - **Pending Actions**: What was next in the plan.
   - **Rollback Instructions**: Steps to revert the last N actions if necessary.

## Circuit Breaker (Auto-Trigger)
- Automatically triggered if **Rule 06** (3-strike failure protocol) is reached on any active branch or task.

## Resumption
- The agent is LOCKED after a freeze.
- Resumption is only possible after the user explicitly reviews the `FREEZE_REPORT.md` and types the `/unfreeze` command.
