---
name: skill-orchestration
description: Governs how skills are matched, invoked, and orchestrated across parallel sub-agents.
---
# Skill Invocation & Orchestration

## Sequence
1. **Determine skill match** — Parse user intent and project context against available `SKILL.md` metadata.
2. **Invoke via skill tool** — Load the full skill payload (Rule 04: Max 3 payloads).
3. **Follow workflow strictly** — Do not skip steps or rationalize bypassing requirements.
4. **Only proceed after required steps** — Complete all verification gates before transitioning.

## Parallel Fan-out
For complex reviews (e.g., during `/ship` or `/review`), the system operates on a parallel fan-out paradigm:
- **Correctness Persona**: Logic, state, and edge cases.
- **Security Persona**: Trust boundaries and STRIDE analysis.
- **Maintainability Persona**: Readability, coupling, and documentation.

## Personas
- Specialized roles with a specific perspective and output format.
- Personas do not spawn other personas; they are orchestrated by the slash-command workflow.
- A merge step deduplicates and synthesizes outputs before human presentation.
