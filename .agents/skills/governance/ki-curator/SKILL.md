---
name: ki-curator
description: Governance skill for Semantic Versioning (SemVer) and archival of Knowledge Items (KIs) during their lifecycle. Use for auditing KIs, framework migrations, or version bumps. Triggers: "curate knowledge", "audit KIs", "upgrade KI", "framework migration", "version bump", "archive knowledge", "ki cleanup".
version: 1.1.0
user-invokable: true
---

# ki-curator — Knowledge Item Lifecycle Governance

## Purpose
This skill ensures that the repository's persistent memory (Knowledge Items in `.agents/knowledge/`) remains accurate, non-redundant, and properly versioned. It implements SemVer principles for KI updates and manages the archival process for superseded knowledge.

## Steps (Strict Order)

1. **Inventory**: Run `list_dir` on `.agents/knowledge/` to catalog all KIs. Group them by domain (playbooks, references, pitfalls, etc.) and purpose.
2. **Version Audit**: For each identified KI, read the YAML frontmatter to extract the current `version` field.
3. **Relevance Scoring**: Rate each KI from 1-5 based on the following criteria:
   - (a) **Recency**: How recently was it updated?
   - (b) **Hit Rate**: How often is it referenced? (Check `crystallization-tracker.py` logs).
   - (c) **Uniqueness**: Does it contain unique, non-overlapping information?
4. **Bump**: Apply Semantic Versioning increments:
   - **Patch**: Minor content updates, typo fixes, or small clarifications.
   - **Minor**: Structural changes, instruction updates, or merging non-conflicting KIs.
   - **Major**: Framework migrations, complete paradigm shifts, or breaking instruction changes.
5. **Archive**: Move superseded or deprecated KIs to `.agents/knowledge/archive/<slug>-v<old-version>.md`.
6. **Conflict Detection**: Identify KIs with overlapping `<purpose>` and >80% content similarity.
7. **/para-knowledge Report**: Output a summary table in the following format:
   | KI | Version | Score | Action |
   |---|---|---|---|
   | [Slug] | [vX.Y.Z] | [1-5] | [Keep/Archive/Update/Merge] |

## Rules
- **Archival Before Deletion**: NEVER delete a KI without moving it to the archive directory first.
- **Commit Discipline**: SemVer bumps require a dedicated git commit per batch of updates.
- **Low-Score Flagging**: Any KI with a score ≤2 for 30+ days must be flagged for explicit user review.
- **Conflict Resolution**: Merge overlapping KIs into a single higher-version artifact and archive both original source files.
- **Path Integrity**: Always use repo-relative paths when referencing KIs or archive targets.

## Quality Gates
- [ ] All KIs in `.agents/knowledge/` possess a `version` field in their YAML frontmatter.
- [ ] No two KIs share identical slugs or filenames.
- [ ] The `.agents/knowledge/archive/` directory exists and contains a `.gitkeep` placeholder.
- [ ] Every archival action is logged in `.agents/CHANGELOG.md`.
