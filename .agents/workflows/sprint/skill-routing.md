---
name: skill-routing
description: Use at session initialization to parse user intent and dispatch to the correct specialist skill or workflow. Maps request types to roles (strategy→CEO, code→eng, security→CSO, etc.).
---
# /skill-routing — Request-Type Dispatch (Session Init Router)

## Source
Derived from: `workflows References Report.md`, Section 1 — Gstack Architecture Workflows, Workflow 5.
Cross-ref: `Vertical Stack Analysis.md` § 6-Layer Architecture, L1 Input + L3 Capability.
Cross-ref: `agent skills agent audit report.md` Rule 2 (Mandatory skill invocation on intent match).

## Purpose
Core routing logic injected at session initialization (via `UserPromptSubmit` lifecycle hook).
Parses the user request, classifies intent, matches to a specialist role, and invokes the
corresponding skill or workflow. Prevents ad-hoc implementation by enforcing skill-first dispatch.

## Invariant (Rule 04 — Progressive Disclosure)
> If a task matches a skill, MUST invoke it.
> NEVER implement directly if a skill applies.
> Always follow the skill instructions exactly — do not partially apply them.

## Session Init Sequence

### Step 1 — Load Skill Metadata (Layer 1)
```
On UserPromptSubmit:
- Load SKILL.md name + description ONLY for all skills in .agents/skills/
- Do NOT load full payloads yet (token budget constraint — Rule 04)
- Build: intent_vocab = {skill_name: description_trigger_phrase}
```

### Step 2 — Parse User Request
```
Analyze the user request for:
- Action verbs: build, fix, review, ship, plan, discover, scan, test, write, research
- Domain signals: feature, bug, security, deploy, PM, strategy, docs, skill
- Urgency/risk signals: production, critical, urgent, breaking
- Artifact references: SPEC.md, PR, branch, task_plan.md, STRATEGY.md
```

### Step 3 — Intent Classification + Role Dispatch

| Request Pattern | Role | Skill/Workflow Invoked |
|-----------------|------|----------------------|
| "new feature", "build X", "add Y" | Feature Build | `/autoplan` → Chain A |
| "strategic direction", "what should we build", "CEO review" | CEO / Strategy | `ce-strategy` skill |
| "fix bug", "broken", "failing test", "CI failure" | Debug / Eng | `/ce-debug` → Chain C |
| "review this PR", "check my code", "quality gate" | Code Reviewer | `/review` → `ce-correctness-reviewer` |
| "security scan", "threat model", "STRIDE", "OWASP" | Security (CSO) | `/security-threat-modeling-pipeline` → Chain B |
| "product discovery", "user research", "what problem" | PM | `/discover` → `opportunity-solution-tree` → Chain D |
| "write a skill", "new capability", "new SKILL.md" | Skill Architect | `/writing-skills` → Chain E |
| "ship", "release", "deploy", "push to main" | Release | `/ship` (with `/guard`) |
| "plan this", "break this down", "implementation plan" | Eng Planner | `/ce-plan` |
| "spec this", "spec before code", "requirements" | Spec Author | `/spec` |
| "retro", "what did we learn", "extract KI" | KI Curator | `/retro` → `ki-curator` |
| "browser automation", "UI test", "click X", "login to" | Browser Agent | `agent-browser` → `/core-loop` |
| "context rot", "KI audit", "knowledge conflict" | Meta-KI | `/para-knowledge` → `ki-curator` |
| "debug session", "systematic debugging" | Debug Specialist | `/systematic-debugging` |
| "git worktree", "isolated branch", "clean workspace" | Workspace | `/using-git-worktrees` |

### Step 4 — Load Full Skill Payload (Layer 2)
```
On intent match:
- Load full SKILL.md for matched skill (max 3 simultaneously — Rule 04)
- Inject into active context
- Surface to agent: "Matched skill: [name]. Following workflow exactly."
```

### Step 5 — Invoke + Follow Strictly
```
- Execute the matched skill/workflow from Step 1
- DO NOT partially apply — follow all steps in sequence
- DO NOT rationalize skipping steps (anti-rationalization table — Rule 01)
- If no skill matches: surface ambiguity to user before proceeding
```

## Anti-Rationalization Guardrails

| Rationalization | Blocked Response | Correct Action |
|-----------------|-----------------|----------------|
| "This is too small for a skill" | Implement directly | Check skill match first; even small tasks may match |
| "I already know how to do this" | Skip skill | Load + follow skill — institutional knowledge may differ |
| "The skill takes too long" | Abbreviate workflow | Follow completely; time pressure is not an override |
| "No skill matches perfectly" | Force nearest skill | Surface to user: "No exact match — recommend: [option A] or [option B]" |

## Power-Chain Routing Summary

```
User Request
     │
     ▼
Parse Intent (Step 2)
     │
     ▼
Match to Role (Step 3)
     │
     ├─ Feature    → Chain A: /autoplan → /spec → /ce-plan → build → /review → /qa → /ship → /retro
     ├─ Security   → Chain B: /security-threat-modeling-pipeline
     ├─ Debug      → Chain C: /ce-debug → /systematic-debugging → /ce-code-review
     ├─ PM         → Chain D: /discover → opportunity-solution-tree → /opsx:propose
     ├─ Skill Auth → Chain E: /writing-skills (RED→GREEN→REFACT)
     ├─ Browser    → Chain G: agent-browser → /core-loop → /login → /state-persist
     └─ Context    → Chain F: /para-knowledge → /ce-compound
```

## Quality Gates
- [ ] Skill metadata loaded at session init (Layer 1 only — no full payloads preloaded)
- [ ] Intent parsed before any implementation begins
- [ ] Matched skill followed completely — no partial application
- [ ] If no match: user surfaced with explicit options (AskUserQuestion)
- [ ] Max 3 full skill payloads loaded simultaneously (Rule 04)
- [ ] L0 compliance: THINK BEFORE CODING — routing completes before first implementation line
