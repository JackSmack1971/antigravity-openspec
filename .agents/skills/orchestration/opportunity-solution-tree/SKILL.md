---
name: opportunity-solution-tree
description: Use when doing product discovery, evaluating feature ideas, making prioritization decisions, or when a stakeholder describes a problem without a clear solution. Triggers: "what should we build", "product decision", "opportunity mapping", "Teresa Torres OST", "discover user needs", "feature prioritization".
version: 1.0.0
user-invokable: true
allowed-tools: Read, Write
---
# opportunity-solution-tree — Teresa Torres Framework

## Core Principles (enforce always)
- One outcome at a time: never mix multiple desired outcomes in a single OST.
- Opportunities, not features: map customer problems/needs, not solutions.
- Compare and contrast: ALWAYS ≥ 3 solutions per opportunity before converging.
- Discovery is non-linear: iterate OST as evidence arrives; never freeze prematurely.

## 6-Step OST Process

1. Define Outcome — single measurable desired outcome (metric + baseline + target).
2. Map Opportunities — brainstorm customer needs/pain points. NO solutions yet.
3. Prioritize Opportunities — impact vs evidence quality vs strategic alignment matrix.
4. Generate Solutions — minimum 3 per priority opportunity. Include wild/unconventional options.
5. Design Experiments — map riskiest assumption per solution → test design (Given/When/Then) → evidence threshold.
6. Select & Feed — choose the top experiment to feed into the `/opsx:propose` workflow.
7. Archive Tree — save the resulting OST to `.agents/knowledge/context/<slug>-ost.md`.
8. Visualize Tree — markdown hierarchy: Outcome → Opportunities → Solutions → Experiments.

## OST Template
```markdown
## Outcome: [measurable metric — baseline X → target Y]

### Opportunity 1: [customer pain or need]
- Solution A: ... | Riskiest assumption: ... | Experiment: ... | Evidence needed: ...
- Solution B: ... | Riskiest assumption: ... | Experiment: ... | Evidence needed: ...
- Solution C: ... | Riskiest assumption: ... | Experiment: ... | Evidence needed: ...
```

## Anti-Patterns (prohibited)
- Jumping to solutions before mapping opportunities.
- Single solution per opportunity (minimum 3 required).
- Mixing multiple desired outcomes in one OST.
- Freezing OST before experiments are run.

## Quality Gates
- [ ] Single measurable outcome with metric defined
- [ ] ≥ 3 solutions documented per prioritized opportunity with Given/When/Then experiments
- [ ] Top experiment fed into `/opsx:propose`
- [ ] Final OST archived to `.agents/knowledge/context/`
- [ ] Process adheres to L0 Foundational Rules (GOAL-DRIVEN)
