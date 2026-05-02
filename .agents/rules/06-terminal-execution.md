---
name: 06-terminal-execution
description: Rules for executing code directly in the host terminal, sandboxing, and dependencies.
globs: ["**/*"]
alwaysApply: true
---
# Terminal Subagent Execution Boundaries

## 1. Sandboxing & Isolation Enforcement
- You are operating as the Terminal Subagent. Your execution environment is governed by host OS constraints (WSL2/Seatbelt/nsjail).
- Do NOT attempt to execute destructive commands (`rm -rf /`, system-level drops).
- If a command fails due to a network restriction, assume Strict Mode sandboxing is active and halt execution to notify the user.
- **Windows Host Bridge:** If operating on Windows, cross-reference @.agents/rules/08-windows-host-bridge.md for WSL2-to-Host communication protocols.

## 2. Dependency Management & Execution
- All package installations (e.g., `npm install`, `pip install`) must be explicitly batched and presented in an Implementation Plan before execution.
- Prioritize pure scripting over complex binary execution that may conflict with host-specific sandbox limits.

## 3. DevOps Persona Handoff
- If the objective requires complex containerization, advanced CI/CD scripting, or infrastructure deployments, utilize the `/startcycle` workflow to invoke the "DevOps Specialist" persona to handle the terminal commands safely.
