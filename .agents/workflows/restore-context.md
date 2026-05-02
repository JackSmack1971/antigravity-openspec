---
name: restore-context
description: Session resume and lifecycle hook management. Auto-triggered on any session start if task_plan.md exists. Slash command: /restore-context
---
# /restore-context — Session Resume Protocol

## Auto-Trigger (Lifecycle Hooks)

### UserPromptSubmit (every message)
```bash
if [ -f task_plan.md ]; then
  echo "[APEX] ACTIVE PLAN DETECTED — injecting context header..."
  echo "=== CURRENT PLAN ===" && head -50 task_plan.md
  echo "=== RECENT PROGRESS ===" && tail -20 progress.md
fi
```

### PreToolUse (on Write/Edit/Bash/Read/Glob/Grep)
Prepend to context: current active phase snippet from task_plan.md.
Reminder: "Current phase: [X]. Objective: [Y]."

### PostToolUse (on Write/Edit)
Append reminder: "Update progress.md. 2-action rule. Tool call count this pair: [N]."

### Stop (session end)
```bash
python3 scripts/check-complete.py
# If milestone complete:
echo "[APEX] Milestone detected. Run /retro to extract KIs from this session."
```

## Manual Restore Workflow

### Step 1: Check for Active Plan
```bash
ls task_plan.md findings.md progress.md 2>/dev/null
```

### Step 2: Read All 3 Files
Read task_plan.md in full. Read findings.md. Tail progress.md (last 30 lines).

### Step 3: Git Sync Check
```bash
git diff --stat
git status --short
```
Identify unsynced changes. Update planning files to reflect actual state.

### Step 4: Session Catchup
```bash
python3 scripts/session-catchup.py  # if available
```

### Step 5: Re-Orient Announcement
"Restored context.
Current phase: [phase name + status].
Last completed action: [last entry in progress.md].
Next action: [next todo in task_plan.md].
Proceeding."

## Success Criteria
Full re-orientation achieved. Current phase and next action clearly announced. 3 files read.
