---
name: path-resolution-pitfalls
description: Handling "Access denied" and "Path outside allowed directories" errors on Windows hosts.
version: 1.1.0
---
# Pitfall: Path Resolution & Filesystem Access (Windows)

## Symptoms
- `MCP Filesystem` returns: `Access denied - path outside allowed directories`.
- Errors when attempting to use absolute paths like `c:\workspaces\...` with MCP tools.

## Root Cause
On Windows systems, the `filesystem` MCP server is often restricted to a specific installation or program directory (e.g., `C:\Users\click\AppData\Local\Programs\Antigravity`) for security sandboxing. It does not have inherent permission to access the entire drive, even if the workspace is located there.

## Resolution Protocol
1.  **Switch to Built-in Tools**: Use the native `list_dir`, `view_file`, and `write_to_file` tools. These tools are designed to work with absolute workspace paths and are not subject to the same MCP sandboxing restrictions.
2.  **Verify Absolute Paths (Tool Level)**: Ensure you are using the full absolute path (starting with `c:\`) for built-in tools to satisfy Rule 11.5 (Tool Path Normalization).
3.  **Repo-Relative Output (Content Level)**: Despite using absolute paths for tool calls, all content written to files MUST remain repo-relative per Rule 11.1.
4.  **Cross-Reference Rule 08**: Always check `08-windows-host-bridge.md` when performing file I/O on Windows.

## Detection Logic
If a `filesystem` MCP call fails with "Access denied", immediately pivot to built-in tools and log a "Path Resolution Pitfall" in the session `/retro`. If token count is high, also trigger a Rule 12 "Consolidation Cycle".
