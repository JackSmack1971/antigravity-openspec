---
name: planning-core-pattern
description: State-saving iteration utilizing the 3-File Persistent Memory pattern. Slash command: /planning-core-pattern
---
# Planning with Files — Core Planning Pattern

## Purpose
The primary state-saving iteration loop, relying on the 3-File Persistent Memory nucleus (`task_plan.md`, `findings.md`, `progress.md`).

## Execution Pattern
1. **Create/Init Tracking Files:** Initialize the 3-file memory nucleus if it does not already exist.
2. **Read Before Decide:** Always read `task_plan.md` and `findings.md` before making any significant architectural or execution decision. Do not rely solely on the context window.
3. **Act + 2-Action Rule Update:** Execute the necessary tool calls. After EVERY 2 actions, write the current status and intermediate results to `progress.md`.
4. **Update After Act:** Update tracking files with new discoveries, errors, or constraints encountered during execution.
5. **Continue After Completion:** Once the current phase is complete, append new phases to `task_plan.md` or invoke `/ce-compound` to finish the loop.
