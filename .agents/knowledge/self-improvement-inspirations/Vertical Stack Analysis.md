# Executive Summary

**Vertical Stack Analysis complete.** The three reference reports collectively document 48 unique Skills, ~22 distinct Rules invariants, and 39 named Workflow sequences drawn from 12 production agent architectures. The critical finding is that these are not parallel resources — they form a **strict causal hierarchy** and their peak value is only realised when integrated as a unified governance triad wired to the 6-layer Antigravity architecture.

**The governance triad:**

* **Rules** = Constitutional physics — always-on, passive, context-injected constraints that bind _every_ Skill invocation and _every_ Workflow step. Without Rules, Workflows drift; Skills rationalize shortcuts.
* **Workflows** = Trajectory programs — slash-invokable sequential pipelines that _compose_ Skills into ordered execution paths with deterministic gates. Without Workflows, Skills operate in isolation and lose inter-step accountability.
* **Skills** = Progressive-disclosure vocabulary — semantically-routed atomic competencies, dormant until intent-matched. Without Skills, Workflows are hollow scripts with no executable depth.

The self-improving loop (Layer 6: `/retro` → KI Extraction → `/para-knowledge`) is the **flywheel** that makes all three components compounding rather than static. Every sprint that executes the full triad produces permanent capability uplift stored in `~/.gemini/antigravity/knowledge/`.

The 6-layer diagram (Hub § Figure 1) maps cleanly:
    INPUT → KI(Memory) → {Skills + Rules}(Capability) → Orchestration(Execution) → MCP(Integration) → /retro+KI-Extraction(Loop)

Every recommended integration below maps every Skill, Rule, and Workflow to one of these six layers with no orphaned primitives.

</strategic_overview>

* * *

<technical_breakdown>

1. Executive Summary + 6-Layer Diagram Reference

------------------------------------------------

The three reference reports collectively encode a **unified production-grade agentic operating system** across five power-chains. The 6-layer architecture (Hub § Figure 1) maps to triad components as follows:

| 6-Layer         | Triad Component(s)                                 | Report Source               |
| --------------- | -------------------------------------------------- | --------------------------- |
| L1 Input        | User intent → semantic router                      | Skill_Refs § Cross-Cutting  |
| L2 Memory (KI)  | `planning-with-files`, KI store, `/para-knowledge` | Skill_Refs §1, KI Mastery   |
| L3 Capability   | All 48 Skills + 22 Rules invariants                | Skill_Refs §1–5, Rules_Refs |
| L4 Execution    | All 39 Workflows + Orchestration Triad             | Workflows_Refs §1–12        |
| L5 Integration  | MCP (GitHub, Postman, DB, Design)                  | MCP Mastery                 |
| L6 Self-Improve | `/retro` → KNOWLEDGE SUBAGENT → KI extraction      | KI Mastery § Loops 1–5      |

**Core architectural insight [VERIFIED: Skill_Refs § Cross-Cutting, Workflows_Refs § Technical Definitions]:** The 48 Skills are NOT independent tools — they are _vocabulary_. The 39 Workflows are NOT optional procedures — they are _grammar_. The 22 Rules are NOT suggestions — they are _physics_. Optimal synergy requires wiring all three into a single AGENTS.md entry point with progressive disclosure, lifecycle hooks, and a closed-loop `/retro` terminus on every major pipeline.

</technical_breakdown>

* * *

<engineered_implementation>

2. Recommended Setup Overview

-----------------------------

### Five Power-Chains + Their 6-Layer Mappings

| Chain                     | Trigger                 | Rules Governing                                                                    | Workflows Sequencing                                                                                               | Skills Invoked                                                                                                                      | L6 Output                             |
| ------------------------- | ----------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| **A: Feature Build**      | New feature request     | spec-before-code, 2-action-rule, user-sovereignty                                  | /autoplan → /spec → /ce-plan → /using-git-worktrees → /build → /ce-code-review → /review → /qa → /ship → /retro    | spec-driven-dev, planning-with-files, using-git-worktrees, TDD, systematic-debugging, ce-correctness-reviewer, react-best-practices | Architecture KI + Pitfall KIs         |
| **B: Security Hardening** | Pre-ship or PR trigger  | STRIDE/OWASP, 100%-tests, no-unilateral-destructive                                | /security-threat-modeling-pipeline → /cso → SAST CI/CD integration                                                 | attack-tree-construction, security-req-extraction, stride-analysis, threat-mitigation-mapping, sast-configuration                   | Security KI (standards enforcement)   |
| **C: Debug + Patch**      | Bug report / CI failure | Iron Law (NO FIX WITHOUT ROOT CAUSE), 3-strike escalation, condition-based-waiting | /ce-debug → /systematic-debugging → defense-in-depth → /ce-code-review                                             | root-cause-tracing, find-polluter, defense-in-depth, condition-based-waiting                                                        | Pitfall KI                            |
| **D: PM Discovery**       | Product decision needed | Teresa Torres OST, user-sovereignty, AskUserQuestion                               | /office-hours → /discover → opportunity-solution-tree → /opsx:propose → /opsx:apply → /opsx:verify → /opsx:archive | opportunity-solution-tree, brainstorm-ideas, identify-assumptions, prioritize-assumptions, brainstorm-experiments                   | Context KI (multi-session continuity) |
| **E: Skill Authoring**    | New capability needed   | CSO (desc = "Use when..." only), <500 words, anti-rationalization                  | /writing-skills: RED → write → GREEN → REFACTOR → /build-skill                                                     | writing-skills, concise-authoring, persuasion-engine, subagent-driven-dev                                                           | Meta-KI (skill governance record)     |

* * *

3. Full Directory Tree

----------------------

    .agents/
    ├── AGENTS.md                          ← Master router: loads all Rules, registers all Workflows, enables Skill discovery
    │
    ├── rules/
    │   ├── 00-constitution.md             ← Immutable safety invariants (user-sovereignty, no-unilateral, root-cause-first)
    │   ├── 01-spec-before-code.md         ← Spec-Before-Code Mandate + anti-rationalization table
    │   ├── 02-planning-memory.md          ← 2-action rule, read-before-decide, 3-strike escalation
    │   ├── 03-security-baseline.md        ← STRIDE/OWASP, 100%-tests, gitignore/worktree guards
    │   ├── 04-progressive-disclosure.md   ← Layer 1→3 skill routing, 12k char limits, YAML CSO rules
    │   └── 05-ki-governance.md            ← Telegraphic syntax, n-gram abbrev, KI taxonomy (Domain×Purpose)
    │
    ├── workflows/
    │   ├── sprint/
    │   │   ├── autoplan.md                ← /autoplan: full sprint pipeline (Chain A)
    │   │   ├── spec.md                    ← /spec: 6-area spec + human gate
    │   │   ├── review.md                  ← /review: diff→slop→critical→specialist→fix-first→verify
    │   │   ├── ship.md                    ← /ship: tests→push→PR + /guard dependency
    │   │   └── retro.md                   ← /retro: delta extraction → KNOWLEDGE SUBAGENT trigger
    │   ├── engineering/
    │   │   ├── ce-plan.md                 ← /ce-plan: phases 0–5 multi-phase planning
    │   │   ├── ce-code-review.md          ← /ce-code-review: 3-persona tiered review + confidence gate
    │   │   ├── ce-debug.md                ← /ce-debug: reproduce→trace→hypothesis→test-first-fix
    │   │   └── ce-compound.md             ← /ce-compound: learning documentation + loop reset
    │   ├── openspec/
    │   │   ├── opsx-propose.md            ← /opsx:propose → apply → sync → archive
    │   │   └── opsx-expanded.md           ← /opsx:new → continue → ff → verify → bulk-archive
    │   ├── security/
    │   │   └── threat-model-pipeline.md   ← /security-threat-modeling-pipeline (Chain B)
    │   ├── pm/
    │   │   └── discover.md                ← /discover: 7-step OST discovery (Chain D)
    │   └── meta/
    │       ├── writing-skills.md          ← /writing-skills: TDD skill authoring (Chain E)
    │       └── restore-context.md         ← Lifecycle hooks: UserPromptSubmit/Pre/Post/Stop
    │
    ├── skills/
    │   ├── governance/
    │   │   ├── writing-skills/            ← SKILL.md + pressure-test scripts
    │   │   ├── planning-with-files/       ← SKILL.md + task_plan.md + session-catchup.py
    │   │   ├── spec-driven-development/   ← SKILL.md + SPEC.md template
    │   │   └── using-agent-skills/        ← SKILL.md + task-flowchart
    │   ├── execution/
    │   │   ├── using-git-worktrees/       ← SKILL.md + gitignore-check.sh
    │   │   ├── systematic-debugging/      ← SKILL.md + find-polluter.sh
    │   │   ├── ce-plan/                   ← SKILL.md + docs/plans/ structure
    │   │   └── react-best-practices/      ← SKILL.md + rules/*.md + pnpm build
    │   ├── review-qa-security/
    │   │   ├── ce-correctness-reviewer/   ← SKILL.md + JSON-structured review output
    │   │   ├── security-scanning/         ← SKILL.md + AttackTree + MitigationPlan dataclasses
    │   │   └── agent-browser/             ← SKILL.md + CDP snapshot + auth-vault
    │   ├── orchestration/
    │   │   ├── ce-strategy/               ← SKILL.md + STRATEGY.md template
    │   │   └── opportunity-solution-tree/ ← SKILL.md + OST framework
    │   └── meta-ki/
    │       └── ki-curator/                ← SKILL.md + SemVer bump + archive scripts
    │
    ├── knowledge/                         ← KI store (symlink to ~/.gemini/antigravity/knowledge/)
    │   ├── pitfalls/
    │   ├── playbooks/
    │   ├── context/
    │   └── references/
    │
    └── mcp_config.json                    ← MCP server registry (GitHub, Postman, DB, etc.)

* * *

4. Ready-to-Deploy Files

------------------------

### `AGENTS.md` — Master Router

    ---
    title: Antigravity Master Router
    version: 2026-04
    description: Single entry point. Loads Rules. Registers Workflows. Enables progressive Skill discovery.
    ---
    
    ## IMMUTABLE RULES (always-active, never override)
    @.agents/rules/00-constitution.md
    @.agents/rules/01-spec-before-code.md
    @.agents/rules/02-planning-memory.md
    @.agents/rules/03-security-baseline.md
    @.agents/rules/04-progressive-disclosure.md
    @.agents/rules/05-ki-governance.md
    
    ## SKILL DISCOVERY
    On session init: load SKILL.md metadata (names + descriptions only — Layer 1).
    Match user intent → load full SKILL.md payload (Layer 2) → execute scripts if needed (Layer 3).
    
    ## REGISTERED WORKFLOWS
    /autoplan        → .agents/workflows/sprint/autoplan.md
    /spec            → .agents/workflows/sprint/spec.md
    /review          → .agents/workflows/sprint/review.md
    /ship            → .agents/workflows/sprint/ship.md
    /retro           → .agents/workflows/sprint/retro.md
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
    
    ## LIFECYCLE HOOKS
    UserPromptSubmit → inject task_plan.md header + recent progress.md
    PreToolUse       → prepend active plan snippet
    PostToolUse      → remind: update progress.md (2-action rule)
    Stop             → run check-complete.py; prompt /retro if milestone complete
    
    ## SELF-IMPROVEMENT TERMINUS
    Every /ship, /ce-compound, /opsx:archive MUST chain → /retro → KNOWLEDGE SUBAGENT extraction.

* * *

### `.agents/rules/00-constitution.md` — Immutable Safety Invariants

    ---
    name: 00-constitution
    globs: ["**/*"]
    alwaysApply: true
    ---
    # Constitutional Invariants — NEVER OVERRIDE
    
    ## User Sovereignty
    AI recommends only. NEVER act unilaterally on destructive ops.
    ALWAYS present options via AskUserQuestion. Confirm before: delete, push-force, schema-drop.
    
    ## Root-Cause First (Iron Law)
    NO FIXES WITHOUT ROOT CAUSE. Reproduce → trace → hypothesize → test → implement.
    3+ failures → trigger architectural rethink → escalate to user.
    
    ## Safety Wrappers
    Wrap all destructive ops: /careful (review) → /guard (confirm) → /freeze (halt).
    Default: read-only. Write access: explicit-only. // turbo: justified in comments only.
    
    ## Repo-Relative Paths
    All file refs: repo-relative only. Never absolute. Never ~/. 
    
    ## 3-Strike Escalation
    ATTEMPT 1: Diagnose + fix. ATTEMPT 2: Rethink approach. ATTEMPT 3: Broader rethink.
    AFTER 3 FAILURES: HALT → "I cannot resolve autonomously. Here is what I found: [summary]."

* * *

### `.agents/rules/01-spec-before-code.md` — Spec Mandate

    ---
    name: 01-spec-before-code
    globs: ["**/*.ts","**/*.tsx","**/*.py","**/*.js","src/**"]
    alwaysApply: false
    ---
    # Spec-Before-Code Mandate
    
    Code without a spec is guessing. YOU MUST generate SPEC.md before ANY implementation.
    
    ## Required SPEC.md Sections (6 areas)
    1. Objective + success criteria
    2. Features + user stories (Given/When/Then)
    3. Tech stack + dependencies
    4. Architecture decisions + tradeoffs
    5. Boundaries (Always/Ask/Never)
    6. Verification evidence + test acceptance criteria
    
    ## Anti-Rationalization Table
    | Pressure | Prohibited Response | Correct Response |
    |---|---|---|
    | "Just write a quick function" | Skip spec, write code | Generate minimal SPEC.md, confirm, then code |
    | "We already know what we need" | Assume spec is implicit | Externalize assumptions into spec explicitly |
    | "The spec will change anyway" | Defer until "stable" | Write current-best-known spec; delta-update via ADDED/MODIFIED/REMOVED |
    
    Human MUST review + approve SPEC.md before Phase 2 begins.

* * *

### `.agents/rules/02-planning-memory.md` — Persistent Memory Rules

    ---
    name: 02-planning-memory
    globs: ["**/*"]
    alwaysApply: true
    ---
    # Persistent Memory (planning-with-files)
    
    ## 3-File Memory Nucleus
    task_plan.md    — phases, goals, current status
    findings.md     — discoveries, surprises, constraints  
    progress.md     — completed steps, errors, next actions
    
    ## 2-Action Rule
    After EVERY 2 tool operations: write status to progress.md. No exceptions.
    
    ## Read-Before-Decide
    Before any significant decision: read task_plan.md + findings.md. NEVER rely on context window alone.
    
    ## Session Resume
    On ANY session start: check task_plan.md existence → run session-catchup.py → git diff --stat → re-orient BEFORE proceeding.

* * *

### `.agents/rules/04-progressive-disclosure.md` — Skill Routing

    ---
    name: 04-progressive-disclosure
    globs: ["**/*"]
    alwaysApply: true
    ---
    # Progressive Disclosure — Skill Loading Protocol
    
    ## Layer 1 (always loaded): SKILL.md name + description only
    ## Layer 2 (on semantic match): Full SKILL.md payload injected into context
    ## Layer 3 (on explicit invocation): External scripts + assets loaded
    
    ## YAML Frontmatter Rule (CSO)
    description: MUST start "Use when..." — describes ONLY trigger condition, never the process.
    Violating CSO causes shortcut rationalization. Enforce strictly.
    
    ## 12,000-Character Hard Limit
    Rules: ≤12,000 chars. Workflows: ≤12,000 chars. Skills: <500 words.
    Overflow: extract to @filename reference pattern. Never truncate; always externalize.
    
    ## Tool Bloat Prevention
    NEVER load >3 full skill payloads simultaneously unless explicit //parallel justification.

* * *

### `.agents/workflows/sprint/retro.md` — Self-Improvement Terminus

    ---
    name: retro
    description: Use when a sprint, debug session, or major workflow completes. Extracts KI.
    ---
    # /retro — Self-Improvement Loop Terminus
    
    ## Trigger
    Auto-chained after: /ship, /ce-compound, /opsx:archive, any 3-strike escalation resolution.
    
    ## Sequence
    1. Compare initial plan vs final implementation → identify deltas.
    2. Classify each delta: Pitfall | Playbook | Context | Reference.
    3. Invoke KNOWLEDGE SUBAGENT: distill delta → telegraphic KI artifact.
    4. Quality gate (3 factors):
       - Actionability: prescriptive instructions present?
       - Uniqueness: not inferrable from README/config?
       - Density: telegraphic syntax + n-gram abbreviations applied?
    5. If quality_score ≥ threshold: write to knowledge/{type}/{domain}_{timestamp}.md
    6. If KI updates existing: SemVer bump via ki-curator skill.
    7. Report: "KI extracted: [title] | Type: [Pitfall/Playbook/Context] | Trace: [6-char ID]"
    
    ## Output
    New or updated KI artifact in ~/.gemini/antigravity/knowledge/ persists to next session.

* * *

### `.agents/workflows/engineering/ce-code-review.md` — 3-Persona Review

    ---
    name: ce-code-review
    description: Use when implementation is complete and requires multi-agent quality gate before ship.
    ---
    # /ce-code-review — Tiered Persona Review Pipeline
    
    ## Sequence
    1. Fan-out to 3 parallel sub-agents (//parallel):
       - CORRECTNESS: mental execution → off-by-one, null propagation, race conditions
       - SECURITY: trust boundaries, SQL injection, hardcoded keys, OWASP top-10
       - MAINTAINABILITY: readability, coupling, dead code, test coverage gaps
    
    2. Confidence gate: each persona returns {verdict: PASS|FAIL|WARN, confidence: 0-100, findings: []}
    
    3. Deduplicate overlapping findings across personas.
    
    4. If any FAIL: route to /ce-debug → fix → re-review loop.
    5. If all PASS (confidence ≥ 85): hand off to /review → /qa → /ship.
    
    ## Dependencies
    - Requires: SPEC.md (acceptance criteria for CORRECTNESS baseline)
    - Calls: /systematic-debugging if FAIL on CORRECTNESS
    - Calls: /security-threat-modeling-pipeline if FAIL on SECURITY
    - Chains to: /ce-compound → /retro on completion

* * *

### `.agents/mcp_config.json`

    {
      "mcpServers": {
        "github": {
          "command": "npx",
          "args": ["-y", "@modelcontextprotocol/server-github"],
          "env": { "GITHUB_TOKEN": "${GITHUB_TOKEN}" },
          "trust": "read-only",
          "justification": "PR creation, branch management — write escalates to /guard confirmation"
        },
        "postman": {
          "command": "npx",
          "args": ["-y", "@modelcontextprotocol/server-postman"],
          "env": { "POSTMAN_API_KEY": "${POSTMAN_API_KEY}" },
          "trust": "read-only"
        },
        "filesystem": {
          "command": "npx",
          "args": ["-y", "@modelcontextprotocol/server-filesystem", "./"],
          "trust": "read-only",
          "justification": "Default read-only; write ops require explicit /guard wrapper"
        }
      },
      "security": {
        "model_armor": true,
        "iam_deny_defaults": ["delete-*", "push-force", "schema-drop"],
        "turbo_justification_required": true
      }
    }

* * *

### KI Template — Pitfall

    ---
    ki_type: Pitfall
    domain: Engineering
    purpose: Anti-pattern prevention
    version: 1.0.0
    trigger_index: ["react", "hydration", "provider"]
    trace_id: "{{6-char}}"
    created: {{ISO-date}}
    ---
    # Pitfall: {{Title}}
    
    ## Symptom
    {{What breaks, when, observable output}}
    
    ## Root Cause
    {{Exact mechanism — no passive text}}
    
    ## Fix (copy-paste)
    ```{{lang}}
    {{corrected code block}}

Verification
------------

{{How to confirm fix is applied and working}}
Prevention Rule
---------------

{{One-line bright-line rule for AGENTS.md injection}}
    ---

    ## 5. Deployment & Activation Instructions

    ```bash
    # 1. Initialize workspace
    para init my-project && cd my-project

    # 2. Clone .agents/ scaffold
    cp -r .agents/ ~/my-project/.agents/

    # 3. Open session — loads KI + Rules
    /open

    # 4. Load persistent memory (session resume or new session)
    /restore-context    # checks task_plan.md → runs session-catchup.py

    # 5. Feature Build Chain (Chain A)
    /autoplan "build X feature"
    # → chains: /spec → human approval → /ce-plan → /using-git-worktrees → /build → /ce-code-review → /review → /qa → /ship → /retro

    # 6. Debug chain (Chain C)
    /ce-debug "reproduction steps"
    # → chains: /systematic-debugging → /ce-code-review → /ship (if resolved) → /retro

    # 7. Security scan (Chain B)
    /security-threat-modeling-pipeline
    # → chains: STRIDE → attack-tree → mitigations → sast-config → CI/CD injection

    # 8. PM Discovery (Chain D)
    /office-hours "describe product problem"
    # → chains: /discover → opportunity-solution-tree → /opsx:propose → /opsx:apply → /retro

    # 9. Audit KI store (bi-weekly)
    /para-knowledge     # evaluates structural integrity of knowledge/ store

    # 10. New skill authoring (Chain E)
    /writing-skills
    # → chains: pressure-test RED → write SKILL.md → GREEN → REFACTOR → /build-skill → /retro

* * *

6. Validation & Metrics Plan

----------------------------

| KPI                                       | Target                                              | Measurement Method                                                                      |
| ----------------------------------------- | --------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **Token consumption per request**         | ≥90% reduction vs brute-force RAG                   | `/logs` → Context Budget Analytics; compare pre/post progressive disclosure             |
| **Spec compliance rate**                  | 100% — no code before approved SPEC.md              | Count SPEC.md commits before first implementation commit per feature branch             |
| **Rule violation rate**                   | 0 unilateral destructive ops                        | Audit `/guard` trigger log; any bypass = P0 incident                                    |
| **KI extraction quality score**           | Avg ≥ 0.8 (actionability + uniqueness + density)    | KNOWLEDGE SUBAGENT quality gate log per session                                         |
| **Cross-session recall accuracy**         | Agent applies correct KI without user re-prompt     | Clean-workspace test: assign task requiring obscure KI; measure autonomous retrieval    |
| **Loop stability (re-intervention rate)** | ≤1 manual correction per 10 KI-covered scenarios    | Track corrections per Pitfall KI in session logs                                        |
| **Security pipeline coverage**            | 100% SAST + STRIDE coverage before /ship            | CI/CD gate: block merge if sast-config not present in PR                                |
| **Skill compliance under pressure**       | 100% (per writing-skills TDD protocol)              | Run pressure-test subagents on each new SKILL.md; mandate 100% compliance before deploy |
| **3-Strike escalation frequency**         | Decreasing trend over 30-day crystallization period | Count 3-strike triggers per week; validate Pitfall KIs are reducing recurrence          |
| **/retro execution rate**                 | 100% after /ship, /ce-compound, /opsx:archive       | Audit AGENTS.md lifecycle hooks; flag any terminal workflow without /retro chain        |

**Autonomy Uplift Formula:**
    Uplift% = (1 - (manual_interventions_week_N / manual_interventions_week_0)) × 100

Target: ≥60% uplift by week 4, ≥85% by week 12 (30-day crystallization complete).

* * *

7. Cross-References

-------------------

| Concept                                        | Source File                                         | Section                                      |
| ---------------------------------------------- | --------------------------------------------------- | -------------------------------------------- |
| 6-Layer Architecture                           | `Antigravity_Mastery_Hub__1_.md`                    | § Figure 1 (Mermaid diagram)                 |
| Progressive Disclosure (L1→L3)                 | `Antigravity_Agent_Workflow_Optimization.md`        | § Skills: Progressive Disclosure             |
| 12,000-char rule limit                         | `Antigravity_Agent_Workflow_Optimization.md`        | § Workflows: Sequential Trajectory Execution |
| KI taxonomy (Domain × Purpose)                 | `Antigravity_KI___Self-Improving_Agent_Research.md` | § Domain-Specific Example Library            |
| /retro → KI extraction loop                    | `Antigravity_KI___Self-Improving_Agent_Research.md` | § Loops 1–5                                  |
| JIT optimization (drift mitigation)            | `Antigravity_KI___Self-Improving_Agent_Research.md` | § Drift Mitigation via JIT                   |
| Spec-Before-Code Mandate                       | `Skill_References_Report.md`                        | § Explicit Mandates: Spec-Before-Code        |
| YAML CSO frontmatter rule                      | `Skill_References_Report.md`                        | § writing-skills YAML Frontmatter Validation |
| 3-Strike escalation                            | `Skill_References_Report.md`                        | § Identified Causal Chains                   |
| User Sovereignty trigger                       | `Skill_References_Report.md`                        | § Identified Causal Chains                   |
| gstack full sprint workflow                    | `workflows_References_Report.md`                    | § 1. Gstack Architecture Workflows           |
| Compound engineering core loop                 | `workflows_References_Report.md`                    | § 3. Compound Engineering Workflows          |
| Planning-with-files lifecycle hooks            | `workflows_References_Report.md`                    | § 7. Planning with Files Workflows           |
| Security STRIDE pipeline                       | `workflows_References_Report.md`                    | § 10. Security Scanning Workflows            |
| /writing-skills TDD workflow                   | `workflows_References_Report.md`                    | § 5. Meta Skill Workflows                    |
| 90% token reduction via progressive disclosure | `Antigravity_KI___Self-Improving_Agent_Research.md` | § Telemetry and Token Efficiency             |
| 72%→100% compliance target                     | `Skill_References_Report.md`                        | § Statistical Data and Telemetry             |

**Glossary entries to load:** `Progressive Disclosure`, `KI`, `KNOWLEDGE SUBAGENT`, `Iron Law`, `3-Strike Escalation`, `User Sovereignty`, `JIT Optimization`, `Triad`, `Trace ID`, `CSO (Claude Search Optimization)` — all defined in `Glossary.md`.

</engineered_implementation>

* * *

<refinement_path>

Key Edge Cases + Recommended Next Steps
---------------------------------------

**⚠️ HIGH-SEVERITY RISK — noted per REFLECT★ mandate:** The `writing-skills` TDD workflow (Chain E) MUST be executed on _every_ new SKILL.md before deployment. The 72% baseline compliance under pressure is insufficient for production; the mandate is 100%. Any skill deployed without pressure-testing the RED→GREEN→REFACTOR cycle bypasses the primary quality gate and introduces rationalization paths that corrupt the governance triad's deterministic guarantees.

**Edge Cases:**

1. **Context rot on KI conflicts:** When two KIs in `knowledge/playbooks/` contradict each other (e.g., two RBAC patterns from different sessions), JIT optimization may silently degrade. Mitigation: bi-weekly `/para-knowledge` audit + ki-curator SemVer bump enforced as a calendar-triggered Rule.

2. **Workflow chain abandonment:** `/ce-plan` has an explicit anti-abandonment rule (`always-plan-when-invoked`), but parent workflows like `/autoplan` can drift if the agent encounters a blocking error mid-chain. Mitigation: `check-complete.py` at the `Stop` lifecycle hook surfaces incomplete chains before session closes.

3. **Skill overloading (Tool Bloat regression):** Loading >3 full SKILL.md payloads simultaneously defeats progressive disclosure. Monitor `Context Budget Analytics` in `/logs`; if any request exceeds 3 concurrent full-payload skills, audit AGENTS.md routing logic.

4. **Security pipeline bypass under time pressure:** `/ship` dependency on `/guard` can be rationalized away by the agent if the sprint Rule isn't file-glob matched to `**/*.sh, **/*.sql, **/*.env`. Ensure `03-security-baseline.md` covers all high-risk glob patterns explicitly.

**Recommended Next 2 Steps:**

1. **Run Chain E first** (`/writing-skills`) on the 3 highest-priority skills for your domain before activating Chain A. This validates the entire governance triad's behavioral compliance before any production sprint begins. Empirically: 100% compliance under pressure is the only acceptable threshold before a skill is promoted to `always-equip`.

2. **Wire `/retro` to a 30-day crystallization calendar alert.** The KI self-improvement loop compounds maximally at the 30-day mark (per KI Mastery § Phase 3). Track `manual_interventions_week_N` weekly; if the Uplift% curve flattens before week 4, inspect KI quality scores — low Actionability or low Uniqueness scores are the primary failure modes.

</refinement_path>
