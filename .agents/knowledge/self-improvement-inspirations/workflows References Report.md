### Technical Definitions

**Workflow (Agentic):** A deterministic, sequential, or state-driven procedure orchestrated by an AI system to achieve a lifecycle objective. In production-grade systems, workflows act as state machines that transition between modular skills, often gated by persistent behavioral constraints and deterministic guardrails. **Slash-Invokable Procedure:** A standardized command paradigm (e.g., `/autoplan`) utilized to trigger specific execution pipelines, explicitly mapping user intent to a predefined sequence of agent capabilities. **State Persistence:** The architectural practice of externalizing an agent's volatile working memory onto persistent storage (e.g., disk-based markdown files) to ensure recovery across context windows or session interruptions.

### Standardized Methodology: Agentic Workflows Audit

The following extracted workflows define the sequential pipelines and orchestrations utilized across the audited repositories to guarantee deterministic agent execution, reliability, and security compliance.

#### 1. Gstack Architecture Workflows

_Note: This standardized methodology is duplicated identically across Exa Search, context7, gstack, and obra brainstorming architectural configurations._

* **Workflow 1: `/autoplan` (full sprint pipeline)** This sequence is invoked upon a feature request and triggers a pipeline: CEO review (`/plan-ceo-review`) → design review → eng review → DX review → implementation → `/review` → `/qa` → `/ship` [gstack agent audit report.md, Section 2]. It explicitly chains multiple specialist skills with intermediate user sovereignty checkpoints [gstack agent audit report.md, Section 2].
* **Workflow 2: `/review` (PR review + fix loop)** Triggered on any branch containing changes, it sequentially executes: Detect branch/plan → diff analysis → slop scan → critical checks (SQL, trust boundaries) → specialist dispatch (parallel agents) → fix-first (auto or ask) → verification [gstack agent audit report.md, Section 2]. It maintains a strict dependency on the `/browse` skill for contextual memory retrieval [gstack agent audit report.md, Section 2].
* **Workflow 3: `/ship` (release workflow)** Executed post-`/review` and `/qa`, this sequence runs tests + review + push + open PR, integrating deeply with `/land-and-deploy` and `/canary` commands [gstack agent audit report.md, Section 2]. It imposes a strict dependency on the `/guard` safety check [gstack agent audit report.md, Section 2].
* **Workflow 4: Overall sprint (Think-Plan-Build-Review-Test-Ship-Reflect)** Enforced via routing rules in the configuration files, the sequence dictates: `/office-hours` → `/plan-ceo-review` → build → `/review` → `/qa` → `/ship` → `/retro` [gstack agent audit report.md, Section 2]. Guardrails like `/freeze` and `/guard` can interrupt this pipeline [gstack agent audit report.md, Section 2].
* **Workflow 5: Skill routing (request-type dispatch)** A core routing logic injected at session initialization parses the user request, matches it to a specialist role, and invokes the corresponding `/skill` (e.g., strategy to CEO, code to eng) [gstack agent audit report.md, Section 2].

#### 2. Agent Skills Workflows

* **Workflow 1: `/spec`** Requires a mandatory human review gate and triggers on the start of a significant codebase change [agent skills agent audit report.md, Section 2]. The sequence is: 1. Understand user intent → ask clarifying questions (objective, features, tech, boundaries) → 2. Generate SPEC.md covering six core areas → 3. Save to repo root → 4. Confirm with human before proceeding [agent skills agent audit report.md, Section 2].
* **Workflow 2: Full development lifecycle (DEFINE → PLAN → BUILD → VERIFY → REVIEW → SHIP)** Skills automatically activate by context through the sequence: `/spec` (DEFINE) → `/plan` (PLAN) → `/build` (BUILD with incremental + TDD) → `/test` (VERIFY) → `/review` (REVIEW) → `/ship` (SHIP) [agent skills agent audit report.md, Section 2].
* **Workflow 3: Spec-driven gated workflow (internal to skill)** An internal pipeline tracking a living document: Phase 1: Specify (assumptions + 6-area spec) → Human review → Phase 2: Plan (components/dependencies) → Human review → Phase 3: Tasks (atomic with acceptance/verify) → Phase 4: Implement (via incremental + TDD) [agent skills agent audit report.md, Section 2].
* **Workflow 4: Skill invocation & orchestration (OpenCode/Claude)** Operates on parallel fan-out for multi-persona review [agent skills agent audit report.md, Section 2]. Sequence: 1. Determine skill match → 2. Invoke via skill tool → 3. Follow workflow strictly → 4. Only proceed after required steps [agent skills agent audit report.md, Section 2].

#### 3. Compound Engineering Workflows

* **Workflow 1: `[/ce-strategy]`** An upstream anchor workflow designed to create/maintain `STRATEGY.md` (target problem, approach, persona, metrics, tracks), which acts as a grounding parameter read by downstream skills [compound engineering agent audit report.md, Section 2].
* **Workflow 2: `[/ce-brainstorm → /ce-plan → /ce-work → /ce-code-review → /ce-compound]` (core loop)** A continuous execution loop: Brainstorm requirements → Plan implementation → Execute with worktrees/task tracking → Multi-agent code review → Document learnings (repeat with compounded context) [compound engineering agent audit report.md, Section 2].
* **Workflow 3: `[/ce-plan]` (multi-phase planning workflow)** Always triggered upon direct invocation to prevent abandonment, iterating through: Phase 0 (Resume/Source/Scope) → Phase 1 (Context/Research) → Phase 2 (Questions) → Phase 3 (Structure) → Phase 4 (Write plan) → Phase 5 (Review/Confidence Check/Handoff) [compound engineering agent audit report.md, Section 2].
* **Workflow 4: `[/ce-code-review]` (multi-agent review)** Invokes sub-agents using a tiered persona pipeline (correctness, security, maintainability), establishes confidence gating, deduplicates pipeline outputs, and hands off to `/ce-compound` or `/ce-polish-beta` [compound engineering agent audit report.md, Section 2].
* **Workflow 5: `[/ce-debug]`** Triggered by bug reports, the system executes: Reproduce failures → trace root cause → form/testable hypotheses → implement test-first fixes [compound engineering agent audit report.md, Section 2].

#### 4. Git Worktrees Workflows

* **Workflow 1: `/using-git-worktrees`** Triggered after the design approval phase to guarantee a clean workspace [git worktrees skill agent audit report.md, Section 2]. The deterministic procedure is: 1. Announce activation. 2. Directory Selection Process. 3. Safety Verification (gitignore check + auto-fix + commit). 4. Project name detection from git toplevel. 5. `git worktree add` + cd into new branch. 6. Auto-detect & run project setup. 7. Baseline test run + verification. 8. Report readiness with path/status [git worktrees skill agent audit report.md, Section 2].

#### 5. Meta Skill (Writing Skills) Workflows

* **Workflow 1: `/writing-skills` (TDD-adapted skill authoring)** Mandatory sequence prior to deploying any skill: 1. Identify need. 2. Run baseline pressure scenario WITHOUT skill (RED). 3. Document exact agent rationalizations/failures. 4. Write minimal SKILL.md. 5. Re-run pressure tests with skill (GREEN). 6. Refactor (REFACTOR cycle) [meta skill agent audit report.md, Section 2].
* **Workflow 2: SKILL.md authoring template invocation** Enforces a progressive disclosure format: 1. YAML frontmatter. 2. Overview. 3. When to Use. 4. Core Pattern / Quick Reference. 5. Implementation. 6. Common Mistakes + fixes. 7. Real-World Impact [meta skill agent audit report.md, Section 2].
* **Workflow 3: Pressure-testing with subagents** Dependent on subagent-driven development: 1. Create multi-pressure scenarios. 2. Force explicit A/B/C choices. 3. Run agent with/without skill. 4. Observe compliance delta. 5. Iterate until 100% compliance [meta skill agent audit report.md, Section 2].

#### 6. OpenSpec Workflows

* **Workflow 1: `/opsx:propose`** Sequence triggers AI generation of planning artifacts based on schema dependencies: 1. User invokes `/opsx:propose "idea"` → 2. Creates `openspec/changes/<name>/` architecture → 3. AI generates planning artifacts → 4. Ready for `/opsx:apply` [openspec agent audit report.md, Section 2].
* **Workflow 2: Core Quick Path** A fluid, artifact-driven pipeline: propose (planning) → apply (implementation with task check-off) → sync (delta specs to main, optional) → archive (move to archive/ with timestamp) [openspec agent audit report.md, Section 2].
* **Workflow 3: Expanded Path** Detailed progression querying schema dependency graphs: new (scaffold) → continue/ff (incremental or all planning artifacts) → apply → verify (validate impl vs artifacts) → archive/bulk-archive [openspec agent audit report.md, Section 2].
* **Workflow 4: `/opsx:explore` (non-structured thinking)** Acts as a thinking partner enabling non-structured investigation, smoothly transitioning to `/opsx:propose` or `/opsx:new` when artifacts must be created [openspec agent audit report.md, Section 2].

#### 7. Planning with Files Workflows

* **Workflow 1: Restore Context (mandatory on skill activation / session resume)** Sequence enforcing state persistence: 1. Check for `task_plan.md` existence. 2. Execute `session-catchup.py`. 3. Run `git diff --stat` if unsynced changes detected. 4. Update planning files. 5. Proceed only after full re-orientation [planning with files agent audit report.md, Section 2].
* **Workflow 2: Lifecycle Hook Injection & Update Cycle** Uses matcher-based hooks across the agent lifecycle: `UserPromptSubmit` → inject plan data header + recent progress; `PreToolUse` → prepend plan snippet; `PostToolUse` → remind "Update progress.md..."; `Stop` → run check-complete script [planning with files agent audit report.md, Section 2].
* **Workflow 3: Core Planning Pattern (3-File Persistent Memory)** State-saving iteration: 1. Create/init tracking files. 2. Read Before Decide. 3. Act + 2-Action Rule update. 4. Update After Act (status + errors). 5. Continue After Completion (append phases) [planning with files agent audit report.md, Section 2].

#### 8. PM-Skills Workflows

* **Workflow 1: `/discover`** Chains minimum of 4 modular skills: Step 1: Understand context → Step 2: Brainstorm ideas → Step 3: Identify assumptions → Step 4: Prioritize assumptions → Step 5: Design experiments → Step 6: Create discovery plan document → Step 7: Offer next steps [pm-skills agent audit report.md, Section 2].
* **Workflow 2: Marketplace-wide command invocation pattern** Uses a cross-plugin methodology: User types `/command-name` → Claude loads relevant plugin + chained skills → Executes step-by-step workflow → Outputs structured artifact + suggests follow-up commands [pm-skills agent audit report.md, Section 2].

#### 9. React Best Practices Workflows

* **Workflow 1: `/build-skill` (maintainer compilation flow)** A deterministic build and test orchestration: `pnpm install` → `pnpm build` (extracts rules → generates `AGENTS.md` + `test-cases.json`) → `pnpm validate` → `pnpm extract-tests` [react best practices skill agent audit report.md, Section 2].
* **Workflow 2: `/create-new-rule` (rule authoring flow)** Maintains exact formatting templates: Copy `rules/_template.md` → rename with area-prefix → fill frontmatter + examples → run `pnpm build` [react best practices skill agent audit report.md, Section 2].
* **Workflow 3: Agent skill invocation trigger** Contextually triggered code execution: Detect React/Next.js task → load `AGENTS.md` → apply relevant rules by category/impact → output optimized code [react best practices skill agent audit report.md, Section 2].

#### 10. Security Scanning Workflows

* **Workflow 1: `/security-threat-modeling-pipeline` (implicit sequential invocation)** An interconnected, defense-in-depth orchestration: 1. STRIDE analysis → 2. Security requirement extraction → 3. Attack tree construction → 4. Threat mitigation mapping → 5. SAST configuration generation [security scanning skill agent audit report.md, Section 2].
* **Workflow 2: Attack tree construction & analysis sequence** Risk-prioritized logic block: Build `AttackTree` → Add `AttackNode(s)` → Compute paths (easiest/cheapest/stealthiest) → JSON export → Visualization [security scanning skill agent audit report.md, Section 2].
* **Workflow 3: SAST tool configuration & CI/CD deployment** Procedural enforcement for scanning integrity: Select tool (Semgrep/SonarQube/CodeQL) → Generate config (YAML/bash) → Integrate into CI/CD → Add custom rules → Validate [security scanning skill agent audit report.md, Section 2].

#### 11. Systematic Debugging Workflows

* **Workflow 1: `/systematic-debugging` (4-Phase Debugging Procedure)** A strict diagnostic mechanism preventing unverified patching: 1. Root Cause Investigation. 2. Pattern Analysis. 3. Hypothesis and Testing. 4. Implementation (triggers architectural query on 3+ failures) [systematic debugging skill agent audit report.md, Section 2].
* **Workflow 2: Backward Root-Cause Tracing** Data flow extraction process: Start from symptom → trace backward through call chain/stack → add instrumentation/logs → identify original trigger; seamlessly integrates with `find-polluter.sh` [systematic debugging skill agent audit report.md, Section 2].
* **Workflow 3: Defense-in-Depth Validation** Triggered immediately post-tracing to layer safety checks: Add 4-layer validation (Entry → Business Logic → Env Guards → Debug Instrumentation) [systematic debugging skill agent audit report.md, Section 2].
* **Workflow 4: Condition-Based Waiting (Flakiness Elimination)** Implementation level routine: Replace arbitrary sleeps/timeouts with `waitFor(condition)` polling loop until predicate is met [systematic debugging skill agent audit report.md, Section 2].

#### 12. Vercel Agent Browser Workflows

* **Workflow 1: `/core-loop` (snapshot-and-ref)** Maintains referential DOM validation via CDP: 1. `agent-browser open <url>` → 2. `agent-browser snapshot -i` → 3. `agent-browser click/fill @eN` (ref from snapshot) → 4. `agent-browser snapshot -i` [vercel agent browser skill agent audit report.md, Section 2].
* **Workflow 2: `/quickstart-batch`** Multi-command serialization logic: `agent-browser batch "open <url>" "snapshot -i" "click @eN" ...` (or JSON stdin) [vercel agent browser skill agent audit report.md, Section 2].
* **Workflow 3: `/login` (with auth vault)** Credential orchestration isolating PII: 1. `agent-browser auth save` → 2. `agent-browser open <login-url>` → 3. `agent-browser auth login` → 4. `agent-browser wait --url "**/dashboard"` → 5. `agent-browser snapshot -i` [vercel agent browser skill agent audit report.md, Section 2].
* **Workflow 4: `/state-persist` (session restore)** Session bridging paradigm: 1. `agent-browser state save ./auth.json` (after login) → 2. Later: `agent-browser --state ./auth.json open <url>` [vercel agent browser skill agent audit report.md, Section 2].
* **Workflow 5: `/specialized-load`** Domain contextual context shifting: `agent-browser skills get core` (or electron/slack/dogfood/vercel-sandbox/agentcore) → use loaded skill commands [vercel agent browser skill agent audit report.md, Section 2].
