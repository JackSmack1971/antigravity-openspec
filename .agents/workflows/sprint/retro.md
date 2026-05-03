---
name: retro
description: Self-improvement flywheel terminus. Extracts Knowledge Items from completed sprints, debug sessions, and workflows. Slash command: /retro. Auto-triggered after /ship, /ce-compound, /opsx:archive, 3-strike resolution.
---
# /retro — Self-Improvement Loop Terminus

## Constitutional Trigger (Rule 05 enforces this — no exceptions)
Auto-chained after: /ship, /ce-compound, /opsx:archive, any 3-strike escalation resolution.
Missing /retro = INCOMPLETE WORKFLOW. Lifecycle Stop hook flags and prompts if omitted.

### Step 1: Context Retrieval
Read `progress.md` (full) + `task_plan.md` (tail 30) + `CHANGELOG.md` (tail 20).

### Step 2: KNOWLEDGE SUBAGENT Sweep
Scan the session trajectory for the following:
- **Errors that occurred 2+ times** → Pitfall KI candidate.
- **Architectural decisions made** → Architecture/Playbook KI candidate.
- **New patterns discovered** → Pattern KI candidate.

### Step 3: KI Distillation
For each candidate: apply `pitfall_extraction.md` template; write to `.agents/knowledge/<category>/`.

### Step 4: Metrics Tracking
Run the following command:
`python .agents/scripts/crystallization-tracker.py --dashboard`

### Step 5: Performance Review
Output: **Session Uplift% Score** + KI Extraction Summary.

### Step 6: Governance Trigger
If **Uplift% < 40%**: Trigger a mandatory governance audit by loading the `metrics-auditor` skill.

### Step 7: Final Logging
Log: "Retro complete. [N] KIs extracted. Uplift%: [X]%".

### Step 8: Progress Archival
Archive `progress.md`: Move to `docs/archive/progress_[timestamp].md`; reset `progress.md` for the next session.

## Success Criteria
≥ 1 KI artifact passes quality gate and is written to .agents/knowledge/.

## Failure Handling
No meaningful delta → log "No new KI: [reason: normal execution / no surprises]".
Never force low-quality KI to meet the mandatory trigger obligation.
