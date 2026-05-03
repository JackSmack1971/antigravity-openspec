---
name: repo-architecture-decisions
description: Key architectural decisions made during the v2026-05 upgrade of antigravity-openspec. Load when making structural changes to .agents/.
version: 1.0.0
purpose: Architecture
domain: Engineering
---

# Repo Architecture Decisions (v2026-05)

This document records the foundational architectural decisions made during the formalization of the `antigravity-openspec` repository.

## 1. 6-Layer Architecture Implementation
The framework is structured into six distinct layers to ensure separation of concerns and deterministic execution:
*   **INPUT Layer**: Managed via `/skill-routing` and intent parsing in `AGENTS.md`.
*   **MEMORY Layer**: Implemented as the 3-file persistent nucleus (`task_plan.md`, `findings.md`, `progress.md`).
*   **CAPABILITY Layer**: Defined by the 13 constitutional rules (`.agents/rules/`) and the 27-skill registry (`.agents/skills/`).
*   **EXECUTION Layer**: Orchestrated via registered workflows (`.agents/workflows/`) and automated Power-Chains.
*   **INTEGRATION Layer**: Handled through `openspec/config.yaml`, `.agents/mcp_config.json`, and CI/CD security gates (`.github/workflows/`).
*   **SELF-IMPROVING LOOP**: Anchored by the `/retro` workflow and automated metrics tracking in `.agents/scripts/`.

## 2. Bootstrapping Order (Rule Separation)
Rules 01-07 were created separately from Rules 00 and 08-12 to facilitate a staged bootstrapping process.
*   **Rationale**: Rules 00-07 establish the foundational "laws of physics" for coding and visual verification. Rules 08-12 introduce advanced host-specific (Windows bridge), metrics (Uplift%), and context (Budget/Resilience) governance.
*   **Legacy Traceability**: Rule 00 contains the original Karpathy Mandates, acting as the root of the constitutional tree.

## 3. OpenSpec Integration (Injection Model)
The `openspec/config.yaml` file acts as a centralized "context injector."
*   **Decision**: All `/opsx:*` workflows MUST load this config first.
*   **Benefit**: This ensures that every generated proposal or specification is grounded in repo-relative paths, project-specific schemas, and non-negotiable architectural invariants without hardcoding them into the workflow files.

## 4. GStack Safety Toolkit (The Chain of Responsibility)
Destructive operations follow a three-stage escalation path:
*   **careful**: Mandatory human review of the diff and potential impact.
*   **guard**: Final execution gate requiring explicit confirmation.
*   **freeze**: Emergency circuit breaker to halt the entire system in case of non-deterministic behavior.

## 5. POWER-CHAINS Design (Pre-wired Invocation)
Power-Chains A–G were designed as pre-wired trajectory programs in `AGENTS.md`.
*   **Decision**: Prioritize automated chaining over manual step-by-step invocation.
*   **Rationale**: Reduces cognitive load on the agent and ensures that mandatory security/verification steps (like SAST gates in Chain B) cannot be skipped by accident.

## 6. Ephemeral Tactical Memory
`progress.md` is explicitly excluded from version control (per `.gitignore`).
*   **Decision**: Tactical memory is session-specific and ephemeral.
*   **Rationale**: Prevents repository pollution with redundant logs and ensures that every session starts with a clean slate while still benefiting from the durable `task_plan.md`.
