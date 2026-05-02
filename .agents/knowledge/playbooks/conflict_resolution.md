---
name: conflict-resolution
description: Precedence matrix and rule nesting protocols (@filename) for managing overlapping governance constraints.
version: 1.0.0
---
# Conflict Resolution — Rule Precedence Matrix

## Precedence Hierarchy (Strict)
1. **Security Baseline** (`03-security-baseline.md`) — Highest operational precedence.
2. **Global Constitution** (`00-constitution.md`) — Absolute foundational rules (Karpathy Mandates).
3. **Workspace Rules** (`.agents/rules/*.md`) — Project-specific physics.
4. **Skills** (`.agents/skills/`) — Capability-specific instructions.
5. **Workflows** (`.agents/workflows/`) — Trajectory-specific sequences.

## Rule Activation Modes
- **Always On**: Universal constraints (keep < 1,000 chars to save quota).
- **Glob**: Conditional injection based on file extension (e.g., `*.tsx`).
- **Model Decision**: Semantic triggering based on task description.
- **Manual**: Explicit `@mention` required.

## Modular Architecture (@filename)
- Use `@filename` to pull supplementary context without bloating the main rule.
- **Relative Paths**: Resolve relative to the rule file.
- **Absolute Paths**: Resolve relative to the workspace root if not found as OS absolute.

## Conflict Handling
- Contradictions between rules on the same tier automatically escalate to **STRICT_MODE**.
- If context exceeds 100k tokens, an audit of rule nesting depth is required.
- Use the `/para-knowledge` bi-weekly audit to resolve "Context Rot" in overlapping KIs.
