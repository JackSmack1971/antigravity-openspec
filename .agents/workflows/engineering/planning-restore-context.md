---
name: planning-restore-context
description: Mandatory sequence on skill activation or session resume enforcing state persistence. Slash command: /planning-restore-context
---
# Planning with Files — Restore Context

## Purpose
A mandatory sequence to enforce state persistence when a session resumes or when the planning skill is activated.

## Procedure
1. **Check for task_plan.md:** Verify the existence of the primary state tracking file (`task_plan.md`).
2. **Execute session-catchup.py:** Run the `session-catchup.py` script to load the persistent memory nucleus.
3. **Run git diff --stat:** Check for any unsynced or uncommitted changes that might conflict with the persistent state.
4. **Update planning files:** Re-align `task_plan.md`, `findings.md`, and `progress.md` with the current workspace reality.
5. **Re-orientation Gate:** Do NOT proceed with execution until full re-orientation is complete and all context is restored.
