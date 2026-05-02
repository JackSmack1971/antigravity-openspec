---
name: state-persist
description: Use to preserve and restore browser session state across separate agent runs. Eliminates repeat logins. Chains state save → state restore via --state flag or AGENT_BROWSER_SESSION_NAME env.
---
# /state-persist — Session Bridging (Cross-Run State Restore)

## Source
Derived from: `vercel agent browser skill agent audit report.md`, Section 2, Workflow 4.
Upstream spec: https://raw.githubusercontent.com/vercel-labs/agent-browser/main/skill-data/core/SKILL.md

## Purpose
Persists authenticated browser session state to disk so subsequent agent runs can resume without
re-authenticating. Eliminates redundant login sequences across separate invocations.

## Trigger Conditions
- Session must be reused across multiple agent runs or pipeline stages
- Login has already been completed (typically via `/login` workflow)
- Task requires a warm session start for efficiency or to avoid auth rate limiting

## Workflow Steps

### Phase A — Save Session State (After Login)
Run this immediately after a successful login to capture the authenticated session:

```bash
agent-browser state save ./auth.json
```
> Writes cookies, localStorage, and session tokens to `./auth.json`.
> Treat this file as a secret — add to `.gitignore`.

### Phase B — Restore Session (Subsequent Runs)

#### Method 1: `--state` Flag (Explicit)
```bash
agent-browser --state ./auth.json open <url>
```
> Loads session from file before navigating. Preferred for explicit, auditable pipelines.

#### Method 2: Named Session (Automatic)
```bash
export AGENT_BROWSER_SESSION_NAME=my-app
agent-browser open <url>   # auto-saves/restores session by name
```
> Session stored in default state directory under `my-app` identifier.
> Useful for long-running agents or persistent dev environments.

## Session File Security (Rule 03)
> `auth.json` contains live session tokens — treat as a secret credential.
> - Add `auth.json` to `.gitignore`
> - Rotate session files after expiry or security events
> - Never commit session files to version control

## State Lifecycle
```
[Login via /login workflow]
       ↓
agent-browser state save ./auth.json
       ↓
[Agent run ends]
       ↓
agent-browser --state ./auth.json open <url>  ← next run resumes here
       ↓
[Session expired? → re-run /login workflow]
```

## Quality Gates
- [ ] `auth.json` excluded from version control (`.gitignore` entry confirmed)
- [ ] Session validated with `snapshot -i` after restore to confirm active state
- [ ] Fallback to `/login` workflow when session is expired or invalid
- [ ] Visual screenshot artifact generated upon task completion (Rule 07)
- [ ] L0 compliance: SIMPLICITY FIRST — use named session for repeated use, `--state` for one-off runs

## Example: Full Save → Restore Pipeline
```bash
# Phase A (after /login workflow completes):
agent-browser state save ./auth.json

# Phase B (next agent invocation):
agent-browser --state ./auth.json open https://app.example.com/dashboard
agent-browser snapshot -i
```
