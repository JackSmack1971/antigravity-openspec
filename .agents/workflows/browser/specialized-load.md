---
name: specialized-load
description: Use when the task falls outside standard web browser interactions (e.g., Electron apps, Slack, Vercel sandbox, agentcore). Loads the appropriate domain skill before proceeding. Never force core skill for non-web tasks.
---
# /specialized-load — Domain Contextual Skill Loading

## Source
Derived from: `vercel agent browser skill agent audit report.md`, Section 2, Workflow 5.
Upstream spec: https://raw.githubusercontent.com/vercel-labs/agent-browser/main/skills/agent-browser/SKILL.md

## Purpose
Shifts the active agent-browser skill context to a domain-specific extension when the target
environment falls outside standard web browser tasks. Maintains modular boundaries and prevents
misuse of the `core` skill for environments it was not designed for.

## Trigger Conditions
- Task targets an **Electron desktop application** (non-web UI)
- Task involves **Slack** workspace automation
- Task runs in a **Vercel sandbox** or preview deployment environment
- Task requires **agentcore** tooling (internal Vercel agent infrastructure)
- Task involves **dogfooding** (internal Vercel product testing)
- Core web commands fail or produce unexpected results in a specialized environment

## Behavioral Constraint (Rule 5 from Audit)
> Never use the `core` skill for non-web environments.
> ALWAYS load the appropriate specialized skill BEFORE executing any commands.

## Available Skill Domains

| Skill Name       | Target Environment                              |
|------------------|-------------------------------------------------|
| `core`           | Standard web browsers (default)                 |
| `electron`       | Electron desktop applications                   |
| `slack`          | Slack workspace UI automation                   |
| `dogfood`        | Internal Vercel product dogfooding              |
| `vercel-sandbox` | Vercel preview/sandbox deployment environments  |
| `agentcore`      | Vercel internal agent infrastructure tooling    |

## Workflow Steps

### Step 1 — Identify the Target Environment
Determine which domain applies based on the task description.

### Step 2 — List Available Skills (Optional Discovery)
```bash
agent-browser skills list
```
> Displays all available skill modules with version metadata.

### Step 3 — Load the Appropriate Skill
```bash
agent-browser skills get core           # default web browser (reset)
agent-browser skills get electron       # Electron desktop apps
agent-browser skills get slack          # Slack automation
agent-browser skills get dogfood        # Vercel internal dogfooding
agent-browser skills get vercel-sandbox # Vercel preview environments
agent-browser skills get agentcore      # Vercel agent infrastructure
```
> Skills are version-matched and fetched from the upstream registry.
> Load BEFORE issuing any domain-specific commands.

### Step 4 — Execute Using Loaded Skill Commands
After loading, use the skill's documented command set. Each specialized skill may expose
domain-specific primitives beyond the core command set.

### Step 5 — Reset to Core (When Done)
```bash
agent-browser skills get core
```
> Restores default web browser context after specialized task completes.

## Quality Gates
- [ ] Correct skill loaded BEFORE any domain-specific commands are issued
- [ ] `skills list` consulted if target domain is uncertain
- [ ] Core skill restored after specialized task completion
- [ ] Visual screenshot or recording artifact generated upon task completion (Rule 07)
- [ ] L0 compliance: SIMPLICITY FIRST — load only the required skill, not multiple simultaneously

## Example: Electron App Automation
```bash
# Load Electron skill context
agent-browser skills get electron

# Proceed with Electron-specific commands
agent-browser open electron://my-app
agent-browser snapshot -i
agent-browser click @e3

# Restore core when done
agent-browser skills get core
```
