---
ki_type: Pitfall
domain: Orchestration
purpose: Anti-pattern prevention
version: 1.0.0
trigger_index: ["autoplan", "workflow", "prerequisite", "skip"]
trace_id: "wf-drft"
created: 2026-05-03
---
# Pitfall: Workflow Shortcut Drift

## Symptom
The agent skip critical "starting" steps (like `/office-hours` diagnostic or workspace initialization) because a conditional prerequisite (e.g., `if SPEC.md exists`) is met. The agent "shortcuts" to the middle of the workflow, leading to strategic misalignment and missing environment setup.

## Root Cause
Ambiguous or overly permissive "jump-to" logic in workflow `.md` files. When a trajectory program allows skipping the diagnostic phase based on the presence of artifacts, it ignores the fact that those artifacts might be stale or belong to a different context.

## Fix (Governance Rule)
Modify workflow prerequisites to enforce a "Strategy Alignment" check even if artifacts exist.
```markdown
## Prerequisite
- If artifacts (e.g., `SPEC.md`) exist, verify them against `STRATEGY.md` (Step 1) before proceeding.
- NEVER skip the diagnostic phase if the session intent is "New Project" or "New Feature".
```

## Verification
1. Run `/autoplan` in a directory with an existing `SPEC.md`.
2. Confirm the agent still initiates Step 1 (Strategy Check) and Step 2 (Diagnostic).

## Prevention Rule
"Workflow prerequisites must prioritize Strategy Alignment over Artifact Presence; never skip diagnostics in a fresh session."
