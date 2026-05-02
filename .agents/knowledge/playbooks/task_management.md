---
name: task-management
description: Distinction between Task Lists (markdown artifacts) and Task Groups (UI-level breakdowns). Use this to manage execution state and multi-agent parallelism.
version: 1.0.0
---
# Task Management — State & Orchestration

## Task List (The Internal Stateful Artifact)
- **Format**: Live markdown checklist (`task.md` or `task_plan.md`).
- **Purpose**: Internal state-management layer for the agent. Tracks action items across Research, Implementation, and Verification.
- **Rule**: Initialize for any objective requiring > 3 file modifications.

## Task Group (The Execution Orchestrator)
- **Format**: UI-level breakdown in Planning Mode.
- **Components**: Overarching Goal, File Pills (for quick auditing), and Subtasks (expandable micro-steps).
- **Parallelism**: Allows the agent to work on multiple parts of a task simultaneously.

## Operational Lifecycle
1. **Implementation Plan**: Predictive blueprint for user review.
2. **Task Group**: Modular execution orchestrator.
3. **Task List**: Persistent internal state tracker.
4. **Walkthrough**: Post-execution summary with visual proof.

## Bottleneck Mitigation: "Pending Steps"
- Terminal command approvals and browser javascript executions surface as "pending steps".
- **Risk**: Silent execution halts in Strict Mode or "Request Review" policies.
- **Fix**: Monitor the Inbox in the Agent Manager (`Cmd + E`) for notifications.
