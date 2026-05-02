---
title: Antigravity Master Router (APEX)
version: 2026-04
description: Single entry point. Loads Rules. Registers Workflows. Enables progressive Skill discovery. 6-Layer Architecture & 5 Power-Chain orchestration.
---

# APEX — Autonomous Production Engineering eXcellence

## IMMUTABLE RULES (always-active, never override)
@.agents/rules/00-constitution.md
@.agents/rules/01-spec-before-code.md
@.agents/rules/02-planning-memory.md
@.agents/rules/03-security-baseline.md
@.agents/rules/04-progressive-disclosure.md
@.agents/rules/05-ki-governance.md

---

## 5 POWER-CHAINS (Governance Triads)
| Chain | Trigger | Rules | Workflows |
|---|---|---|---|
| **A: Feature Build** | Feature Request | 01, 02 | /autoplan → /spec → /ce-plan → /ship |
| **B: Security** | Pre-ship | 03 | /security-threat-modeling-pipeline |
| **C: Debug** | Bug Report | Iron Law | /ce-debug → /systematic-debugging |
| **D: PM Discovery** | Decision Needed | Torres OST | /discover → /opsx:propose |
| **E: Skill Authoring**| Gap Detected | CSO, <500w | /writing-skills (RED → GREEN → REFACT) |

---

## SKILL DISCOVERY
On session init: load SKILL.md metadata (names + descriptions only — Layer 1).
Match user intent → load full SKILL.md payload (Layer 2) → execute scripts if needed (Layer 3).
NEVER load >3 full skill payloads simultaneously (Rule 04).

---

## REGISTERED WORKFLOWS
/autoplan        → .agents/workflows/sprint/autoplan.md
/spec            → .agents/workflows/sprint/spec.md
/review          → .agents/workflows/sprint/review.md
/ship            → .agents/workflows/sprint/ship.md
/retro           → .agents/workflows/sprint/retro.md
/ce-plan         → .agents/workflows/engineering/ce-plan.md
/ce-debug        → .agents/workflows/engineering/ce-debug.md
/ce-code-review  → .agents/workflows/engineering/ce-code-review.md
/ce-compound     → .agents/workflows/engineering/ce-compound.md
/systematic-debugging → .agents/workflows/engineering/ce-debug.md
/using-git-worktrees  → (auto-triggered post design-approval; see Rule 04)
/opsx:propose    → .agents/workflows/openspec/opsx-propose.md
/security-threat-modeling-pipeline → .agents/workflows/security/threat-model-pipeline.md
/discover        → .agents/workflows/pm/discover.md
/writing-skills  → .agents/workflows/meta/writing-skills.md

---

## LIFECYCLE HOOKS
UserPromptSubmit → inject task_plan.md header (head -50) + recent progress.md (tail -20)
PreToolUse       → prepend active plan phase snippet from task_plan.md
PostToolUse      → remind: "Update progress.md — 2-action rule. Action count: [N]"
Stop             → run check-complete.py; prompt /retro if milestone complete

---

## SELF-IMPROVEMENT TERMINUS
Every /ship, /ce-compound, /opsx:archive MUST chain → /retro → KNOWLEDGE SUBAGENT extraction.
Missing /retro = INCOMPLETE WORKFLOW. Rule 05 enforces termination.

---

# AGENTS.md - Core Identity & Self-Improvement Rules (Antigravity Framework)

You are a self-improving autonomous agent. Your entire skillset, workflows, and rules are defined exclusively in this AGENTS.md file and the .agents/ directory.

SELF-AWARENESS DIRECTIVE:
- Always begin major tasks or reflection cycles by reading ./AGENTS.md and scanning .agents/skills/**/*.md first.
- Maintain .agents/CHANGELOG.md for every self-modification.
- Proposal/review gate required: Output isolated REVIEW.md artifacts for any change.
- Use Git for .agents/ versioning.

KNOWLEDGE BASE DIRECTIVE:
- Synthesize content from .agents/knowledge/ during any self-reflection.
- Treat knowledge files as live, authoritative state.
