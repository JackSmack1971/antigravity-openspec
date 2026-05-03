# Plan: <Feature Name>

> **Status:** Draft | In Review | Approved**CS:** [N]%**Author:** @<agent-or-user>**Date:** YYYY-MM-DD

* * *

## Overview

<!-- 2–4 sentences. What changes, why, what it unblocks. -->

* * *

## Implementation Units

### IU1: <Short Name>

* **File:** `src/path/to/file.ext` ← repo-relative
* **Change type:** Create | Modify | Delete | Refactor
* **Rationale:** Why this unit exists.
* **DPs:** IU2, IU4 (none if independent)
* **AC:**
  * [ ] <Specific, testable condition 1>
  * [ ] <Specific, testable condition 2>

### IU2: <Short Name>

* **File:** `src/path/to/other.ext`
* **Change type:** Modify
* **Rationale:** ...
* **DPs:** IU1
* **AC:**
  * [ ] <Condition>

<!-- Add IU blocks as needed -->

* * *

## Dependencies

<!-- External DPs: libraries, services, environment flags, team sign-offs -->

| DP  | Type | Owner | Blocking? |
| --- | --- | --- | --- |
| `library@version` | Package | DevOps | Yes |

* * *

## Risks

| Risk | Likelihood | Impact | Mitigation |
| --- | --- | --- | --- |
| <Risk 1> | Medium | High | <Action> |
| <Risk 2> | Low | Medium | <Action> |

* * *

## Test Scenarios

<!-- Behaviour-driven; no implementation code -->

1. **Happy path:** Given X, when Y, then Z.
2. **Edge case:** Given X with boundary condition, when Y, then Z.
3. **Failure path:** Given invalid X, when Y, then error Z is surfaced.

* * *

## Acceptance Criteria

<!-- Plan-level; implementation units carry their own IU-level AC -->

* [ ] All IUs implemented with passing unit tests.
* [ ] No regressions in existing test suite.
* [ ] <Feature-specific observable outcome>.
* [ ] Code reviewed and merged to main.

* * *

## CS: [N]%

<!-- Replace [N] with 0–100. Must be ≥ 70 before handoff. -->

<!-- Gap justification if CS < 70: <what's missing> -->
