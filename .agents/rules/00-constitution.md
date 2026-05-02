---
name: 00-constitution
globs: ["**/*"]
alwaysApply: true
---
# Constitutional Invariants — NEVER OVERRIDE

## L0 Foundational Rules (Karpathy Mandates)
1. **THINK BEFORE CODING** — Write intent in comments before any implementation line.
2. **SURGICAL EDITS** — Change only what the task requires. Zero opportunistic refactoring.
3. **SIMPLICITY FIRST** — When two solutions exist, always choose the simpler one.
4. **GOAL-DRIVEN** — Define the verification / acceptance criterion before writing implementation.
*Note: These Karpathy Mandates were previously defined in legacy GEMINI.md and are now the primary L0 Foundational Rules.*

## User Sovereignty
AI recommends only. NEVER act unilaterally on destructive ops.
ALWAYS present options via AskUserQuestion. Confirm before: delete, push-force, schema-drop.

## Root-Cause First (Iron Law)
NO FIXES WITHOUT ROOT CAUSE. Reproduce → trace → hypothesize → test → implement.
Follow the `/ce-debug` workflow for all systematic investigations.
3+ failures → trigger architectural rethink → escalate to user.

## Compliance & Governance
1. **100% Compliance Threshold**: All agent skills must maintain 100% compliance with L0 mandates during pressure-tests.
2. **Skill Promotion Gate**: No skill is promoted to "Always-Equip" status without a successful `/writing-skills` TDD cycle.

## 3-Strike Escalation
ATTEMPT 1: Diagnose + fix. ATTEMPT 2: Rethink approach. ATTEMPT 3: Broader rethink.
AFTER 3 FAILURES: HALT → "I cannot resolve autonomously. Here is what I found: [summary]."
Mandatory `/retro` extraction follows all escalations.
