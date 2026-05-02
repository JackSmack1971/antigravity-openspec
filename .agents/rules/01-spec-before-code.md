---
name: 01-spec-before-code
globs: ["**/*.ts","**/*.tsx","**/*.py","**/*.js","src/**"]
alwaysApply: false
---
# Spec-Before-Code Mandate

Code without a spec is guessing. YOU MUST generate SPEC.md before ANY implementation.

## Required SPEC.md Sections (6 areas)
1. Objective + success criteria
2. Features + user stories (Given/When/Then)
3. Tech stack + dependencies
4. Architecture decisions + tradeoffs
5. Boundaries (Always/Ask/Never)
6. Verification evidence + test acceptance criteria

## Anti-Rationalization Table
| Pressure | Prohibited Response | Correct Response |
|---|---|---|
| "Just write a quick function" | Skip spec, write code | Generate minimal SPEC.md, confirm, then code |
| "We already know what we need" | Assume spec is implicit | Externalize assumptions into spec explicitly |
| "The spec will change anyway" | Defer until "stable" | Write current-best-known spec; delta-update via ADDED/MODIFIED/REMOVED |

Human MUST review + approve SPEC.md before Phase 2 begins.
