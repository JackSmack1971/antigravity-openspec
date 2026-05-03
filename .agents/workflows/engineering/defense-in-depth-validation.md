---
name: defense-in-depth-validation
description: Triggered immediately post-tracing to layer safety checks.
---
# Defense-in-Depth Validation

## Purpose
Triggered immediately post-tracing, this workflow ensures that fixes are not fragile by layering multiple safety checks, catching errors as early as possible.

## 4-Layer Validation Implementation
When applying a fix, you must implement the following 4-layer validation strategy:
1. **Entry Guards:** Validate the shape, type, and existence of incoming data at the boundaries (e.g., API boundaries, function inputs).
2. **Business Logic Checks:** Ensure the core business logic enforces state transitions correctly and rejects invalid intermediate states.
3. **Environment Guards:** Verify that necessary external dependencies or environment variables are present and healthy before execution.
4. **Debug Instrumentation:** Leave trace logs or assertions in place (compiled out in production if necessary) to catch regressions immediately in development/testing.
