---
name: using-agent-skills
description: Meta-discovery skill for determining the appropriate specialized skill or workflow for a given task. Use when unsure how to proceed, when multiple skills might apply, or when "skill discovery" is required. Triggers: "which skill", "what should I use", "how to proceed", "skill discovery".
version: 1.0.0
---

# using-agent-skills

## Purpose
This is a meta-discovery skill designed to help the agent navigate the available skillset and workflows. It provides a decision-making framework to ensure the most appropriate specialized tool is invoked for any given task.

## Decision Flowchart

```mermaid
graph TD
    Start[Start Task] --> Ambiguous{Is the task ambiguous?}
    Ambiguous -- Yes --> Discovery[Invoke using-agent-skills]
    Ambiguous -- No --> Type{Task Type?}
    
    Discovery --> Type
    
    Type -- "Security Change?" --> Security[security-scanning]
    Type -- "New Feature?" --> SDD[spec-driven-development] --> CEPlan[ce-plan]
    Type -- "Bug/Error?" --> Debug[systematic-debugging]
    Type -- "Multi-session/Complex?" --> Memory[planning-with-files]
    Type -- "PM Decision/Discovery?" --> OST[opportunity-solution-tree]
    Type -- "Skill Gap/Meta Improvement?" --> Writing[writing-skills / self_evolution]
    Type -- "React/Next.js?" --> React[react-best-practices]
    Type -- "Ready to Ship?" --> Ship[/ship chain]
```

### Detailed Mapping Table

| Scenario | Recommended Skill/Workflow |
|---|---|
| Security vulnerability or hardening | `review-qa-security/security-scanning` |
| New feature or significant change | `governance/spec-driven-development` → `execution/ce-plan` |
| Bug report or unexpected behavior | `execution/systematic-debugging` |
| Large task (>3 steps) or multi-session | `governance/planning-with-files` |
| Strategic planning or decision needed | `orchestration/opportunity-solution-tree` |
| Creating or fixing an agent skill | `governance/writing-skills` (TDD cycle) |
| Frontend specific (React/Next.js) | `execution/react-best-practices` |
| Final verification and release | `/ship` chain (governed by `AGENTS.md`) |

## Rules
1. **Load First**: On any ambiguous task, this skill SHOULD be consulted first to select the correct downstream specialist.
2. **Rule 04 Compliance**: NEVER load more than 3 full skill payloads simultaneously. Use Layer 1 discovery first.
3. **Hierarchy**: Constitutional rules (AGENTS.md) always take precedence over skill-level logic.
4. **Context Resilience**: If a task spans multiple domains, prefer the most specific skill first.

## Quality Gates
- [ ] Correct specialist skill identified based on task intent.
- [ ] Selection aligns with the APEX Power-Chains defined in AGENTS.md.
- [ ] No more than 3 skill payloads currently active in the context.
