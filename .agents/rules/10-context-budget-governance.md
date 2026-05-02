---
name: 10-context-budget-governance
description: Manage context window density, plan compression, and JIT skill unloading.
globs: ["**/*"]
alwaysApply: true
---
# Rule 10 — Context Budget Governance

*Activation Mode: Always On*

## 1. Context Density Thresholds
To maintain high reasoning fidelity, the agent must monitor "Context Budget Analytics":
- **Plan Bloat:** If `task_plan.md` or `findings.md` exceeds 12,000 characters, it MUST be compressed. Move detailed logs to `archive/` and maintain only a high-level summary.
- **Token Ceiling:** If the current context exceeds 80k tokens, trigger a "Memory Consolidation" step: update `progress.md` and prune irrelevant historical tool outputs using the `.agents/knowledge/playbooks/context_resilience_playbook.md`.

### 1.3 Reasoning Anchor Protocol
- **Trigger:** Context token count > 80,000 OR turn count > 5 since last anchor.
- **Action:** The agent MUST explicitly restate the "Current Goal" and "Active Hypothesis/Sub-task" in the thought trace.
- **Mandate:** This prevents "Context Drift" where the agent loses the original root-cause hypothesis during long tool execution chains.

## 2. Skill Unloading (JIT Protocol)
Adhere to the "3-Skill Cap" from Rule 04. 
- If a new skill is required that would exceed the 3-active-skill limit, the agent MUST explicitly "unload" the least relevant skill before loading the new one.
- **Log Entry:** "Unloading [Skill A] to make room for [Skill B] — Context Budget Management."

## 3. Plan-Before-Bloat
NEVER allow a plan to become a monolithic implementation guide. 
- Use `@filename` references for complex sub-component specs.
- Keep the main `implementation_plan.md` focused on *decisions* and *architecture*, not code snippets.

## 4. Hallucination Circuit Breaker
To prevent the "Infinite Hallucination Loop" often caused by context pollution or environment mismatch:
- **3-Strike Tool Strike:** If the same tool call fails with the same error 3 times in a row, the agent MUST stop and issue a `STRIKE_THREE_HALT` report.
- **Mandatory Escalation:** In the event of a circuit breaker trip, the agent MUST recommend a "Context Reset" to the user (e.g., "Please start a new session or manually prune the last 10 turns").
- **Recovery:** Do not attempt the same failing action a 4th time without a manual override or a significant change in strategy (branching).

## 5. Monitoring & Metrics
- Include a "Context Budget" status in every 2-action `progress.md` update if the context is > 50% full.
- Violation of Rule 10 triggers a mandatory `/para-knowledge` audit at session close.
