---
name: 12-context-resilience
description: Formalize Power-Chain F protocols for proactive context management and hallucination prevention.
globs: ["**/*"]
alwaysApply: true
---
# Rule 12 — Context Resilience (Power-Chain F)

*Activation Mode: Always On*

## 1. Resilience Trigger
The agent MUST activate Context Resilience protocols when:
- The total token count exceeds 80,000.
- `progress.md` tactical history exceeds 10 turns.
- The same complex reasoning branch is repeated across multiple thoughts.

## 2. Pruning Workflow
When a trigger is met, the agent MUST perform a "Consolidation Cycle":
1. **Strategic Sync**: Update `task_plan.md` with the current mission state.
2. **Tactical Reset**: Truncate `progress.md` to the last 2-4 actions.
3. **Drafting Findings**: Move historical detail from active thoughts into a `findings.md` or `docs/archive/` file.
4. **Tool Pruning**: Cease parallel tool execution and switch to sequential mode to reduce noise.

## 3. Anti-Hallucination Reset
If the Hallucination Circuit Breaker (Rule 10.4) is nearing a trip (2 tool strikes):
- **Immediate Action**: Stop current tool chain.
- **Context Refresh**: Use `view_file` to re-read core rules and the current spec to "anchor" reasoning.
- **Strategy Shift**: Explicitly state "Resetting context anchor..." in the thought trace.

## 4. Periodic Audit
Power-Chain F mandates a bi-weekly audit of the knowledge base via the `/para-knowledge` workflow to ensure that the "Resilience" protocols themselves haven't succumbed to context rot.
