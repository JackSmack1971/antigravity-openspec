---
name: opsx-expanded-path
description: Detailed progression querying schema dependency graphs: new → continue/ff → apply → verify → archive/bulk-archive.
---
# OpenSpec Expanded Path

## Purpose
A detailed, granular progression path for complex features, querying schema dependency graphs throughout the lifecycle.

## Workflow Sequence
1. **new (`/opsx:new`):** Scaffold the initial proposal directory and empty artifacts.
2. **continue/ff (`/opsx:continue` or `/opsx:ff`):** Incrementally generate (`continue`) or fast-forward (`ff`) all planning artifacts based on the schema dependency graph.
3. **apply (`/opsx:apply`):** Execute the implementation phase based on the fully generated artifacts.
4. **verify (`/opsx:verify`):** Validate the actual implementation against the planning artifacts to ensure strict compliance.
5. **archive/bulk-archive (`/opsx:archive` or `/opsx:bulk-archive`):** Archive the single completed proposal or bulk-archive multiple completed changes into the archive directory.
