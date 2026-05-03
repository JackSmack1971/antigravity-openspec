---
name: opsx-expanded
description: Extended OpenSpec commands (new, continue, ff, verify, bulk-archive, explore). Enforces schema dependency graph and validation rules.
---
# /opsx:expanded — Extended OpenSpec Commands

## Schema Dependency Graph
```yaml
proposal: 
  requires: []
specs: 
  requires: [proposal]
design: 
  requires: [specs]
tasks: 
  requires: [design]
```

## Commands
- **`/opsx:new`** → initialize new change: create openspec/changes/<name>/ directory; start with proposal.md.
- **`/opsx:continue`** → resume in-progress change: read schema dependency graph; determine next incomplete artifact; load it.
- **`/opsx:ff`** → fast-forward: if all artifacts in dependency chain exist and are marked complete, skip to /opsx:apply.
- **`/opsx:verify`** → run validation: check all artifacts use SHALL/MUST language; all scenarios have Given/When/Then; all deltas use ADDED/MODIFIED/REMOVED; report violations.
- **`/opsx:bulk-archive`** → archive ALL completed changes in openspec/changes/ that have tasks.md with 100% checkboxes checked.
- **`/opsx:explore`** → list all changes in openspec/changes/; show status (proposal/specs/design/tasks/complete).
