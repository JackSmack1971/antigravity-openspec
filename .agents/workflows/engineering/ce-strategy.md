---
name: ce-strategy
description: Upstream anchor workflow to create/maintain STRATEGY.md (target problem, approach, persona, metrics, tracks), acting as a grounding parameter read by downstream skills.
---
# /ce-strategy — Strategy Definition

## Purpose
An upstream anchor workflow designed to create and maintain `STRATEGY.md`. This file acts as a grounding parameter and source of truth read by downstream skills to maintain alignment throughout the core loop.

## Components of STRATEGY.md
1. **Target Problem:** Clearly define the problem space and the core issue being solved.
2. **Approach:** Outline the high-level technical or product approach to solving the problem.
3. **Persona:** Identify the target user or system persona the solution is built for.
4. **Metrics:** Define the exact success metrics (KPIs, performance bounds, or acceptance thresholds).
5. **Tracks:** Break down the initiative into parallel or sequential work tracks.

## Execution
- On invocation, review existing context, user request, and project goals.
- Generate or update `STRATEGY.md` with the 5 components above.
- Proceed to `/ce-brainstorm` to kick off the core engineering loop.
