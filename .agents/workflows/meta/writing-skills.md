---
name: writing-skills
description: TDD skill authoring cycle. Enforces pressure testing, baseline-fail confirmation, and imperative framing with CSO optimization.
---
# /writing-skills — Meta Skill Authoring Cycle
1. **Identify skill gap** (from /retro output or explicit user request).
2. **Write test cases FIRST**: what should the skill do? What should it NOT do? Write pressure tests.
3. **Run baseline**: test current behavior → confirm it FAILS the pressure tests (baseline-fail confirmation).
4. **Write SKILL.md**: follow YAML frontmatter conventions; use imperative "YOU MUST"; bright-line rules.
5. **Token limit**: <500 words; CSO (Claude Search Optimization) in description field.
6. **Persuasion principles**: imperative framing, bright-line rules, 72%+ compliance baseline target.
7. **Test under pressure**: simulate adversarial prompts; verify skill holds.
8. **Iterate until 100% compliance** under all pressure tests.
9. **Register skill in AGENTS.md** SKILL REGISTRY section.
10. **Output**: new SKILL.md in appropriate .agents/skills/ subdirectory.
