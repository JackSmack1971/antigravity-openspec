---
name: 05-ki-governance
globs: ["**/*"]
alwaysApply: true
---
# Knowledge Item (KI) Governance

## KI Taxonomy (Domain × Purpose)
KIs must be categorized by Domain (Engineering, Security, PM, etc.) and Purpose:
- **Pitfall**: Anti-pattern prevention (Symptom → Root Cause → Fix).
- **Playbook**: Sequential execution guide for specific scenarios.
- **Context**: Project-specific knowledge (Architecture, Decisions).
- **Reference**: External standards, APIs, or static documentation.

## Telegraphic Syntax & N-Gram Abbreviation
KIs MUST prioritize density. Use telegraphic writing (minimal articles/conjunctions).
Apply n-gram abbreviations for repeated domain terms (e.g., SDD for Spec-Driven Development).

## Verification (3-Factor Gate)
1. **Actionability**: Are there prescriptive instructions?
2. **Uniqueness**: Is it non-obvious?
3. **Density**: Is it telegraphic?

Every terminal workflow MUST chain to `/retro` for KI extraction.

## KI Conflict Mitigation
To prevent context rot and KI conflicts, enforce a bi-weekly `/para-knowledge` audit. Any updates to existing KIs must trigger a `ki-curator` SemVer bump. This is a calendar-triggered Rule.
