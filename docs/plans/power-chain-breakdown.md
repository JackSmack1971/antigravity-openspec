# Implementation Plan — Power-Chain Uplift Breakdown

This plan details the modifications to the crystallization tracker to support granular uplift tracking across the 7 APEX Power-Chains.

## Proposed Changes

### [Metrics Engine]

#### [MODIFY] [.agents/scripts/crystallization-tracker.py](file:///c:/workspaces/apex-production-pipeline/.agents/scripts/crystallization-tracker.py)
- Update `log_session` to accept `chain` (string).
- Update `get_total_uplift` to return a dictionary of chain stats.
- Update `print_dashboard` to render the breakdown table.
- Use `argparse` for cleaner CLI handling (replacing `sys.argv` indexing).

### [Data Layer]

#### [MODIFY] [.agents/logs/metrics.json](file:///c:/workspaces/apex-production-pipeline/.agents/logs/metrics.json)
- New field `chain` in session objects.
- Handle legacy sessions by defaulting to `U` (Unknown).

## Verification Plan

### Automated Tests
- `python .agents/scripts/crystallization-tracker.py 1 0 --chain A`
- `python .agents/scripts/crystallization-tracker.py --dashboard`

### Acceptance Criteria (AC)
- [ ] Session is saved with `chain: "A"`.
- [ ] Dashboard displays "A" with 100% uplift.
- [ ] Legacy sessions are grouped under "U".
