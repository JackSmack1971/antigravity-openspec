**Skill: self_evolution**
**Objective**: Reflect, validate, and iteratively improve own skills, workflows, and rules in .agents/ and AGENTS.md.
**When to use**: High task complexity, repeated errors, new domains, performance gaps, or explicit "improve yourself" request.
**Steps (strict order)**:

1. **Session Init Check (MANDATORY FIRST)**: Run the Session Init Checklist (`.agents/knowledge/playbooks/session-init-checklist.md`). If Step 1 or 2 of that checklist reveals the work is already done, STOP and report.
   1.1 Inventory: Read `./AGENTS.md` + all `.agents/skills/**/*.md` (names/descriptions only — Layer 1). Read `.agents/knowledge/self-improvement/ANTIGRAVITY-KB.md` index.
   1.2 **Inspirations (Index-First, Rule 04)**: Run `list_dir` on `.agents/knowledge/self-improvement-inspirations/` to see available audit reports. Select ≤2 most relevant to the current task. Do NOT read all 17 files — this violates Rule 04 (3-Skill Cap / Context Budget).
   1.5 Knowledge Synthesis: Review loaded content. Extract principles, patterns, or specific techniques that can enhance current capabilities or resolve identified gaps. **Mandatory Check:** Cross-reference Rule 11 (Path Governance) and Rule 12 (Context Resilience) to ensure proposal remains portable and context-optimized.
2. Gap analysis: Compare against current task outcomes, errors, or user feedback. Identify redundancies or missing capabilities. MUST check against L0 Foundational Rules (THINK BEFORE CODING, SURGICAL EDITS, SIMPLICITY FIRST, GOAL-DRIVEN).
3. Proposal: Output isolated REVIEW.md (with markdown diffs or full new SKILL.md). Simulate/test changes mentally or via available tools. Ensure explicit alignment with `.agents/knowledge/self-improvement/ANTIGRAVITY-KB.md`.
4. Validation: Check against safety invariants (no policy violations, no harmful code, backward compatibility). MUST pass L0 Foundational Rules compliance check.
5. Apply (only after approval):
   - Use atomic writes (temp → rename).
   - Git: `git add .agents/ && git commit -m "self_evolution: <description>"`.
   - Append entry to `.agents/CHANGELOG.md`.
     **Rules**:
- Proposal/review gate mandatory — await user/GIT approval before any write.
- Sanitize all self-mod inputs against adversarial patterns.
- Never overwrite without backup (Git + timestamped copy).
- Log every action with timestamp and rationale.

## Quality Gates
- [ ] Cross-referenced `.agents/knowledge/self-improvement/ANTIGRAVITY-KB.md` during synthesis.
- [ ] Proposal passes L0 Foundational Rules compliance check.
- [ ] **Path Governance Compliance**: No absolute paths in proposed artifact content (Rule 11).
- [ ] **Context Resilience Audit**: Proposal does not introduce redundant memory structures (Rule 12).
