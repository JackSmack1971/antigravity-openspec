---
name: sast-configuration
description: Generate Static Application Security Testing (SAST) configurations and CI/CD integration for the project.
version: 1.0.0
triggers: ["SAST", "static analysis", "Semgrep", "CI security"]
---

# sast-configuration

## Purpose
Automate security scanning in the development pipeline by configuring static analysis tools.

## Tool Selection Logic
- **Semgrep**: Default choice for general-purpose scanning.
- **SonarQube**: Use for enterprise-grade compliance.
- **CodeQL**: Use for deep analysis in GitHub Actions environments.

## CI/CD Integration
Generate pipeline snippets for:
- GitHub Actions
- GitLab CI
- Jenkins

## Custom Rule Generation
Create specialized SAST rules that target the specific attack patterns identified in the **Attack Tree Construction** phase.

## Output
- Tool configuration file (e.g., `.semgrep.yml`).
- Pipeline definition file (e.g., `.github/workflows/sast.yml`).

## Rules
- **Commit Gate**: SAST configuration MUST be committed before any code merge.
- **Enforcement**: This gate is enforced in the `/ship` workflow.
