# Agent Architecture Audit Report

**Repository**: https://github.com/OthmanAdi/planning-with-files  
**Analysis Date**: Saturday, May 02, 2026  
**Files Analyzed**: 

- https://raw.githubusercontent.com/OthmanAdi/planning-with-files/master/README.md
- https://raw.githubusercontent.com/OthmanAdi/planning-with-files/master/AGENTS.md
- https://raw.githubusercontent.com/OthmanAdi/planning-with-files/master/skills/planning-with-files/SKILL.md

## 1. Rules (Persistent Behavioral & Security Constraints)

* Rule 1: Create Plan First  
  • Source file: https://raw.githubusercontent.com/OthmanAdi/planning-with-files/master/skills/planning-with-files/SKILL.md  
  • Excerpt: "Never start a complex task without `task_plan.md`. Non-negotiable."  
  • Implications: Enforces mandatory structured planning for any complex/multi-step task (5+ tool calls) to prevent goal drift and context loss; triggers before any execution.

* Rule 2: The 2-Action Rule  
  • Source file: https://raw.githubusercontent.com/OthmanAdi/planning-with-files/master/skills/planning-with-files/SKILL.md  
  • Excerpt: "After every 2 view/browser/search operations, IMMEDIATELY save key findings to text files."  
  • Implications: Prevents irreversible loss of multimodal/visual data; persistent storage acts as unlimited disk-based working memory.

* Rule 3: Read Before Decide / Update After Act  
  • Source file: https://raw.githubusercontent.com/OthmanAdi/planning-with-files/master/skills/planning-with-files/SKILL.md  
  • Excerpt: "Before major decisions, read the plan file. This keeps goals in your attention window." / "After completing any phase: Mark phase status: `in_progress` → `complete`"  
  • Implications: Maintains alignment with persistent state; hooks enforce re-orientation on every lifecycle event.

* Rule 4: Log ALL Errors & Never Repeat Failures  
  • Source file: https://raw.githubusercontent.com/OthmanAdi/planning-with-files/master/skills/planning-with-files/SKILL.md  
  • Excerpt: "Every error goes in the plan file. ... if action_failed: next_action != same_action"  
  • Implications: Builds cumulative knowledge in `task_plan.md`; explicit mutation of failing strategies.

* Rule 5: 3-Strike Error Protocol  
  • Source file: https://raw.githubusercontent.com/OthmanAdi/planning-with-files/master/skills/planning-with-files/SKILL.md  
  • Excerpt: "ATTEMPT 1: Diagnose & Fix ... ATTEMPT 3: Broader Rethink ... AFTER 3 FAILURES: Escalate to User"  
  • Implications: Structured escalation path; prevents infinite loops and forces user intervention after exhaustion of alternatives.

* Rule 6: Repository Maintenance Constraints (meta-rules for agent contributors)  
  • Source file: https://raw.githubusercontent.com/OthmanAdi/planning-with-files/master/AGENTS.md  
  • Excerpt: "Conventional Commits... One squashed commit per release... All 19 files must be bumped to the same version string every release... No Co-Authored-By trailers."  
  • Implications: Enforces strict versioning, changelog, and contributor tracking across 19 mirrored SKILL.md files and IDE adapters.

## 2. Workflows (Sequential, Slash-Invokable Procedures)

* Workflow 1: Restore Context (mandatory on skill activation / session resume)  
  • Source file: https://raw.githubusercontent.com/OthmanAdi/planning-with-files/master/skills/planning-with-files/SKILL.md  
  • Sequence: 1. Check for `task_plan.md` existence → read `task_plan.md`, `progress.md`, `findings.md`. 2. Execute session-catchup.py (Python script via platform-specific paths). 3. Run `git diff --stat` if unsynced changes detected. 4. Update planning files based on catchup + diff. 5. Proceed only after full re-orientation.  
  • Triggers/Dependencies: UserPromptSubmit hook; automatic on /clear or new session; depends on `${CLAUDE_PLUGIN_ROOT}/scripts/session-catchup.py`.

* Workflow 2: Lifecycle Hook Injection & Update Cycle  
  • Source file: https://raw.githubusercontent.com/OthmanAdi/planning-with-files/master/skills/planning-with-files/SKILL.md  
  • Sequence: UserPromptSubmit → inject plan data header + recent progress; PreToolUse (on Write/Edit/Bash/Read/Glob/Grep) → prepend plan snippet; PostToolUse (on Write/Edit) → remind "Update progress.md..."; Stop → run check-complete script.  
  • Triggers/Dependencies: IDE/agent hook system; matcher-based; enforces persistent memory refresh on every tool interaction.

* Workflow 3: Core Planning Pattern (3-File Persistent Memory)  
  • Source file: https://raw.githubusercontent.com/OthmanAdi/planning-with-files/master/skills/planning-with-files/SKILL.md  
  • Sequence: 1. Create/init `task_plan.md` (phases + status), `findings.md` (discoveries), `progress.md` (logs). 2. Read Before Decide. 3. Act + 2-Action Rule update. 4. Update After Act (status + errors). 5. Continue After Completion (append phases).  
  • Triggers/Dependencies: User-invocable skill activation; templates/ folder reference; project-root placement.

## 3. Skills (Modular Capabilities & Tools)

* Skill 1: planning-with-files (core agentic capability)  
  • Source file: https://raw.githubusercontent.com/OthmanAdi/planning-with-files/master/skills/planning-with-files/SKILL.md  
  • Description: Implements Manus-style persistent markdown "working memory on disk" using exactly 3 files (`task_plan.md`, `findings.md`, `progress.md`) for context engineering, goal tracking, error persistence, and automatic session recovery across tool calls.  
  • Inputs/Outputs: user-invocable: true; allowed-tools: "Read Write Edit Bash Glob Grep"; outputs context-injection strings via hooks; supports 17+ IDEs via mirrored configs.  
  • Implementation excerpt: "hooks: UserPromptSubmit: ... head -50 task_plan.md ... tail -20 progress.md ..."; metadata version 2.36.3; "Context Window = RAM ... Filesystem = Disk".

* Skill 2: Session Recovery & Multi-Plan Isolation (via scripts/hooks)  
  • Source file: https://raw.githubusercontent.com/OthmanAdi/planning-with-files/master/skills/planning-with-files/SKILL.md  
  • Description: Automatic catchup on resume + slug-mode plan directories (`.planning/<slug>/.active_plan` pinning) for parallel/concurrent plans.  
  • Inputs/Outputs: Platform-specific PowerShell/bash execution of check-complete/init scripts; git diff integration.  
  • Implementation excerpt: "if [ -f task_plan.md ]; then echo '[planning-with-files] ACTIVE PLAN...'; ... SKILL_PS1=... powershell.exe ... check-complete.ps1".

## 4. Interconnections & Architecture Summary

* How Rules constrain Workflows/Skills: Critical Rules (Create Plan First, 2-Action, 3-Strike, Log Errors) are embedded directly in SKILL.md and enforced at every hook boundary; AGENTS.md rules further constrain human-maintainer workflows that ship new skill versions across 19 mirrored files.  
* How Workflows invoke Skills: User-invokable skill entry point triggers Restore Context workflow → lifecycle hooks → iterative 3-file update cycle; hooks act as the invocation glue between IDE events and persistent state.  
* Overall agent design insights: This is a portable meta-skill that turns any LLM agent (Claude Code + 17 IDE adapters) into a Manus-like system by externalizing volatile context to disk-based markdown files. Rules and hooks create a self-correcting, recoverable loop that survives /clear, session gaps, and tool-use interruptions; the entire architecture is mirrored across IDE-specific folders for zero-config deployment.

**End of Report**
