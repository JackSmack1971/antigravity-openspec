---
name: chain-b-security
description: Full security hardening pipeline. STRIDE → Requirements → Attack Tree → Mitigations → SAST. Slash command: /chain-b or /security-threat-modeling-pipeline
---
# Chain B: Security Hardening Pipeline

## Trigger
Pre-ship gate (always active). Explicit /chain-b invocation. Any PR touching auth/data/infra.

## Sequence

### B1: STRIDE Analysis
@apex-security-officer: stride-analysis-patterns.
All 6 STRIDE categories documented. ThreatModel.md output with threat matrix.
No shortcuts: all 6 = Spoofing, Tampering, Repudiation, Information Disclosure, DoS, EoP.

### B2: Security Requirement Extraction
security-requirement-extraction skill.
STRIDE threat_id → SecurityRequirement (Given/When/Then) → automated test_case.
RequirementSet with full traceability chain.
Output: SecurityRequirements.md

### B3: Attack Tree Construction
attack-tree-construction skill.
Build AttackTree for top 3 threats by impact.
Path-finding: easiest / cheapest / stealthiest attack vectors.
Output: AttackTree.json + visualization markdown.

### B4: Threat Mitigation Mapping Gate: STRICT_MODE
threat-mitigation-mapping skill.
Map threats → controls (from ControlLibrary) → MitigationPlan.
Coverage score computed (0.0–1.0). Score < 0.8 → HOLD.
Gap analysis: every unmitigated threat → explicit RISK-ACCEPT decision with owner.
Fix cycle: generate recommendations → @apex-engineer → re-run B4. Max 3 cycles.
Output: MitigationPlan.md with score ≥ 0.8.

### B5: SAST Configuration
sast-configuration skill.
Tool: Semgrep default; SonarQube or CodeQL as alternatives.
Generate: .semgrep.yml (or equivalent) + CI/CD pipeline snippet.
Custom rules for attack patterns found in B3.
Validate SAST run: zero critical findings before proceeding.
Output: .semgrep.yml + GitHub Actions pipeline step.

### B6: Security Sign-off
@apex-security-officer: all 5 artifacts verified. Issue Security PASS report.
Chain B blocks /ship until sign-off issued.

## Success Criteria
ThreatModel.md + SecurityRequirements.md + AttackTree.json + MitigationPlan.md (≥0.8) + SAST config committed.

## Failure Handling
Coverage < 0.8 after 3 cycles → escalate to user. Security cannot be bypassed for timeline pressure.
