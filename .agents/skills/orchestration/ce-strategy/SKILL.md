---
name: ce-strategy
description: Upstream anchor skill to create and maintain the `STRATEGY.md` document. Acts as a grounding parameter for all downstream engineering and product workflows.
version: 1.0.0
triggers: ["strategy", "roadmap", "plan the project", "STRATEGY.md", "project direction", "what should we build"]
---

# ce-strategy — Project Strategy & Grounding Anchor

## Purpose
This skill ensures that every project has a clearly defined technical and product strategy. The resulting `STRATEGY.md` file serves as the authoritative source of truth for all subsequent planning and execution phases.

## STRATEGY.md Structure (Mandatory Sections)
1. **Target Problem**: One concise paragraph describing who has what problem and why solving it matters.
2. **Approach**: The core technical approach, including key architectural decisions and tradeoffs.
3. **Persona**: Definition of primary and secondary users and their specific goals.
4. **Success Metrics**: Quantifiable targets such as latency goals, conversion rates, or error budgets.
5. **Execution Tracks**: Parallel workstreams with defined owners, milestones, and cross-track dependencies.

## Grounding Rules
- **First Step Requirement**: All downstream workflows (including `/ce-plan`, `/spec`, and `/autoplan`) MUST read `STRATEGY.md` as their first step to ensure alignment.
- **Update Trigger**: Any significant architectural or product decision that deviates from the current `STRATEGY.md` requires an update to the strategy document BEFORE implementation begins.
- **Anti-Drift**: If implementation work is detected as deviating from the strategy without an explicit update, it MUST be flagged as technical debt.

## Output
- `STRATEGY.md` file located at the repository root.
