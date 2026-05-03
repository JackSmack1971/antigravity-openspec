# GOLDEN PAIR — ce-plan Few-Shot Example

# Load this file only when IU structure or AC quality is uncertain.

* * *

## EXAMPLE: Add Rate-Limiting to Auth API

### Overview

Add per-user rate limiting (60 req/min) to the `/auth/token` endpoint. Prevents brute-force attacks. Unblocks SOC-2 compliance review.

### Implementation Units

#### IU1: Rate-Limit Middleware

* **File:** `src/middleware/rate-limit.ts`
* **Change type:** Create
* **Rationale:** Isolates rate-limiting logic from route handlers; testable in isolation.
* **DPs:** none
* **AC:**
  * [ ] Returns HTTP 429 with `Retry-After` header when limit exceeded.
  * [ ] Limit resets after 60-second sliding window.
  * [ ] Unit tests cover: under-limit, at-limit, over-limit, and window-reset cases.

#### IU2: Attach Middleware to Auth Router

* **File:** `src/routes/auth.ts`
* **Change type:** Modify
* **Rationale:** Apply rate-limit middleware only to `/auth/token`; preserve unrestricted access to `/auth/refresh`.
* **DPs:** IU1
* **AC:**
  * [ ] `/auth/token` rejects 61st request within window.
  * [ ] `/auth/refresh` unaffected by rate-limit middleware.
  * [ ] Integration test confirms middleware ordering.

#### IU3: Redis Store for Rate-Limit State

* **File:** `src/lib/redis-client.ts`
* **Change type:** Modify
* **Rationale:** In-memory stores fail under horizontal scaling; Redis ensures shared state across pods.
* **DPs:** IU1
* **AC:**
  * [ ] Redis TTL matches sliding window (60s).
  * [ ] Graceful fallback to in-memory store if Redis unreachable (logs warning).
  * [ ] E2E test confirms state persistence across two separate server instances.

### Dependencies

| DP  | Type | Owner | Blocking? |
| --- | --- | --- | --- |
| `express-rate-limit@7` | Package | FE team | Yes |
| Redis 7.2 instance in staging | Infrastructure | DevOps | Yes |

### Risks

| Risk | Likelihood | Impact | Mitigation |
| --- | --- | --- | --- |
| Redis unavailable in prod | Low | High | In-memory fallback + PagerDuty alert |
| Sliding window too aggressive | Medium | Medium | Feature-flag the limit value; tune post-deploy |

### Test Scenarios

1. **Happy path:** User sends 60 requests in 60s → all succeed.
2. **Edge case:** 61st request at t=59s → 429 + `Retry-After: 1`.
3. **Failure path:** Redis unavailable → fallback to in-memory; warning logged; requests still processed.

### Acceptance Criteria

* [ ] All three IUs implemented with passing unit + integration tests.
* [ ] No regressions in existing auth test suite.
* [ ] 429 response format matches API error contract (`{ error, retryAfter }`).
* [ ] Reviewed and merged.

### CS: 92%

Gap: Redis provisioning in CI is DevOps dependency (not blocking plan quality).
