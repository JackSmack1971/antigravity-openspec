---
name: login
description: Use for any login or authentication task. Orchestrates the auth vault to isolate credentials from shell history. Chains auth save → open → auth login → wait → snapshot.
---
# /login — Auth Vault Credential Orchestration

## Source
Derived from: `vercel agent browser skill agent audit report.md`, Section 2, Workflow 3.
Upstream spec: https://raw.githubusercontent.com/vercel-labs/agent-browser/main/skill-data/core/SKILL.md

## Purpose
Isolates PII (usernames, passwords) from shell history and environment variables by using the
`agent-browser` auth vault. Credentials are stored once, then referenced by name — never echoed inline.

## Trigger Conditions
- Task requires logging in to a web application
- Credentials must not appear in shell history or agent transcripts
- Session must be persisted after login for downstream tasks (see `/state-persist`)

## Security Constraint (Rule 03)
> NEVER pass credentials inline as CLI arguments or shell env vars.
> ALWAYS use the auth vault (`agent-browser auth save`) for PII isolation.

## Workflow Steps

### Step 1 — Save Credentials to Auth Vault (One-Time Setup)
```bash
agent-browser auth save <app-name> \
  --url <login-url> \
  --username <username> \
  --password-stdin
# Then type password at the prompt — never echoed to shell history
```
> `<app-name>` is a reusable alias (e.g., `my-app`, `staging`, `vercel-prod`).

### Step 2 — Open Login Page
```bash
agent-browser open <login-url>
```

### Step 3 — Execute Auth Login (Vault-Injected)
```bash
agent-browser auth login <app-name>
```
> Retrieves credentials from vault and fills the login form automatically.
> No credentials exposed in shell, agent transcript, or logs.

### Step 4 — Wait for Post-Login URL
```bash
agent-browser wait --url "**/dashboard"
```
> Blocks until the URL matches the post-login destination pattern.
> Customize the glob pattern to match the target app's redirect path.

### Step 5 — Snapshot Post-Login State
```bash
agent-browser snapshot -i
```
> Confirms successful login; captures fresh refs for downstream interaction.

## Credential Vault Management
```bash
agent-browser auth list              # view saved apps
agent-browser auth delete <app-name> # remove stored credentials
```

## Quality Gates
- [ ] Credentials stored via `--password-stdin` only (never inline)
- [ ] `auth login` succeeds before any post-login interaction
- [ ] `wait --url` confirms navigation before snapshotting
- [ ] Visual screenshot artifact generated upon completion (Rule 07)
- [ ] L0 compliance: SECURITY FIRST — no PII in shell history or agent transcript

## Example: Full Login Flow
```bash
# One-time setup (run manually or via secure bootstrap):
agent-browser auth save my-app \
  --url https://app.example.com/login \
  --username admin@example.com \
  --password-stdin

# Repeatable login sequence:
agent-browser open https://app.example.com/login
agent-browser auth login my-app
agent-browser wait --url "**/dashboard"
agent-browser snapshot -i
```
