---
name: using-git-worktrees
description: Use when starting any implementation after design approval, creating isolated experiments, or executing parallel branches. Required before any file writes to main working directory. Triggers: after spec/brainstorm approval, "start building", "create branch", "isolated workspace needed".
version: 1.0.0
user-invokable: true
allowed-tools: Read, Write, Bash
---
# using-git-worktrees

## Announcement (MANDATORY — always say this first)
"I'm using the using-git-worktrees skill to set up an isolated workspace."

## Workflow (execute in exact order — no steps skippable)

### Step 1: Directory Selection (priority order — NEVER assume)
1. Check: does .worktrees/ or worktrees/ already exist?
2. Check: grep CLAUDE.md for preferred worktree location.
3. If neither: AskUserQuestion — global (~/.config/worktrees/) vs local (.worktrees/)?

### Step 2: Safety Verification (MUST complete before creating worktree)
1. Run gitignore-check.sh:
   ```bash
   bash scripts/gitignore-check.sh
   ```
2. Verify with git check-ignore:
   ```bash
   git check-ignore .worktrees/ worktrees/
   ```
If NOT ignored → add to .gitignore → commit before ANY worktree creation.
NEVER skip this step. Unsuppressed worktrees corrupt repo history.

### Step 3: Create Worktree
```bash
git worktree add .worktrees/<feature-name> -b feature/<feature-name>
cd .worktrees/<feature-name>
```

### Step 4: Project Setup (auto-detect)
Check for: package.json → npm install | Cargo.toml → cargo build | requirements.txt → pip install -r.

### Step 5: Baseline Tests
Run full test suite. Report results.
NEVER proceed with failing tests without explicit user permission.

### Step 6: Report Readiness
"Workspace ready at .worktrees/<name>. Branch: feature/<name>. Tests: [PASS/FAIL N]."

## Hard Rules
- NEVER create worktree before gitignore verification (project-local dirs).
- NEVER skip baseline test verification.
- NEVER assume directory without priority-order check.
- **Worktree Cleanup**: Run `git worktree remove` after merging the feature branch.
- **Rule 11 Compliance**: All paths within the worktree must be repo-relative.

## Quality Gates
- [ ] .worktrees/ (or worktrees/) is gitignored and committed
- [ ] Baseline tests pass (or user explicitly confirmed failing baseline acceptable)
- [ ] Adheres to L0 Foundational Rules (SURGICAL EDITS)
