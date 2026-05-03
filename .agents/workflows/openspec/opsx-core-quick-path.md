---
name: opsx-core-quick-path
description: A fluid, artifact-driven pipeline for OpenSpec: propose → apply → sync → archive.
---
# OpenSpec Core Quick Path

## Purpose
A fluid, artifact-driven pipeline for rapid feature delivery using the OpenSpec architecture.

## Workflow Sequence
1. **propose (`/opsx:propose`):** Generate planning artifacts based on the initial idea.
2. **apply (`/opsx:apply`):** Implement the changes defined in the planning artifacts, checking off tasks as they are completed.
3. **sync (`/opsx:sync`):** (Optional) Sync delta specifications to the main branch or trunk.
4. **archive (`/opsx:archive`):** Move the completed `openspec/changes/<name>/` directory to `openspec/archive/` and append a timestamp.
