---
name: restore-context
description: Session recovery and lifecycle hook handler. Orchestrates task_plan.md, progress.md, and crystallization tracking.
---
# /restore-context — Lifecycle Hook Management

## UserPromptSubmit Hook
1. **Read task_plan.md (head -50 lines)** → inject as session preamble.
2. **Read progress.md (tail -20 lines)** → inject as recent context.
3. **Read CHANGELOG.md (tail -10 lines)** → check for recent changes.
4. **If task_plan.md missing**: initialize with current user intent.

## PreToolUse Hook
1. **Prepend active plan phase snippet** from task_plan.md.
2. **Check action count**: if approaching 2-action threshold, remind to update progress.md.

## PostToolUse Hook
1. **Increment action counter**.
2. **If counter mod 2 == 0**: trigger progress.md update.
3. **Log**: "[timestamp] ACTION: [tool] | RESULT: [outcome] | NEXT: [step]".

## Stop Hook
1. **Run `python .agents/scripts/crystallization-tracker.py --dashboard`**.
2. **Run `python .agents/scripts/check-complete.py`**.
3. **If incomplete milestone**: prompt /retro.
4. **Truncate progress.md** to last 5 entries; archive older entries.
