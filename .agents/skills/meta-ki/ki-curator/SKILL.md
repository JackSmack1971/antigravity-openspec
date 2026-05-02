---
name: ki-curator
description: Use when updating, merging, or modifying an existing Knowledge Item (KI) artifact in the `.agents/knowledge/` directory, especially during the bi-weekly `/para-knowledge` audit.
version: 1.0.0
---
# ki-curator — Knowledge Item (KI) Semantic Versioning

## Core Principle
When a Knowledge Item (KI) is updated, merged, or modified to resolve context rot, the artifact MUST have its `version` field in the YAML frontmatter bumped according to Semantic Versioning (SemVer) principles. This ensures a strict audit trail for the agent's persistent memory.

## Trigger Scenarios
- When the `/para-knowledge` workflow detects redundant or conflicting KIs and merges them.
- When the `/retro` workflow updates an existing Pitfall or Playbook KI instead of creating a new one.

## SemVer Bumping Rules
1. **Patch Bump (`x.y.Z`)**: Use for minor phrasing changes, fixing typos, or small clarifications that do not alter the structural instructions or prescriptive rules of the KI.
2. **Minor Bump (`x.Y.z`)**: Use for structural changes, merging multiple KIs into one, updating code snippets to newer standards, or modifying the actionable instructions of the KI.
3. **Major Bump (`X.y.z`)**: Use for complete rewrites of the KI paradigm or domain model.

## Execution Steps
1. Review the existing KI's frontmatter to find the current `version`. (Defaults to `1.0.0` if absent).
2. Determine the correct SemVer bump (Patch or Minor) based on the magnitude of the update.
3. Apply the updated `version` string to the KI's YAML frontmatter.
4. If this update merged multiple KIs, archive the deprecated KIs by moving them to `.agents/knowledge/references/` or permanently deleting them to prevent future conflicts.
5. Ensure the updated KI still adheres to the Quality Gate constraints (Actionability, Uniqueness, Density).
