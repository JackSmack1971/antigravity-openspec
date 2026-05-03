# ANTIGRAVITY-KB Index — Persistent Framework Knowledge

This Knowledge Item serves as the master index for the Antigravity production engineering framework (v2026-05). Monolithic content has been defragmented into modular KIs for optimal context discovery.

## 1. Core Architecture & Governance
- [Repo Architecture Decisions](file:///.agents/knowledge/references/repo_architecture_decisions.md): Decisions made in v2026-05 upgrade.
- [Sub-Agent Architecture](file:///.agents/knowledge/references/subagent_architecture.md): Mechanics of Planner, Terminal, and Browser agents.
- [Conflict Resolution & Precedence](file:///.agents/knowledge/playbooks/conflict_resolution.md): Rule activation modes and the precedence matrix.
- [Progressive Disclosure](file:///.agents/knowledge/playbooks/progressive_disclosure.md): Activation mechanics for Agent Skills.

## 2. Memory & Task Execution
- [KI Lifecycle & Extraction](file:///.agents/knowledge/playbooks/ki_lifecycle.md): Passive memory extraction and /retro mechanics.
- [Pitfall Extraction & Crystallization](file:///.agents/knowledge/playbooks/pitfall_extraction.md): Standardized template for high-density Pitfall KIs.
- [Context Resilience & Budget](file:///.agents/knowledge/playbooks/context_resilience_playbook.md): Power-Chain F protocols and Hallucination Circuit Breaker.
- [Circuit Breaker Reporting](file:///.agents/knowledge/playbooks/circuit_breaker_reporting.md): STRIKE_THREE_HALT report template (Rule 10.4).
- [Session Init Checklist](file:///.agents/knowledge/playbooks/session-init-checklist.md): Mandatory session-start verification to prevent repeated bootstrapping.
- [Task Management & Orchestration](file:///.agents/knowledge/playbooks/task_management.md): Task Lists vs. Task Groups.
- [Visual Verification Protocols](file:///.agents/knowledge/playbooks/visual_verification.md): Standards for screenshots and recordings in walkthroughs.

## 3. Extension Protocols
- [MCP Integration & Configuration](file:///.agents/knowledge/references/mcp_integration.md): Secure bridge to external tools (Context7, GitHub, Filesystem).
- [Upgrade Bootstrap Ordering](file:///.agents/knowledge/pitfalls/upgrade_bootstrap_ordering.md): Correct sequence for new repo bootstrapping.
- [Path Resolution Pitfalls](file:///.agents/knowledge/pitfalls/path_resolution_pitfalls.md): Handling filesystem access errors on Windows.
- [Session Continuity Failure](file:///.agents/knowledge/pitfalls/session_continuity_failure.md): Preventing repeated bootstrapping loops across sessions (18+ hit trigger).

---
> [!NOTE]
> This index is part of the "Vertical Stack Architecture". Always prefer granular KIs over this monolithic index for task-specific reasoning.
