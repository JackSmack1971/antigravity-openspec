# Agent Architecture Audit Report

**Repository**: https://github.com/phuryn/pm-skills  
**Analysis Date**: May 02, 2026  
**Files Analyzed**: https://raw.githubusercontent.com/phuryn/pm-skills/main/README.md, https://raw.githubusercontent.com/phuryn/pm-skills/main/validate_plugins.py, https://raw.githubusercontent.com/phuryn/pm-skills/main/CONTRIBUTING.md, https://raw.githubusercontent.com/phuryn/pm-skills/main/.claude-plugin/marketplace.json, https://raw.githubusercontent.com/phuryn/pm-skills/main/pm-product-discovery/.claude-plugin/plugin.json, https://raw.githubusercontent.com/phuryn/pm-skills/main/pm-product-discovery/commands/discover.md, https://raw.githubusercontent.com/phuryn/pm-skills/main/pm-product-discovery/skills/opportunity-solution-tree/SKILL.md

## 1. Rules (Persistent Behavioral & Security Constraints)

* Rule 1: Plugin manifest validation (required fields and structure)  
  • Source file: https://raw.githubusercontent.com/phuryn/pm-skills/main/validate_plugins.py  
  • Excerpt: "REQUIRED_MANIFEST_FIELDS = ["name", "version", "description"] ... Name must match directory name ... Version format ... Author validation ... Keywords must be an array"  
  • Implications: Enforces consistent plugin packaging; prevents malformed or misnamed plugins from being installed or validated; behavioral constraint on all marketplace entries.

* Rule 2: Skill and command frontmatter requirements (YAML structure and naming)  
  • Source file: https://raw.githubusercontent.com/phuryn/pm-skills/main/validate_plugins.py  
  • Excerpt: "REQUIRED_SKILL_FIELDS = ["name", "description"] ... REQUIRED_COMMAND_FIELDS = ["description"] ... RECOMMENDED_COMMAND_FIELDS = ["argument-hint"] ... Name must match directory name (agentskills.io spec)"  
  • Implications: All skills/commands must start with --- YAML frontmatter; enforces discoverability and compatibility with Claude Code plugin loader; no frontmatter = validation failure.

* Rule 3: Contribution and naming conventions (nouns vs verbs, no cross-plugin refs)  
  • Source file: https://raw.githubusercontent.com/phuryn/pm-skills/main/CONTRIBUTING.md  
  • Excerpt: "Follow existing patterns: skills are nouns (domain knowledge), commands are verbs (workflows). ... Skill `name` must match its directory name. ... No cross-plugin references in commands. ... Run the validator before submitting: `python3 validate_plugins.py`"  
  • Implications: Persistent behavioral constraint on extensibility; keeps marketplace modular and prevents dependency breakage across the 8 plugins.

* Rule 4: Core PM framework principles embedded in skills (behavioral guardrails)  
  • Source file: https://raw.githubusercontent.com/phuryn/pm-skills/main/pm-product-discovery/skills/opportunity-solution-tree/SKILL.md  
  • Excerpt: "Key principles: - **One outcome at a time.** ... **Opportunities, not features.** ... **Compare and contrast.** Always generate at least 3 solutions per opportunity ... **Discovery is not linear.**"  
  • Implications: Security/quality constraints on AI reasoning; forces structured, non-hallucinated PM decision-making (Teresa Torres, Alberto Savoia frameworks); prevents premature solution-jumping.

* Rule 5: Automatic skill loading with optional force-invocation  
  • Source file: https://raw.githubusercontent.com/phuryn/pm-skills/main/README.md  
  • Excerpt: "Skills are loaded automatically when relevant ... If needed ... you can **force loading skills** with `/plugin-name:skill-name` or `/skill-name`"  
  • Implications: Behavioral constraint on context management; skills act as persistent domain knowledge without explicit user action unless overridden.

## 2. Workflows (Sequential, Slash-Invokable Procedures)

* Workflow 1: /discover  
  • Source file: https://raw.githubusercontent.com/phuryn/pm-skills/main/pm-product-discovery/commands/discover.md  
  • Sequence: Step 1: Understand context (existing/new product) → Step 2: Brainstorm ideas (brainstorm-ideas-* skill) → Step 3: Identify assumptions (identify-assumptions-* skill) → Step 4: Prioritize assumptions (prioritize-assumptions skill) → Step 5: Design experiments (brainstorm-experiments-* skill) → Step 6: Create discovery plan document → Step 7: Offer next steps (PRD, interview, metrics)  
  • Triggers/Dependencies: Invoked via `/discover <product or feature idea>`; chains 4+ skills; accepts uploaded files/research; includes checkpoints for user redirection.

* Workflow 2: Marketplace-wide command invocation pattern  
  • Source file: https://raw.githubusercontent.com/phuryn/pm-skills/main/README.md  
  • Sequence: User types `/command-name` → Claude loads relevant plugin + chained skills → Executes step-by-step workflow → Outputs structured artifact + suggests follow-up commands  
  • Triggers/Dependencies: Slash-command prefix; depends on installed plugins (8 total via marketplace.json); flows between plugins via natural-language suggestions only (no direct cross-ref per rules).

## 3. Skills (Modular Capabilities & Tools)

* Skill 1: opportunity-solution-tree  
  • Source file: https://raw.githubusercontent.com/phuryn/pm-skills/main/pm-product-discovery/skills/opportunity-solution-tree/SKILL.md  
  • Description: Build an Opportunity Solution Tree (OST) to structure product discovery — map outcome → opportunities → solutions → experiments (Teresa Torres framework).  
  • Inputs/Outputs: Input: desired outcome, research data; Output: hierarchical markdown tree + prioritized opportunities/solutions/experiments.  
  • Implementation excerpt: "You are helping a product team build an Opportunity Solution Tree for **$ARGUMENTS**. ... Process: 1. Define outcome 2. Map opportunities 3. Prioritize 4. Generate solutions 5. Design experiments 6. Visualize the tree"

* Skill 2: Generic skill loading / modular PM capability (all 65 skills)  
  • Source file: https://raw.githubusercontent.com/phuryn/pm-skills/main/README.md + https://raw.githubusercontent.com/phuryn/pm-skills/main/pm-product-discovery/.claude-plugin/plugin.json  
  • Description: Domain-specific PM building blocks (ideation, assumption mapping, prioritization, etc.) loaded automatically; each in skills/<name>/SKILL.md with YAML frontmatter.  
  • Inputs/Outputs: Triggered by context or /force; provides frameworks, step-by-step guidance, further reading.  
  • Implementation excerpt: "Each skill encodes a proven PM framework ... walks you through it step by step. ... Skills compatible with other AI assistants via skills/*/SKILL.md"

## 4. Interconnections & Architecture Summary

* How Rules constrain Workflows/Skills:  
  Validate_plugins.py + CONTRIBUTING.md enforce frontmatter, naming, and no cross-plugin refs → guarantees every /command (workflow) can safely chain only intra-plugin skills; principles in SKILL.md (e.g., "one outcome at a time") act as runtime behavioral guardrails inside workflows.

* How Workflows invoke Skills:  
  Commands (e.g., /discover.md) explicitly reference and chain named skills by directory name (brainstorm-ideas-*, identify-assumptions-*, etc.); skills provide the modular execution blocks while workflows orchestrate the sequence + checkpoints + artifact generation.

* Overall agent design insights:  
  Hybrid marketplace architecture: 1 marketplace.json registers 8 plugins → each plugin.json + commands/*.md + skills/*/SKILL.md forms self-contained, installable units. Designed for Claude Code/Cowork but portable (SKILL.md universal format). 65 skills (modular knowledge) + 36 workflows (slash-invokable chains) create an "AI Operating System for PM decisions". Validator ensures structural integrity at contribution time. No security policies beyond MIT license and validation; focus is on deterministic, framework-driven PM rigor.

**End of Report**
