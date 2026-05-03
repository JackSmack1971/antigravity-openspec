---
name: threat-model-pipeline
description: Full STRIDE-to-SAST security pipeline. Steps: STRIDE analysis, security requirements, attack tree, mitigation gate (score ≥ 0.8), and SAST config.
---
# /security-threat-modeling-pipeline — Full Security Pipeline
1. **Load security-scanning skill (Layer 2)** + all 5 sub-skills.
2. **Step 1 — STRIDE**: run stride-analysis-patterns → output ThreatModel.md.
3. **Step 2 — REQUIREMENTS**: run security-requirement-extraction → output SecurityRequirements.md.
4. **Step 3 — ATTACK TREE**: run attack-tree-construction (top 3 threats) → output AttackTree.json.
5. **Step 4 — MITIGATION GATE**: run threat-mitigation-mapping → compute coverage score.
   - If coverage < 0.8: HOLD; output fix list; HALT until fixes applied; re-run step 4.
   - If coverage ≥ 0.8: proceed.
6. **Step 5 — SAST CONFIG**: run sast-configuration → output .semgrep.yml + CI pipeline snippet.
7. **RISK-ACCEPT**: for each unmitigated threat: user MUST explicitly accept or remediate.
8. **Output**: SecurityReport.md (summary of all 5 steps + coverage score).
9. **Chain → /retro**: extract Security KI if new threat patterns found.
