---
name: 01-spec-before-code
description: Spec-Before-Code Mandate — enforced on all implementation file globs
alwaysApply: false
globs: ["**/*.ts","**/*.tsx","**/*.py","**/*.js","**/*.go","src/**","app/**","lib/**"]
---
# Spec-Before-Code Mandate

Code without a spec is guessing. YOU MUST generate SPEC.md before ANY implementation.

## Required SPEC.md Sections (6 Areas — all mandatory)
1. Objective + measurable success criteria
2. Features + user stories (Given/When/Then format)
3. Tech stack + explicit dependency versions
4. Architecture decisions + tradeoffs considered
5. Boundaries: Always / Ask-First / Never
6. Verification evidence + test acceptance criteria

## Anti-Rationalization Table
| Pressure | Prohibited Response | Correct Response |
|---|---|---|
| "Just write a quick function" | Skip spec, write code | Generate minimal SPEC.md, confirm, then code |
| "We already know what we need" | Assume spec is implicit | Externalize all assumptions explicitly |
| "The spec will change anyway" | Defer until stable | Write current-best-known; delta via ADDED/MODIFIED/REMOVED |
| "This is urgent" | Skip gates under pressure | Compress spec to minimum viable; STILL gate |
| "This is too small for a spec" | Skip for small tasks | Small ≠ no spec. Write minimal acceptance criteria |

Human MUST review + approve SPEC.md before Phase 2 begins. No exceptions.
Delta commits: prefix with ADDED / MODIFIED / REMOVED.
