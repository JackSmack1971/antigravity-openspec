---
name: 02-planning-memory
description: Persistent 3-file working memory nucleus with lifecycle hook enforcement
alwaysApply: true
---
# Persistent Memory — planning-with-files

## Core Principle
Context Window = RAM (volatile). Filesystem = Disk (persistent).
NEVER rely on context window alone for multi-session or multi-step tasks.

## 3-File Memory Nucleus
task_plan.md  — phases, goals, current status, error log (phases: todo/in_progress/complete)
findings.md   — discoveries, surprises, constraints, KI candidates
progress.md   — completed steps, errors, next actions (append-only running log)

## 2-Action Rule
After EVERY 2 tool operations: write status to progress.md. No exceptions.
Visual data (screenshots, DOM snapshots, API responses) MUST be saved within 2 operations — irreversible loss otherwise.

## Read-Before-Decide
Before any significant architecture or approach decision: read task_plan.md + findings.md.
NEVER make decisions from context window alone on complex or multi-session tasks.

## Session Resume Protocol (execute on any session start)
1. Check for task_plan.md existence.
2. If exists: read all 3 files → run session-catchup.py if available.
3. Run: git diff --stat → identify unsynced changes.
4. Update planning files based on diff.
5. Re-orient: announce current phase + next action BEFORE proceeding.

## Log ALL Errors
Every error → task_plan.md error log with: error message + context + attempted fix.
If action_failed: next_action MUST differ from failed_action.

## Phase Status Lifecycle
todo → in_progress → complete. Never skip statuses. Never leave in_progress at session end.
