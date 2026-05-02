---
name: metrics-auditor
description: Use to check aggregate Autonomy Uplift metrics and log session results using crystallization-tracker.py.
version: 1.0.0
---
# metrics-auditor — Autonomy Uplift Monitoring

## Core Principle
The framework's effectiveness is measured by the reduction of manual interventions. This skill provides the interface to the `crystallization-tracker.py` utility to ensure transparent metric-driven governance.

## Trigger Scenarios
- During `/retro` to log session wins/interventions.
- When requested by the user to "report progress" or "show metrics".
- When `Uplift%` falls below the 40% threshold defined in Rule 09.

## Actionable Instructions
1. **Check Aggregate Metrics**: Run `python .agents/scripts/crystallization-tracker.py` without arguments.
2. **Log Session Data**: Run `python .agents/scripts/crystallization-tracker.py [wins] [interventions]`.
   - `wins`: Number of tasks completed without manual intervention (beyond initial prompt).
   - `interventions`: Number of times the user had to correct the agent's path or provide missing info.
3. **Governance Compliance Audit**: 
   - Scan the last 10 turns of `progress.md`.
   - Verify that Rule 11.1 (Repo-Relative) was maintained in all artifacts.
   - Verify that Rule 10.1 (Context Budget) was respected (no plan bloat).
   - Report any "Near Misses" (Strike Two) during `/retro`.

## Quality Gate
- MUST report the aggregate `Uplift%` in the session's final `Walkthrough` artifact.
- MUST trigger a Governance Audit if current session `Uplift%` is < 50% for tasks of "Medium" complexity or higher.
- MUST verify "Trust Anchor" resolution (Rule 11.5) was correctly logged for all Windows tool calls.
