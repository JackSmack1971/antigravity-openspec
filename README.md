# APEX — Autonomous Production Engineering eXcellence

> **Version:** 2026-05-path-hardened-v3  
> **Repository:** [JackSmack1971/antigravity-openspec](https://github.com/JackSmack1971/antigravity-openspec)

APEX is a **configuration framework for AI coding agents**. Think of it as a rulebook, playbook, and memory system that tells an AI assistant (like Antigravity/Gemini-class agents) exactly *how* to behave on every task — so it's consistent, safe, and self-improving.

---

## 📖 Table of Contents

1. [What is APEX?](#what-is-apex)
2. [Who is this for?](#who-is-this-for)
3. [How it Works — The Big Picture](#how-it-works--the-big-picture)
4. [Project Structure](#project-structure)
5. [Core Concepts](#core-concepts)
   - [Constitutional Rules](#constitutional-rules)
   - [Power-Chains](#power-chains)
   - [Workflows (Slash Commands)](#workflows-slash-commands)
   - [Skills](#skills)
   - [Personas](#personas)
   - [Knowledge Base (KIs)](#knowledge-base-kis)
   - [The Memory Nucleus](#the-memory-nucleus)
6. [Automation Scripts](#automation-scripts)
7. [Getting Started](#getting-started)
8. [The Self-Improvement Loop](#the-self-improvement-loop)
9. [Security Model](#security-model)
10. [Glossary](#glossary)
11. [Contributing](#contributing)

---

## What is APEX?

Imagine hiring a contractor who forgets everything between jobs, skips planning, never writes tests, and pushes secrets to GitHub by accident. That's an AI agent without a framework.

**APEX fixes that.** It is a set of Markdown files that the AI agent reads at the start of every session. These files define:

- **Rules** — hard constraints the agent can never break (e.g., "never commit API keys")
- **Workflows** — step-by-step procedures for common engineering tasks
- **Skills** — specialist knowledge loaded on demand
- **Knowledge Items (KIs)** — lessons learned from past mistakes, stored so they're never repeated

The agent reads `AGENTS.md` first, which loads everything else automatically.

---

## Who is this for?

| You are... | APEX helps you... |
|---|---|
| A developer using an AI coding assistant | Make the AI consistent and trustworthy |
| A team lead | Enforce coding standards and review gates automatically |
| An AI/automation researcher | Study a self-improving agent governance framework |
| A complete beginner | Understand how production-grade AI agents are structured |

**No prior AI framework experience required.** This README explains every concept from scratch.

---

## How it Works — The Big Picture

```
You type a request
       │
       ▼
  AGENTS.md (Master Router)
       │
       ├── Loads 13 Constitutional Rules (always-on constraints)
       ├── Matches your request to a Power-Chain
       │       └── Triggers the right Workflow sequence
       ├── Loads relevant Skills on demand
       └── Reads the Knowledge Base for past lessons
```

Every session, the agent:
1. Reads `AGENTS.md`
2. Checks `task_plan.md`, `progress.md`, and `findings.md` (the "memory")
3. Runs `session-catchup.py` to re-orient itself
4. Executes the right workflow
5. Logs results to the knowledge base via `/retro`

---

## Project Structure

```
apex-production-pipeline/
│
├── AGENTS.md                        # 🧠 Master router — read this first
├── task_plan.md                     # 📋 Active task phases & goals
├── progress.md                      # 📝 Step-by-step session log
│
├── scripts/
│   └── check-complete.py            # ✅ Validates all tasks done before release
│
└── .agents/
    ├── rules/                       # ⚖️  13 constitutional rules (always enforced)
    │   ├── 00-constitution.md       #    L0 Karpathy Mandates + core invariants
    │   ├── 01-spec-before-code.md   #    Spec MUST exist before any code is written
    │   ├── 02-planning-memory.md    #    3-file memory nucleus + 2-action rule
    │   ├── 03-security-baseline.md  #    STRIDE + SAST + zero destructive ops
    │   ├── 04-progressive-disclosure.md
    │   ├── 05-ki-governance.md      #    Knowledge Item lifecycle rules
    │   ├── 06-terminal-execution.md
    │   ├── 07-visual-verification.md
    │   ├── 08-windows-host-bridge.md
    │   ├── 09-self-improvement-uplift.md  # Uplift% metric + 30-day crystallization
    │   ├── 10-context-budget-governance.md
    │   ├── 11-path-governance.md    #    Repo-relative paths; Windows Trust Anchor
    │   └── 12-context-resilience.md
    │
    ├── workflows/
    │   ├── sprint/                  # 🚀 Feature delivery pipeline
    │   │   ├── autoplan.md          #    Full Chain A: spec → build → ship → retro
    │   │   ├── spec.md              #    6-area specification generator
    │   │   ├── review.md            #    PR review gate
    │   │   ├── ship.md              #    Release workflow
    │   │   └── retro.md             #    Self-improvement loop terminus
    │   ├── engineering/             # 🔧 Technical execution
    │   │   ├── ce-plan.md
    │   │   ├── ce-debug.md          #    Systematic debugging (Iron Law)
    │   │   ├── ce-code-review.md
    │   │   └── ce-compound.md
    │   ├── meta/                    # 🔄 Framework maintenance
    │   │   ├── para-knowledge.md    #    Bi-weekly KI audit
    │   │   ├── writing-skills.md
    │   │   └── restore-context.md
    │   ├── security/
    │   │   └── threat-model-pipeline.md
    │   ├── pm/
    │   │   └── discover.md
    │   └── openspec/
    │       └── opsx-propose.md
    │
    ├── skills/                      # 🛠️  On-demand specialist knowledge
    │   ├── execution/               #    ce-plan, react-best-practices,
    │   │   │                        #    systematic-debugging, using-git-worktrees
    │   ├── governance/              #    metrics-auditor, planning-with-files,
    │   │   │                        #    self_evolution, spec-driven-development,
    │   │   │                        #    writing-skills
    │   ├── meta-ki/                 #    ki-curator (KI versioning)
    │   ├── orchestration/           #    opportunity-solution-tree
    │   └── review-qa-security/      #    agent-browser, security-scanning
    │
    ├── knowledge/                   # 📚 Persistent lessons learned
    │   ├── pitfalls/                #    Anti-patterns (what went wrong)
    │   ├── playbooks/               #    Positive patterns (what worked)
    │   ├── references/              #    External knowledge, deprecated KIs
    │   └── self-improvement/        #    Framework evolution notes
    │
    ├── personas/                    # 🎭 5 agent roles
    │   ├── apex-engineer.md
    │   ├── apex-planner.md
    │   ├── apex-pm.md
    │   ├── apex-reviewer.md
    │   └── apex-security-officer.md
    │
    ├── scripts/                     # 🐍 Python automation utilities
    │   ├── crystallization-tracker.py   # Logs Uplift% metrics
    │   ├── check-complete.py            # Task completion gate
    │   └── session-catchup.py           # Session re-orientation
    │
    └── logs/
        └── metrics.json             # 📊 Historical Uplift% data
```

---

## Core Concepts

### Constitutional Rules

> **Plain English:** These are the laws the AI can never break, no matter what you tell it.

There are 13 rules, always active. The most important are:

**The L0 Karpathy Mandates** (Rule 00 — the highest law):

| Mandate | What it means in practice |
|---|---|
| **Think Before Coding** | Write what you intend in comments *before* writing any code |
| **Surgical Edits** | Only change exactly what the task requires — no bonus refactoring |
| **Simplicity First** | When two solutions exist, always pick the simpler one |
| **Goal-Driven** | Define how you'll know you succeeded *before* you start |

**Other key rules:**

- **Rule 01 — Spec Before Code:** The agent must write a `SPEC.md` file (a 6-section plan) before writing a single line of implementation code. You must approve it first.
- **Rule 02 — Planning Memory:** The agent writes to `progress.md` after every 2 tool operations so it never loses context.
- **Rule 03 — Security Baseline:** No secrets in git. No destructive actions without your explicit confirmation. SAST scans must pass before any release.
- **Rule 09 — Self-Improvement:** The agent tracks an `Uplift%` score. If it falls below 40%, a governance audit is automatically triggered.
- **Rule 11 — Path Governance:** All file paths in plans/docs must be repo-relative (e.g., `./scripts/foo.py`), never absolute (e.g., `C:\Users\...`).

**Conflict Resolution Precedence** (highest wins):
```
Rule 03 (Security) > Rule 00 (Constitution) > Rules 01-12 > Skills > Workflows
```

---

### Power-Chains

> **Plain English:** Pre-wired sequences that fire automatically based on what you ask for.

| Chain | When it fires | What it runs |
|---|---|---|
| **A: Feature Build** | You request a new feature | `/autoplan` → `/spec` → `/ce-plan` → `/ship` |
| **B: Security** | Pre-release check | `/security-threat-modeling-pipeline` |
| **C: Debug** | You report a bug | `/ce-debug` → `/ce-code-review` → `/retro` |
| **D: PM Discovery** | A decision is needed | `/discover` → `/opsx:propose` |
| **E: Skill Authoring** | A capability gap is found | `/writing-skills` (TDD cycle) |
| **F: Context Resilience** | Context window is getting large | `/para-knowledge` → `/ce-compound` |

---

### Workflows (Slash Commands)

> **Plain English:** Type one of these "slash commands" to kick off a defined procedure.

Workflows are Markdown files in `.agents/workflows/`. Each one is a numbered checklist the agent follows step-by-step, in order, without skipping.

| Workflow | Chain | Description |
|---|---|---|
| `/autoplan` | **A** | Full sprint pipeline: spec → build → ship → retro |
| `/ce-plan` | **A** | Multi-phase implementation planning |
| `/ce-debug` | **C** | Systematic 4-phase root-cause debugging |
| `/ce-code-review` | **C** | Multi-persona tiered quality gate |
| `/ce-compound` | **F** | Learning documentation + context reset |
| `/retro` | **A/F** | Self-improvement knowledge extraction |
| `/opsx:propose` | **D** | Core OpenSpec proposal pipeline |
| `/opsx:apply` | **D** | Execute OpenSpec task implementation |
| `/opsx:sync` | **D** | Synchronize OpenSpec artifacts |
| `/opsx:archive` | **D** | Archive completed OpenSpec changes |
| `/security-threat-modeling-pipeline` | **B** | Full STRIDE-to-SAST security pipeline |
| `/discover` | **D** | 7-step PM discovery & OST mapping |

---

### OpenSpec Integration

OpenSpec is the spec-driven governance layer for Antigravity. It uses a structured artifact pipeline to ensure every change is proposed, specified, designed, and tracked deterministically.

- **Config**: `openspec/config.yaml` provides the project context and per-artifact rule injection (e.g., SHALL/MUST for specs).
- **Changes**: Active changes live in `openspec/changes/<change-name>/`.
- **Schema**: `openspec/schemas/spec-driven/schema.yaml` defines the Antigravity-native artifact dependency graph.
- **Commands**: `/opsx:propose` kicks off a new change by injecting project context and rules directly into the AI's generation prompt.

---

### MCP Integration

The APEX framework utilizes the Model Context Protocol (MCP) to extend agent capabilities via specialized servers.

- **Registry**: `.agents/mcp_config.json` serves as the canonical server registry.
- **Credentials**: All sensitive credentials (tokens, API keys) use `${ENV_VAR}` substitution to prevent accidental commitment of secrets.
- **Security**: Model Armor is enabled for all remote HTTP/SSE servers to enforce read-only access and safety constraints.

---

### Session Persistence

The APEX framework implements high-fidelity session persistence via the "Planning-with-Files" methodology.

- **Nucleus**: `task_plan.md` (phases and goals), `findings.md` (research results), and `progress.md` (runtime logs) form the persistent working memory.
- **Rule 02**: Mandates the use of these files to survive context window loss.
- **Governance**: Managed by the `planning-with-files` skill to ensure the agent always has a canonical source of truth for the current task state.

**The most important workflow — `/autoplan`** (Chain A, full feature delivery):

```
Step 1: /office-hours  → Strategic problem framing
Step 2: YOU APPROVE    → Approve feature proposal
Step 3: /spec          → Generate 6-area SPEC.md
Step 4: YOU APPROVE    → Human reviews and approves the spec
Step 5: /ce-plan       → Detailed implementation plan (docs/plans/)
Step 6: /build         → Git worktree isolation (auto-triggered)
Step 7: /ship          → Tests + SAST + /guard → Release
Step 8: /retro         → Knowledge extraction (MANDATORY)
```

**The `/retro` workflow** (self-improvement terminus):

After every ship, the agent:
1. Compares the original plan vs. what actually happened
2. Classifies discoveries as Pitfalls, Playbooks, or References
3. Writes new **Knowledge Items** (KIs) to `.agents/knowledge/`
4. Calculates the session's `Uplift%` score

> ⚠️ Missing `/retro` = incomplete workflow. The system flags and blocks the stop hook.

**The `/ce-debug` workflow** (the Iron Law):

```
Rule: NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST.

Phase 1: Check .agents/knowledge/pitfalls/ for known issues
         Reproduce the bug exactly
         Document root cause in findings.md BEFORE touching code

Phase 2: Find a working baseline; compare what changed

Phase 3: Write ONE test BEFORE implementing the fix

Phase 4: Apply fix at root cause (not the symptom)
         After 3 failed attempts → STOP → escalate to user
```

---

### Skills

> **Plain English:** Specialist knowledge modules loaded on demand — like hiring a subject-matter expert only when you need them.

Skills live in `.agents/skills/`. Each has a `SKILL.md` file.

**Rule:** Never load more than 3 full skill payloads at once (prevents context overload).

**Available skills:**

| Skill | Category | What it does |
|---|---|---|
| `metrics-auditor` | Governance | Reads `crystallization-tracker.py`, reports `Uplift%` |
| `ki-curator` | Meta-KI | SemVer-bumps Knowledge Items when they're updated |
| `writing-skills` | Governance | TDD cycle for creating new SKILL.md files |
| `systematic-debugging` | Execution | Structured bug investigation protocol |
| `ce-plan` | Execution | Multi-phase implementation planning |
| `react-best-practices` | Execution | React/Next.js critical rules |
| `using-git-worktrees` | Execution | Workspace isolation before file writes |
| `security-scanning` | Review/QA | STRIDE + SAST pipeline integration |
| `agent-browser` | Review/QA | Headless Chromium CDP core loop |
| `ce-correctness-reviewer` | Review/QA | JSON-structured 3-persona logic review |
| `ce-strategy` | Orchestration | STRATEGY.md grounding anchor |
| `opportunity-solution-tree` | Orchestration | Teresa Torres OST framework |
| `browse` | GStack | Persistent browser session daemon |
| `office-hours` | GStack | YC-style strategic CEO diagnostic |
| `codex` | GStack | Multi-AI verification for high-stakes decisions |
| `careful` | GStack | Destructive operation review wrapper |
| `guard` | GStack | Final execution gate + safety checklist |
| `freeze` | GStack | Emergency circuit breaker / halt |

---

### Personas

> **Plain English:** Different "hats" the agent wears for different phases of work.

| Persona | When active | Core philosophy |
|---|---|---|
| `apex-engineer` | After SPEC.md is approved | 80% planning, 20% execution |
| `apex-planner` | During `/ce-plan` | Decisions-not-code in plans |
| `apex-pm` | During `/discover` | Torres OST framework |
| `apex-reviewer` | During `/ce-code-review` | 3-persona quality gate |
| `apex-security-officer` | During `/ship` | Zero trust, STRIDE coverage |

---

### Knowledge Base (KIs)

> **Plain English:** A library of lessons learned that the agent reads before every task, so it never makes the same mistake twice.

Knowledge Items (KIs) live in `.agents/knowledge/` and come in four types:

| Type | Location | Purpose |
|---|---|---|
| **Pitfall** | `pitfalls/` | Anti-patterns — what went wrong and how to avoid it |
| **Playbook** | `playbooks/` | Positive patterns — what worked and should be repeated |
| **Reference** | `references/` | External knowledge, deprecated KIs |
| **Context** | `self-improvement/` | Multi-session state, domain knowledge |

Every KI has a **SemVer version** (`1.0.0`) in its YAML frontmatter. The `ki-curator` skill bumps this version whenever a KI is updated:

```yaml
---
name: my-knowledge-item
version: 1.2.0   # ← bumped from 1.1.0 after structural update
---
```

**The `/para-knowledge` audit** runs every 14 days to detect conflicting KIs and merge them before "context rot" degrades the agent's performance.

---

### The Memory Nucleus

> **Plain English:** Three files that act as the agent's short-term and long-term memory across sessions.

```
task_plan.md   → What the agent is working on (phases, goals, status)
findings.md    → Surprising discoveries and constraints found mid-task
progress.md    → Step-by-step log of what was done, errors hit, next actions
```

**The 2-Action Rule:** After every 2 tool operations, the agent writes its current status to `progress.md`. No exceptions. This means even if a session crashes or times out, the next session can pick up exactly where it left off.

**Session resume protocol:**
```bash
# What the agent does at the start of every session:
python .agents/scripts/session-catchup.py

# Output example:
# [FOUND] task_plan.md
# [FOUND] progress.md
# [MISSING] findings.md
# [RESUME] 2 in-progress, 3 pending tasks found.
# [ACTION] Read task_plan.md and resume from the first [/] item.
```

---

## Automation Scripts

Three Python scripts power the framework's automation. All use **script-relative absolute paths** internally (Rule 11.5) to prevent `CWD`-dependent failures on Windows.

### `crystallization-tracker.py`

Tracks the **Autonomy Uplift%** metric — how often the agent completes tasks without needing a human correction.

```bash
# View the full dashboard
python .agents/scripts/crystallization-tracker.py --dashboard

# Log a session (e.g., 8 wins, 2 interventions)
python .agents/scripts/crystallization-tracker.py 8 2

# Quick aggregate check
python .agents/scripts/crystallization-tracker.py
```

**Sample dashboard output:**
```
==================================================
  AUTONOMY UPLIFT DASHBOARD (Rule 09.6)
==================================================
  Aggregate Uplift%:      78.50%
  Total Wins:             314
  Total Interventions:    86
  Total Sessions:         42

  30-Day Window Uplift%:  82.10%
  30-Day Sessions:        18
  [OK]   Uplift% is within acceptable range.
==================================================
```

**What "Uplift%" means:**
```
Uplift% = (Tasks completed without human correction / Total tasks) × 100

Target: ≥ 60% within 4 weeks of deployment
Alert:  < 40% → triggers automatic /para-knowledge governance audit
```

---

### `check-complete.py`

A gate that runs before every `/retro`. It reads `task_plan.md` and counts unchecked items (`- [ ]`). If any remain, it blocks the retro and prints a warning.

```bash
python .agents/scripts/check-complete.py

# Possible outputs:
# [SUCCESS] All tasks completed. Proceeding to /retro.
# [WARNING] 3 tasks remain incomplete in task_plan.md.
# [FAIL] Mandatory /retro loop blocked by incomplete tasks.
```

---

### `session-catchup.py`

Runs at the start of every session to re-orient the agent. Reads the memory nucleus files and reports the current state.

```bash
python .agents/scripts/session-catchup.py
```

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- An AI coding assistant that supports `AGENTS.md` (e.g., Antigravity, Cursor, GitHub Copilot Workspace)

### Step 1: Clone the repository

```bash
git clone https://github.com/JackSmack1971/antigravity-openspec.git
cd antigravity-openspec
```

### Step 2: Point your AI assistant at `AGENTS.md`

Your AI assistant should automatically detect and load `AGENTS.md` from the repository root. If it doesn't, configure it to load this file at session start.

### Step 3: Run the session catchup script

```bash
python .agents/scripts/session-catchup.py
```

This confirms the memory nucleus is present and shows any in-progress work.

### Step 4: Start a task using a slash command

For a new feature, type:
```
/autoplan
```

For a bug, type:
```
/ce-debug
```

For a security check before release, type:
```
/security-threat-modeling-pipeline
```

### Step 5: Follow the workflow

The agent will guide you step by step. Your only required actions are:
- **Approving SPEC.md** before implementation starts (Rule 01)
- **Confirming destructive operations** like `git push --force` or `schema-drop` (Rule 03)

---

## The Self-Improvement Loop

This is the most important concept in APEX. The framework is designed to **get better over time** through a feedback loop:

```
Task Completed
      │
      ▼
  /retro triggered (mandatory)
      │
      ├── Compare plan vs. actual
      ├── Classify discoveries (Pitfall / Playbook / Reference)
      ├── Write new KI artifacts to .agents/knowledge/
      ├── Calculate session Uplift%
      └── Log to metrics.json
            │
            ▼
      Next session reads the new KIs
      and avoids the same mistakes
```

**The 30-Day Crystallization Period:**

APEX v2026-05 is in a crystallization period ending **2026-06-01**. During this window:
- Every repeated manual intervention (same issue, twice in 7 days) **must** become a new Pitfall KI
- The `/para-knowledge` audit runs every 14 days
- The target is ≥60% Uplift% by end of period

---

## Security Model

APEX enforces a layered security model with zero exceptions:

### Never committed to git
- `.env` files
- API keys and secrets
- Auth tokens and private keys (`.pem`, `.key`)
- Git worktree directories (`.worktrees/`)

### Requires explicit user confirmation before execution
- `git push --force`
- Database schema drops
- Environment variable mutation
- Any delete operation

### Required before every `/ship`
- All unit tests passing
- All integration tests passing
- SAST scan green (Semgrep / SonarQube / CodeQL)

### STRIDE threat model applied to all features touching:
- Authentication/authorization
- Data storage or transmission
- Infrastructure configuration

> **STRIDE** stands for: **S**poofing, **T**ampering, **R**epudiation, **I**nformation Disclosure, **D**enial of Service, **E**levation of Privilege.

---

## Glossary

| Term | Definition |
|---|---|
| **APEX** | Autonomous Production Engineering eXcellence — this framework |
| **Agent** | An AI coding assistant operating under APEX rules |
| **Constitutional Rule** | An always-on constraint the agent can never override |
| **KI (Knowledge Item)** | A lesson learned, stored as a Markdown file in `.agents/knowledge/` |
| **Power-Chain** | A pre-wired trigger → rules → workflow sequence |
| **Uplift%** | Percentage of tasks completed without human correction |
| **Crystallization** | The process of turning repeated mistakes into permanent KIs |
| **Retro** | The mandatory self-improvement step after every completed workflow |
| **SAST** | Static Application Security Testing — automated code security scanning |
| **STRIDE** | Threat modeling framework covering 6 attack categories |
| **SemVer** | Semantic Versioning (MAJOR.MINOR.PATCH) — used on all KI files |
| **3-File Nucleus** | task_plan.md + findings.md + progress.md — the agent's memory |
| **2-Action Rule** | Write to progress.md after every 2 tool operations |
| **3-Strike Protocol** | After 3 failed fix attempts, STOP and escalate to the user |
| **Trust Anchor** | Absolute path used internally for Windows tool calls (Rule 11.5) |
| **Context Rot** | Degraded agent performance caused by conflicting or stale KIs |

---

## Contributing

Contributions to APEX follow the same framework it enforces:

1. **Fork** the repository and create a feature branch
2. Run `/spec` — write a `SPEC.md` for your change before touching any files
3. Get the spec approved (open an issue or PR for discussion)
4. Implement with surgical edits only (no opportunistic refactoring)
5. Ensure all security rules are followed — no secrets, no absolute paths in docs
6. Run `/ship` — tests must pass, SAST must be green
7. Run `/retro` — extract any new KIs from what you learned

**Adding a new rule:** Rules are numbered sequentially. Open an issue proposing the rule text. It must not contradict Rule 03 (Security Baseline) or Rule 00 (Constitution).

**Adding a new skill:** Use the `/writing-skills` TDD workflow. The skill must pass a pressure-test at 100% L0 compliance before being merged.

**Adding a new KI:** Follow the `pitfall_extraction.md` template in `.agents/knowledge/playbooks/`. Quality gate: Actionable + Unique + Telegraphic (dense, imperative, no narrative prose).

---

<p align="center">
  <strong>APEX v2026-05</strong> · Built with the Antigravity Framework · 30-Day Crystallization Period ends 2026-06-01
</p>
