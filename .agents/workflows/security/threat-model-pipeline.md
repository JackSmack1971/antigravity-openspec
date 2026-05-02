---
name: threat-model-pipeline
description: Implicit sequential invocation for defense-in-depth orchestration. Slash command: /security-threat-modeling-pipeline
---
# /security-threat-modeling-pipeline (Chain B)

## Purpose
An interconnected, defense-in-depth orchestration workflow used for comprehensive security hardening and threat modeling prior to shipping.

## Sequential Invocation
This workflow enforces a strict implicit sequence:
1. **STRIDE analysis:** Systematically identify threats (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) against the system architecture.
2. **Security requirement extraction:** Translate identified threats into actionable security requirements and constraints.
3. **Attack tree construction:** Map exploitation paths using risk-prioritized logic.
4. **Threat mitigation mapping:** Map the identified risks and attack paths to specific mitigations and code-level defenses.
5. **SAST configuration generation:** Enforce continuous automated scanning of the mitigated threats.

