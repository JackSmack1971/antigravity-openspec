---
name: guard
description: Final confirmation gate before destructive execution. Triggered after `/careful` review or as a pre-merge gate. Triggers on "guard this", "pre-merge gate".
version: 1.0.0
---

# guard — Final Execution Gate

## Purpose
Acts as the final barrier before code is merged or destructive actions are taken, ensuring all safety checks have passed.

## Final Checklist (All MUST pass)
- [ ] **Review**: `/careful` enumeration was presented and understood.
- **Verification**:
  - [ ] SAST gate passed with zero criticals (Rule 03).
  - [ ] Secret Check: `git grep` confirms no API keys or secrets in the diff.
- [ ] **Confirmation**: User typed the explicit confirmation string (e.g., "CONFIRMED").
- [ ] **Safety**: A rollback plan is documented in the `walkthrough.md` or `progress.md`.

## Workflow
If any checklist item is incomplete, the `/guard` skill MUST fail and block the `/ship` or merge process.
