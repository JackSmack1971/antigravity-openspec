---
name: para-knowledge
description: Bi-weekly KI audit workflow. Use this to audit the knowledge base, detect KI conflicts, and prevent context rot.
---
# /para-knowledge — Bi-Weekly KI Audit Workflow

## Trigger
Calendar alert every 14 days, or manual `/para-knowledge` invocation.

## Purpose
To evaluate the structural integrity of the `knowledge/` store, resolve conflicting guidance, and prevent JIT optimization degradation due to context rot.

## Step 1: Ingest All KI Artifacts
Read all active KIs across `.agents/knowledge/playbooks/` and `.agents/knowledge/pitfalls/`.
Group by Domain and trace triggers.

## Step 2: Conflict Detection (Context Rot Audit)
Identify overlapping triggers across multiple KIs.
For each overlap, analyze the prescriptive instructions:
- Do they contradict each other? (e.g., two RBAC patterns dictating different schemas)
- Are they redundant?
- Is one a subset of the other?

## Step 3: Resolution & SemVer Bump
For conflicting or redundant KIs:
1. Merge the context into a single, cohesive, upgraded KI.
2. Maintain the telegraphic syntax and high density.
3. Run the `ki-curator` skill to bump the SemVer (patch for minor phrasing, minor for structural changes).
4. Archive the deprecated KIs into `.agents/knowledge/references/` or delete them.

## Step 4: Verification
Verify that no duplicate triggers remain.
Confirm all KIs still adhere to the Quality Gate constraints (Actionability, Uniqueness, Density).

## Step 5: Report
Output an audit report detailing merged KIs, version bumps, and total active KIs by domain.
