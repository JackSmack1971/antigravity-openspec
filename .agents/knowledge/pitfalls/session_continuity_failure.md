---
name: session-continuity-failure
description: Pitfall KI for repeated bootstrapping — when each new session re-discovers the same framework improvements instead of compounding on previous work.
version: 1.1.0
---
# Pitfall: Session Continuity Failure (Repeated Bootstrapping)

## Summary
- **Symptom**: Each new session receiving an "improve yourself" prompt performs the same hardening steps already completed in prior sessions. No compound progress is made — the framework loops rather than spirals upward.
- **Root Cause**: The agent lacks a mechanism to detect "already done" improvements. Session context is discarded at session end. Without reading `progress.md`, `CHANGELOG.md`, and the conversation summaries at session START, the agent re-discovers completed work.

## Quantified Occurrence
This pitfall was triggered 18+ times in a single day (2026-05-02). Every conversation in the history log performed near-identical APEX hardening work. This is the most critical recurring blocker in the system.

## Resolution Protocol
1. **Detection**: At session start, run `python .agents/scripts/session-catchup.py`. If it reports MISSING `task_plan.md`, read `CHANGELOG.md` head (last 30 lines) and `progress.md` before any analysis.
2. **Immediate Fix**: Before proposing ANY framework improvement, MUST read `.agents/CHANGELOG.md` (tail 40 lines) and check if the proposed change was already made.
3. **Anti-Duplication Check**: Search for the target concept in `.agents/rules/`, `.agents/knowledge/`, and `.agents/skills/` before creating new files.
4. **Prevention**: Run the **Session Init Checklist** (`.agents/knowledge/playbooks/session-init-checklist.md`) at the start of every meta/governance task.

## Context Anchor
- **Rule Reference**: Rule 02 (Planning Memory), Rule 09 (Self-Improvement Uplift)
- **Extraction Gate**: This pitfall qualifies under the 2-Hit Rule (Rule 09.4) — 18+ occurrences within 7 days.
- **Linked Playbook**: `.agents/knowledge/playbooks/session-init-checklist.md`

## Prevention Signal
If you find yourself about to create a file that likely already exists in `.agents/rules/` or `.agents/knowledge/`, STOP and use `list_dir` first. Never assume the framework is missing something without checking.
