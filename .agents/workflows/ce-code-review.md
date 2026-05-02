---
name: ce-code-review
description: 3-persona tiered code review with confidence gating. Blocks ship if any persona fails. Slash command: /ce-code-review
---
# /ce-code-review — 3-Persona Tiered Review

## Precondition
Requires: SPEC.md (for CORRECTNESS acceptance criteria baseline).
Requires: implementation diff or PR reference.

## Step 1: Fan-out (//parallel — all 3 simultaneously)

**CORRECTNESS** (@apex-reviewer):
Mental execution of code. Check: off-by-one errors, null/undefined propagation, race conditions,
error propagation paths, state machine transitions, async error handling.

**SECURITY** (@apex-security-officer):
Trust boundary violations, SQL/XSS/command injection, hardcoded secrets,
missing authentication/authorization, OWASP top-10, insecure direct object references.

**MAINTAINABILITY** (@apex-reviewer):
Readability, tight coupling, single responsibility violations, dead code,
insufficient test coverage, unclear naming, missing error messages.

Each returns: `{reviewer, verdict: PASS|FAIL|WARN, confidence: 0-100, findings: []}`

## Step 2: Confidence Gate Gate: STRICT_MODE
All PASS with confidence ≥ 85 → proceed to Step 3.
Any FAIL → route to @apex-engineer + /chain-c-debug. Provide structured findings.
Any WARN with confidence < 85 → request specific clarification. Do not block, but flag.
Max 3 review-fix iterations. After 3: escalate to user with all findings across iterations.

## Step 3: Deduplication
Identify overlapping findings across all 3 personas.
Consolidate into single structured report. Remove duplicate findings; keep most specific description.

## Step 4: Slop Scan
Check for: vague implementations, TODO comments in production code,
copy-paste artifacts (repeated logic blocks), incomplete error handling (bare `catch {}`),
magic numbers without named constants.
Any slop found → return to @apex-engineer for cleanup BEFORE PASS issued.

## Output Format
```json
{
  "verdict": "PASS|FAIL",
  "personas": [
    {"reviewer": "CORRECTNESS", "verdict": "PASS", "confidence": 92, "findings": []},
    {"reviewer": "SECURITY", "verdict": "PASS", "confidence": 88, "findings": []},
    {"reviewer": "MAINTAINABILITY", "verdict": "PASS", "confidence": 90, "findings": []}
  ],
  "consolidated_findings": [],
  "slop_detected": false
}
```

## Success Criteria
All 3 personas: PASS, confidence ≥ 85. Slop = 0. Consolidated report generated.
