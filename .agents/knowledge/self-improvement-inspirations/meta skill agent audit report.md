# Agent Architecture Audit Report

**Repository**: https://github.com/obra/superpowers/tree/main/skills/writing-skills  
**Analysis Date**: Saturday, May 02, 2026  
**Files Analyzed**: 

- https://raw.githubusercontent.com/obra/superpowers/main/skills/writing-skills/SKILL.md
- https://raw.githubusercontent.com/obra/superpowers/main/skills/writing-skills/anthropic-best-practices.md
- https://raw.githubusercontent.com/obra/superpowers/main/skills/writing-skills/persuasion-principles.md

## 1. Rules (Persistent Behavioral & Security Constraints)

* Rule 1: Skill frontmatter validation  
  • Source file: https://raw.githubusercontent.com/obra/superpowers/main/skills/writing-skills/SKILL.md  
  • Excerpt: "Frontmatter (YAML): Two required fields: `name` and `description` ... Max 1024 characters total ... `name`: Use letters, numbers, and hyphens only ... `description`: Third-person, describes ONLY when to use (NOT what it does) ... Start with "Use when..." ... NEVER summarize the skill's process or workflow"  
  • Implications: Enforces discoverability and prevents Claude from shortcutting full skill content; violation causes agents to ignore detailed instructions.  

* Rule 2: Claude Search Optimization (CSO) / description constraints  
  • Source file: https://raw.githubusercontent.com/obra/superpowers/main/skills/writing-skills/SKILL.md  
  • Excerpt: "Description = When to Use, NOT What the Skill Does ... The trap: Descriptions that summarize workflow create a shortcut Claude will take ... CRITICAL: NEVER summarize the skill's process or workflow"  
  • Implications: Persistent guardrail against rationalization/shortcutting; forces full skill loading and compliance.  

* Rule 3: Token efficiency & conciseness mandate  
  • Source file: https://raw.githubusercontent.com/obra/superpowers/main/skills/writing-skills/SKILL.md  
  • Excerpt: "Target word counts: ... Frequently-loaded skills: <200 words total ... Other skills: <500 words ... Challenge each piece of information: 'Does Claude really need this explanation?'"  
  • Implications: Hard constraint on context-window consumption; applies to all agent skills in the superpowers framework.  

* Rule 4: Persuasion principle enforcement for compliance  
  • Source file: https://raw.githubusercontent.com/obra/superpowers/main/skills/writing-skills/persuasion-principles.md  
  • Excerpt: "Imperative language: 'YOU MUST', 'Never', 'Always' ... Authority + Commitment + Social Proof ... Bright-line rules reduce rationalization ... No exceptions"  
  • Implications: Security constraint against agent rationalization under pressure (time, sunk cost, authority); ethical boundary: must serve user's genuine interests.  

* Rule 5: Degrees-of-freedom matching & model testing  
  • Source file: https://raw.githubusercontent.com/obra/superpowers/main/skills/writing-skills/anthropic-best-practices.md  
  • Excerpt: "Match the level of specificity to the task's fragility ... Test your Skill with all the models you plan to use ... Default assumption: Claude is already very smart"  
  • Implications: Prevents over/under-constraining agent behavior; enforces empirical validation across models (Haiku/Sonnet/Opus).  

* Rule 6: Skill creation eligibility criteria  
  • Source file: https://raw.githubusercontent.com/obra/superpowers/main/skills/writing-skills/SKILL.md  
  • Excerpt: "Create when: Technique wasn't intuitively obvious ... Pattern applies broadly ... Don't create for: One-off solutions ... Project-specific conventions (put in CLAUDE.md) ... Mechanical constraints (automate instead)"  
  • Implications: Filters noise; only persistent, generalizable judgment calls become skills.  

## 2. Workflows (Sequential, Slash-Invokable Procedures)

* Workflow 1: /writing-skills (TDD-adapted skill authoring)  
  • Source file: https://raw.githubusercontent.com/obra/superpowers/main/skills/writing-skills/SKILL.md  
  • Sequence: 1. Identify need (non-obvious technique/pattern). 2. Run baseline pressure scenario WITHOUT skill (RED). 3. Document exact agent rationalizations/failures. 4. Write minimal SKILL.md addressing those failures. 5. Re-run pressure tests with skill (GREEN). 6. Refactor: identify new loopholes → plug → re-verify (REFACTOR cycle).  
  • Triggers/Dependencies: REQUIRES prior superpowers:test-driven-development skill; uses subagents for pressure testing; mandatory before any skill deployment.  

* Workflow 2: SKILL.md authoring template invocation  
  • Source file: https://raw.githubusercontent.com/obra/superpowers/main/skills/writing-skills/SKILL.md  
  • Sequence: 1. YAML frontmatter (name + "Use when..." description). 2. Overview (core principle). 3. When to Use (symptoms + flowchart if needed). 4. Core Pattern / Quick Reference. 5. Implementation (inline or links). 6. Common Mistakes + fixes. 7. (Optional) Real-World Impact.  
  • Triggers/Dependencies: Invoked inside /writing-skills workflow; progressive disclosure to supporting files.  

* Workflow 3: Pressure-testing with subagents  
  • Source file: https://raw.githubusercontent.com/obra/superpowers/main/skills/writing-skills/SKILL.md (and referenced in testing-skills-with-subagents.md patterns)  
  • Sequence: 1. Create multi-pressure scenarios (time pressure, sunk cost, authority, etc.). 2. Force explicit A/B/C choices. 3. Run agent with/without skill. 4. Observe compliance delta. 5. Iterate until 100% compliance under all pressures.  
  • Triggers/Dependencies: Dependent on /writing-skills; uses subagent-driven-development skill.  

## 3. Skills (Modular Capabilities & Tools)

* Skill 1: writing-skills (meta-skill)  
  • Source file: https://raw.githubusercontent.com/obra/superpowers/main/skills/writing-skills/SKILL.md  
  • Description: Meta-capability for creating, editing, or verifying skills via TDD applied to process documentation.  
  • Inputs/Outputs: Inputs = non-obvious technique/pattern + pressure scenarios; Outputs = validated SKILL.md + supporting files.  
  • Implementation excerpt: "**Writing skills IS Test-Driven Development applied to process documentation.** ... You write test cases (pressure scenarios with subagents), watch them fail (baseline behavior), write the skill (documentation), watch tests pass (agents comply), and refactor (close loopholes)."  

* Skill 2: Claude Search Optimization (CSO) module  
  • Source file: https://raw.githubusercontent.com/obra/superpowers/main/skills/writing-skills/SKILL.md  
  • Description: Keyword-coverage, descriptive naming, and description-crafting capability to ensure future agents discover and load the correct skill.  
  • Inputs/Outputs: Inputs = skill triggers/symptoms; Outputs = optimized description + name.  
  • Implementation excerpt: "Use words Claude would search for: Error messages ... Symptoms ... Synonyms ... Tools ... Descriptive Naming: Use active voice, verb-first: `creating-skills` not `skill-creation`."  

* Skill 3: Persuasion-engine for skill compliance  
  • Source file: https://raw.githubusercontent.com/obra/superpowers/main/skills/writing-skills/persuasion-principles.md  
  • Description: Reusable psychology module (7 principles) to design skills that achieve 72%+ compliance under pressure.  
  • Inputs/Outputs: Inputs = skill type (discipline/guidance); Outputs = imperative language + bright-line rules.  
  • Implementation excerpt: "Authority + Commitment + Social Proof ... 'YOU MUST', 'Never', 'Always' ... 'Every time' ... Bright-line rules reduce rationalization."  

* Skill 4: Concise-authoring & progressive-disclosure engine  
  • Source file: https://raw.githubusercontent.com/obra/superpowers/main/skills/writing-skills/anthropic-best-practices.md  
  • Description: Modular capability for token-efficient writing, degrees-of-freedom calibration, and structure that scales across models.  
  • Inputs/Outputs: Inputs = raw technique; Outputs = SKILL.md under token limits with appropriate specificity.  
  • Implementation excerpt: "Concise is key ... Match the level of specificity to the task's fragility ... Progressive disclosure patterns ... Keep SKILL.md body under 500 lines."  

## 4. Interconnections & Architecture Summary

* How Rules constrain Workflows/Skills:  
  Frontmatter/CSO/token rules rigidly gate the TDD workflow (/writing-skills) and all output SKILL.md files; persuasion principles are mandatory in discipline-enforcing workflows to block rationalization; degrees-of-freedom rule forces workflow to match task fragility; all skills are validated only via subagent pressure tests (no untested documentation allowed).  

* How Workflows invoke Skills:  
  /writing-skills workflow directly invokes CSO, persuasion-engine, and concise-authoring skills at each step (baseline → write → test → refactor); progressive disclosure in SKILL.md structure invokes supporting files/skills only when needed; TDD cycle explicitly calls subagent-driven-development and test-driven-development skills.  

* Overall agent design insights:  
  This directory implements the meta-layer of the superpowers agentic framework: a self-improving skill factory where "writing skills" is itself a skill that enforces TDD on all other agent capabilities. The architecture creates a closed-loop system of persistent rules → testable workflows → modular skills that agents discover/load dynamically, with built-in anti-rationalization and token-efficiency safeguards. No narratives or one-offs allowed—only empirically pressure-tested reference guides.  

**End of Report**
