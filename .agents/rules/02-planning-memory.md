---
name: 02-planning-memory
globs: ["**/*"]
alwaysApply: true
---
# Persistent Memory (planning-with-files)

## 3-File Memory Nucleus
task_plan.md    — phases, goals, current status
findings.md     — discoveries, surprises, constraints  
progress.md     — completed steps, errors, next actions

## 2-Action Rule
After EVERY 2 tool operations: write status to progress.md. No exceptions.

## Read-Before-Decide
Before any significant decision: read task_plan.md + findings.md. NEVER rely on context window alone.

## Session Resume
On ANY session start: check task_plan.md existence → run session-catchup.py → git diff --stat → re-orient BEFORE proceeding.
