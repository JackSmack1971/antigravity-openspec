# Agent Architecture Audit Report

**Repository**: https://github.com/wshobson/agents/tree/main/plugins/security-scanning/skills  
**Analysis Date**: May 2, 2026  
**Files Analyzed**: 

- https://raw.githubusercontent.com/wshobson/agents/main/plugins/security-scanning/skills/attack-tree-construction/SKILL.md
- https://raw.githubusercontent.com/wshobson/agents/main/plugins/security-scanning/skills/sast-configuration/SKILL.md
- https://raw.githubusercontent.com/wshobson/agents/main/plugins/security-scanning/skills/security-requirement-extraction/SKILL.md
- https://raw.githubusercontent.com/wshobson/agents/main/plugins/security-scanning/skills/stride-analysis-patterns/SKILL.md
- https://raw.githubusercontent.com/wshobson/agents/main/plugins/security-scanning/skills/threat-mitigation-mapping/SKILL.md

## 1. Rules (Persistent Behavioral & Security Constraints)

* Rule 1: Exhaustive coverage via STRIDE threat modeling (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege)  
  • Source file: https://raw.githubusercontent.com/wshobson/agents/main/plugins/security-scanning/skills/stride-analysis-patterns/SKILL.md  
  • Excerpt: "Core Concepts: STRIDE threat modeling templates... threat matrix"  
  • Implications: Enforces systematic, category-based threat enumeration to prevent incomplete analysis; constrains all downstream skills.

* Rule 2: Defense-in-depth and traceability for security requirements  
  • Source file: https://raw.githubusercontent.com/wshobson/agents/main/plugins/security-scanning/skills/security-requirement-extraction/SKILL.md  
  • Excerpt: "SecurityRequirement dataclass... RequirementSet with traceability"  
  • Implications: Requires explicit mapping of requirements to threats/tests; no orphan requirements allowed; persistent validation logic across agent pipeline.

* Rule 3: Control coverage scoring and gap analysis for mitigations  
  • Source file: https://raw.githubusercontent.com/wshobson/agents/main/plugins/security-scanning/skills/threat-mitigation-mapping/SKILL.md  
  • Excerpt: "MitigationPlan dataclasses; coverage scoring, gap analysis, ControlLibrary"  
  • Implications: Hard constraint on completeness; agents must quantify mitigation effectiveness and flag gaps before proceeding.

* Rule 4: Standardized, reproducible SAST configuration (Semgrep/SonarQube/CodeQL + CI/CD)  
  • Source file: https://raw.githubusercontent.com/wshobson/agents/main/plugins/security-scanning/skills/sast-configuration/SKILL.md  
  • Excerpt: "SAST config for Semgrep, SonarQube, CodeQL; CI/CD integration patterns, custom rules... bash, yaml templates"  
  • Implications: Security guardrail enforcing tool-specific configs and integration patterns; prevents ad-hoc scanning setups.

* Rule 5: Attack path prioritization by risk (easiest/cheapest/stealthiest)  
  • Source file: https://raw.githubusercontent.com/wshobson/agents/main/plugins/security-scanning/skills/attack-tree-construction/SKILL.md  
  • Excerpt: "AttackNode, AttackTree dataclasses... path finding (easiest/cheapest/stealthiest)"  
  • Implications: Persistent behavioral constraint on tree analysis; forces risk-ordered output for all attack modeling.

## 2. Workflows (Sequential, Slash-Invokable Procedures)

* Workflow 1: /security-threat-modeling-pipeline (implicit sequential invocation)  
  • Source file: All 5 SKILL.md files (interconnected)  
  • Sequence: 1. STRIDE analysis → 2. Security requirement extraction → 3. Attack tree construction → 4. Threat mitigation mapping → 5. SAST configuration generation  
  • Triggers/Dependencies: Activated on code/project input; depends on STRIDE patterns first; progressive disclosure via skills.

* Workflow 2: Attack tree construction & analysis sequence  
  • Source file: https://raw.githubusercontent.com/wshobson/agents/main/plugins/security-scanning/skills/attack-tree-construction/SKILL.md  
  • Sequence: Build AttackTree → Add AttackNode(s) → Compute paths (easiest/cheapest/stealthiest) → JSON export → Visualization  
  • Triggers/Dependencies: Triggered post-STRIDE; uses AttackTree builder pattern; depends on threat model input.

* Workflow 3: SAST tool configuration & CI/CD deployment  
  • Source file: https://raw.githubusercontent.com/wshobson/agents/main/plugins/security-scanning/skills/sast-configuration/SKILL.md  
  • Sequence: Select tool (Semgrep/SonarQube/CodeQL) → Generate config (YAML/bash) → Integrate into CI/CD → Add custom rules → Validate  
  • Triggers/Dependencies: Post-mitigation mapping; requires project context.

## 3. Skills (Modular Capabilities & Tools)

* Skill 1: attack-tree-construction  
  • Source file: https://raw.githubusercontent.com/wshobson/agents/main/plugins/security-scanning/skills/attack-tree-construction/SKILL.md  
  • Description: Constructs and analyzes attack trees using dataclass models for nodes/trees, path-finding algorithms, and export capabilities  
  • Inputs/Outputs: Input: threats/attack vectors; Output: AttackTree object + JSON/visualization  
  • Implementation excerpt: "Python AttackNode, AttackTree dataclasses for modeling, path finding (easiest/cheapest/stealthiest), JSON export. Builder pattern."

* Skill 2: sast-configuration  
  • Source file: https://raw.githubusercontent.com/wshobson/agents/main/plugins/security-scanning/skills/sast-configuration/SKILL.md  
  • Description: Generates configuration for Semgrep, SonarQube, CodeQL including CI/CD integration and custom rules  
  • Inputs/Outputs: Input: project type/language; Output: YAML/bash config files + integration scripts  
  • Implementation excerpt: "SAST config for Semgrep, SonarQube, CodeQL; CI/CD integration patterns, custom rules... bash, yaml templates for setup."

* Skill 3: security-requirement-extraction  
  • Source file: https://raw.githubusercontent.com/wshobson/agents/main/plugins/security-scanning/skills/security-requirement-extraction/SKILL.md  
  • Description: Extracts security requirements from threats using STRIDE mappings, generates user stories/tests with full traceability  
  • Inputs/Outputs: Input: threat model; Output: SecurityRequirement dataclass instances + RequirementSet  
  • Implementation excerpt: "SecurityRequirement dataclass model, RequirementExtractor with STRIDE mappings to generate user stories/tests, RequirementSet with traceability."

* Skill 4: stride-analysis-patterns  
  • Source file: https://raw.githubusercontent.com/wshobson/agents/main/plugins/security-scanning/skills/stride-analysis-patterns/SKILL.md  
  • Description: Provides STRIDE threat modeling templates, Threat/ThreatModel Python classes, and threat matrix generation  
  • Inputs/Outputs: Input: system description; Output: populated ThreatModel + markdown matrix  
  • Implementation excerpt: "STRIDE threat modeling templates (markdown doc structure, Python Threat/ThreatModel classes), threat matrix."

* Skill 5: threat-mitigation-mapping  
  • Source file: https://raw.githubusercontent.com/wshobson/agents/main/plugins/security-scanning/skills/threat-mitigation-mapping/SKILL.md  
  • Description: Maps threats to controls/mitigations with coverage scoring, gap analysis, and MitigationPlan dataclasses  
  • Inputs/Outputs: Input: threats/requirements; Output: MitigationPlan + ControlLibrary usage + scores  
  • Implementation excerpt: "SecurityControl, MitigationMapping, MitigationPlan dataclasses; coverage scoring, gap analysis, ControlLibrary."

## 4. Interconnections & Architecture Summary

* How Rules constrain Workflows/Skills: STRIDE exhaustive coverage rule gates all workflows; traceability and gap-analysis rules are enforced inside every skill's dataclass validation and output generation; defense-in-depth propagates from requirements → mitigations → SAST config.
* How Workflows invoke Skills: The top-level threat-modeling pipeline sequentially composes the 5 skills (progressive disclosure pattern); each skill's builder/processor templates are invoked as modular steps within the pipeline.
* Overall agent design insights: This security-scanning skills directory implements a single-responsibility, composable threat-modeling pipeline using pure Python dataclass-based domain models and templates. No hard-coded slash commands or agent-level guardrails here—these are pure modular Skills designed for invocation by higher-level agents/commands in the parent security-scanning plugin. The architecture follows the repo's three-tier minimal-component strategy with progressive disclosure.

**End of Report**
