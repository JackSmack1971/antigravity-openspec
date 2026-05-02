---
name: 05-ki-governance
description: Knowledge Item governance — taxonomy, quality gates, and /retro self-improvement flywheel enforcement
alwaysApply: true
---
# KI Governance — Self-Improvement Flywheel

## KI Taxonomy (Domain × Purpose Matrix)
Types: Pitfall | Playbook | Context | Reference
Domains: Engineering | Security | PM | Meta | Architecture

## Telegraphic Syntax Rules
KIs: short sentences, active voice, imperative mood.
n-gram abbreviations: permitted for recurring high-frequency patterns.
Never narrative. Always prescriptive. Length: <300 words per KI artifact.

## Quality Gate (ALL 3 factors required for KI promotion)
1. Actionability: prescriptive instructions present (not just an observation)?
2. Uniqueness: not inferrable from README / config / docs / code comments?
3. Density: telegraphic syntax + n-gram abbreviations applied?
quality_score < threshold → DISCARD. Do not pollute KI store with low-quality entries.

## /retro Mandatory Terminus (Constitutional Invariant)
EVERY /ship, /ce-compound, /opsx:archive, 3-strike resolution MUST chain → /retro.
NO EXCEPTIONS. Missing /retro = INCOMPLETE WORKFLOW. Lifecycle Stop hook enforces.

## KI Update Protocol
When updating existing KI: bump SemVer (patch for minor edits, minor for structural changes).
Never silently overwrite. All edits traceable.

## Bi-Weekly Audit
Run /para-knowledge audit every 2 weeks: resolve KI conflicts, remove stale entries.
KI conflict: two Playbooks with contradictory guidance → ki-curator arbitration.

## Crystallization Timeline
Week 0: baseline (record manual_interventions_week_0).
Week 4: target ≥60% Uplift%. Week 12: target ≥85% Uplift%.
Uplift% = (1 - manual_interventions_N / manual_interventions_0) × 100
Flat curve before Week 4: inspect KI quality scores for low Actionability / low Uniqueness.
