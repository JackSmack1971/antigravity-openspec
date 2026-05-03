---
name: careful
description: Mandatory review wrapper for all destructive operations. Enforces explicit user confirmation before deletion or data loss. Triggers on "delete", "drop", "remove", "overwrite", "push --force".
version: 1.0.0
---

# careful — Destructive Op Review Wrapper

## Purpose
Prevents accidental data loss or irreversible changes by forcing a structured review of every destructive action.

## Protocol
1. **Enumeration**: List exactly which files, records, or configurations will be changed or deleted.
2. **Impact Assessment**: State the consequence of this deletion (e.g., "This will permanently remove all user session data").
3. **Presentation**: Display the enumeration and impact to the user via a clear prompt.
4. **Halt**: Do NOT proceed with the command. Wait for explicit confirmation.

## Enforcement
- Blocks `/ship`, `/guard`, and any destructive bash commands until the user provides explicit confirmation.
- Adheres to **User Sovereignty** (Rule 00): NEVER act unilaterally on destructive operations.
