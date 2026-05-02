---
name: 04-progressive-disclosure
globs: ["**/*"]
alwaysApply: true
---
# Progressive Disclosure — Skill Loading Protocol

## Layer 1 (always loaded): SKILL.md name + description only
## Layer 2 (on semantic match): Full SKILL.md payload injected into context
## Layer 3 (on explicit invocation): External scripts + assets loaded

## YAML Frontmatter Rule (CSO)
description: MUST start "Use when..." — describes ONLY trigger condition, never the process.
Violating CSO causes shortcut rationalization. Enforce strictly.

## 12,000-Character Hard Limit
Rules: ≤12,000 chars. Workflows: ≤12,000 chars. Skills: <500 words.
Overflow: extract to @filename reference pattern. Never truncate; always externalize.

## Tool Bloat Prevention
NEVER load >3 full skill payloads simultaneously unless explicit //parallel justification.
