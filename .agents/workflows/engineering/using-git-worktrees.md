---
name: using-git-worktrees
description: Auto-triggered post design-approval to guarantee a clean, isolated workspace using git worktrees. Slash command: /using-git-worktrees
---
# /using-git-worktrees — Clean Workspace Guarantee

## Purpose
Triggered automatically after the design approval phase to guarantee a clean, isolated workspace before execution begins. Prevents polluting the main development branch.

## Deterministic Procedure

1. **Announce Activation:** explicitly state that the `/using-git-worktrees` workflow has been triggered.
2. **Directory Selection Process:** Determine the appropriate directory path for the new worktree (e.g., `../<project-name>-<branch-name>`).
3. **Safety Verification:**
   - Check `.gitignore` for proper exclusion of worktree directories if they are placed inside the repo (though sibling directories are preferred).
   - Auto-fix the `.gitignore` if necessary.
   - Commit any `.gitignore` fixes.
4. **Project Name Detection & Git Safety:**
   - Query git repository root (`git rev-parse --show-toplevel`).
   - If `git rev-parse` fails (not a repo), execute `git init`, create a skeleton `.gitignore`, and make an initial commit.
5. **Create Worktree:** Execute `git worktree add -b <new-branch> <path>` and navigate into the new branch directory.
6. **Auto-Detect & Run Project Setup:** Detect dependency managers (e.g., `npm install`, `pip install -r requirements.txt`) and run them to bootstrap the new workspace.
7. **Baseline Test Run & Verification:** Execute the existing test suite to ensure the fresh worktree is fully functional before changes begin.
8. **Report Readiness:** Output the final readiness state, including the exact path of the new worktree, current status, and branch name.

## Success Criteria
- An isolated workspace is active.
- Dependencies are installed.
- Tests pass on the baseline branch.
- Readiness is reported to the user.
