---
name: pitfall-extraction
description: Standardized template and procedure for crystallizing Pitfall Knowledge Items.
version: 1.0.0
---
# Pitfall Extraction Playbook (Crystallization)

This playbook defines the standard for creating high-density, telegraphic Pitfall KIs during the `/retro` phase.

## 1. The 2-Hit Rule
A manual intervention or recurring blocker becomes a candidate for a "Pitfall KI" if it occurs **twice** within a 7-day period.

## 2. KI Structure (Telegraphic)
Each Pitfall KI MUST follow this structure:

### Summary
- **Symptom**: [What does the error look like? (e.g., error code, visual glitch)]
- **Root Cause**: [Why did it happen? (e.g., OS restriction, stale cache)]

### Resolution Protocol
1.  **Detection**: [How do I know I'm hitting this pitfall?]
2.  **Immediate Fix**: [Step-by-step resolution.]
3.  **Prevention**: [How to avoid it next time (e.g., use absolute paths, clear tmp).]

### Context Anchor
- **Rule Reference**: [Which rule does this pitfall relate to? (e.g., Rule 11)]

## 3. Extraction Gate Procedure
1.  **Draft**: Draft the content during the `/retro` thought trace.
2.  **Verify**: Ensure the resolution is falsifiable and tested.
3.  **Commit**: Save as `.agents/knowledge/pitfalls/[kebab-case-name].md`.
4.  **Index**: Link the new KI in `ANTIGRAVITY-KB.md`.

## 4. Quality Gate
- **No Fluff**: Remove all conversational filler.
- **Actionable**: A new agent reading this KI must be able to resolve the issue in < 1 minute.
