---
name: codex
description: Multi-AI verification skill. Passes current context to independent AI models for second opinions on high-stakes decisions. Triggers on "second opinion", "verify with codex", "multi-AI", "double check".
version: 1.0.0
---

# codex — Multi-AI Verification

## Purpose
Mitigates single-model hallucination or bias by seeking an independent second opinion from OpenAI Codex (or other high-tier models) via CLI integration.

## Workflow
1. **Context Export**: Bundle the current `task_plan.md`, `findings.md`, and relevant code snippets.
2. **Codex Call**: Execute the `codex` CLI with the bundled context and a specific verification prompt.
3. **Opinion Diff**: Compare the Codex response with your current plan or code.
4. **Disagreement Management**: Explicitly surface any areas where the models disagree for user review.

## Rules
- **High-Stakes Only**: Use ONLY for architectural changes, security fixes, or destructive operations to conserve context budget (Rule 04).
- **Transparency**: ALWAYS state when a second opinion was sought and what the result was.
