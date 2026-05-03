---
name: context-resilience-playbook
description: Playbook for Rule 12 (Context Resilience) and Rule 10 (Context Budget Governance) to prevent context rot and hallucination.
version: 1.1.0
---
# Context Resilience Playbook (Power-Chain F)

This playbook details the operational procedures for maintaining high reasoning fidelity through proactive context management.

## 1. Trigger Identification
Active monitoring of the session state is mandatory. Trigger the **Consolidation Cycle** when:
- **Token Density**: Context exceeds 80,000 tokens.
- **Turn count**: `progress.md` exceeds 10 turns.
- **Repetition**: The same reasoning error or tool failure occurs twice (Strike Two).

## 2. Consolidation Cycle Procedure
1.  **Strategic Sync**:
    - Update `task_plan.md` with a high-density summary of achievements and remaining blockers.
    - Reference specific files by name (Rule 11) to maintain anchors.
2.  **Tactical Reset**:
    - Truncate `progress.md` to show only the last 2-4 actions.
    - Archive older tactical logs into `docs/archive/progress_archive_[date].md`.
3.  **Findings Extraction**:
    - Move verified facts and research results into a `findings.md` file.
    - Prune raw tool output from the active context by summarizing it in the thought trace.
4.  **Sequential Pivot**:
    - If parallel tool use is causing "Context Noise", switch to 100% sequential execution for the next 5 turns.

## 3. Hallucination Circuit Breaker (Rule 10.4)
If the **3-Strike Tool Strike** is imminent:
- **Strike 1**: Log the failure and verify the path (Rule 11.5).
- **Strike 2**: Stop. Re-read the core rule and the target file content using `view_file` (Context Anchor).
- **Strike 3 (HALT)**: Trigger a `STRIKE_THREE_HALT`. Output the report structure defined below.

### 🛑 STRIKE_THREE_HALT Report Structure
When a circuit breaker is triggered, output this report for manual user reset:
- **Target Action**: [What tool/action was being attempted?]
- **Error Pattern**: [The recurring error message.]
- **Attempt History**: [1. Action -> Error, 2. Action -> Error, 3. Action -> Error]
- **Root Cause Hypothesis**: [Concise explanation of the blockage.]
- **Manual Reset Instructions**: [Concrete technical steps the user must take.]

## 4. JIT Skill Management
- Maintain the **3-Skill Cap**.
- Before loading a new skill, explicitly unload the least active skill.
- Log: `"Unloading [Skill] to preserve Context Budget."`

## 5. Verification
After every Consolidation Cycle, verify that the `task_plan.md` still accurately reflects the goal without legacy bloat.
