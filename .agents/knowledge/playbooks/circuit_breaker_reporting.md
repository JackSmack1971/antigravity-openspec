---
name: circuit-breaker-reporting
description: Standardized reporting template for Rule 10.4 (Hallucination Circuit Breaker).
version: 1.0.0
---
# Circuit Breaker Reporting Playbook

This playbook defines the `STRIKE_THREE_HALT` report format to ensure manual interventions are efficient and goal-oriented.

## 1. The STRIKE_THREE_HALT Report Template
When a circuit breaker is triggered, the agent MUST output the following structure:

### 🛑 STRIKE_THREE_HALT: [Brief Error Description]
- **Target Action**: [What tool/action was being attempted?]
- **Error Pattern**: [The recurring error message.]
- **Attempt History**:
  1. [Action 1] -> [Error 1]
  2. [Action 2] -> [Error 2]
  3. [Action 3] -> [Error 3]

### Root Cause Hypothesis
[Concise explanation of why the agent believes this is failing (e.g., path mismatch, tool restriction, environment state).]

### Manual Reset Instructions
1. [Action 1 for the user (e.g., "Prune the last 5 turns of context")]
2. [Action 2 for the user (e.g., "Manually run [Command] to verify path")]
3. [Action 3 for the user (e.g., "Provide the absolute path to [File]")]

## 2. Quality Gate
- **No Apologies**: The report must be clinical and technical.
- **Actionable**: Every reset instruction must be a concrete step the user can take.
- **Goal-Oriented**: Clearly state if the task should be restarted or if a strategy pivot is recommended.
