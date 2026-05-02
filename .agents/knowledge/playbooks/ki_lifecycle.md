---
name: ki-lifecycle
description: Protocols for autonomous Knowledge Item (KI) extraction, persistent memory retrieval, and /retro-driven self-improvement.
version: 1.0.0
---
# Knowledge Item (KI) Lifecycle — Persistent Memory

## Core Pattern
KIs are the *archival* artifacts of the Antigravity system. They bundle summaries and underlying artifacts (code snippets, diagrams, rules) into a global memory store (`~/.antigravity/`).

## The Extraction Engine
- **Passive Extraction**: The system automatically analyzes conversation history and generated artifacts (Walkthroughs, Plans) to formulate new KIs.
- **Trigger**: The completion of a task or the `/retro` command.
- **Structure**: Title + Summary + Artifact Collection.

## Progressive Retrieval
- **Shallow Awareness**: Agents are initially provided only with KI *summaries* to inform baseline responses.
- **Deep Study**: If a summary is semantically relevant to the prompt, the agent "cracks open" the KI to study specific historical artifacts (diffs, docs).

## Operational Rules
1. **Sanitization**: NEVER include secrets (API keys, URIs) in artifacts, as they will be permanently extracted into KIs.
2. **Pruning**: Periodically audit KIs in the Agent Manager to remove "Context Drift" (stale architectural decisions).
3. **High Fidelity**: In `Walkthrough` artifacts, include a "Core Patterns" section to provide high-quality raw material for the extraction engine.

## The /retro Workflow
- Mandated upon session termination by `check-complete.py`.
- Responsible for identifying "Pitfalls" and "Playbooks" to be formalized as KIs.
