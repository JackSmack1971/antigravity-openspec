---
name: ki-lifecycle
description: Protocols for autonomous Knowledge Item (KI) extraction, persistent memory retrieval, and /retro-driven self-improvement.
version: 1.1.0
---
# Knowledge Item (KI) Lifecycle — Persistent Memory

## 1. Core Pattern
KIs are the *archival* artifacts of the Antigravity system. They bundle summaries and underlying artifacts into a global memory store.

## 2. The Extraction Engine
- **Passive Extraction**: The system automatically analyzes conversation history and generated artifacts (Walkthroughs, Plans) to formulate new KIs.
- **Trigger**: The completion of a task or the `/retro` command.

## 3. Pitfall Extraction Standard (The 2-Hit Rule)
A manual intervention or recurring blocker becomes a candidate for a "Pitfall KI" if it occurs **twice** within a 7-day period.

### Telegraphic Structure for Pitfalls
- **Symptom**: [What does the error look like?]
- **Root Cause**: [Why did it happen?]
- **Resolution Protocol**: [Detection, Immediate Fix, Prevention steps.]
- **Rule Reference**: [Which rule does this pitfall relate to?]

## 4. Operational Rules
1. **Sanitization**: NEVER include secrets (API keys, URIs) in artifacts.
2. **Pruning**: Periodically audit KIs to remove "Context Drift" (stale architectural decisions).
3. **High Fidelity**: In `Walkthrough` artifacts, include a "Core Patterns" section.

## 5. Progressive Retrieval
- **Shallow Awareness**: Agents read KI *summaries* first.
- **Deep Study**: Agents "crack open" relevant KIs to study specific historical artifacts.

## 6. The /retro Workflow
Mandated upon session termination. Responsible for identifying "Pitfalls" and "Playbooks" using the structure above.
