---
name: create-new-rule
description: Rule authoring flow maintaining exact formatting templates. Slash command: /create-new-rule
---
# /create-new-rule — Rule Authoring Flow

## Purpose
A deterministic workflow for authoring new React/Next.js best practice rules, ensuring exact formatting templates are maintained across the skill.

## Workflow Sequence
1. **Copy Template:** Copy `rules/_template.md` to start a new rule.
2. **Rename:** Rename the file using the appropriate area-prefix (e.g., `performance-`, `architecture-`, `security-`).
3. **Fill Content:** Fill out the YAML frontmatter, provide the rule context, and insert the precise code examples (good vs bad patterns).
4. **Compile:** Run `pnpm build` (via `/build-skill`) to integrate the new rule into the master `AGENTS.md` payload.
