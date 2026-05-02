---
name: sast-deployment
description: Procedural enforcement for SAST tool configuration and CI/CD integration.
---
# SAST Tool Configuration & CI/CD Deployment

## Purpose
Procedural enforcement for scanning integrity, ensuring that static application security testing (SAST) is properly configured and integrated into the deployment pipeline.

## Sequence
1. **Select tool:** Choose the appropriate SAST tool based on language and ecosystem (e.g., Semgrep, SonarQube, CodeQL).
2. **Generate config:** Create the corresponding configuration files (YAML, bash scripts, or tool-specific config formats) tailored to the project's threat model.
3. **Integrate into CI/CD:** Inject the configuration and execution steps directly into the CI/CD pipeline (e.g., GitHub Actions, GitLab CI).
4. **Add custom rules:** Port specific security requirements from the threat modeling phase into custom SAST rules to catch domain-specific vulnerabilities.
5. **Validate:** Execute a dry-run or baseline scan to validate that the tool runs correctly and the rules trigger appropriately without excessive false positives.
