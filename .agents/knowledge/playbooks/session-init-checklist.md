---
name: session-init-checklist
description: Mandatory verification checklist for the start of every meta/governance or self-improvement session. Prevents repeated bootstrapping (see pitfall: session_continuity_failure.md).
version: 1.0.0
---
# Session Init Checklist (Anti-Bootstrapping Protocol)

> [!IMPORTANT]
> This checklist MUST be executed before any framework analysis or improvement work begins. Skipping it is the primary cause of repeated bootstrapping loops.

## Step 0: Context Re-Orientation (Always First)
- [ ] Run `python .agents/scripts/session-catchup.py` — reports nucleus file status and in-progress tasks.
- [ ] Read `progress.md` — confirms last session's status and tactical history.

## Step 1: Recent Work Audit (Anti-Duplication Gate)
- [ ] Read last 40 lines of `.agents/CHANGELOG.md` — determines what was changed in the last 1-3 sessions.
- [ ] If CHANGELOG shows recent changes to the area you're about to work on → **STOP. Report to user that work is already done.**

## Step 2: Conversation History Check
- [ ] Check the conversation summaries (provided in system context) — are there 3+ recent conversations with the same objective?
- [ ] If YES → This is a **Session Continuity Failure** (see `.agents/knowledge/pitfalls/session_continuity_failure.md`). Explicitly call it out.

## Step 3: Knowledge Base Scan (Before Proposing New Files)
- [ ] Run `list_dir` on `.agents/rules/` — count existing rules (13 rules as of v2026-05).
- [ ] Run `list_dir` on `.agents/knowledge/pitfalls/` — check for existing pitfalls before creating new ones.
- [ ] Run `list_dir` on `.agents/knowledge/playbooks/` — check for existing playbooks before creating new ones.

## Step 4: Gap-First Analysis
Based on Steps 1-3, identify **concrete, evidence-backed gaps only**:
- A gap is valid if it's NOT in CHANGELOG and NOT already a file in the knowledge base.
- A gap is a **real gap** if it has observable symptoms (e.g., script failure, missing index entry, broken reference).

## Step 5: Declare Intent Before Acting
Per L0 Mandate #1 (THINK BEFORE CODING), explicitly state:
- What 3 specific improvements you will make.
- What evidence supports each (file path, CHANGELOG line, symptom).
- What the verification criterion is.

## Quality Gate
- **Pass**: All 5 steps completed. Improvements are evidence-backed and non-duplicative.
- **Fail**: If Step 1 or 2 reveals the work is already done → output: "Prior session completed this work: [CHANGELOG reference]. No new improvements needed."
