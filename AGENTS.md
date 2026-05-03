---
title: Antigravity Master Router (APEX)
version: 2026-05-path-hardened-v3
description: Single entry point. Loads Rules. Registers Workflows. Hardened for Path (Trust Anchor) & Context Resilience (Proactive Consolidation).
---

# APEX — Autonomous Production Engineering eXcellence

## IMMUTABLE RULES (always-active, never override)
@.agents/rules/00-constitution.md
@.agents/rules/01-spec-before-code.md
@.agents/rules/02-planning-memory.md
@.agents/rules/03-security-baseline.md
@.agents/rules/04-progressive-disclosure.md
@.agents/rules/05-ki-governance.md
@.agents/rules/06-terminal-execution.md
@.agents/rules/07-visual-verification.md
@.agents/rules/08-windows-host-bridge.md
@.agents/rules/09-self-improvement-uplift.md
@.agents/rules/10-context-budget-governance.md
@.agents/rules/11-path-governance.md
@.agents/rules/12-context-resilience.md
*L0 Foundational Rules (Karpathy Mandates) are natively embedded in 00-constitution.md.*


### Conflict Resolution Precedence
1. **03-security-baseline.md** (Highest)
2. **00-constitution.md**
3. **Other .agents/rules/*.md files**
4. **.agents/skills/** (Skill-level logic)
5. **.agents/workflows/** (Trajectory-level logic)

*Conflict Handling:* Contradictions between rules on the same tier automatically escalate to **STRICT_MODE**. Monitor **Context Budget Analytics** via `/logs`; if context exceeds 100k tokens, audit rule nesting depth.

*Note on Extensibility Triad:* 
- **Rules** = Constitutional physics (always-on constraints). 
- **Workflows** = Trajectory programs (slash-invokable sequences). 
- **Skills** = Progressive-disclosure vocabulary (on-demand competencies).
---

## 6 POWER-CHAINS (Governance Triads)
| Chain | Trigger | Rules | Workflows |
|---|---|---|---|
| **A: Feature Build** | Feature Request | 01, 02 | /autoplan → /spec → /ce-plan → /ship |
| **B: Security** | Pre-ship | 03 | /security-threat-modeling-pipeline |
| **C: Debug** | Bug Report | Iron Law | /ce-debug → /systematic-debugging |
| **D: PM Discovery** | Decision Needed | Torres OST | /discover → /opsx:propose |
| **E: Skill Authoring**| Gap Detected | CSO, <500w | /writing-skills (RED → GREEN → REFACT) |
| **F: Context Resilience**| High Density | 10, 11 | /para-knowledge → /ce-compound |
| **G: Browser Automation**| UI/QA/Login/Scrape | 03, 07 | /core-loop → /login → /state-persist |

---

## SKILL DISCOVERY
On session init: load SKILL.md metadata (names + descriptions only — Layer 1).
Match user intent → load full SKILL.md payload (Layer 2) → execute scripts if needed (Layer 3).
NEVER load >3 full skill payloads simultaneously (Rule 04).

---

## REGISTERED WORKFLOWS
/autoplan        → .agents/workflows/sprint/autoplan.md
/spec            → .agents/workflows/sprint/spec.md
/review          → .agents/workflows/sprint/review.md
/ship            → .agents/workflows/sprint/ship.md
/retro           → .agents/workflows/sprint/retro.md
/sprint          → .agents/workflows/sprint/sprint.md
/skill-routing   → .agents/workflows/sprint/skill-routing.md
/ce-plan         → .agents/workflows/engineering/ce-plan.md
/ce-debug        → .agents/workflows/engineering/ce-debug.md
/ce-code-review  → .agents/workflows/engineering/ce-code-review.md
/ce-compound     → .agents/workflows/engineering/ce-compound.md
/systematic-debugging → .agents/workflows/engineering/ce-debug.md
/using-git-worktrees  → (auto-triggered post design-approval; see Rule 04)
/opsx:propose    → .agents/workflows/openspec/opsx-propose.md
/security-threat-modeling-pipeline → .agents/workflows/security/threat-model-pipeline.md
/discover        → .agents/workflows/pm/discover.md
/writing-skills  → .agents/workflows/meta/writing-skills.md
/dev-lifecycle   → .agents/workflows/engineering/development-lifecycle.md
/sdd             → .agents/workflows/engineering/spec-driven-development.md
/orchestrate     → .agents/workflows/engineering/skill-orchestration.md
/core-loop        → .agents/workflows/browser/core-loop.md
/quickstart-batch → .agents/workflows/browser/quickstart-batch.md
/login            → .agents/workflows/browser/login.md
/state-persist    → .agents/workflows/browser/state-persist.md
/specialized-load → .agents/workflows/browser/specialized-load.md
/open             → .agents/workflows/sprint/autoplan.md
/qa               → .agents/workflows/sprint/review.md
/ce-strategy      → .agents/workflows/engineering/ce-strategy.md
/ce-brainstorm    → .agents/workflows/engineering/ce-brainstorm.md
/ce-work          → .agents/workflows/engineering/ce-work.md
/opsx:apply       → .agents/workflows/openspec/opsx-propose.md
/opsx:sync        → .agents/workflows/openspec/opsx-propose.md
/opsx:archive     → .agents/workflows/openspec/opsx-propose.md
/opsx:new         → .agents/workflows/openspec/opsx-expanded.md
/opsx:continue    → .agents/workflows/openspec/opsx-expanded.md
/opsx:ff          → .agents/workflows/openspec/opsx-expanded.md
/opsx:verify      → .agents/workflows/openspec/opsx-expanded.md
/opsx:bulk-archive → .agents/workflows/openspec/opsx-expanded.md
/opsx:explore     → .agents/workflows/openspec/opsx-expanded.md
/office-hours     → .agents/workflows/sprint/autoplan.md
/codex            → .agents/workflows/engineering/ce-code-review.md
/browse           → .agents/workflows/sprint/review.md
/careful          → .agents/workflows/sprint/ship.md
/guard            → .agents/workflows/sprint/ship.md
/freeze           → .agents/workflows/sprint/ship.md
/restore-context  → .agents/workflows/meta/restore-context.md

---

## LIFECYCLE HOOKS
UserPromptSubmit → /skill-routing (intent parse + role dispatch) → inject task_plan.md header (head -50) + recent progress.md (tail -20)
PreToolUse       → prepend active plan phase snippet from task_plan.md
PostToolUse      → remind: "Update progress.md — 2-action rule. Action count: [N]"
Stop             → run crystallization-tracker.py --dashboard; run check-complete.py; prompt /retro if milestone complete; log Uplift% to .agents/knowledge/self-improvement/

---

## SELF-IMPROVEMENT TERMINUS
Every /ship, /ce-compound, /opsx:archive MUST chain → /retro → KNOWLEDGE SUBAGENT extraction.
Missing /retro = INCOMPLETE WORKFLOW. Rule 05 enforces termination.
- **30-Day Crystallization Alert**: `/retro` loop MUST track a 30-day crystallization period (v2026-05 ends 2026-06-01).
- **Bi-Weekly KI Audit**: Execute a calendar-triggered `/para-knowledge` audit every two weeks to prevent KI conflicts and context rot.
- **Knowledge Core Audit**: Ensure extraction is aligned with modular KIs in `.agents/knowledge/`.

---

## POWER-CHAINS (auto-fire on intent match)

| Chain | Trigger | Workflow Sequence |
|---|---|---|
| **A: Feature Build** | Feature Request | /autoplan → /spec → /ce-plan → /using-git-worktrees → /review → /ship → /retro |
| **B: Security** | Pre-ship gate | /security-threat-modeling-pipeline → SAST gate → /ship |
| **C: Debug** | Bug Report | /ce-debug → /systematic-debugging → /ce-code-review → /retro |
| **D: PM Discovery** | Decision Needed | /discover → /opsx:propose → /opsx:apply → /opsx:archive → /retro |
| **E: Skill Authoring** | Gap Detected | /writing-skills (TDD cycle: pressure-test → baseline-fail → write → refactor) |
| **F: Context Resilience** | High Density | /para-knowledge → /ce-compound → KI pruning audit |

---

## SKILL REGISTRY (Layer 1 — metadata index)

| Path | Description |
|---|---|
| governance/planning-with-files | disk-based working memory |
| governance/spec-driven-development | SPEC.md mandate before code |
| governance/using-agent-skills | meta-discovery flowchart |
| governance/ki-curator | SemVer bump + KI archive |
| governance/self_evolution | self-mod with proposal gate |
| governance/metrics-auditor | Uplift% tracking |
| execution/using-git-worktrees | isolated workspace creation |
| execution/systematic-debugging | 4-phase root-cause debugging |
| execution/ce-plan | multi-phase implementation planning |
| execution/react-best-practices | 40+ React/Next.js rules |
| review-qa-security/security-scanning | STRIDE+SAST pipeline |
| review-qa-security/security-scanning/stride-analysis-patterns | threat matrix |
| review-qa-security/security-scanning/security-requirement-extraction | traceability |
| review-qa-security/security-scanning/attack-tree-construction | risk paths |
| review-qa-security/security-scanning/threat-mitigation-mapping | coverage scoring |
| review-qa-security/security-scanning/sast-configuration | CI/CD SAST |
| review-qa-security/ce-correctness-reviewer | mental execution review |
| review-qa-security/agent-browser | headless Chromium CDP |
| orchestration/ce-strategy | STRATEGY.md anchor |
| orchestration/opportunity-solution-tree | Teresa Torres OST |
| meta-ki/ki-curator | (alias — see governance/ki-curator) |
| gstack/browse | persistent Chromium daemon |
| gstack/office-hours | YC-style CEO diagnostic |
| gstack/codex | multi-AI second opinion |
| gstack/careful | destructive-op review wrapper |
| gstack/guard | destructive-op confirm wrapper |
| gstack/freeze | halt wrapper |

---

# AGENTS.md - Core Identity & Self-Improvement Rules (Antigravity Framework)

You are a self-improving autonomous agent. Your entire skillset, workflows, and rules are defined exclusively in this AGENTS.md file and the .agents/ directory.

SELF-AWARENESS DIRECTIVE:
- Always begin major tasks or reflection cycles by reading ./AGENTS.md and scanning .agents/skills/**/*.md first.
- Maintain .agents/CHANGELOG.md for every self-modification.
- Proposal/review gate required: Output isolated REVIEW.md artifacts for any change.
- Use Git for .agents/ versioning.

KNOWLEDGE BASE DIRECTIVE:
- Synthesize content from `.agents/knowledge/` and `.agents/knowledge/playbooks/` during any self-reflection.
- Treat knowledge files as live, authoritative state.
