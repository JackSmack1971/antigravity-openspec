---
name: planning-with-files
description: Use when starting any complex task requiring 5+ tool calls, multi-session continuity, or when context window loss would cause irreversible task failure. Triggers include: complex implementation, session resume, "continue from last time", "I was working on", or when task_plan.md already exists.
version: 2.36.3
user-invokable: true
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---
# planning-with-files

## Core Principle
Context Window = RAM (volatile). Filesystem = Disk (persistent).
Use disk for ALL working memory on complex tasks.

## 3-File Memory Nucleus
task_plan.md  — phases + goals + status (todo/in_progress/complete) + error log
findings.md   — discoveries, constraints, KI candidates, surprises
progress.md   — append-only running log: completed steps, errors, next actions

## Mandatory Workflow

### On Session Start (every time)
1. Check for task_plan.md. If exists: read all 3 files.
2. Run session-catchup.py if available.
3. git diff --stat for unsynced changes.
4. Announce: "Restored. Phase: [X]. Last: [Y]. Next: [Z]."
5. Begin ONLY after full re-orientation.

### During Execution
- 2-Action Rule: after every 2 tool ops → write to progress.md.
- Read-Before-Decide: read task_plan.md before any significant decision.
- Log ALL errors with: error + context + attempted fix.
- 3-Strike: Attempt 1 → diagnose. Attempt 2 → rethink. Attempt 3 → escalate.

### On Session End (Stop hook)
Run check-complete.py → if milestone complete → prompt /retro.

## Common Mistakes
- Starting without plan → PROHIBITED. Non-negotiable.
- Relying on context window for multi-session state → PROHIBITED.
- Not logging errors → enables infinite failure loops.
- Saving visual data after >2 actions → data lost forever.

## Quality Gates
- [ ] task_plan.md created before any significant action
- [ ] progress.md updated every 2 tool operations
- [ ] Adheres strictly to L0 Foundational Rules (THINK BEFORE CODING)

