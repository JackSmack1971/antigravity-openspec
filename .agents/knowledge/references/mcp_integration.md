---
name: mcp-integration
description: Governance and usage protocols for Model Context Protocol (MCP) servers (Context7, GitHub, Filesystem).
version: 1.0.0
---
# MCP Integration & Configuration

This Knowledge Item establishes the standard protocols for utilizing MCP servers within the APEX framework.

## 1. Context7 (Library Documentation)
- **Priority**: Use `context7` as the PRIMARY source for programming library, framework, and API documentation.
- **Workflow**:
    1. Call `resolve-library-id` first to get the exact ID.
    2. Call `query-docs` with the resolved ID.
    3. Use `researchMode: true` ONLY if initial results are insufficient.
- **Constraint**: Prefer `context7` over general web search to avoid hallucinating stale API versions.

## 2. GitHub (Remote Repository Management)
- **Branching**: Use `create_branch` before starting any new feature or fix that requires remote pushing.
- **Pull Requests**: Use `create_pull_request` to submit changes for user review.
- **Governance**: Rule 03 (Security Baseline) mandates that no secrets or `.env` files are ever pushed via MCP.

## 3. Filesystem (Hybrid Access)
- **Built-in vs MCP**:
    - Use **Built-in Tools** (`list_dir`, `view_file`) for absolute paths and direct workspace interaction on Windows.
    - Use **MCP Filesystem** for sandboxed operations or when specifically required by a specialized skill.
- **Constraint**: On Windows hosts, the `filesystem` MCP server may be restricted to specific program directories. Always cross-reference Rule 08 (Windows Host Bridge) and the "Path Resolution Pitfalls" KI.

## 4. MCP Security & Governance
- **Rule 11 (Path Governance)**: ALL file content references generated from MCP tool outputs MUST be repo-relative.
- **Rule 12 (Context Resilience)**: For high-density MCP operations (e.g., massive doc queries), the agent MUST trigger a "Consolidation Cycle" if token count exceeds 80k.
- **Read-Only Default**: Assume all MCP connections are read-only unless an explicit write operation is required by the task.
- **Guard Confirmation**: Destructive operations (delete, push-force) via MCP MUST trigger the `/guard` gate.
