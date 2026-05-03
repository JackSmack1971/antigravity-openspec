---
name: browse
description: Persistent headless Chromium daemon (Playwright) wrapper. Reuses browser sessions across calls to maintain stateful memory and context. Triggers on "browse to", "check website", "open browser", "persistent browser", "browser session".
version: 1.0.0
---

# browse — Persistent CDP Browser

## Purpose
Enables persistent, stateful browser interactions that maintain session memory across multiple tool calls. This is optimized for long-running QA sessions, deep research, and multi-page regression testing.

## Core Mechanics
- **Persistent Daemon**: Uses a background Playwright/Chromium process.
- **GBrain Integration**: Syncs browser state (cookies, local storage, session variables) with the agent's persistent memory.
- **CDP Loop**: Follows the standard `agent-browser` snapshot-and-ref loop but preserves session context between discrete tasks.

## Usage in Workflows
- **/review**: Used to fetch and compare live UI diffs.
- **/qa**: Used for executing end-to-end regression tests that require authenticated sessions.
