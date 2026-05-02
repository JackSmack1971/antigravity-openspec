---
name: writing-skills
description: Use when creating a new SKILL.md from scratch, editing an existing skill for compliance, or verifying a skill achieves 100% compliance under pressure before deployment. Required before any skill is promoted to always-equip status.
version: 1.0.0
user-invokable: true
allowed-tools: Read, Write, Edit, Bash
---
# writing-skills — TDD for Process Documentation

## Core Principle
Writing skills IS Test-Driven Development applied to process documentation.
Test cases = pressure scenarios. Failing tests = baseline agent failures.
Green = skill achieves 100% compliance. Refactor = close loopholes.
Must strictly enforce L0 Foundational Rules (THINK BEFORE CODING, SURGICAL EDITS, SIMPLICITY FIRST, GOAL-DRIVEN).

## TDD Workflow

### RED Phase (Baseline WITHOUT skill)
1. Identify non-obvious technique or broadly applicable pattern.
2. Create pressure scenarios: time pressure, sunk cost, authority, "this is obvious".
3. Run subagent WITHOUT skill. Record exact rationalizations and failure modes.
4. Document: what shortcuts did the agent take? What did it rationalize away?

### GREEN Phase (Write Skill)
5. Write MINIMAL SKILL.md addressing ONLY the documented failures.
6. Re-run identical pressure scenarios WITH new skill.
7. Verify: 100% compliance required. Ensure skill forces agent to adhere to L0 Foundational Rules. Any failure → return to step 5.

### REFACTOR Phase (Harden)
8. Identify new loopholes exposed in GREEN phase. Plug. Re-verify.
9. Token budget check: body <500 words. Externalize to @file if longer.
10. CSO check: description = "Use when..." ONLY. Zero process summary.

## Frontmatter Requirements (CSO)
name: lowercase letters, numbers, hyphens only.
description: third-person, starts exactly "Use when...", NEVER describes what the skill does.
version: semver string.

## Compliance Thresholds
72% baseline compliance = INSUFFICIENT for production.
100% under all pressure scenarios = ONLY acceptable deployment threshold.

## Quality Gates
- [ ] RED phase documented before writing any SKILL.md content
- [ ] GREEN phase verified with 100% compliance
- [ ] REFACTOR executed at least once
- [ ] description starts "Use when..." with zero process summary
- [ ] Skill explicitly ensures L0 Foundational Rules compliance
