---
name: 04-progressive-disclosure
description: Skill loading protocol — 3-layer progressive disclosure with token budget enforcement
alwaysApply: true
---
# Progressive Disclosure — Skill Loading Protocol

## 3-Layer Loading (STRICT)
Layer 1 — ALWAYS loaded: SKILL.md name + description only (metadata for routing).
Layer 2 — On semantic match: Full SKILL.md payload injected into context.
Layer 3 — On explicit invocation: External scripts + assets loaded via @filename.

## YAML Frontmatter Rule (CSO — Claude/Gemini Search Optimization)
description: MUST start "Use when..." — describes ONLY the trigger condition.
NEVER summarize the skill's process or workflow in the description.
Violating CSO creates a description shortcut that agents exploit to bypass full content.
name: lowercase letters, numbers, hyphens ONLY. No spaces, no underscores.

## 12,000-Character Hard Limit
Rules: ≤12,000 chars. Workflows: ≤12,000 chars. Skills: <500 words body.
Overflow: extract to @filename reference. NEVER truncate. Always externalize.

## Tool Bloat Prevention
NEVER load >3 full skill payloads simultaneously.
Exception: //parallel explicitly justified in workflow comments.
If any request exceeds 3 concurrent full-payload skills: audit AGENTS.md routing.

## Skill Invocation Mandate (Anti-Bypass)
If a task matches a registered skill, YOU MUST invoke it.
NEVER implement directly if a skill applies.
Follow skill instructions exactly — no partial application.
"This is too obvious for a skill" → PROHIBITED rationalization.

## Skill Eligibility Criteria (before authoring new skills)
CREATE when: technique is non-obvious AND pattern is broadly applicable (≥3 use cases).
DO NOT create for: one-off solutions, project-specific conventions (put in CLAUDE.md), mechanical constraints (automate instead).
