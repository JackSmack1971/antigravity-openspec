# Agent Architecture Audit Report

**Repository**: https://github.com/Fission-AI/OpenSpec  
**Analysis Date**: May 02, 2026  
**Files Analyzed**: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/README.md, https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/opsx.md, https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/commands.md, https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/workflows.md, https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/concepts.md, https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/schemas/spec-driven/schema.yaml, https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/schemas/spec-driven/templates/proposal.md

## 1. Rules (Persistent Behavioral & Security Constraints)

* Rule 1: OpenSpec Philosophy (fluid not rigid, iterative not waterfall, easy not complex, built for brownfield not just greenfield, scalable from personal to enterprises)  
  • Source file: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/README.md  
  • Excerpt: "→ fluid not rigid  
  → iterative not waterfall  
  → easy not complex  
  → built for brownfield not just greenfield  
  → scalable from personal projects to enterprises"  
  • Implications: Constrains all workflows and skills to prioritize flexibility over rigid phase gates; no hardcoded instructions; changes must support wide variety of users/agents/models.

* Rule 2: Artifact Rules Injection from Project Config  
  • Source file: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/opsx.md  
  • Excerpt: "rules:  
  proposal:  
  
  - Include rollback plan  
  - Identify affected teams  
    specs:  
  - Use Given/When/Then format for scenarios"  
    • Implications: Per-artifact behavioral constraints injected as <rules> tags; validated against schema artifact IDs; unknown IDs generate warnings.

* Rule 3: Spec Format & Language Constraints (SHALL/MUST, Given/When/Then, exact markdown headers)  
  • Source file: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/concepts.md  
  • Excerpt: "Specs as source of truth... Requirements and Scenarios using SHALL/MUST... Given/When/Then format" (cross-referenced in schema.yaml instructions)  
  • Implications: Enforces verifiable, testable specs; delta operations limited to ADDED/MODIFIED/REMOVED; constrains AI output in skills to prevent vague or non-delta changes.

* Rule 4: Telemetry & Privacy Constraints  
  • Source file: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/README.md  
  • Excerpt: "OpenSpec collects anonymous usage stats... only command names and version... No arguments, paths, content, or PII. Automatically disabled in CI. Opt-out: export OPENSPEC_TELEMETRY=0"  
  • Implications: Security/privacy guardrail; no PII ever collected; applies globally to all CLI and slash command executions.

## 2. Workflows (Sequential, Slash-Invokable Procedures)

* Workflow 1: /opsx:propose  
  • Source file: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/opsx.md  
  • Sequence: 1. User invokes /opsx:propose "idea" → 2. Creates openspec/changes/<name>/ with proposal.md, specs/, design.md, tasks.md → 3. AI generates planning artifacts per schema dependencies → 4. Ready for /opsx:apply  
  • Triggers/Dependencies: Core profile default; requires no prior artifacts; can transition from /opsx:explore.

* Workflow 2: Core Quick Path (/opsx:propose → /opsx:apply → /opsx:sync → /opsx:archive)  
  • Source file: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/workflows.md  
  • Sequence: propose (planning) → apply (implementation with task check-off) → sync (delta specs to main, optional) → archive (move to archive/ with timestamp)  
  • Triggers/Dependencies: Default `core` profile; fluid (any action anytime); artifacts follow proposal → specs → design → tasks dependency graph.

* Workflow 3: Expanded Path (/opsx:new → /opsx:continue or /opsx:ff → /opsx:apply → /opsx:verify → /opsx:bulk-archive or /opsx:archive)  
  • Source file: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/opsx.md  
  • Sequence: new (scaffold) → continue/ff (incremental or all planning artifacts) → apply → verify (validate impl vs artifacts) → archive/bulk-archive  
  • Triggers/Dependencies: Enabled via `openspec config profile`; /opsx:continue shows ready artifacts based on schema dependencies.

* Workflow 4: /opsx:explore (non-structured thinking)  
  • Source file: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/commands.md  
  • Sequence: Invoke /opsx:explore → AI acts as thinking partner (investigate, compare options) → Transition to /opsx:propose or /opsx:new when ready  
  • Triggers/Dependencies: No structure required; anytime action; no artifact creation until propose.

## 3. Skills (Modular Capabilities & Tools)

* Skill 1: Artifact Generation (proposal/specs/design/tasks)  
  • Source file: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/schemas/spec-driven/schema.yaml  
  • Description: Generates structured artifacts from templates with injected context/rules; enforces dependency graph (proposal requires [], specs requires proposal, etc.)  
  • Inputs/Outputs: Input: slash command + user prompt; Output: markdown files in openspec/changes/<name>/ with exact sections (e.g., Why/What Changes/Capabilities for proposal)  
  • Implementation excerpt: "artifacts: proposal: requires: [] ... specs: requires: [proposal] ... instructions: [full prompt template with <context> and <rules> injection]"

* Skill 2: /opsx:apply (Task Implementation & Check-off)  
  • Source file: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/opsx.md  
  • Description: Executes tasks from tasks.md, updates artifacts as needed, checks off completed items; supports multiple changes  
  • Inputs/Outputs: Input: /opsx:apply [optional change-name]; Output: Code changes + task checkboxes updated  
  • Implementation excerpt: "Works through tasks, checking them off as you go... If juggling multiple changes... infer from conversation"

* Skill 3: Config & Context Injection  
  • Source file: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/opsx.md  
  • Description: Loads openspec/config.yaml; injects project context (<context> tags) and per-artifact rules (<rules> tags) into all skills  
  • Inputs/Outputs: Input: YAML config (schema, context, rules); Output: Augmented AI instructions for every artifact/skill  
  • Implementation excerpt: "Context is prepended to every artifact's instructions... Rules are only injected for matching artifacts... 50KB size limit"

* Skill 4: CLI Integration & Skill Auto-Detection (openspec init/update)  
  • Source file: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/README.md  
  • Description: Initializes project (creates .claude/skills/ or equivalent), updates agent instructions; supports 25+ tools via supported-tools.md paths  
  • Inputs/Outputs: Input: `openspec init` or `update`; Output: Configured workspace with auto-detected slash skills  
  • Implementation excerpt: "openspec init... creates skills in .claude/skills/ (or equivalent) that AI coding assistants auto-detect"

## 4. Interconnections & Architecture Summary

* How Rules constrain Workflows/Skills: Philosophy rules enforce fluid/iterative design across all /opsx: workflows; project config rules + schema validation are injected directly into every skill's prompt templates (via <rules> tags); format rules (Given/When/Then, deltas, checkboxes) are hardcoded in schema.yaml instructions to constrain AI output in artifact skills and apply workflow.  
* How Workflows invoke Skills: Slash commands (/opsx:*) map 1:1 to modular skills (propose invokes artifact generation skill with schema dependency graph; apply invokes task execution skill); CLI commands (init/update) bootstrap skills and refresh instructions; /opsx:continue/ff query the schema dependency graph to determine next skill invocation.  
* Overall agent design insights: Spec-driven (SDD) architecture where schemas define both structure (artifacts + deps) and behavior (prompt templates as skills); fully customizable via editable schema.yaml/templates and config.yaml; agent-agnostic (works via slash commands in 25+ tools); prioritizes modularity and user-editable instructions over hardcoded logic for rapid iteration without package updates.  

**End of Report**
