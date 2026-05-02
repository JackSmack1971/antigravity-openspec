---
name: 08-windows-host-bridge
description: Handles WSL2 networking and Browser-to-Terminal subagent communication on Windows hosts.
globs: ["**/*"]
alwaysApply: false
---
# Windows Host Bridge & WSL2 Networking

This rule addresses the network isolation between the Terminal Subagent (WSL2) and the Browser Subagent (Native Windows Chrome) on Windows environments.

## 1. Network Bridge Requirement
- Because the Terminal Subagent compiles/runs code in WSL2 and the Browser Subagent tests the UI in Windows, they must communicate via port 9222 (CDP) or local dev ports (e.g., 3000).
- **Mirrored Networking (Windows 11):** If the user is on Windows 11, ensure `%USERPROFILE%\.wslconfig` has `networkingMode=mirrored` enabled.
- **Port Proxy (Windows 10):** If on Windows 10, utilize `netsh interface portproxy` or `socat` tunnels to bridge the gap.

## 2. Localhost Resolution
- Always check if `localhost` in WSL2 resolves to the Windows host IP. If not, use `$(hostname).local` or the internal WSL2 bridge IP.
- If a "Connection Refused" error occurs during UI testing, immediately halt and provide the user with the appropriate `netsh` or `.wslconfig` snippet.

## 3. Visual Verification
- On Windows, visual artifacts (screenshots/recordings) are the ONLY way to verify that the WSL2-to-Windows network bridge is functioning correctly.
- If the Browser Subagent cannot reach the WSL2 dev server, capture the error screen and request a network audit.
