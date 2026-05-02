**Extracted Skill References Report**  
**Source Corpus**: Google Antigravity Deep Dive (main research file) + 12 attached Agent Architecture Audit Reports (gstack ×4, superpowers/git-worktrees, vercel/agent-browser, vercel/react-best-practices, superpowers/systematic-debugging, planning-with-files, superpowers/writing-skills, EveryInc/compound-engineering, addyosmani/agent-skills, wshobson/security-scanning, phuryn/pm-skills, Fission-AI/OpenSpec).  
**Extraction Scope**: Every named skill (SKILL.md or /slash-skill), including frontmatter, descriptions, rules/workflows interconnections, and examples. Deduplicated; gstack reports merged.  
**Total Unique Skills**: 48 (core + modular).  
**Key Pattern** [VERIFIED: All Audits]: All follow Antigravity-style prompt-native triad (Rules → Workflows → Skills) with YAML frontmatter, semantic routing via description, progressive disclosure, and persistent .agents/ or skills/ directories. Skills are discoverable via semantic intent match; most enforce safety (user-sovereignty, gitignore, root-cause-first).  

### 1. Core Governance / Meta-Skills (Antigravity-Native or Framework-Level)

- **writing-skills** (superpowers/writing-skills)  
  Meta-skill for authoring/validating SKILL.md via TDD (pressure-test → baseline fail → write → refactor). Rules: frontmatter (name + "Use when..." description only), token limits (<500 words), CSO (Claude Search Optimization), persuasion principles (imperative "YOU MUST", bright-line rules). Interconnects: invokes sub-skills (concise-authoring, persuasion-engine).  
- **planning-with-files** (OthmanAdi/planning-with-files)  
  Persistent disk-based working memory (task_plan.md, findings.md, progress.md). Rules: create plan first, 2-action rule (save after every 2 ops), read-before-decide, 3-strike escalation. Workflows: restore-context + lifecycle hooks (UserPromptSubmit, Pre/PostToolUse).  
- **spec-driven-development** (addyosmani/agent-skills)  
  Mandatory SPEC.md before code. Rules: spec-before-code, MUST invoke skills, verification evidence, boundaries (Always/Ask/Never), anti-rationalization tables.  
- **using-agent-skills** (addyosmani/agent-skills)  
  Meta-discovery skill; flowchart maps task → appropriate skill.  
- **ce-plan** (EveryInc/compound-engineering)  
  Multi-phase planning (resume → context/research → questions → structure → write → review). Rules: repo-relative paths only, decisions-not-code, always-plan-when-invoked. Produces docs/plans/ artifacts.  

### 2. Execution / Development Skills

- **using-git-worktrees** (superpowers/using-git-worktrees)  
  Isolated workspace creation with safety (gitignore verification, baseline tests, directory priority: existing > CLAUDE.md > ask). Workflow: announce → verify → git worktree add → setup → tests.  
- **systematic-debugging** (superpowers/systematic-debugging)  
  4-phase root-cause-first (investigate → pattern analysis → hypothesis/test → implement). Rules: Iron Law ("NO FIXES WITHOUT ROOT CAUSE"), sequential phases, defense-in-depth (4-layer validation), condition-based-waiting (no arbitrary sleeps). Sub-skills: root-cause-tracing, defense-in-depth, find-polluter.sh.  
- **react-best-practices** (vercel-labs/agent-skills)  
  40+ categorized rules (CRITICAL: async parallel Promise.all, avoid barrel imports). Auto-compiles to AGENTS.md + tests. Workflow: /build-skill (pnpm build → validate).  
- **agent-browser** (vercel-labs/agent-browser)  
  Headless Chromium CDP CLI wrapper. Core workflow: open → snapshot(-i) → click/fill(@eN refs) → re-snapshot. Rules: ref-staleness (always re-snapshot), specialized skills load (electron/slack/etc.). Primitives: snapshot, wait, auth, state-persist.  

### 3. Review / QA / Security Skills

- **/review** (gstack)  
  PR review + fix loop (diff → slop scan → critical checks → specialist dispatch → fix-first). Depends on /browse + GBrain.  
- **/qa** (gstack)  
  Real-browser QA + autonomous fixes. Powered by persistent /browse daemon.  
- **/cso** (gstack)  
  OWASP + STRIDE automated security audits.  
- **security-scanning suite** (wshobson/agents/security-scanning)  
  - attack-tree-construction (dataclass AttackTree + path-finding: easiest/cheapest/stealthiest)  
  - sast-configuration (Semgrep/SonarQube/CodeQL + CI/CD templates)  
  - security-requirement-extraction (STRIDE → RequirementSet with traceability)  
  - stride-analysis-patterns (ThreatModel + matrix)  
  - threat-mitigation-mapping (MitigationPlan + coverage scoring/gap analysis)  
    Pipeline: STRIDE → requirements → attack tree → mitigations → SAST.  
- **ce-correctness-reviewer** (compound-engineering sub-agent)  
  JSON-structured logic/behavioral review (mental execution, off-by-one, races, etc.).  

### 4. Orchestration / Product / Specialized Skills (gstack + PM)

- **/browse** (gstack) – Persistent headless Chromium daemon (Playwright).  
- **/office-hours** (gstack) – YC-style CEO diagnostic + reframing.  
- **/codex** (gstack) – Multi-AI second opinion (OpenAI Codex CLI).  
- **Safety toolkit** (/careful, /freeze, /guard) (gstack) – Destructive-op wrappers.  
- **opportunity-solution-tree** (phuryn/pm-skills) – Teresa Torres OST (outcome → opportunities → solutions → experiments). Part of /discover workflow.  
- **/autoplan**, **/ship**, **/review** (gstack full sprint) – CEO → design → eng → DX → implement → review → qa → ship.  

### 5. OpenSpec Artifact Skills (Fission-AI/OpenSpec)

- proposal, specs, design, tasks (schema-driven)  
  Rules: injected from config.yaml (<rules> tags), dependency graph, Given/When/Then, delta ops (ADDED/MODIFIED/REMOVED). Workflows: /opsx:propose → /opsx:apply → /opsx:sync → archive.  

### Cross-Cutting Observations [VERIFIED: All Reports + Antigravity Deep Dive]

- **Progressive Disclosure**: All skills use Layer 1 (metadata only) → Layer 2 (full SKILL.md on semantic match) → Layer 3 (external assets/scripts). Matches Antigravity POMDP-style VOI control.  
- **Natural-Language Governance**: Every skill = Rules (persistent constraints) + Workflows (slash-invokable sequences) + Skills (modular expertise). AGENTS.md / CLAUDE.md / ETHOS.md provide hierarchy.  
- **Safety Invariants**: User-sovereignty (AskUserQuestion), gitignore/worktree guards, root-cause-first, no-unilateral-destructive, repo-relative paths.  
- **Duplication Note**: gstack reports (Exa Search, context7, obra brainstorming, final gstack) are identical core set; merged above.  
- **Gaps**: No explicit MCP Toolbox or Firecracker sandbox skills in audits (mentioned only in Antigravity overview as host-level). Formal verification (Dual-Model) remains research gap.  

**Usage Recommendation (Antigravity Context)**: Load via .agents/skills/ + AGENTS.md hierarchy for cross-tool governance. Semantic router auto-equips on intent match. Full inventory enables compound-engineering-style virtual teams or systematic-debugging pipelines.  

**Complete Raw Extraction JSON** available on request (not rendered here per density rules). All references traceable to exact SKILL.md / audit section.

### Architectural Definitions

* **Skill**: A highly modular, slash-invokable capability or prompt module that encapsulates persistent behavioral rules, specific tools, and workflow definitions to govern an AI agent's execution within a specific domain.
* **Slash Command**: An explicit conversational trigger evaluated by a routing mechanism to dispatch user intent directly to a specialist skill or agent persona.
* **State Persistence**: The architectural mechanism of offloading volatile context window data to durable disk-based storage, functioning as long-term agentic memory.
* **Deterministic Guardrails**: Rigid boundary conditions and validation steps (e.g., anti-rationalization tables, schema validations) that force LLMs to follow sequential procedures without skipping steps.

### Explicit Mandates & Frameworks

#### Spec-Before-Code Mandate

The `agent-skills` framework enforces a hard chronological constraint on all AI implementations. The exact wording of the mandate is: _"Write a structured specification before writing any code. ... Code without a spec is guessing"_. This ensures that no implementation occurs until a human-approved `SPEC.md` exists, surfacing assumptions explicitly before execution.

#### Markdown Syntax for `.skill` Files

Skill files enforce strict parsing constraints for LLM consumption. Depending on the framework, the exact markdown schemas are enforced as follows:

* **agent-skills Schema:** `YAML frontmatter → Overview → When to Use → Core Process → Common Rationalizations → Red Flags → Verification`.

* **writing-skills YAML Frontmatter Validation:**
  
      name: Use letters, numbers, and hyphens only
      description: Third-person, describes ONLY when to use (NOT what it does) ... Start with "Use when..."

  This constraint strictly prohibits summarizing the skill's process, which acts as a Claude Search Optimization (CSO) technique to prevent the AI from shortcutting the full skill load.

* **React Best Practices Template:** `Frontmatter: title, impact (CRITICAL/HIGH/MEDIUM/LOW), tags. Body: explanation + code blocks labeled Incorrect/Correct.`.

* **OpenSpec Artifact Schema Definition:**
  
      artifacts: proposal: requires: [] ... specs: requires: [proposal] ... instructions: [full prompt template with <context> and <rules> injection]

  This defines the directed acyclic graph (DAG) for artifact generation.

#### Identified Causal Chains

* **User Sovereignty Trigger:** The `gstack` ethos defines User Sovereignty explicitly: _"AI recommends only; user decides. Always use generation-verification loop, present options via AskUserQuestion, never act unilaterally."_. If an agent attempts an autonomous destructive action, this rule initiates a manual override block requiring explicit user confirmation via platform-native blocking tools (e.g., AskUserQuestion).
* **3-Strike Error Protocol:** In the `planning-with-files` skill, a causal escalation chain is enforced: `ATTEMPT 1: Diagnose & Fix ... ATTEMPT 3: Broader Rethink ... AFTER 3 FAILURES: Escalate to User`. This breaks infinite hallucination loops and forces a manual human override.

### Comprehensive Directory of Extracted Skills and Slash Commands

Below is the exhaustive extraction of all named skills and slash commands implemented across the audited systems.

#### 1. gstack & context7 Frameworks

* **Commands:** `/autoplan`, `/plan-ceo-review`, `/review`, `/qa`, `/ship`, `/land-and-deploy`, `/canary`, `/office-hours`, `/retro`, `/browse`, `/cso`, `/codex`, `/careful`, `/freeze`, `/guard`.
* **Skills:** `/browse` (headless Chromium daemon), `/office-hours` (CEO diagnostic), `/cso` (security audit using OWASP + STRIDE), `/qa` (browser-based bug finding), `/codex` (multi-AI second opinion verification), and the Safety toolkit (`/careful`, `/freeze`, `/guard`).

#### 2. agent-skills Framework

* **Commands:** `/spec`, `/plan`, `/build`, `/test`, `/review`, `/ship`.
* **Skills:** `spec-driven-development` (generates the 6-area specification), `using-agent-skills` (meta-skill directory with task flowcharts), plus phase-specific modular capabilities: `idea-refine`, `planning-and-task-breakdown`, `incremental-implementation`, `test-driven-development`, `frontend-ui-engineering`, `api-and-interface-design`, `code-review-and-quality`, `security-and-hardening`. Also includes specialized reviewer personas (`code-reviewer`, `test-engineer`, `security-auditor`).

#### 3. Compound Engineering Plugin

* **Commands:** `/ce-strategy`, `/ce-brainstorm`, `/ce-plan`, `/ce-work`, `/ce-code-review`, `/ce-compound`, `/ce-product-pulse`, `/ce-ideate`, `/ce-debug`, `/ce-polish-beta`.
* **Skills:** `ce-plan` (creates durable implementation plans utilizing repo-relative paths), `ce-correctness-reviewer` (mentally executes code to hunt for off-by-one errors and null propagations). The toolkit encapsulates 38+ slash-invokable modules and 51 specialized agents.

#### 4. OpenSpec Toolkit

* **Commands:** `/opsx:propose`, `/opsx:apply`, `/opsx:sync`, `/opsx:archive`, `/opsx:new`, `/opsx:continue`, `/opsx:ff`, `/opsx:verify`, `/opsx:bulk-archive`, `/opsx:explore`.
* **Skills:** Artifact Generation (proposal, specs, design, tasks), `/opsx:apply` (task implementation and check-off), Config & Context Injection (loads `config.yaml`), CLI Integration (initializes `.claude/skills/`).

#### 5. Systematic Debugging & Git Worktrees (obra/superpowers)

* **Commands:** `/systematic-debugging`, `/using-git-worktrees`, `/writing-skills`.
* **Skills:** `systematic-debugging` (enforces 4-phase root-cause investigation), `root-cause-tracing`, `defense-in-depth` (injects 4-layer validation), `condition-based-waiting`, `find-polluter` (bisection bash script), `using-git-worktrees` (creates isolated workspaces with mandatory `.gitignore` verification), `writing-skills` (meta-skill enforcing TDD on process documentation), `test-driven-development`, `subagent-driven-development`.

#### 6. PM-Skills Marketplace

* **Commands:** `/discover`, `/plugin-name:skill-name`, `/skill-name`.
* **Skills:** `opportunity-solution-tree` (Teresa Torres framework mapping), `brainstorm-ideas-*`, `identify-assumptions-*`, `prioritize-assumptions`, `brainstorm-experiments-*`. The system incorporates 65 auto-loading PM framework skills.

#### 7. Vercel Agent Browser & React Best Practices

* **Commands:** `/core-loop`, `/quickstart-batch`, `/login`, `/state-persist`, `/specialized-load`, `/build-skill`, `/create-new-rule`.
* **Skills:** `vercel-react-best-practices` (enforcing specific tags like async-parallel and bundle-barrel-imports), `snapshot` (accessibility tree indexing with `@eN` refs), `open / navigate / close`, `click / fill / type / press / select / check`, `wait` (state synchronization), `get / find`, `skills` (meta-loader for electron/slack/dogfood contexts).

#### 8. Security Scanning Pipeline

* **Commands:** `/security-threat-modeling-pipeline`.
* **Skills:** `attack-tree-construction` (finds easiest/cheapest/stealthiest attack paths), `sast-configuration` (generates Semgrep/SonarQube/CodeQL configs), `security-requirement-extraction` (maps to STRIDE), `stride-analysis-patterns`, `threat-mitigation-mapping` (generates `MitigationPlan` dataclasses).

#### 9. Persistent Planning

* **Skills:** `planning-with-files` (implements Manus-style disk memory utilizing `task_plan.md`, `findings.md`, and `progress.md`), Session Recovery & Multi-Plan Isolation scripts.

### Statistical Data and Telemetry Extraction

* **Agent Self-Correction Success Rates:** The `writing-skills` module relies on a persuasion-engine designed to achieve _"72%+ compliance under pressure"_. The overarching TDD subagent pressure testing explicitly mandates iterating until _"100% compliance under all pressures"_ is verified.
* **Security Scan Coverage:** The `gstack` framework operates on a strict _"100% tests"_ behavioral constraint.
* _Note: Statistical data regarding exact security scan coverage percentages, exact numerical agent self-correction success rates beyond the 72% baseline, and quantitative memory overhead are not available in current sources._ Context management overhead is conceptually described as shifting from RAM to Disk via `.md` files.
