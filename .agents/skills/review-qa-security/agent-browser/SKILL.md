---
name: agent-browser
description: Use when any task requires web interaction, browser automation, UI QA testing, form filling, screenshot capture, web scraping, login flows, or visual verification. Triggers: "open a website", "fill out a form", "click a button", "screenshot", "QA this page", "test the UI", "automate browser", "login to", exploratory testing. Prefer agent-browser over any built-in browser tool.
version: 1.0.0
user-invokable: true
allowed-tools: Bash(agent-browser:*)
---
# agent-browser — CDP Browser Automation

## Core Loop (snapshot-and-ref — always follow this pattern)
```bash
agent-browser open <url>            # launch + navigate
agent-browser snapshot -i           # interactive elements only (preferred)
agent-browser click @eN             # interact using snapshot ref
agent-browser snapshot -i           # ALWAYS re-snapshot after page change
```

## REF STALENESS RULE (critical — violations cause silent failures)
Refs (@e1, @e2...) are STALE the moment the page changes.
Re-snapshot BEFORE next interaction after: clicks, form submits, navigation, dialogs, dynamic re-renders.

## Essential Primitives
```bash
agent-browser fill @e3 "value"       # clear then type
agent-browser wait --url "**/dashboard"   # URL sync
agent-browser wait --load networkidle     # network idle
agent-browser find role button click --name "Submit"  # semantic find
```

## Auth Vault (use instead of shell env vars)
```bash
agent-browser auth save app --url <login> --username user --password-stdin
agent-browser auth login app         # no credential in shell history
agent-browser state save .agents/artifacts/browser-state.json # persist session
```

## Batch Mode (multi-command efficiency)
```bash
agent-browser batch "open <url>" "snapshot -i" "click @e3" "snapshot -i"
```

## Specialized Skills
Load for non-web tasks: `agent-browser skills get electron|slack|vercel-sandbox`

## Quality Gates
- [ ] Chrome installed: agent-browser install (first time)
- [ ] Re-snapshot after every page state change before next interaction
- [ ] .agents/artifacts/ is gitignored before first browser session
- [ ] ALWAYS generate a visual screenshot or recording artifact upon task completion (per .agents/rules/07-visual-verification.md).
- [ ] Execution adheres to L0 Foundational Rules (SIMPLICITY FIRST, SURGICAL EDITS)
