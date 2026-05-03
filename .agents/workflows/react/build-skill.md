---
name: build-skill
description: Deterministic build and test orchestration for the React Best Practices skill. Slash command: /build-skill
---
# /build-skill — Maintainer Compilation Flow

## Purpose
A deterministic build and test orchestration workflow used by maintainers to compile the React Best Practices skill.

## Workflow Sequence
1. **Dependencies:** Run `pnpm install` to ensure all required dependencies are present.
2. **Compile:** Run `pnpm build`. This step extracts individual markdown rules from the `rules/` directory, compiles them into the canonical `AGENTS.md` payload, and generates the `test-cases.json` suite.
3. **Validate:** Run `pnpm validate` to ensure the generated payload meets schema requirements and token budget limits.
4. **Extract Tests:** Run `pnpm extract-tests` to finalize the test suites for continuous integration.
