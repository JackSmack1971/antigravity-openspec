---
name: ce-correctness-reviewer
description: Use when performing code reviews, logic audits, or correctness checks on pull requests. Employs a 3-persona tiered model (Logic, Behavioral, Concurrency) and outputs results strictly in JSON format.
version: 1.0.0
triggers: ["code review", "correctness check", "review this code", "check logic"]
---

# ce-correctness-reviewer — JSON-Structured 3-Persona Review

## Overview
This skill implements a deterministic, multi-perspective code review process designed to identify bugs across logic, behavior, and concurrency before code is merged.

## 3-Persona Tiered Review Model
1. **Persona 1 — LOGIC AUDITOR**: Mentally execute every code path. Identify off-by-one errors, null propagation risks, incorrect conditionals, and boundary condition failures.
2. **Persona 2 — BEHAVIORAL AUDITOR**: Cross-reference the implementation against the original spec/intent. Identify missing edge cases and incorrect assumptions about caller or dependency behavior.
3. **Persona 3 — CONCURRENCY AUDITOR**: Analyze for race conditions, shared state mutations without locking, deadlocks, and async ordering issues (e.g., floating promises).

## Confidence Gate
The review process MUST only proceed if your confidence in understanding the codebase and the changes is **≥ 80%**. If confidence is lower, you must halt and request clarification from the user before providing a verdict.

## Output Format
Strictly JSON only. No conversational prose is allowed in the output (Rule 07).

```json
{
  "verdict": "PASS | FAIL | WARN",
  "logic_issues": ["string"],
  "behavioral_issues": ["string"],
  "concurrency_issues": ["string"],
  "fix_required_before_merge": boolean,
  "confidence": 0.0 - 1.0
}
```

## Rules
- **Prose Restriction**: Do not include any text outside the JSON block.
- **Workflow Integration**: This skill is auto-triggered by the `/ce-code-review` workflow and its verdict feeds directly into the `/ship` gate.
