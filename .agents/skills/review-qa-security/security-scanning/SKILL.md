---
name: security-scanning
description: Use when performing security review, running pre-ship security gate, threat modeling a new feature, or when any auth/data/infrastructure change is being made. Triggers: "security review", "threat model", "STRIDE", "OWASP", "before ship", any PR touching auth/database/API/infra.
version: 1.0.0
user-invokable: true
allowed-tools: Read, Write, Bash
---
# security-scanning — Full STRIDE Pipeline

## Pipeline Sequence (no step skippable — each feeds the next)

### Step 1: STRIDE Analysis
Evaluate against ALL 6 categories: Spoofing, Tampering, Repudiation,
Information Disclosure, Denial of Service, Elevation of Privilege.
Output: ThreatModel.md with populated threat matrix.

### Step 2: Security Requirement Extraction
Map threats → SecurityRequirement instances (Given/When/Then).
RequirementSet MUST include traceability: threat_id → requirement → test_case.
Output: SecurityRequirements.md

### Step 3: Attack Tree Construction
Build AttackTree for highest-risk threats (top 3 by impact).
Compute paths: easiest / cheapest / stealthiest.
Output: AttackTree.json + visualization markdown.

### Step 4: Threat Mitigation Mapping (GATE)
Map threats → controls → MitigationPlan. Score coverage (0.0–1.0).
Coverage < 0.8 → HOLD /ship. Generate fix recommendations. Re-run after fixes.
RISK-ACCEPT decision required for every unmitigated threat.
Output: MitigationPlan.md (must show score ≥ 0.8 to pass).

### Step 5: SAST Configuration
Select: Semgrep (default) / SonarQube / CodeQL.
Generate config (YAML) + CI/CD pipeline integration.
Custom rules for identified attack patterns.
Output: .semgrep.yml (or equivalent) + CI/CD pipeline snippet.

## Hard Rules
- Coverage < 0.8 → HOLD /ship. No exceptions.
- Every security requirement → traceable automated test.
- SAST CI/CD gate must be committed before any merge.

## Quality Gates
- [ ] All 6 STRIDE categories documented in ThreatModel.md
- [ ] MitigationPlan coverage score ≥ 0.8
- [ ] SAST config committed to repo with CI/CD integration
