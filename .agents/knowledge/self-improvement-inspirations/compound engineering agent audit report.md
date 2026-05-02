# Agent Architecture Audit Report

**Repository**: https://github.com/EveryInc/compound-engineering-plugin  
**Analysis Date**: May 02, 2026  
**Files Analyzed**: https://raw.githubusercontent.com/EveryInc/compound-engineering-plugin/main/README.md; https://raw.githubusercontent.com/EveryInc/compound-engineering-plugin/main/plugins/compound-engineering/README.md; https://raw.githubusercontent.com/EveryInc/compound-engineering-plugin/main/AGENTS.md; https://raw.githubusercontent.com/EveryInc/compound-engineering-plugin/main/CLAUDE.md; https://raw.githubusercontent.com/EveryInc/compound-engineering-plugin/main/.claude-plugin/marketplace.json; https://raw.githubusercontent.com/EveryInc/compound-engineering-plugin/main/plugins/compound-engineering/skills/ce-plan/SKILL.md; https://raw.githubusercontent.com/EveryInc/compound-engineering-plugin/main/plugins/compound-engineering/agents/ce-correctness-reviewer.agent.md

## 1. Rules (Persistent Behavioral & Security Constraints)

* Rule 1: Compound engineering philosophy (each unit of work must make subsequent units easier)  
  • Source file: https://raw.githubusercontent.com/EveryInc/compound-engineering-plugin/main/README.md  
  • Excerpt: "Each unit of engineering work should make subsequent units easier -- not harder. ... Compound engineering inverts this. 80% is in planning and review, 20% is in execution"  
  • Implications: Constrains all skills/workflows to prioritize planning/review/knowledge codification over raw execution; inverts traditional technical debt accumulation

* Rule 2: Repo-relative paths only (never absolute paths)  
  • Source file: https://raw.githubusercontent.com/EveryInc/compound-engineering-plugin/main/plugins/compound-engineering/skills/ce-plan/SKILL.md  
  • Excerpt: "**IMPORTANT: All file references in the plan document must use repo-relative paths (e.g., `src/models/user.rb`), never absolute paths (e.g., `/Users/name/Code/project/src/models/user.rb`). This applies everywhere — implementation unit file lists, pattern references, origin document links, and prose mentions.**"  
  • Implications: Enforces portability across machines/worktrees/teammates; applies to all plans, reviews, and artifacts

* Rule 3: Always plan when directly invoked (no abandonment)  
  • Source file: https://raw.githubusercontent.com/EveryInc/compound-engineering-plugin/main/plugins/compound-engineering/skills/ce-plan/SKILL.md  
  • Excerpt: "**When directly invoked, always plan.** Never classify a direct invocation as 'not a planning task' and abandon the workflow. If the input is unclear, ask clarifying questions or use the planning bootstrap... but always stay in the planning workflow."  
  • Implications: Prevents workflow exit on ambiguous input; forces interactive clarification via blocking user-question tools

* Rule 4: Decisions not code (plans contain approach/rationale only)  
  • Source file: https://raw.githubusercontent.com/EveryInc/compound-engineering-plugin/main/plugins/compound-engineering/skills/ce-plan/SKILL.md  
  • Excerpt: "**Decisions, not code** - Capture approach, boundaries, files, dependencies, risks, and test scenarios. Do not pre-write implementation code..."  
  • Implications: Separates planning from execution; pseudo-code only if framed as directional guidance

* Rule 5: Safety / non-destructive behavior (agent repo rules)  
  • Source file: https://raw.githubusercontent.com/EveryInc/compound-engineering-plugin/main/AGENTS.md  
  • Excerpt: "**Safety:** Do not delete or overwrite user data. Avoid destructive commands."  
  • Implications: Global constraint on all skills/agents; extends to scratch-space rules (prefer OS temp over .context/ except for user-curated artifacts)

* Rule 6: Use blocking user-question tools (one question at a time)  
  • Source file: https://raw.githubusercontent.com/EveryInc/compound-engineering-plugin/main/plugins/compound-engineering/skills/ce-plan/SKILL.md  
  • Excerpt: "When asking the user a question, use the platform's blocking question tool: `AskUserQuestion` in Claude Code ... Ask one question at a time. Prefer a concise single-select choice..."  
  • Implications: Enforces interactive, non-assumptive behavior across platforms (Claude/Codex/etc.)

* Rule 7: Privacy / no telemetry (plugin-level)  
  • Source file: inferred from plugin context in https://raw.githubusercontent.com/EveryInc/compound-engineering-plugin/main/plugins/compound-engineering/README.md and marketplace metadata  
  • Excerpt: (cross-referenced with standard plugin privacy; no backend service)  
  • Implications: All data handling is host-AI-tool only or explicit opt-in; no analytics

## 2. Workflows (Sequential, Slash-Invokable Procedures)

* Workflow 1: [/ce-strategy]  
  • Source file: https://raw.githubusercontent.com/EveryInc/compound-engineering-plugin/main/plugins/compound-engineering/README.md  
  • Sequence: Create/maintain STRATEGY.md (target problem, approach, persona, metrics, tracks) → read as grounding by downstream skills  
  • Triggers/Dependencies: Upstream anchor for ideate/brainstorm/plan; re-runnable

* Workflow 2: [/ce-brainstorm → /ce-plan → /ce-work → /ce-code-review → /ce-compound] (core loop)  
  • Source file: https://raw.githubusercontent.com/EveryInc/compound-engineering-plugin/main/README.md  
  • Sequence: Brainstorm requirements → Plan implementation → Execute with worktrees/task tracking → Multi-agent code review → Document learnings (repeat with compounded context)  
  • Triggers/Dependencies: Optional /ce-ideate upstream; /ce-strategy grounding; /ce-product-pulse as read-side companion

* Workflow 3: [/ce-plan] (multi-phase planning workflow)  
  • Source file: https://raw.githubusercontent.com/EveryInc/compound-engineering-plugin/main/plugins/compound-engineering/skills/ce-plan/SKILL.md  
  • Sequence: Phase 0 (Resume/Source/Scope + optional deepening fast-path) → Phase 1 (Context/Research) → Phase 2 (Questions) → Phase 3 (Structure) → Phase 4 (Write plan) → Phase 5 (Review/Confidence Check/Handoff); includes interactive deepening if "deepen" intent detected  
  • Triggers/Dependencies: Direct /ce-plan invocation (always plans); prior brainstorm/requirements doc optional; repo context + user questions

* Workflow 4: [/ce-code-review] (multi-agent review)  
  • Source file: https://raw.githubusercontent.com/EveryInc/compound-engineering-plugin/main/plugins/compound-engineering/README.md  
  • Sequence: Tiered persona agents (correctness, security, maintainability, etc.) → confidence gating → dedup pipeline → handoff to /ce-compound or /ce-polish-beta  
  • Triggers/Dependencies: Post-/ce-work; invokes sub-agents like ce-correctness-reviewer

* Workflow 5: [/ce-debug]  
  • Source file: https://raw.githubusercontent.com/EveryInc/compound-engineering-plugin/main/plugins/compound-engineering/README.md  
  • Sequence: Reproduce failures → trace root cause → form/testable hypotheses → implement test-first fixes  
  • Triggers/Dependencies: Bug reports; pairs with /ce-code-review + /ce-compound

## 3. Skills (Modular Capabilities & Tools)

* Skill 1: ce-plan  
  • Source file: https://raw.githubusercontent.com/EveryInc/compound-engineering-plugin/main/plugins/compound-engineering/skills/ce-plan/SKILL.md  
  • Description: Creates structured plans for multi-step tasks or deepens existing plans; produces durable implementation plan artifact in docs/plans/  
  • Inputs/Outputs: Input = feature desc/requirements doc/plan path; Output = plan doc with traceability, decisions, test scenarios, repo-relative paths  
  • Implementation excerpt: "ce-plan defines **HOW** to build it. ... Workflow produces a durable implementation plan. It does **not** implement code..."

* Skill 2: ce-correctness-reviewer (sub-agent skill)  
  • Source file: https://raw.githubusercontent.com/EveryInc/compound-engineering-plugin/main/plugins/compound-engineering/agents/ce-correctness-reviewer.agent.md  
  • Description: Logic/behavioral correctness reviewer; mentally executes code, hunts off-by-one, null propagation, races, state transitions, error propagation  
  • Inputs/Outputs: Input = code diff/PR; Output = JSON findings {reviewer, findings, residual_risks, testing_gaps} per anchored confidence rubric  
  • Implementation excerpt: "You are a logic and behavioral correctness expert who reads code by mentally executing it... Return your findings as JSON matching the findings schema."

* Skill 3: Compound engineering skill set (/ce-*)  
  • Source file: https://raw.githubusercontent.com/EveryInc/compound-engineering-plugin/main/plugins/compound-engineering/README.md  
  • Description: 38+ slash-invokable modular capabilities (core workflow + research/git/utilities/review/etc.); ships with 50+ specialized agents  
  • Inputs/Outputs: Platform slash-command invocation; outputs to repo artifacts (plans, reviews, compounds, pulse reports)  
  • Implementation excerpt: "The compound-engineering plugin currently ships 37 skills and 51 agents. ... primary entry points for engineering work, invoked as slash commands."

* Skill 4: Marketplace plugin loader  
  • Source file: https://raw.githubusercontent.com/EveryInc/compound-engineering-plugin/main/.claude-plugin/marketplace.json  
  • Description: Distributes compound-engineering + coding-tutor plugins across Claude/Cursor/Codex/etc. platforms via marketplace manifests  
  • Inputs/Outputs: Marketplace add/install commands; source = ./plugins/compound-engineering  
  • Implementation excerpt: JSON manifest with name, description, tags, source mapping to plugin subdir

## 4. Interconnections & Architecture Summary

* How Rules constrain Workflows/Skills: Core philosophy rule (80/20 planning/review) gates all /ce-* workflows; repo-relative-paths and "decisions-not-code" rules are enforced inside ce-plan and propagated to reviewers/compound skills; safety/non-destructive rules apply globally to agents and scratch-space handling; confidence calibration rules in reviewers prevent low-evidence findings from blocking workflows

* How Workflows invoke Skills: /ce-plan invokes sub-agents for research/review; /ce-code-review orchestrates 20+ reviewer agents (e.g. ce-correctness-reviewer) in parallel with dedup; core loop explicitly chains slash commands (/ce-brainstorm calls into plan → work → review → compound); skills like /ce-work delegate to git worktrees/task tracking; /ce-strategy and /ce-product-pulse provide persistent grounding/read-side for the entire loop

* Overall agent design insights: Plugin is a slash-command-driven, prompt-native agentic system layered on top of host AI coding tools (Claude Code, Cursor, Codex, etc.). Skills = high-level slash-invokable orchestrators defined in SKILL.md (phased workflows + rules); Agents = specialized sub-personas defined in *.agent.md (focused role + output schema). Architecture emphasizes compounding (knowledge reuse via STRATEGY.md, compounds, pulse reports) and strict separation of concerns (plan ≠ execute). Converter CLI in src/ enables cross-platform portability; all behavior is declarative/prompt-based with no backend service.
