# Agent Architecture Audit Report

**Repository**: https://github.com/obra/superpowers/tree/main/skills/using-git-worktrees  
**Analysis Date**: May 2, 2026  
**Files Analyzed**: [https://raw.githubusercontent.com/obra/superpowers/main/skills/using-git-worktrees/SKILL.md](https://raw.githubusercontent.com/obra/superpowers/main/skills/using-git-worktrees/SKILL.md)

## 1. Rules (Persistent Behavioral & Security Constraints)

* Rule 1: Mandatory gitignore verification for project-local worktree directories  
  • Source file: https://raw.githubusercontent.com/obra/superpowers/main/skills/using-git-worktrees/SKILL.md  
  • Excerpt: "MUST verify project-local worktree dirs (.worktrees/ or worktrees/) are gitignored using git check-ignore before creation; if not, add to .gitignore and commit."  
  • Implications: Enforces immediate fix of broken state (Jesse's rule) to prevent accidental commits of temporary workspaces into the main repo; blocks any worktree creation until safety is confirmed.

* Rule 2: Never create worktree without ignore verification (project-local)  
  • Source file: https://raw.githubusercontent.com/obra/superpowers/main/skills/using-git-worktrees/SKILL.md  
  • Excerpt: "Never create worktree without verifying ignore (project-local)."  
  • Implications: Hard security guardrail against polluting the repository with untracked worktree paths; applies only to local .worktrees/ or worktrees/ dirs (global ~/.config/superpowers/worktrees/ is exempt).

* Rule 3: Never skip baseline test verification or proceed with failing tests without explicit user permission  
  • Source file: https://raw.githubusercontent.com/obra/superpowers/main/skills/using-git-worktrees/SKILL.md  
  • Excerpt: "Never skip baseline test verification or proceed with failing tests without asking user."  
  • Implications: Guarantees clean starting state for every isolated workspace; prevents downstream task execution on broken codebases.

* Rule 4: Always follow exact directory selection priority (existing dirs > CLAUDE.md > ask user)  
  • Source file: https://raw.githubusercontent.com/obra/superpowers/main/skills/using-git-worktrees/SKILL.md  
  • Excerpt: "Never assume directory location; always follow priority: existing dirs > CLAUDE.md check > ask user."  
  • Implications: Deterministic, non-hallucinated workspace placement; integrates with project context files (CLAUDE.md) for user-preferred isolation strategy.

* Rule 5: Always announce skill activation at start  
  • Source file: https://raw.githubusercontent.com/obra/superpowers/main/skills/using-git-worktrees/SKILL.md  
  • Excerpt: "Always announce: 'I'm using the using-git-worktrees skill to set up an isolated workspace.'"  
  • Implications: Provides transparency and auditability in multi-skill agent conversations; signals transition from design/brainstorming to execution phase.

## 2. Workflows (Sequential, Slash-Invokable Procedures)

* Workflow 1: /using-git-worktrees (invoked by announcement or context trigger)  
  • Source file: https://raw.githubusercontent.com/obra/superpowers/main/skills/using-git-worktrees/SKILL.md  
  • Sequence: 1. Announce activation. 2. Directory Selection Process (priority: .worktrees/ or worktrees/ existing → grep CLAUDE.md → ask user for global vs local). 3. Safety Verification (gitignore check + auto-fix + commit). 4. Project name detection from git toplevel. 5. git worktree add + cd into new branch. 6. Auto-detect & run project setup (npm install, cargo build, etc. from package.json/Cargo.toml). 7. Baseline test run + verification. 8. Report readiness with path/status.  
  • Triggers/Dependencies: Triggered after design approval in brainstorming phase; required before task execution in subagent-driven-development/executing-plans; pairs with finishing-a-development-branch for cleanup.

## 3. Skills (Modular Capabilities & Tools)

* Skill 1: using-git-worktrees  
  • Source file: https://raw.githubusercontent.com/obra/superpowers/main/skills/using-git-worktrees/SKILL.md  
  • Description: Creates isolated Git worktrees (sharing the same repo) for parallel branch work with smart directory selection, mandatory safety checks, auto project setup, and clean baseline test verification.  
  • Inputs/Outputs: Inputs: branch/feature context and project files (e.g. CLAUDE.md, package.json). Outputs: ready isolated workspace path with confirmed clean tests.  
  • Implementation excerpt: "Creates isolated git worktrees for parallel branch work. Smart dir selection, safety checks, project setup, baseline tests."

## 4. Interconnections & Architecture Summary

* How Rules constrain Workflows/Skills: Every step of the using-git-worktrees workflow is gated by the five core Rules (gitignore MUST, Never assumptions, baseline tests, priority selection, announcement); Red Flags/Common Mistakes sections explicitly list violations that halt execution.  
* How Workflows invoke Skills: This workflow is a composable primitive invoked by higher-level skills (brainstorming → using-git-worktrees → writing-plans/subagent-driven-development); serves as mandatory Collaboration skill in the Superpowers agentic coding methodology.  
* Overall agent design insights: Superpowers is a complete agentic software development methodology built from composable SKILL.md modules. Each skill (like this one) encodes mandatory sequential workflows, persistent safety Rules, and reusable capabilities; the using-git-worktrees skill enforces workspace isolation as a foundational precondition for all development tasks, preventing common Git contamination failures in multi-branch agent workflows.  

**End of Report**
