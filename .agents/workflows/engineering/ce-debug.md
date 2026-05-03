---
name: ce-debug
description: 4-phase root-cause debugging. Enforces IRON LAW: NO FIXES WITHOUT ROOT CAUSE. Includes pitfall audit, repro, hypothesis testing, and 3-strike rule.
---
# /ce-debug — Systematic Debugging
1. **MANDATORY**: check .agents/knowledge/pitfalls/ FIRST — is this a known pitfall?
2. **If known pitfall KI exists**: apply resolution protocol from KI; skip to Phase 4
3. **Phase 1 — INVESTIGATE**: reproduce exact error; read full error message; check git log -10
4. **Phase 2 — PATTERN ANALYSIS**: classify error (logic/race/env/dependency/data); find all related sites
5. **Phase 3 — HYPOTHESIS + TEST**: state 1 falsifiable hypothesis; write minimal repro; test hypothesis
6. **Phase 4 — IMPLEMENT + VERIFY**: surgical fix (Rule 07); run `git diff` before/after; run full test suite
7. **3-strike rule**: 3 failed Phase 3 attempts → architectural rethink → escalate to user
8. **If new error type**: extract Pitfall KI candidate → queue for /retro
