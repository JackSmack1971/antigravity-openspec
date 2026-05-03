---
name: opsx-propose
description: Sequence triggers AI generation of planning artifacts based on schema dependencies. Slash command: /opsx:propose
---
# /opsx:propose — OpenSpec Proposal Generation

## Purpose
Used to propose new features or changes using OpenSpec artifacts. The sequence triggers AI generation of planning artifacts based on schema dependencies.

## Sequence
1. **Invocation:** User invokes `/opsx:propose "idea"`.
2. **Directory Creation:** Agent creates `openspec/changes/<name>/` architecture.
3. **Artifact Generation:** Agent generates planning artifacts based on schema dependencies inside the new directory.
4. **Handoff:** The proposal is now ready for `/opsx:apply`.
