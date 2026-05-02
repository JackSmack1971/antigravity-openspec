---
name: pressure-testing
description: Subagent-driven development for pressure testing SKILL.md compliance.
---
# /pressure-testing — Subagent Pressure Testing

## Purpose
Dependent on subagent-driven development, this workflow is used to ensure a new skill forces 100% compliance under stress and bypass attempts.

## Procedure
1. **Create multi-pressure scenarios:** Design prompts embedded with psychological or systemic pressure (e.g., time pressure, sunk cost fallacy, false user authority, or "this is obvious" bypass attempts).
2. **Force explicit A/B/C choices:** Provide the subagent with execution options where the incorrect/unsafe choice appears significantly easier or faster.
3. **Run agent with/without skill:** Execute the scenarios first without the skill equipped (establishing a baseline failure rate), then execute again with the newly authored skill equipped.
4. **Observe compliance delta:** Measure the difference in behavior. Did the skill force the agent to reject the easy path and adhere to L0 Foundational Rules? Document exact rationalizations.
5. **Iterate until 100% compliance:** If the subagent fails, rationalizes a shortcut, or bypasses the rules in ANY scenario, return to the skill authoring phase. Harden the skill to plug the loophole, and repeat testing until 100% compliance is achieved. 72% compliance is insufficient for production.
