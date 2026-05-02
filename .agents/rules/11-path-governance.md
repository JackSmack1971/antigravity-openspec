---
name: 11-path-governance
description: Enforce repo-relative pathing globally to ensure portability and prevent Windows path pitfalls.
globs: ["**/*.md", "**/*.plan", "**/*.spec"]
alwaysApply: true
---
# Rule 11 — Path Governance

*Activation Mode: Always On*

## 1. Repo-Relative Mandate
To ensure portability across different host operating systems (Windows, macOS, Linux) and to prevent "Access Denied" errors in MCP tools:
- **Rule:** ALL file references in plans, specifications, and walkthroughs MUST use repo-relative paths (e.g., `./src/main.js` or `docs/plan.md`).
- **Forbidden:** Never use absolute paths (e.g., `C:\workspaces\...` or `/Users/name/Code/...`) unless explicitly requested for system-level configuration outside the workspace.

## 2. Anti-Absolute Quality Gate
Before creating or updating any `implementation_plan.md`, `task.md`, or `walkthrough.md` artifact, the agent MUST:
1. Scan for any absolute path strings.
2. Convert them to repo-relative format relative to the workspace root.
3. Assert compliance in the internal reasoning trace.

## 3. Tool Interaction
When using built-in tools like `view_file` or `write_to_file`, the agent may use absolute paths for the tool call itself (to satisfy API requirements), but the *content* of the generated files must adhere to Rule 11.1.

## 4. Conflict Resolution
If a legacy document contains absolute paths, the agent MUST normalize them to repo-relative paths during the first "Surgical Edit" of that document.

## 5. Tool Path Normalization (Windows Protocol)
When calling built-in tools (e.g., `view_file`, `list_dir`) on Windows hosts, the agent MUST use absolute paths to ensure compatibility with Windows host restrictions.
- **Protocol**: Resolve repo-relative paths to absolute workspace paths *internally* for the tool call.
- **Mandate**: NEVER use relative paths with built-in tools on Windows. The absolute path acts as a "Trust Anchor" for the Windows OS bridge.
- **Trust Anchor Handshake**: If a tool fails with "Access Denied", the agent MUST explicitly log the attempt to verify the absolute path against the `mcp_filesystem_list_allowed_directories` or known workspace anchors before escalating.
- **Verification**: If a tool fails, retry ONCE with the fully qualified absolute path before declaring a Strike.
