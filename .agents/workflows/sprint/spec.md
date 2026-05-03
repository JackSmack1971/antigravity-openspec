---
name: spec
description: Use when starting a new codebase change. Generates the 6-area SPEC.md.
---
# /spec — Spec-Driven Development
1. **Load `spec-driven-development` skill** (Layer 2).
2. **Ask 5 clarifying questions**:
   - What is the primary objective and success criteria?
   - What is the detailed scope of features?
   - What is the target tech stack and architectural constraints?
   - What are the known security or performance boundaries?
   - What does "Done" look like (acceptance criteria)?
3. **Generate 6-area SPEC.md** (Save to repo root or feature dir).
   - Objective | Commands | Structure | Style | Testing | Boundaries.
4. **Present SPEC.md → HALT** awaiting user approval.
5. **On approval**: Log "SPEC approved" to `progress.md`; proceed to `/ce-plan`.

## Mandatory Human Review Gate
- No implementation code may be written until `SPEC.md` is approved.
- Triggers on the start of any significant codebase change.
