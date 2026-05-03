---
name: upgrade-bootstrap-ordering
description: Pitfall — incorrect order when bootstrapping new Antigravity repos causes rules/workflows to reference non-existent files.
version: 1.0.0
purpose: Pitfall
domain: Engineering
---

# Pitfall: Upgrade Bootstrap Ordering

## Symptom
The agent enters a hallucination loop or reports "file not found" errors when attempting to execute slash commands (e.g., `/autoplan`) during a repository upgrade or new environment initialization.

## Root Cause
Incorrect ordering of artifact creation during the formalization phase. Workflows frequently reference Rules for compliance gates, and `AGENTS.md` registers Skills and Workflows by their filesystem paths. If a consumer is created before its dependency, the system breaks.

## Resolution Protocol (The Correct Sequence)
To prevent bootstrapping failures, artifacts MUST be created in the following order:

1.  **Rules**: Establish the constitutional physics (00-12).
2.  **Skills**: Build the atomic capabilities (`SKILL.md` files).
3.  **Workflows**: Author the trajectory programs (`.md` files) that orchestrate the skills.
4.  **AGENTS.md (Master Router)**: Register all slash commands, skills, and power-chains.
5.  **Config**: Author `openspec/config.yaml` and `.agents/mcp_config.json`.
6.  **Validation**: Run the final cross-reference audit pass.

## Prevention
Never register a workflow in `AGENTS.md` before the underlying `.md` file exists in `.agents/workflows/`. Always verify Rule existence before adding compliance gates to a skill.
