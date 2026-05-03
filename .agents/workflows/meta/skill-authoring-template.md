---
name: skill-authoring-template
description: Enforces a progressive disclosure format for SKILL.md creation.
---
# /skill-authoring-template — SKILL.md Progressive Disclosure

## Purpose
Invoked to enforce a progressive disclosure format when authoring a new `SKILL.md` file.

## Required Structure
Every `SKILL.md` must strictly adhere to the following 7-part progressive disclosure format to prevent context bloat and ensure fast agent ingestion:

1. **YAML frontmatter:** Contains `name`, `description` (must start with "Use when..."), `version`, `user-invokable`, and `allowed-tools` (Claude Search Optimization).
2. **Overview:** A concise summary of the skill's purpose and governing principle.
3. **When to Use:** Explicit triggers and conditions defining exactly when this skill applies.
4. **Core Pattern / Quick Reference:** The canonical pattern or single most important rule/heuristic to follow.
5. **Implementation:** Step-by-step deterministic instructions for execution.
6. **Common Mistakes + fixes:** Known pitfalls, common agent rationalizations, and their immediate corrections.
7. **Real-World Impact:** Examples of why this skill is necessary and the systemic failure that occurs if it is ignored.
