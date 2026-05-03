---
name: ce-plan
description: Multi-phase compound engineering planning. Steps 1-9 cover STRATEGY.md check, ce-plan skill load, Phase 0-5 iteration, and task_plan.md update.
---
# /ce-plan — Multi-Phase Planning
1. **Check if STRATEGY.md exists** → read it; if not, trigger /ce-strategy first
2. **Load ce-plan skill** (Layer 2)
3. **Phase 0: RESUME** — read task_plan.md; list remaining tasks
4. **Phase 1: CONTEXT** — read relevant source files; extract existing patterns
5. **Phase 2: QUESTIONS** — surface ambiguities; HALT for user answers
6. **Phase 3: STRUCTURE** — define component map (repo-relative paths only)
7. **Phase 4: WRITE** — generate docs/plans/<name>.md
8. **Phase 5: REVIEW GATE** — present plan; HALT for user approval
9. **Post-approval**: initialize task_plan.md if new plan; update if continuing
