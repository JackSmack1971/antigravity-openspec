---
name: ce-compound
description: Learning documentation and loop reset. Triggers /retro, extracts KIs, updates crystallization dashboard, and resets task_plan.md.
---
# /ce-compound — Learning Documentation & Loop Reset
1. **Run /retro workflow (full)** → capture all KI candidates
2. **Extract**: all architectural decisions from this session → Architecture KI
3. **Extract**: all new patterns discovered → Pattern KI
4. **Run `python .agents/scripts/crystallization-tracker.py --dashboard`**
5. **Update STRATEGY.md** if any strategic pivots occurred
6. **Reset task_plan.md** for next compound cycle (archive current to docs/archive/)
7. **Update AGENTS.md version timestamp** if any framework changes were made
8. **Log**: "Compound cycle complete. Context reset. Uplift%: [X]%"
9. **Output**: compound-learning-summary.md to .agents/artifacts/
