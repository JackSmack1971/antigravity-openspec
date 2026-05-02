# Agent Architecture Audit Report

**Repository**: https://github.com/garrytan/gstack  
**Analysis Date**: Saturday, May 02, 2026  
**Files Analyzed**: [https://raw.githubusercontent.com/garrytan/gstack/main/README.md, https://raw.githubusercontent.com/garrytan/gstack/main/CLAUDE.md, https://raw.githubusercontent.com/garrytan/gstack/main/ETHOS.md, https://raw.githubusercontent.com/garrytan/gstack/main/ARCHITECTURE.md, https://raw.githubusercontent.com/garrytan/gstack/main/SKILL.md, https://raw.githubusercontent.com/garrytan/gstack/main/AGENTS.md, https://raw.githubusercontent.com/garrytan/gstack/main/docs/skills.md, https://raw.githubusercontent.com/garrytan/gstack/main/review/SKILL.md]

## 1. Rules (Persistent Behavioral & Security Constraints)

* Rule 1: Boil the Lake (prioritize completeness)  
  • Source file: https://raw.githubusercontent.com/garrytan/gstack/main/ETHOS.md  
  • Excerpt: "Prefer complete implementations (full features, 100% tests, edge cases) over shortcuts since AI makes marginal cost near-zero. Boil lakes, flag oceans."  
  • Implications: Forces AI agents to deliver production-grade output (tests, docs, security) rather than incremental prototypes; constrains all skills to avoid partial work.

* Rule 2: Search Before Building (3-layer knowledge policy)  
  • Source file: https://raw.githubusercontent.com/garrytan/gstack/main/ETHOS.md  
  • Excerpt: "Always search existing solutions first (3 layers: tried-and-true, popular, first principles). Eureka moments when conventional is wrong."  
  • Implications: Mandatory pre-build research step injected into every planning/review skill; prevents reinventing the wheel and enforces evidence-based decisions.

* Rule 3: User Sovereignty (recommend-only + AskUserQuestion)  
  • Source file: https://raw.githubusercontent.com/garrytan/gstack/main/ETHOS.md  
  • Excerpt: "AI recommends only; user decides. Always use generation-verification loop, present options via AskUserQuestion, never act unilaterally."  
  • Implications: Core safety invariant across all workflows; no autonomous destructive actions allowed without explicit user confirmation.

* Rule 4: Security & sandbox constraints (localhost-only, dual-listener, careful/freeze/guard)  
  • Source file: https://raw.githubusercontent.com/garrytan/gstack/main/ARCHITECTURE.md  
  • Excerpt: "Localhost-only HTTP server, dual-listener for tunnels (local vs tunnel ports with allowlists), prompt injection defenses implied, careful/freeze/guard skills for destructive ops."  
  • Implications: Hard architectural guardrails; /careful warns, /freeze locks edits, /guard combines; blocks external tool misuse.

* Rule 5: Platform-agnostic + commit discipline  
  • Source file: https://raw.githubusercontent.com/garrytan/gstack/main/CLAUDE.md  
  • Excerpt: "Platform-agnostic, natural language logic... Commit rules: one logical change per commit. Never edit generated SKILL.md directly."  
  • Implications: Enforces clean, reviewable output; generated files are immutable by agents.

## 2. Workflows (Sequential, Slash-Invokable Procedures)

* Workflow 1: /autoplan (full sprint pipeline)  
  • Source file: https://raw.githubusercontent.com/garrytan/gstack/main/docs/skills.md  
  • Sequence: CEO review (/plan-ceo-review) → design review → eng review → DX review → implementation → /review → /qa → /ship.  
  • Triggers/Dependencies: Invoked on feature request; chains multiple specialist skills with intermediate user checkpoints.

* Workflow 2: /review (PR review + fix loop)  
  • Source file: https://raw.githubusercontent.com/garrytan/gstack/main/review/SKILL.md  
  • Sequence: Detect branch/plan → diff analysis → slop scan → critical checks (SQL, trust boundaries) → specialist dispatch (parallel agents) → fix-first (auto or ask) → verification.  
  • Triggers/Dependencies: Triggered on any branch with changes; depends on /browse for context and GBrain memory.

* Workflow 3: /ship (release workflow)  
  • Source file: https://raw.githubusercontent.com/garrytan/gstack/main/docs/skills.md  
  • Sequence: Tests + review + push + open PR; integrates with /land-and-deploy and /canary.  
  • Triggers/Dependencies: Post-/review and /qa; requires /guard safety check.

* Workflow 4: Overall sprint (Think-Plan-Build-Review-Test-Ship-Reflect)  
  • Source file: https://raw.githubusercontent.com/garrytan/gstack/main/README.md  
  • Sequence: /office-hours → /plan-ceo-review → build → /review → /qa → /ship → /retro.  
  • Triggers/Dependencies: Enforced via skill routing rules in CLAUDE.md/AGENTS.md; /freeze and /guard can interrupt.

* Workflow 5: Skill routing (request-type dispatch)  
  • Source file: https://raw.githubusercontent.com/garrytan/gstack/main/CLAUDE.md  
  • Sequence: Parse user request → match to specialist role → invoke corresponding /skill (strategy→CEO, code→eng, etc.).  
  • Triggers/Dependencies: Core routing logic injected at session start.

## 3. Skills (Modular Capabilities & Tools)

* Skill 1: /browse (headless Chromium daemon)  
  • Source file: https://raw.githubusercontent.com/garrytan/gstack/main/docs/skills.md  
  • Description: Persistent browser control for QA, scraping, visual verification; powers /qa and review skills.  
  • Inputs/Outputs: URL or task → screenshots, DOM, actions; persistent session state.  
  • Implementation excerpt: "Headless browser CLI (Playwright) with daemon for stateful browsing."

* Skill 2: /office-hours (CEO diagnostic)  
  • Source file: https://raw.githubusercontent.com/garrytan/gstack/main/docs/skills.md  
  • Description: YC-style product interrogation and reframing for new ideas/features.  
  • Inputs/Outputs: Idea description → structured plan with risks/priors.  
  • Implementation excerpt: "Office Hours — startup diagnostic + builder brainstorm."

* Skill 3: /cso (security audit)  
  • Source file: https://raw.githubusercontent.com/garrytan/gstack/main/docs/skills.md  
  • Description: OWASP + STRIDE automated audits with fix recommendations.  
  • Inputs/Outputs: Repo/branch → security report + /guard enforcement.  
  • Implementation excerpt: "/cso skill (security officer who runs OWASP + STRIDE audits)."

* Skill 4: /qa (browser-based QA + fix loop)  
  • Source file: https://raw.githubusercontent.com/garrytan/gstack/main/docs/skills.md  
  • Description: Real-browser testing, bug finding, and autonomous fixes.  
  • Inputs/Outputs: Staging URL → bug report + proposed patches.  
  • Implementation excerpt: "/qa skill (QA lead who opens a real browser)."

* Skill 5: /codex (multi-AI second opinion)  
  • Source file: https://raw.githubusercontent.com/garrytan/gstack/main/docs/skills.md  
  • Description: Cross-model verification using OpenAI Codex CLI.  
  • Inputs/Outputs: Code/task → alternative analysis from non-Claude model.  
  • Implementation excerpt: "/codex skill (multi-AI second opinion via OpenAI Codex CLI)."

* Skill 6: Safety toolkit (/careful, /freeze, /guard)  
  • Source file: https://raw.githubusercontent.com/garrytan/gstack/main/ARCHITECTURE.md  
  • Description: Destructive-op wrappers with warnings, edit locks, and combined enforcement.  
  • Inputs/Outputs: Command → confirmation or lock state.  
  • Implementation excerpt: "/careful warns on destructive cmds; /freeze locks edits to dir; /guard combines."

(Additional modular skills in skill dirs follow identical SKILL.md.tmpl pattern: preamble + tools + triggers.)

## 4. Interconnections & Architecture Summary

* How Rules constrain Workflows/Skills: Ethos Rules (Boil the Lake, Search Before Building, User Sovereignty) are injected as preambles into every SKILL.md; security Rules (/careful/freeze/guard) are mandatory checkpoints in all release/QA workflows; platform-agnostic rules enforce consistent behavior across Claude/Code, OpenClaw, etc.

* How Workflows invoke Skills: Slash-command router (in CLAUDE.md/AGENTS.md) dispatches user intent to specialist skills; /autoplan and /review explicitly chain multiple skills in sequence with parallel specialist dispatch; GBrain + /browse provide shared memory/context across invocations.

* Overall agent design insights: gstack implements a "virtual engineering team" via 23+ composable, slash-invokable prompt modules that turn a single LLM session into a governed multi-role agency. Rules are enforced at preamble level, workflows are explicit slash pipelines, and skills are self-contained (each with its own SKILL.md + dir implementation). Designed for both solo Claude Code and multi-agent OpenClaw orchestration; heavy emphasis on safety, completeness, and measurable productivity acceleration.

**End of Report**
