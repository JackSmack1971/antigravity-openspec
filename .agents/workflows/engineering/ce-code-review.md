---
name: ce-code-review
description: Multi-persona code review (CORRECTNESS, SECURITY, MAINTAINABILITY). Blocks ship on FAIL. Includes security scanning and React best practices audits.
---
# /ce-code-review — Multi-Persona Review
1. **Load ce-correctness-reviewer skill (Layer 2)**
2. **Run 3-persona review** (logic → behavioral → concurrency)
3. **Output JSON review artifact** to .agents/artifacts/review_<timestamp>.json
4. **If verdict=FAIL**: block /ship; present fix list to user; HALT
5. **If verdict=WARN**: present warnings; user decision gate
6. **Load security-scanning skill** if: auth / database / API / infra files changed
7. **Security gate**: MitigationPlan coverage must be ≥ 0.8 (Rule 03)
8. **Load react-best-practices skill** if: .tsx/.jsx files changed; self-audit CRITICAL rules
9. **Final**: output walkthrough summary to .agents/artifacts/review_summary.md
