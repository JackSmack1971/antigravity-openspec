# APEX Framework Changelog

## [2026-05-03] - Execution Skills: git-worktrees + systematic-debugging
### Added
- `.agents/skills/execution/using-git-worktrees/scripts/gitignore-check.sh`
- `.agents/skills/execution/systematic-debugging/scripts/find-polluter.sh`

### Changed
- `.agents/skills/execution/using-git-worktrees/SKILL.md`: Surgically updated to mandate `gitignore-check.sh`, include Worktree Cleanup and Rule 11 (repo-relative paths) mandates.
- `.agents/skills/execution/systematic-debugging/SKILL.md`: Surgically updated to mandate Pitfall KI check in Phase 1 and include 3-Strike Escalation and Sub-skills list.

## [2026-05-03] - KI Curator Skill + Archive Directory
### Added
- `.agents/skills/governance/ki-curator/SKILL.md` (SemVer+archive governance for KI lifecycle).
- `.agents/knowledge/archive/.gitkeep` (archive directory for superseded KIs).

## [2026-05-03] - Governance Skills Update
### Added
- `.agents/skills/governance/using-agent-skills/SKILL.md` (meta-discovery flowchart for task-to-skill mapping).

### Skipped (GOLDEN RULE)
- `.agents/skills/governance/planning-with-files/SKILL.md` — Existing file is highly mature (v2.36.3), contains all requested 3-file nucleus and 2-action rule mechanics.
- `.agents/skills/governance/spec-driven-development/SKILL.md` — Existing file is mature, contains requested 6-area spec structure and human review gates.

## [2026-05-03] - AGENTS.md Master Router v2026-05-full
### Changed
- Registered 22 additional slash commands (`/open`, `/qa`, `/ce-strategy`, `/ce-brainstorm`, `/ce-work`, `/opsx:apply`, `/opsx:sync`, `/opsx:archive`, `/opsx:new`, `/opsx:continue`, `/opsx:ff`, `/opsx:verify`, `/opsx:bulk-archive`, `/opsx:explore`, `/office-hours`, `/codex`, `/browse`, `/careful`, `/guard`, `/freeze`, `/discover` alias, `/restore-context`) in REGISTERED WORKFLOWS.
- Enhanced `Stop` lifecycle hook: added `--dashboard` flag to `crystallization-tracker.py`, conditional `/retro` prompt on milestone complete, and Uplift% logging directive to `.agents/knowledge/self-improvement/`.
- GOLDEN RULE applied to IMMUTABLE RULES: `@.agents/rules/01–07` already present (00–12 registered); no duplicate entries added.

### Added
- **POWER-CHAINS (auto-fire)** section after SELF-IMPROVEMENT TERMINUS: Chains A–F with full workflow sequences (distinct from existing Governance Triads table which is more mature and retained).
- **SKILL REGISTRY** section (27 entries): Layer 1 metadata index mapping skill paths to descriptions across governance, execution, review-qa-security, orchestration, meta-ki, and gstack categories.

## [2026-05-03] - Governance Audit: Full 13-Rule Set Verified (v2026-05-rules-audit)
### Verified (GOLDEN RULE — no overwrites)
- Audited `.agents/rules/` — all 13 rule files (00–12) confirmed present and more mature than spec.
- Rules 01–05 (`spec-before-code`, `planning-memory`, `security-baseline`, `progressive-disclosure`, `ki-governance`) contain evolved content (STRIDE, 3-File Nucleus, CSO, YAML frontmatter descriptions) exceeding the requested spec. No overwrites applied.
- Rules 06 (`terminal-execution`) and 07 (`visual-verification`) are the repository's evolved equivalents of the spec's `orchestration-safety` and `output-discipline` — retained as authoritative.
- GOLDEN RULE applied: "If a better more mature file already exists, skip any modifications."

## [2026-05-02] - ce-plan Level 4 Upgrade (v2026-05-ce-plan-l4)
### Changed
- Upgraded `.agents/skills/execution/ce-plan/SKILL.md` from Level 2 to Level 4: Added telegraphic phases, positive framing, and n-gram abbreviations (IU, AC, CS, DP).
- Replaced the prose-based Phase 5 confidence gate with a deterministic black-box Python script (`scripts/validate-plan.py`).
- Appended a `<ki_extraction>` block to enforce the `/retro` loop and continuous self-improvement.

### Added
- Created `.agents/skills/execution/ce-plan/scripts/validate-plan.py` for deterministic plan validation.
- Created `.agents/skills/execution/ce-plan/examples/golden-plan.md` to provide a few-shot semantic scaffold.
- Created `.agents/skills/execution/ce-plan/resources/plan-template.md` as the reusable markdown baseline.
- Updated `plan-template.md` with detailed scaffolding (Status/CS tracking, formal IU definitions, table structures for Dependencies and Risks, and distinct plan-level vs IU-level Acceptance Criteria).
- Updated `golden-plan.md` with a high-fidelity "Rate-Limiting Auth API" scenario, demonstrating proper IU abstraction, table formatting, and gap justification for CS < 100%.
- Upgraded `validate-plan.py` to a robust script utilizing Regex extraction to ensure strict compliance (no absolute paths, Confidence Score >= 70, per-IU Acceptance Criteria) and returning standardized JSON stdout for deterministic agent handoff.

## [2026-05-02] - Systematic Debugging Workflows Update (v2026-05-debug-workflows)
### Added
- Created `.agents/workflows/engineering/backward-root-cause-tracing.md` — Backward Root-Cause Tracing sequence: Deterministic data flow extraction integrating with find-polluter.sh.
- Created `.agents/workflows/engineering/defense-in-depth-validation.md` — Defense-in-Depth Validation workflow: 4-layer safety check (Entry → Business Logic → Env Guards → Debug Instrumentation).
- Created `.agents/workflows/engineering/condition-based-waiting.md` — Condition-Based Waiting routine: Flakiness elimination via predicate polling loops.

### Changed
- Renamed and upgraded `ce-debug.md` to `.agents/workflows/engineering/systematic-debugging.md` — `/systematic-debugging`: Enforced strict 4-Phase Procedure (Root Cause Investigation → Pattern Analysis → Hypothesis/Testing → Implementation) with architectural escalation triggers on 3+ failures.

## [2026-05-02] - Security Scanning Workflows Update (v2026-05-security-workflows)
### Added
- Created `.agents/workflows/security/attack-tree-construction.md` — Attack tree construction sequence: Risk-prioritized logic block (Build → Add Nodes → Compute paths → JSON export → Visualization).
- Created `.agents/workflows/security/sast-deployment.md` — SAST Tool Configuration & CI/CD Deployment: Procedural enforcement for automated scanning (Select → Configure → Integrate → Custom rules → Validate).

### Changed
- Upgraded `.agents/workflows/security/threat-model-pipeline.md` — `/security-threat-modeling-pipeline`: Explicitly detailed the interconnected 5-step defense-in-depth orchestration sequence.

## [2026-05-02] - React Best Practices Workflows Update (v2026-05-react-workflows)
### Added
- Created `.agents/workflows/react/build-skill.md` — `/build-skill` workflow: Deterministic compilation flow (pnpm install → build → validate → extract-tests).
- Created `.agents/workflows/react/create-new-rule.md` — `/create-new-rule` workflow: Exact template formatting rule authoring flow.
- Created `.agents/workflows/react/react-skill-invocation.md` — Agent Skill Invocation workflow: Contextually triggered activation for React/Next.js domain tasks.

## [2026-05-02] - PM-Skills Workflows Update (v2026-05-pm-workflows)
### Added
- Created `.agents/workflows/pm/marketplace-invocation.md` — Marketplace-wide Command Invocation Pattern: Cross-plugin methodology for fluid execution and handoffs.

### Changed
- Upgraded `.agents/workflows/pm/discover.md` — `/discover`: Explicitly structured the 7-step sequence (Understand context → Brainstorm → Identify assumptions → Prioritize → Design experiments → Create plan → Offer next steps).

## [2026-05-02] - Planning with Files Workflows Update (v2026-05-planning-workflows)
### Added
- Created `.agents/workflows/engineering/planning-restore-context.md` — `/planning-restore-context` workflow: Mandatory state persistence sequence on session resume.
- Created `.agents/workflows/engineering/planning-lifecycle-hooks.md` — `/planning-lifecycle-hooks` workflow: Matcher-based hooks (UserPromptSubmit, PreToolUse, PostToolUse, Stop) across the operational lifecycle.
- Created `.agents/workflows/engineering/planning-core-pattern.md` — `/planning-core-pattern` workflow: 3-File Persistent Memory state-saving iteration loop (task_plan, progress, findings).

## [2026-05-02] - OpenSpec Workflows Update (v2026-05-openspec-workflows)
### Added
- Created `.agents/workflows/openspec/opsx-core-quick-path.md` — Core Quick Path workflow: propose → apply → sync → archive.
- Created `.agents/workflows/openspec/opsx-expanded-path.md` — Expanded Path workflow: new → continue/ff → apply → verify → archive/bulk-archive.
- Created `.agents/workflows/openspec/opsx-explore.md` — `/opsx:explore` workflow: Non-structured thinking partner transitioning to proposal artifacts.

### Changed
- Upgraded `.agents/workflows/openspec/opsx-propose.md` — `/opsx:propose`: Formalized the 4-step AI generation sequence based on schema dependencies.

## [2026-05-02] - Meta Skill Workflows Update (v2026-05-meta-workflows)
### Added
- Created `.agents/workflows/meta/skill-authoring-template.md` — `/skill-authoring-template` workflow: Enforces a progressive disclosure format for SKILL.md creation.
- Created `.agents/workflows/meta/pressure-testing.md` — `/pressure-testing` workflow: Subagent-driven development for pressure testing SKILL.md compliance.

### Changed
- Upgraded `.agents/workflows/meta/writing-skills.md` — `/writing-skills`: Streamlined the TDD skill authoring sequence into a mandatory 6-step loop.

## [2026-05-02] - Compound Engineering Workflows Update (v2026-05-ce-workflows)
### Added
- Created `.agents/workflows/engineering/ce-strategy.md` — `/ce-strategy` workflow: Upstream anchor for STRATEGY.md initialization.
- Created `.agents/workflows/engineering/ce-brainstorm.md` — `/ce-brainstorm` workflow: Requirements brainstorming phase.
- Created `.agents/workflows/engineering/ce-work.md` — `/ce-work` workflow: Execution and implementation phase.
- Created `.agents/workflows/engineering/using-git-worktrees.md` — `/using-git-worktrees` workflow: 8-step deterministic clean workspace guarantee.

### Changed
- Upgraded `.agents/workflows/engineering/ce-plan.md` — `/ce-plan`: Detailed the 6 iterative phases explicitly (Phase 0 to Phase 5).
- Upgraded `.agents/workflows/engineering/ce-code-review.md` — `/ce-code-review`: Explicitly defined handoff criteria to `/ce-compound` or `/ce-polish-beta`.
- Upgraded `.agents/workflows/engineering/ce-debug.md` — `/ce-debug`: Structured exactly to a 4-step sequence (Reproduce failures → trace root cause → form testable hypotheses → implement test-first fixes).
- Upgraded `.agents/workflows/engineering/ce-compound.md` — `/ce-compound`: Explicitly represented as the final phase of the continuous core loop.

## [2026-05-02] - Agent Skills Workflow Suite (v2026-05-agent-skills-v1)
### Added
- Created `.agents/workflows/engineering/development-lifecycle.md` — `/dev-lifecycle` workflow: Full development lifecycle (DEFINE → PLAN → BUILD → VERIFY → REVIEW → SHIP).
- Created `.agents/workflows/engineering/spec-driven-development.md` — `/sdd` workflow: Internal spec-driven gated workflow for tracking living documents.
- Created `.agents/workflows/engineering/skill-orchestration.md` — `/orchestrate` workflow: Skill invocation & orchestration with parallel fan-out personas.

### Changed
- Upgraded `.agents/workflows/sprint/spec.md` — `/spec`: Added mandatory human review gate and 6-area generation sequence.

## [2026-05-02] - Gstack Sprint Workflow Suite (v2026-05-gstack-sprint-v1)
### Added
- Created `.agents/workflows/sprint/sprint.md` — `/sprint` workflow: canonical Think-Plan-Build-Review-Test-Ship-Reflect sprint lifecycle; phase map with `/office-hours → /plan-ceo-review → /spec → build → /review → /qa → /ship → /retro`; guardrail interrupt table (`/freeze`, `/guard`, 3-Strike). (Workflows Refs §1, Workflow 4)
- Created `.agents/workflows/sprint/skill-routing.md` — `/skill-routing` workflow: session-init request-type dispatcher; 15-row intent→role→workflow routing table; Power-Chain routing diagram (Chains A–G); anti-rationalization guardrail table. (Workflows Refs §1, Workflow 5)

### Changed (upgraded stubs to full gstack spec)
- Upgraded `.agents/workflows/sprint/autoplan.md` — `/autoplan`: expanded stub (9 lines) to full gstack sprint pipeline; added CEO review, design review, eng review, DX review phases; 4 User Sovereignty Checkpoints; guardrail interrupt section. (Workflows Refs §1, Workflow 1)
- Upgraded `.agents/workflows/sprint/review.md` — `/review`: expanded stub (5 lines) to full PR review + fix loop; 7-step sequence (detect→diff→slop→critical→parallel-dispatch→fix-first→verify); `/browse` skill dependency; parallel 3-agent specialist dispatch with confidence gating. (Workflows Refs §1, Workflow 2)
- Upgraded `.agents/workflows/sprint/ship.md` — `/ship`: expanded stub (5 lines) to full release workflow; strict `/guard` dependency; `/land-and-deploy` and `/canary` integration; stale review detection; mandatory `/retro` terminus. (Workflows Refs §1, Workflow 3)
- Updated `AGENTS.md` lifecycle hook: `UserPromptSubmit` now chains `/skill-routing` before plan injection; registered `/sprint` and `/skill-routing` in REGISTERED WORKFLOWS.

## [2026-05-02] - Browser Automation Workflow Suite (v2026-05-browser-workflows-v1)
### Added

- Created `.agents/workflows/browser/core-loop.md` — `/core-loop` workflow: CDP referential DOM validation via snapshot-and-ref loop. Enforces mandatory re-snapshot after every page state change. (Audit Report §2, Workflow 1)
- Created `.agents/workflows/browser/quickstart-batch.md` — `/quickstart-batch` workflow: Multi-command serialization via `agent-browser batch`; supports inline string args and JSON stdin with `--bail` fail-fast mode. (Audit Report §2, Workflow 2)
- Created `.agents/workflows/browser/login.md` — `/login` workflow: Auth vault credential orchestration isolating PII from shell history; chains `auth save → open → auth login → wait --url → snapshot -i`. (Audit Report §2, Workflow 3)
- Created `.agents/workflows/browser/state-persist.md` — `/state-persist` workflow: Session bridging paradigm for cross-run restore via `state save ./auth.json` and `--state` flag or `AGENT_BROWSER_SESSION_NAME` env. (Audit Report §2, Workflow 4)
- Created `.agents/workflows/browser/specialized-load.md` — `/specialized-load` workflow: Domain context shifting via `agent-browser skills get <domain>`; covers electron/slack/dogfood/vercel-sandbox/agentcore. (Audit Report §2, Workflow 5)

### Changed
- Upgraded Master Router (`AGENTS.md`) to **v2026-05-browser-workflows-v1**: registered all 5 browser workflows, expanded Power-Chain table from 5 to 6 chains with new **Chain G: Browser Automation** (Rules 03, 07 → /core-loop → /login → /state-persist).

## [2026-05-02] - Session Continuity Hardening & Script Path Fixes (v2026-05-continuity-v1)
### Fixed

- **Critical**: Fixed CWD-relative path bug in all 3 Python scripts (`crystallization-tracker.py`, `check-complete.py`, `session-catchup.py`). All scripts now use `os.path.abspath(__file__)` to resolve workspace root, preventing failures when called from any working directory on Windows (Rule 11.5).

### Added
- **Pitfall KI**: Created `.agents/knowledge/pitfalls/session_continuity_failure.md` — crystallization of the repeated bootstrapping pattern (18+ hit trigger, 2026-05-02). Documents the root cause, resolution protocol, and prevention signal.
- **Playbook**: Created `.agents/knowledge/playbooks/session-init-checklist.md` — mandatory pre-flight checklist for all meta/governance sessions. Enforces CHANGELOG audit and conversation history check before any framework analysis.
- **`crystallization-tracker.py`**: Added `--dashboard` flag for full Autonomy Uplift Dashboard output (Rule 09.6 format). Added `get_30day_uplift()` function for 30-day crystallization window tracking. Added session history display (last 5 sessions).
- **`session-catchup.py`**: Added in-progress `[/]` task detection — agents resuming a session now know exactly which task to pick up.

### Changed
- Updated `ANTIGRAVITY-KB.md` index to reference `circuit_breaker_reporting.md` (created in v2026-05-path-hardened-v3 but missing from index) and new `session-init-checklist.md` and `session_continuity_failure.md`.
- Updated `.agents/skills/governance/self_evolution/SKILL.md` Step 1: replaced "read all 17 inspirations files" with index-first progressive disclosure (select ≤2 relevant files per Rule 04 3-Skill Cap). Added Session Init Checklist as mandatory first step.


### Added
- Created `.agents/knowledge/playbooks/circuit_breaker_reporting.md` to standardize `STRIKE_THREE_HALT` reports.
- Added **Governance Compliance Audit** mandate to `.agents/skills/governance/metrics-auditor/SKILL.md`.

### Changed
- Hardened Rule 10 (Context Budget) with a **Proactive Consolidation** trigger at 80k tokens.
- Hardened Rule 11 (Path Governance) with the **Trust Anchor Handshake** protocol for Windows tool resolution.
- Upgraded Master Router (`AGENTS.md`) to **v2026-05-path-hardened-v3**.

### Added
- Created `.agents/knowledge/playbooks/context_resilience_playbook.md` to formalize Power-Chain F (Rule 12) and Hallucination Circuit Breaker (Rule 10.4) protocols.

### Changed
- Upgraded Master Router (`AGENTS.md`) to **v2026-05-path-hardened-v2**.
- Hardened `.agents/skills/governance/self_evolution/SKILL.md` with Rule 11 (Path Governance) and Rule 12 (Context Resilience) Quality Gates.
- Synchronized modular Knowledge Items (`mcp_integration.md`, `path_resolution_pitfalls.md`, `ANTIGRAVITY-KB.md`) with the latest v2026-05 governance mandates.
- Integrated Rule 11.5 (Tool Path Normalization) into Windows-specific resolution protocols.

## [2026-05-02] - Path Governance & Hallucination Circuit Breaker (v2026-05-path-hardened)
### Added
- Created `.agents/rules/11-path-governance.md` to strictly mandate repo-relative paths and prevent Windows path resolution pitfalls.
- Added **Power-Chain F: Context Resilience** to `AGENTS.md` for proactive high-density context management.

## [2026-05-02] - Framework Hardening & Governance Unification (v2026-05-hardened-v2)
### Added
- Created `.agents/rules/12-context-resilience.md` to formalize Power-Chain F protocols.
- Created `progress.md` in workspace root for tactical 2-action tracking.
- Added "Rule Discovery" note to `00-constitution.md` for legacy Karpathy Mandate traceability.

### Changed
- Hardened `11-path-governance.md` with **Tool Path Normalization** (absolute path mandate for tool calls).
- Synchronized Master Router (`AGENTS.md`) with Rule 12 and formalized tactical tracking hooks.

### Changed
- Upgraded Master Router (`AGENTS.md`) to **v2026-05-path-hardened**.
- Hardened `.agents/rules/10-context-budget-governance.md` with the **Hallucination Circuit Breaker** (3-Strike Tool Strike protocol).
- Expanded Master Router description to include Path Governance.

## [2026-05-02] - Framework Hardening v2 (v2026-05-hardened-v2)
### Added
- Created `.agents/knowledge/playbooks/pitfall_extraction.md` to standardize high-density KI creation.
- Implemented **Reasoning Anchor Protocol** in `.agents/rules/10-context-budget-governance.md`.
- Implemented **Autonomy Uplift Dashboard** mandate in `.agents/rules/09-self-improvement-uplift.md`.

### Changed
- Hardened **Windows Tool Path Normalization** in `.agents/rules/11-path-governance.md` with absolute path mandate.
- Integrated **Uplift Dashboard** and **Pitfall Template** into `.agents/workflows/sprint/retro.md`.
- Linked Pitfall Extraction playbook in `.agents/knowledge/self-improvement/ANTIGRAVITY-KB.md`.

## [2026-05-02] - Framework Hardening & Context Governance (v2026-05-hardened)
### Added
- Created `.agents/rules/10-context-budget-governance.md` to formalize context window management and JIT skill unloading.
- Created `.agents/skills/governance/metrics-auditor/SKILL.md` to automate autonomy uplift logging via `crystallization-tracker.py`.

### Changed
- Upgraded Master Router (`AGENTS.md`) to **v2026-05-hardened**.
- Hardened `.agents/rules/09-self-improvement-uplift.md` with the **Pre-emptive Pitfall Analysis** mandate and Extraction Gate.
- Expanded `.agents/workflows/engineering/ce-debug.md` to mandate a Pitfall Audit in Phase 1 (Investigate).

## [2026-05-02] - Framework Hardening & Knowledge Base Completion
### Added
- Created `.agents/knowledge/references/mcp_integration.md` to formalize Context7, GitHub, and Filesystem MCP governance.
- Created `.agents/knowledge/pitfalls/path_resolution_pitfalls.md` to document Windows filesystem access restrictions.

### Changed
- Reconciled `.agents/knowledge/playbooks/conflict_resolution.md` with the v2026-05 precedence hierarchy (Security > Constitution).
- Updated `.agents/rules/09-self-improvement-uplift.md` with the **Pitfall Mandate** for automated crystallization.
- Finalized `.agents/knowledge/self-improvement/ANTIGRAVITY-KB.md` index by removing "Planned" markers and linking new KIs.


### Added
- Created `.agents/rules/09-self-improvement-uplift.md` to define `Uplift%` metrics and the 30-day crystallization period.
- Implemented `.agents/scripts/crystallization-tracker.py` to automate autonomy uplift logging and aggregate metrics calculation.
- Defragmented monolithic `ANTIGRAVITY-KB.md` into specialized Knowledge Items:
    - `.agents/knowledge/playbooks/progressive_disclosure.md`
    - `.agents/knowledge/references/subagent_architecture.md`
    - `.agents/knowledge/playbooks/ki_lifecycle.md`
    - `.agents/knowledge/playbooks/conflict_resolution.md`
    - `.agents/knowledge/playbooks/task_management.md`
    - `.agents/knowledge/playbooks/visual_verification.md`

### Changed
- Upgraded Master Router (`AGENTS.md`) to **v2026-05**.
- Integrated Rule 09 and automated metrics logging into the `Stop` lifecycle hook in `AGENTS.md`.
- Hardened `00-constitution.md` with the **100% Compliance Threshold** mandate for all agent skills.
- Pruned `ANTIGRAVITY-KB.md` to a lean index for optimized context routing.
- Re-targeted KNOWLEDGE BASE DIRECTIVE in `AGENTS.md` to the new modular KI directories.


## [2026-05-02] - Framework Hardening & Windows Host Bridge
### Added
- Created `.agents/rules/08-windows-host-bridge.md` to handle WSL2 networking and Browser-to-Terminal subagent communication on Windows.
- Implemented `.agents/scripts/session-catchup.py` for persistent memory nucleus catchup.
- Implemented `.agents/scripts/check-complete.py` to enforce /retro loop completion.

### Changed
- Updated `AGENTS.md` to register the new Windows bridge rule and refined the `Conflict Resolution Precedence` matrix with `STRICT_MODE` escalation.
- Added `Context Budget Analytics` monitoring mandate to `AGENTS.md`.
- Modified `.agents/rules/06-terminal-execution.md` to mandate cross-referencing the Windows bridge rule on Windows hosts.

## [2026-05-02] - Knowledge Base Integration & Framework Hardening
### Added
- Integrated the `3-Strike Error Protocol` into `.agents/rules/02-planning-memory.md` to prevent infinite hallucination loops and force manual overrides.
- Added 4-layer validation (`defense-in-depth`) and `condition-based-waiting` constraints to `.agents/workflows/engineering/ce-debug.md`.

### Changed
- Expanded `/ce-debug` workflow to formally enforce the 4-phase root-cause-first rules (Investigate -> Pattern Analysis -> Hypothesis/Test -> Implement).
- Hardened `/ce-plan` workflow to strictly enforce `repo-relative paths only`, `decisions-not-code`, and centralized output to the `docs/plans/` directory.


## [2026-05-02] - Formalizing the Self-Improvement Loop
### Added
- Created `.agents/skills/meta-ki/ki-curator/SKILL.md` to properly handle Semantic Versioning (SemVer) of Knowledge Items (KIs) during conflict resolution and to prevent context rot.

### Changed
- Massively expanded `.agents/workflows/meta/writing-skills.md` from a stub into a full workflow.
- Enforced a strict 100% compliance threshold for the `writing-skills` GREEN TDD phase. The agent must successfully adhere to all L0 Foundational Rules under pressure scenarios before a skill can be promoted.

## [2026-05-02] - APEX Self-Improvement Architecture Formalization
### Added
- Created `.agents/workflows/meta/para-knowledge.md` for bi-weekly KI conflict resolution and context rot prevention.

### Changed
- Modified `.agents/rules/04-progressive-disclosure.md` to strictly enforce a maximum limit of 3 full `SKILL.md` payloads and monitor Context Budget Analytics.
- Modified `.agents/workflows/sprint/retro.md` to integrate the 30-day crystallization tracker and `Uplift%` metric tracking.
- Updated `scripts/check-complete.py` to make chaining to `/retro` mandatory on session closure to prevent dropped learnings.

## [2026-05-02] - Knowledge Base Integration & L0 Governance Audit
### Added
- Explicit L0 Foundational Rules (Karpathy Behavioral Mandates) to `.agents/rules/00-constitution.md`.
- Formalized references to `.agents/knowledge/self-improvement/ANTIGRAVITY-KB.md` in `AGENTS.md` to hardcode the self-improvement loop.
- Added L0 Compliance Quality Gates across all Agent Skills in `.agents/skills/` to ensure pressure-tested governance and 100% compliance threshold.

### Changed
- Updated `self_evolution` skill to explicitly mandate synthesizing the KB and checking L0 compliance during proposal phases.
- Updated `writing-skills` to enforce L0 compliance testing during the GREEN TDD phase.

## [2026-05-02] - Subagent Architecture & Governance
### Added
- Created `.agents/rules/06-terminal-execution.md` to establish boundaries for CLI orchestration and OS-level sandboxing expectations.
- Created `.agents/rules/07-visual-verification.md` to mandate visual proof and walkthrough generation for the Browser Subagent.
- Added Conflict Resolution Precedence Matrix to `AGENTS.md` explicitly defining the Constitutional Physics > Workflows > Skills Triad hierarchy.

### Changed
- Updated `agent-browser` SKILL.md to reference `07-visual-verification.md` as a mandatory Quality Gate.

## [2026-05-02] - Framework Edge-Case Hardening
### Added
- Created `scripts/check-complete.py` hook to prevent parent workflow abandonment by checking `task_plan.md` on session closure.
- Added 30-Day Crystallization tracking and Bi-Weekly KI Audit triggers to `AGENTS.md` SELF-IMPROVEMENT TERMINUS.

### Changed
- Hardened Rule 03 (Security Baseline) with a strict anti-bypass clause preventing `/guard` circumvention under time pressure.
- Hardened Rule 05 (KI Governance) with a KI Conflict Mitigation clause mandating bi-weekly audits and `ki-curator` SemVer bumps.

## [2026-04-02] - Framework Evolution v2026-04
### Added
- 5 Power-Chain orchestration mapping in `AGENTS.md`.
- Lifecycle hooks (`UserPromptSubmit`, `PreToolUse`, `PostToolUse`, `Stop`) for automated memory and `/retro`.
- Categorized directory structure for workflows (`sprint/`, `engineering/`, etc.) and skills (`governance/`, `execution/`, etc.).
- New high-density workflows: `/autoplan`, `/spec`, `/ce-plan`, `/ce-debug`, etc.

### Changed
- Hardened Rule 00 (Constitution) with "Iron Law" and "3-Strike Escalation".
- Hardened Rule 01 (Spec-Before-Code) with "Anti-Rationalization Table".
- Hardened Rule 02 (Planning Memory) with "2-Action Rule".
- Hardened Rule 04 (Progressive Disclosure) with 12k character hard limits and Layer 1→3 routing.
- Hardened Rule 05 (KI Governance) with telegraphic syntax and taxonomy mandates.
- Upgraded Master Router (`AGENTS.md`) to v2026-04.

### Removed
- Legacy flat workflow files (`chain-*.md`, `main-pipeline.md`).
