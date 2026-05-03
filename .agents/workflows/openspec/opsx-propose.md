---
name: opsx-propose
description: Core OpenSpec proposal pipeline (propose, apply, sync, archive). Enforces SHALL/MUST language, Given/When/Then scenarios, and ADDED/MODIFIED/REMOVED deltas.
---
# /opsx:propose — Core OpenSpec Proposal Pipeline
1. **Load openspec/config.yaml (if exists)** → inject `<context>` and `<rules>` for this artifact type.
2. **Check dependency graph**: 
   - `proposal`: requires: [] 
   - `specs`: requires: [proposal] 
   - `design`: requires: [specs] 
   - `tasks`: requires: [design]
3. **HALT if dependency not satisfied**; report which upstream artifact is missing.
4. **`/opsx:propose`** → create openspec/changes/<change-name>/proposal.md with sections:
   - Why (problem statement)
   - What Changes (delta ops: ADDED/MODIFIED/REMOVED)
   - Capabilities (new/changed user-facing capabilities)
   - Rollback Plan (per artifact rules injection from config.yaml if configured)
5. **`/opsx:apply`** → load tasks.md; work through tasks; check off completed items; update artifacts.
6. **`/opsx:sync`** → re-read all artifacts; verify consistency; flag any deltas.
7. **`/opsx:archive`** → mark change complete; archive to openspec/archive/<name>/; chain → /retro.
8. **Format rules**: 
   - ALL requirement language uses SHALL/MUST.
   - Scenarios use Given/When/Then.
   - Deltas use ADDED/MODIFIED/REMOVED ONLY.
