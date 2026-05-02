---
name: retro
description: Self-improvement flywheel terminus. Extracts Knowledge Items from completed sprints, debug sessions, and workflows. Slash command: /retro. Auto-triggered after /ship, /ce-compound, /opsx:archive, 3-strike resolution.
---
# /retro — Self-Improvement Loop Terminus

## Constitutional Trigger (Rule 05 enforces this — no exceptions)
Auto-chained after: /ship, /ce-compound, /opsx:archive, any 3-strike escalation resolution.
Missing /retro = INCOMPLETE WORKFLOW. Lifecycle Stop hook flags and prompts if omitted.

## Step 1: Delta Extraction
Compare task_plan.md (Phase 0 — original plan) vs actual implementation (progress.md final state).
Identify all deltas: what changed, what was harder than expected, what worked perfectly,
what failed, what was discovered mid-execution.

## Step 2: KI Classification
Classify each meaningful delta:
- **Pitfall**: anti-pattern to prevent; something that went wrong unexpectedly
- **Playbook**: positive pattern to replicate; approach that worked better than expected
- **Context**: multi-session continuity data; domain-specific persistent state
- **Reference**: external knowledge that proved critical; non-obvious dependency

## Step 3: KNOWLEDGE SUBAGENT Invocation
Distill each classified delta → telegraphic KI artifact.
Telegraphic = short sentences, active voice, imperative mood, n-gram abbreviations.
Not narrative. Not observational. Prescriptive and actionable.

## Step 4: Quality Gate Gate: STRICT_MODE
For each KI candidate, verify all 3 factors:
1. Actionability: does it contain prescriptive instructions (not just description of what happened)?
2. Uniqueness: is it NOT inferrable from README / config / existing docs?
3. Density: telegraphic syntax applied? Unnecessary words removed?
quality_score < threshold → DISCARD. Do not write low-quality KI to store.

## Step 5: Write Approved KI Artifacts
Write to: `.agents/knowledge/{type}/{domain}_{timestamp}.md`
Existing KI updated: SemVer bump (patch for minor, minor for structural).
**Mandate**: Use the `.agents/knowledge/playbooks/pitfall_extraction.md` template for all Pitfall KIs.

## Step 6: 30-Day Crystallization & Metrics Dashboard
1. Track `manual_interventions` vs `autonomous_wins` in the current session.
2. Calculate Session `Uplift%` per Rule 09.2.
3. **Dashboard Generation**: The agent MUST generate the "Autonomy Uplift Dashboard" for the `walkthrough.md` during this step.
4. If `Uplift%` < 40%, flag a "Quality Score Alert" for immediate KI audit.

## Step 7: Report
Output: "KI extracted: [title] | Type: [Pitfall/Playbook/Context] | Domain: [X] | Trace: [6-char-id] | Uplift: [X%]"

## Success Criteria
≥ 1 KI artifact passes quality gate and is written to .agents/knowledge/.

## Failure Handling
No meaningful delta → log "No new KI: [reason: normal execution / no surprises]".
Never force low-quality KI to meet the mandatory trigger obligation.
