---
name: planning-lifecycle-hooks
description: Uses matcher-based hooks across the agent lifecycle for continuous planning integration. Slash command: /planning-lifecycle-hooks
---
# Planning with Files — Lifecycle Hook Injection & Update Cycle

## Purpose
Integrates continuous state tracking across the entire agent operational lifecycle using matcher-based hooks.

## Lifecycle Hooks
1. **UserPromptSubmit:** Inject the active plan data header (e.g., `head -50` of `task_plan.md`) and recent progress (`tail -20` of `progress.md`) to establish context before processing the prompt.
2. **PreToolUse:** Prepend the active plan phase snippet before executing any tool to ensure the action aligns with the current objective.
3. **PostToolUse:** Remind the agent to "Update progress.md — 2-action rule."
4. **Stop:** On session termination, run the `check-complete.py` script to verify if the `/retro` loop is required and ensure no tasks are abandoned.
