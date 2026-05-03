---
name: marketplace-invocation
description: Cross-plugin methodology for Marketplace-wide command invocation.
---
# Marketplace-wide Command Invocation Pattern

## Purpose
A standardized cross-plugin methodology for invoking commands across the agent marketplace. It ensures fluid, continuous workflows that span multiple domains.

## Invocation Pattern
1. **Trigger:** The user types `/command-name` (e.g., `/discover`, `/opsx:propose`).
2. **Plugin Loading:** The master router loads the relevant plugin along with any chained or prerequisite skills.
3. **Execution:** The agent executes the step-by-step workflow as defined in the loaded skill/workflow document.
4. **Output & Handoff:** The workflow culminates by outputting a structured artifact and explicitly suggesting the next logical follow-up commands to maintain momentum.
