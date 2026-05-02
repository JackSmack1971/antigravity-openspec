---
name: main-pipeline
description: Master orchestrator. Use to start any sprint, feature, or when the full APEX pipeline is needed. Routes to appropriate Power-Chain based on intent. Slash command: /autoplan
---
# APEX Main Pipeline — /autoplan

## Entry: `@workspace /autoplan "<task description>"`

## Step 1: Session Initialization
@apex-planner: Invoke /restore-context workflow.
Load task_plan.md + findings.md + progress.md. Announce current state.

## Step 2: Intent Classification (Semantic Router)
Classify user intent into Power-Chain:
| Intent | Chain | Workflow |
|---|---|---|
| New feature / build | A | /chain-a |
| Security hardening | B | /chain-b |
| Bug / test failure | C | /chain-c |
| Product decision / discovery | D | /chain-d |
| New skill pattern identified | E | /chain-e |

Gate: STRICT_MODE — user confirms classification before execution.

## Step 3: Chain Execution
Dispatch to classified sub-workflow. Each chain is self-contained with own gates.

## Step 4: Cross-Chain Quality Gate Gate: STRICT_MODE
After any chain completes a build:
- /ce-code-review: 3-persona parallel (CORRECTNESS + SECURITY + MAINTAINABILITY)
- /qa: agent-browser skill real-browser testing of staging URL
- @apex-security-officer: /chain-b pre-ship pass

## Step 5: Ship Gate Gate: STRICT_MODE
All conditions required:
- /ce-code-review: all 3 personas PASS, confidence ≥ 85, zero slop
- SAST CI/CD gate: green in pipeline
- STRIDE coverage: all 6 categories documented
- SPEC.md acceptance criteria: all verified with evidence (tests/screenshots/outputs)
- progress.md: all phases marked complete

## Step 6: Retro (Constitutional Invariant — no exceptions)
/retro → KNOWLEDGE SUBAGENT extraction → KI quality gate → write to .agents/knowledge/.
Report: "KI extracted: [title] | Type: [type] | Domain: [X] | Trace: [6-char]"

## Success Criteria
SPEC.md approved. All tests passing. /ce-code-review all PASS. /retro KI produced.

## Failure Handling
Gate failure → @apex-planner updates task_plan.md with failure log.
3-strike → HALT. User notified with: root cause + all attempts + recommendation.
