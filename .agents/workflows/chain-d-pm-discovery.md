---
name: chain-d-pm-discovery
description: Product discovery pipeline using Teresa Torres OST framework. Slash command: /chain-d or /discover or /office-hours
---
# Chain D: PM Discovery Pipeline

## Sequence

### D1: Problem Framing (/office-hours)
@apex-pm: YC-style CEO diagnostic.
AskUserQuestion: What is the real problem? Who experiences it? What's been tried? What would success look like?
One question at a time. Single-select choices preferred.
Output: clear framed problem statement (not a solution).

### D2: OST Construction
@apex-pm: invoke opportunity-solution-tree skill.
Define measurable desired outcome (metric + baseline + target).
Map customer opportunities (problems/needs) without constraining to solutions.
Output: OST.md scaffold.

### D3: Assumption Identification
For each opportunity: identify critical assumptions.
Classify by risk: riskiest first for experiment prioritization.

### D4: Assumption Prioritization
Impact vs confidence matrix. Top 3 assumptions → experiment design.

### D5: Experiment Design
One experiment per top assumption.
Define: what evidence would change the decision? What's the minimum viable test?
Output: discovery-plan.md

### D6: OpenSpec Artifacts Gate: STRICT_MODE
@apex-pm → invoke OpenSpec workflow:
/opsx:propose → creates: proposal.md (Why/What/Capabilities) + specs/ + design.md + tasks.md.
Dependency graph enforced: proposal → specs → design → tasks.
GATE: Human approves proposal.md before specs generation.

### D7: Handoff to Engineering
OST.md + OpenSpec artifacts → @apex-planner.
@apex-planner: use OST + proposal as context for SPEC.md generation.
Transition: Chain A begins at step A2 with pre-populated context.

## Success Criteria
Single measurable outcome defined. OST with ≥ 3 solutions per priority opportunity.
OpenSpec artifacts committed. @apex-planner briefed.

## Failure Handling
Ambiguous outcome → AskUserQuestion (one question, single-select). Never assume. Never blend outcomes.
