---
name: core-loop
description: Use for any page interaction task. Maintains referential DOM validation via CDP snapshot-and-ref. Always re-snapshot after any page state change.
---
# /core-loop — Snapshot-and-Ref (CDP Referential DOM Validation)

## Source
Derived from: `vercel agent browser skill agent audit report.md`, Section 2, Workflow 1.
Upstream spec: https://raw.githubusercontent.com/vercel-labs/agent-browser/main/skill-data/core/SKILL.md

## Purpose
Maintains safe, non-stale element references during agentic browser interaction.
Refs (`@e1`, `@e2`, …) are **invalidated on every page change** — this workflow enforces mandatory re-validation.

## Trigger Conditions
- Any task requiring page interaction (clicking, form filling, navigation)
- Browser session is (or must be) active
- Agent must interact with elements identified via accessibility tree refs

## Prerequisites
```bash
agent-browser install   # first-time: download Chrome for Testing (CDP)
```

## Workflow Steps

### Step 1 — Open URL
```bash
agent-browser open <url>
```
> Launches Chromium CDP session and navigates to target URL.

### Step 2 — Snapshot (Initial)
```bash
agent-browser snapshot -i
```
> Returns compact accessibility tree with fresh `@eN` refs.
> Use `-i` flag to show **interactive elements only** (preferred — token-efficient).

### Step 3 — Interact via Ref
```bash
agent-browser click @eN          # click element by ref
agent-browser fill @eN "value"   # clear + type into field
agent-browser press @eN "Enter"  # keyboard action
```
> Use ONLY refs from the **most recent** snapshot.

### Step 4 — Re-Snapshot (After Every State Change)
```bash
agent-browser snapshot -i
```
> MANDATORY after: clicks that navigate, form submits, dynamic re-renders, dialog opens.
> Loop back to Step 3 as needed.

## REF STALENESS RULE (Hard Stop)
> Refs become stale the moment the page changes.
> **Never reuse a ref across a page state change without re-snapshotting first.**

## Quality Gates
- [ ] `agent-browser install` run at least once (Chrome for Testing present)
- [ ] Re-snapshot taken after every interaction that changes page state
- [ ] Visual screenshot or recording artifact generated upon task completion (Rule 07)
- [ ] L0 compliance: SIMPLICITY FIRST — use `snapshot -i` over full tree unless scoping required

## Example: Full Navigation Interaction
```bash
agent-browser open https://example.com
agent-browser snapshot -i
agent-browser click @e3
agent-browser snapshot -i         # re-snapshot after navigation
agent-browser fill @e5 "search term"
agent-browser press @e5 "Enter"
agent-browser snapshot -i         # re-snapshot after submit
```
