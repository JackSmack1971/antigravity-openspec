# Agent Architecture Audit Report

**Repository**: https://github.com/addyosmani/agent-skills  
**Analysis Date**: Saturday, May 02, 2026  
**Files Analyzed**: https://raw.githubusercontent.com/addyosmani/agent-skills/main/README.md, https://raw.githubusercontent.com/addyosmani/agent-skills/main/docs/getting-started.md, https://raw.githubusercontent.com/addyosmani/agent-skills/main/docs/skill-anatomy.md, https://raw.githubusercontent.com/addyosmani/agent-skills/main/skills/spec-driven-development/SKILL.md, https://raw.githubusercontent.com/addyosmani/agent-skills/main/CLAUDE.md, https://raw.githubusercontent.com/addyosmani/agent-skills/main/AGENTS.md, https://raw.githubusercontent.com/addyosmani/agent-skills/main/.claude/commands/spec.md

## 1. Rules (Persistent Behavioral & Security Constraints)

* Rule 1: Spec-before-code mandate  
  • Source file: https://raw.githubusercontent.com/addyosmani/agent-skills/main/skills/spec-driven-development/SKILL.md  
  • Excerpt: "Write a structured specification before writing any code. ... Code without a spec is guessing."  
  • Implications: Enforces gated progression; no implementation until human-approved SPEC.md exists; surfaces assumptions explicitly before any coding begins.

* Rule 2: Mandatory skill invocation on intent match  
  • Source file: https://raw.githubusercontent.com/addyosmani/agent-skills/main/AGENTS.md  
  • Excerpt: "If a task matches a skill, you MUST invoke it ... Never implement directly if a skill applies. Always follow the skill instructions exactly (do not partially apply them)"  
  • Implications: Prevents ad-hoc coding; agent must check skill applicability first and cannot bypass workflows; anti-rationalization tables block "this is too small" excuses.

* Rule 3: Non-negotiable verification gates & evidence requirements  
  • Source file: https://raw.githubusercontent.com/addyosmani/agent-skills/main/docs/skill-anatomy.md  
  • Excerpt: "Every verification checkbox should be verifiable with evidence (test output, build result, screenshot, etc.)"  
  • Implications: Every skill ends with explicit checklist; agent cannot declare completion without proof; applies across all lifecycle phases.

* Rule 4: Boundaries (Always/Ask-First/Never) enforcement  
  • Source file: https://raw.githubusercontent.com/addyosmani/agent-skills/main/skills/spec-driven-development/SKILL.md  
  • Excerpt: "Boundaries — Three-tier system: - Always do: ... - Ask first: ... - Never do: ..."  
  • Implications: Hard constraints on actions (e.g., never commit secrets); forces human escalation for high-risk changes; embedded in every spec.

* Rule 5: Anti-rationalization tables as guardrails  
  • Source file: https://raw.githubusercontent.com/addyosmani/agent-skills/main/skills/spec-driven-development/SKILL.md  
  • Excerpt: "Common Rationalizations | Rationalization | Reality | ... 'This is simple, I don't need a spec' | Simple tasks don't need *long* specs, but they still need acceptance criteria."  
  • Implications: Persistent behavioral constraint; counters common agent shortcuts with factual rebuttals; present in every skill.

* Rule 6: Token-conscious & progressive disclosure  
  • Source file: https://raw.githubusercontent.com/addyosmani/agent-skills/main/docs/skill-anatomy.md  
  • Excerpt: "Keep SKILL.md under 500 lines — put detailed reference material in separate files ... Progressive disclosure."  
  • Implications: Rules prevent context bloat; only load full skill when triggered; supports long-running agent sessions.

## 2. Workflows (Sequential, Slash-Invokable Procedures)

* Workflow 1: /spec  
  • Source file: https://raw.githubusercontent.com/addyosmani/agent-skills/main/.claude/commands/spec.md  
  • Sequence: 1. Understand user intent → ask clarifying questions (objective, features, tech, boundaries) → 2. Generate SPEC.md covering six core areas → 3. Save to repo root → 4. Confirm with human before proceeding.  
  • Triggers/Dependencies: Triggered by /spec command or new feature/start of significant change; invokes spec-driven-development skill; human review gate required.

* Workflow 2: Full development lifecycle (DEFINE → PLAN → BUILD → VERIFY → REVIEW → SHIP)  
  • Source file: https://raw.githubusercontent.com/addyosmani/agent-skills/main/README.md  
  • Sequence: /spec (DEFINE) → /plan (PLAN) → /build (BUILD with incremental + TDD) → /test (VERIFY) → /review (REVIEW) → /ship (SHIP); skills auto-activate by context.  
  • Triggers/Dependencies: Slash commands or implicit intent mapping; gated with human reviews at each phase; maps to 20 skills.

* Workflow 3: Spec-driven gated workflow (internal to skill)  
  • Source file: https://raw.githubusercontent.com/addyosmani/agent-skills/main/skills/spec-driven-development/SKILL.md  
  • Sequence: Phase 1: Specify (assumptions + 6-area spec) → Human review → Phase 2: Plan (components/dependencies) → Human review → Phase 3: Tasks (atomic with acceptance/verify) → Phase 4: Implement (via incremental + TDD).  
  • Triggers/Dependencies: New project/feature; living document; update on scope change; commits to repo.

* Workflow 4: Skill invocation & orchestration (OpenCode/Claude)  
  • Source file: https://raw.githubusercontent.com/addyosmani/agent-skills/main/AGENTS.md  
  • Sequence: 1. Determine skill match → 2. Invoke via `skill` tool → 3. Follow workflow strictly → 4. Only proceed after required steps; parallel fan-out for review (code-reviewer + security-auditor + test-engineer).  
  • Triggers/Dependencies: User intent or slash command; personas do not spawn other personas; slash commands orchestrate.

## 3. Skills (Modular Capabilities & Tools)

* Skill 1: spec-driven-development  
  • Source file: https://raw.githubusercontent.com/addyosmani/agent-skills/main/skills/spec-driven-development/SKILL.md  
  • Description: Creates structured PRD/spec before any code; surfaces assumptions; six core sections (objective, commands, structure, style, testing, boundaries).  
  • Inputs/Outputs: Input: vague idea/requirements; Output: SPEC.md artifact + human approval.  
  • Implementation excerpt: "Write a spec document covering these six core areas: ... Spec template: # Spec: [Name] ## Objective ... ## Boundaries ..."

* Skill 2: using-agent-skills (meta-skill)  
  • Source file: https://raw.githubusercontent.com/addyosmani/agent-skills/main/README.md  
  • Description: Maps task types to appropriate skills via flowchart; enables discovery and selective loading.  
  • Inputs/Outputs: Input: current task description; Output: recommended skill(s) to load.  
  • Implementation excerpt: "Use the meta-skill for discovery. Start with the `using-agent-skills` skill loaded. It contains a flowchart that maps task types to the appropriate skill."

* Skill 3: All phase-specific skills (modular, 20 total)  
  • Source file: https://raw.githubusercontent.com/addyosmani/agent-skills/main/docs/skill-anatomy.md  
  • Description: Reusable, structured workflows (idea-refine, planning-and-task-breakdown, incremental-implementation, test-driven-development, frontend-ui-engineering, api-and-interface-design, code-review-and-quality, security-and-hardening, etc.).  
  • Inputs/Outputs: Input: task context/trigger; Output: completed workflow with verification checklist.  
  • Implementation excerpt: "Every skill follows the same structure: YAML frontmatter → Overview → When to Use → Core Process → Common Rationalizations → Red Flags → Verification."

* Skill 4: Agent personas (code-reviewer, test-engineer, security-auditor)  
  • Source file: https://raw.githubusercontent.com/addyosmani/agent-skills/main/AGENTS.md  
  • Description: Specialized roles with perspective/output format; used for parallel review during /ship or /review.  
  • Inputs/Outputs: Input: change to review; Output: structured report per axis (correctness, readability, etc.).  
  • Implementation excerpt: "Personas (agents/<role>.md) — roles with a perspective and an output format. The *who*. ... parallel fan-out with a merge step."

## 4. Interconnections & Architecture Summary

* How Rules constrain Workflows/Skills: Rules (spec-before-code, MUST invoke, verification evidence, boundaries, anti-rationalizations) are embedded in every skill's Rationalizations/Red Flags/Verification sections and CLAUDE.md/AGENTS.md boundaries; they gate all workflows and prevent partial/bypass execution.
* How Workflows invoke Skills: Slash commands (/spec etc. in .claude/commands/) act as entry points that directly invoke matching SKILL.md (e.g. /spec → spec-driven-development); implicit intent mapping in AGENTS.md triggers skills automatically; lifecycle workflow composes multiple skills sequentially or in parallel.
* Overall agent design insights: Layered architecture (Commands orchestrate → Skills provide workflows → Personas provide specialized review → References supply checklists). Designed for any Markdown-supporting agent (Claude, Cursor, Gemini, Copilot, OpenCode); progressive disclosure + token-conscious rules optimize context; anti-rationalization + gated human review creates production-grade guardrails for autonomous coding agents.

**End of Report**
