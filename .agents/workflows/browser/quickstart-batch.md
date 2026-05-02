---
name: quickstart-batch
description: Use when >1 agent-browser commands are needed in a single session. Avoids per-command startup overhead. Supports string args or JSON stdin.
---
# /quickstart-batch — Multi-Command Serialization

## Source
Derived from: `vercel agent browser skill agent audit report.md`, Section 2, Workflow 2.
Upstream spec: https://raw.githubusercontent.com/vercel-labs/agent-browser/main/README.md

## Purpose
Serializes multiple `agent-browser` commands into a single session invocation.
Eliminates per-command browser startup cost and is the preferred mode for any multi-step automation.

## Trigger Conditions
- Two or more agent-browser commands are required in sequence
- Automation script or pipeline needing efficient single-session execution
- CI/CD or scripted QA runs where overhead matters

## Workflow Steps

### Method A — Inline String Args
```bash
agent-browser batch \
  "open <url>" \
  "snapshot -i" \
  "click @eN" \
  "snapshot -i" \
  "fill @eN value" \
  "snapshot -i"
```

### Method B — JSON Stdin
```bash
echo '[
  {"cmd": "open", "args": ["<url>"]},
  {"cmd": "snapshot", "args": ["-i"]},
  {"cmd": "click", "args": ["@eN"]}
]' | agent-browser batch
```

### Optional: Fail-Fast Mode
```bash
agent-browser batch --bail "open <url>" "click @eN" "snapshot -i"
```
> `--bail` stops execution immediately on first command failure.
> Use in CI pipelines where partial execution is unacceptable.

## Constraints
- Refs (`@eN`) in batch are resolved from the **immediately preceding `snapshot` command** in the sequence
- Re-snapshot commands must be included inline after any state-changing action (same rule as `/core-loop`)
- Commands execute **sequentially** in declaration order — no parallelism

## Quality Gates
- [ ] Snapshot command included before every ref-based interaction within the batch
- [ ] `--bail` flag used in CI/automated contexts to prevent cascading failures
- [ ] Visual screenshot or recording artifact generated upon task completion (Rule 07)
- [ ] L0 compliance: batch size kept minimal (SIMPLICITY FIRST) — no unnecessary commands

## Example: Full Login + Navigation Batch
```bash
agent-browser batch \
  "open https://app.example.com/login" \
  "snapshot -i" \
  "fill @e2 user@example.com" \
  "fill @e3 mypassword" \
  "click @e4" \
  "wait --url **/dashboard" \
  "snapshot -i"
```
