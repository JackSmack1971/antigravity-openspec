---
name: spec
description: Use when starting a new codebase change. Generates the 6-area SPEC.md.
---
# /spec — 6-Area Specification

## Sequence
1. **Understand user intent** — Read the prompt and codebase context.
2. **Ask clarifying questions** — Objective, features, tech stack, and boundaries.
3. **Generate SPEC.md** — Cover the six core areas:
    - **Objective**: Problem statement and success criteria.
    - **Commands**: UI/CLI interactions and expected behaviors.
    - **Structure**: File layout and architectural decisions.
    - **Style**: Aesthetic and code quality standards.
    - **Testing**: Verification evidence and acceptance criteria.
    - **Boundaries**: Always/Ask-First/Never constraints.
4. **Save to repo root** — Write `SPEC.md` to the current workspace root.
5. **Confirm with human** — Wait for explicit approval before proceeding to any implementation.

## Mandatory Human Review Gate
- No implementation code may be written until `SPEC.md` is approved.
- Triggers on the start of any significant codebase change.
