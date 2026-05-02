---
name: writing-skills
description: TDD-adapted skill authoring sequence. Mandatory before deploying any skill.
---
# /writing-skills — TDD Skill Authoring (Chain E)

## Purpose
A mandatory sequence prior to deploying any skill. Enforces Test-Driven Development (TDD) principles to guarantee 100% compliance with L0 Foundational Rules under pressure.

## Mandatory Sequence
1. **Identify need:** Determine the non-obvious technique or broadly applicable pattern that requires a new skill.
2. **Run baseline pressure scenario WITHOUT skill (RED):** Invoke `/pressure-testing` without the skill to establish a baseline of failure.
3. **Document exact agent rationalizations/failures:** Record exactly what shortcuts the agent took and what rules it bypassed during the baseline failure.
4. **Write minimal SKILL.md:** Author the skill using the `/skill-authoring-template`. Address ONLY the documented failures from the RED phase.
5. **Re-run pressure tests with skill (GREEN):** Re-invoke `/pressure-testing` with the new skill equipped. 100% compliance is required.
6. **Refactor (REFACTOR cycle):** Identify new loopholes exposed during GREEN, plug them, check token budgets (<500 words), verify CSO frontmatter constraints, and re-verify until the skill is hardened.
