# Agent Architecture Audit Report

**Repository**: https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices  
**Analysis Date**: May 02, 2026  
**Files Analyzed**: https://raw.githubusercontent.com/vercel-labs/agent-skills/main/README.md, https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/react-best-practices/README.md, https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/react-best-practices/SKILL.md, https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/react-best-practices/AGENTS.md, https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/react-best-practices/metadata.json, https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/react-best-practices/rules/_sections.md, https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/react-best-practices/rules/async-parallel.md, https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/react-best-practices/rules/bundle-barrel-imports.md

## 1. Rules (Persistent Behavioral & Security Constraints)

* Rule 1: Use Promise.all() for independent async operations (CRITICAL impact)  
  • Source file: https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/react-best-practices/rules/async-parallel.md  
  • Excerpt: "Incorrect: Sequential awaits. Correct: Promise.all([...]) for concurrent execution (2-10× improvement). Tags: async, parallelization."  
  • Implications: Enforces non-blocking data fetching; agents must refactor sequential awaits in React/Next.js code gen/review to prevent waterfalls.  

* Rule 2: Avoid barrel file imports (CRITICAL impact)  
  • Source file: https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/react-best-practices/rules/bundle-barrel-imports.md  
  • Excerpt: "Do not re-export everything from an index.ts barrel file; import directly from source files."  
  • Implications: Constrains bundling behavior; agents must reject barrel patterns during code generation to prevent bundle bloat and slow builds.  

* Rule 3: All rules follow strict frontmatter + Incorrect/Correct code template  
  • Source file: https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/react-best-practices/rules/_template.md (and _sections.md)  
  • Excerpt: "Frontmatter: title, impact (CRITICAL/HIGH/MEDIUM/LOW), tags. Body: explanation + code blocks labeled Incorrect/Correct."  
  • Implications: Persistent validation constraint; every rule file and generated output (AGENTS.md) must conform or build fails.  

* Rule 4: 8 categorized performance sections with priority ordering  
  • Source file: https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/react-best-practices/rules/_sections.md  
  • Excerpt: "Sections: async- (CRITICAL), bundle- (CRITICAL), rendering- (HIGH), rerender- (HIGH), server- (HIGH), state- (MEDIUM), testing- (LOW), misc- (LOW)."  
  • Implications: Hierarchical constraint; agents must prioritize CRITICAL rules first in any React/Next.js optimization task.  

## 2. Workflows (Sequential, Slash-Invokable Procedures)

* Workflow 1: /build-skill (maintainer compilation flow)  
  • Source file: https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/react-best-practices/README.md  
  • Sequence: pnpm install → pnpm build (extracts rules → generates AGENTS.md + test-cases.json) → pnpm validate → pnpm extract-tests.  
  • Triggers/Dependencies: Triggered on rule changes; depends on src/ build scripts and rule template compliance.  

* Workflow 2: /create-new-rule (rule authoring flow)  
  • Source file: https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/react-best-practices/README.md  
  • Sequence: Copy rules/_template.md → rename with area-prefix (e.g., async-*) → fill frontmatter + examples → run pnpm build.  
  • Triggers/Dependencies: Contributor workflow; depends on _sections.md for valid category/impact.  

* Workflow 3: Agent skill invocation trigger  
  • Source file: https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/react-best-practices/SKILL.md  
  • Sequence: Detect React/Next.js task (writing/reviewing/refactoring) → load AGENTS.md → apply relevant rules by category/impact → output optimized code.  
  • Triggers/Dependencies: When-to-apply section in SKILL.md; depends on metadata.json skill registration.  

## 3. Skills (Modular Capabilities & Tools)

* Skill 1: vercel-react-best-practices  
  • Source file: https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/react-best-practices/SKILL.md  
  • Description: Comprehensive performance optimization guidelines for AI agents generating/reviewing React/Next.js code; bundles 40+ categorized rules with code examples.  
  • Inputs/Outputs: Input: React/Next.js code or task; Output: rule-compliant refactored code or validation report (via AGENTS.md).  
  • Implementation excerpt: "name: vercel-react-best-practices\ndescription: React/Next.js perf optimization for agents\nwhenToApply: writing new components/pages, data fetching, code review, refactoring"  

* Skill 2: Rule compilation & test extraction  
  • Source file: https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/react-best-practices/metadata.json + README.md  
  • Description: Automated build capability that compiles individual rule .md files into single AGENTS.md consumable by LLMs/agents and extracts test cases.  
  • Inputs/Outputs: Input: rules/*.md; Output: AGENTS.md (full guide), test-cases.json.  
  • Implementation excerpt: "version: 1.0.0\norganization: Vercel Engineering\nabstract: performance optimization rules with impact metrics for AI agents"  

## 4. Interconnections & Architecture Summary

* How Rules constrain Workflows/Skills: All 40+ Rules (with impact levels and code examples) are the core payload of the vercel-react-best-practices Skill; every Workflow (build, create, invocation) enforces rule template compliance and category ordering. CRITICAL rules act as hard guardrails in agent code gen.  
* How Workflows invoke Skills: /build-skill and /create-new-rule workflows produce the compiled AGENTS.md that powers the main Skill invocation; agent trigger workflow loads the Skill → applies Rules sequentially by impact.  
* Overall agent design insights: Pure rule-centric skill package (no slash commands in agent runtime); designed for easy npx skills add integration. AGENTS.md serves as the single source of truth for LLM consumption; modular .md rules enable community contributions while build workflow guarantees consistency for agentic React/Next.js systems.  

**End of Report**
