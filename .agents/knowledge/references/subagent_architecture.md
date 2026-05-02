---
name: subagent-architecture
description: Taxonomy and operational mechanics of Terminal and Browser subagents in Antigravity's multi-agent architecture.
version: 1.0.0
---
# Sub-Agent Architecture — Multi-Agent Orchestration

## Core Pattern
Antigravity utilizes specialized sub-agents to handle specific toolsets. These agents operate asynchronously, communicating results via Artifacts (screenshots, logs, diffs).

## Sub-Agent Taxonomy
1. **Terminal Subagent**:
   - **Role**: Executes shell commands, manages git worktrees, and runs build/test pipelines.
   - **Constraint**: Subject to "Terminal Command Auto Execution" policies and "Strict Mode" sandboxing.
2. **Browser Subagent**:
   - **Role**: Actuates a headless browser for UI testing, data extraction, and visual verification.
   - **Artifacts**: Produces `.png` screenshots and `.mp4` recordings.
3. **Planner Agent**:
   - **Role**: High-level orchestrator. Generates Implementation Plans and Task Lists. Bridges the gap between user intent and sub-agent execution.

## Interaction Model
- **Handoffs**: The Planner Agent assigns tasks to sub-agents via "Task Groups".
- **Asynchronicity**: Multiple agents can work in parallel across different workspaces.
- **Unified Inbox**: Pending reviews (terminal approvals, plan proceeds) are centralized in the Agent Manager Inbox.

## Visual Verification Protocol
- Explicitly prompt the agent to "take a screenshot" or "record the session" to force the creation of a visual artifact.
- Use these artifacts in `Walkthrough` documents to prove successful execution of UI tasks.
