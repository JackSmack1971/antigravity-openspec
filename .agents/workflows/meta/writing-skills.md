---
name: writing-skills
description: Use when a new capability is needed. Enforces Test-Driven Development (TDD) on SKILL.md files.
---
# /writing-skills — TDD Skill Authoring (Chain E)

## Trigger
Use this workflow when you need to author a new SKILL.md file from scratch or when editing an existing skill to ensure it achieves 100% compliance with L0 Foundational Rules.

## Step 1: RED Phase (Baseline WITHOUT skill)
1. Identify the non-obvious technique or broadly applicable pattern needed.
2. Create pressure scenarios: time pressure, sunk cost, authority, "this is obvious".
3. Run the subagent **WITHOUT** the new skill.
4. Record exact rationalizations and failure modes. Document what shortcuts the agent took and what rules it bypassed.

## Step 2: WRITE Phase
1. Author a minimal `SKILL.md`.
2. Address ONLY the documented failures from the RED Phase.
3. Ensure the YAML frontmatter strictly follows Claude Search Optimization (CSO): `description` MUST start with "Use when..." and describe ONLY the trigger condition, not the process.

## Step 3: GREEN Phase (Run with skill)
1. Re-run identical pressure scenarios **WITH** the newly authored skill.
2. **Quality Gate:** 100% compliance is required. The skill must force the agent to adhere to L0 Foundational Rules under all pressure scenarios.
3. 72% baseline compliance is INSUFFICIENT for production.
4. Any failure → Return to Step 2 (WRITE).

## Step 4: REFACTOR Phase (Harden)
1. Identify any new loopholes exposed during the GREEN phase. Plug them and re-verify.
2. Verify token budget constraint: Ensure the markdown body is `<500` words. If longer, extract sections using the `@filename` reference pattern.
3. Re-verify the CSO frontmatter constraint.

## Output
A highly compliant, production-ready `SKILL.md` capable of withstanding L0 Foundational Rules bypass attempts.
