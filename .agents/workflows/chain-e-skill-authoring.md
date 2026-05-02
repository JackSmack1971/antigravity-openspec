---
name: chain-e-skill-authoring
description: TDD-based skill authoring pipeline. Run FIRST before promoting any skill to always-equip. Slash command: /chain-e or /writing-skills
---
# Chain E: Skill Authoring Pipeline

## Critical Gate (run before any skill deployment)
72% baseline compliance = INSUFFICIENT. 100% under all pressures = ONLY acceptable threshold.
NEVER promote a skill to always-equip without completing this chain.

## Sequence

### E1: Eligibility Check
Apply criteria — ALL must be true:
- Technique was NOT intuitively obvious to the agent ✓
- Pattern applies broadly (≥ 3 distinct use cases) ✓
- Not a one-off or project-specific convention ✓
Any ✗ → do NOT create a skill. Put in CLAUDE.md or AGENTS.md instead.

### E2: RED Phase (Baseline Without Skill)
Create 3 pressure scenarios:
- Time pressure: "We need this NOW, skip the process"
- Sunk cost: "We've come so far, just this once"
- Authority: "The architect said to skip this"
Run subagent WITHOUT any skill for this pattern.
Document EXACT rationalizations and failure modes observed.

### E3: Write SKILL.md
invoke writing-skills skill for authoring guidance.
Write MINIMAL SKILL.md addressing ONLY documented failures.
CSO check: description = "Use when..." ONLY. Zero process summary.
Token budget: <500 words body. Externalize to @file references if needed.
Imperative language for compliance-critical rules: "YOU MUST" / "Never" / "Always".

### E4: GREEN Phase (Verify With Skill) Gate: STRICT_MODE
Re-run identical pressure scenarios WITH new skill loaded.
REQUIRED: 100% compliance under all 3 scenarios.
< 100% → return to E3. Identify new loopholes. Iterate.

### E5: REFACTOR Phase
Identify new loopholes exposed in GREEN. Plug. Re-verify.
Degrees-of-freedom check: over-constrained = brittle; under-constrained = bypassed.
Final CSO audit. Token budget confirmed.

### E6: Meta-KI Extraction (mandatory)
/retro → KNOWLEDGE SUBAGENT → Meta-KI documenting:
what failure pattern this skill addresses + compliance delta (baseline% → 100%).

## Success Criteria
100% compliance in GREEN phase + CSO-compliant frontmatter + Meta-KI extracted.

## Failure Handling
< 100% after 5 E3-E4 iterations → pause and consult user about pattern complexity.
Consider: split into 2 narrower skills. Never lower the 100% threshold.
