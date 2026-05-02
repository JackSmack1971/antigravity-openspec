# Rule 09 — Self-Improvement & Autonomy Uplift

*Activation Mode: Always On*

## 1. 30-Day Crystallization Period
- This framework version (v2026-05) is subject to a 30-day crystallization period ending on 2026-06-01.
- During this period, the agent must prioritize identifying and formalizing "Pitfall" KIs to prevent repeated manual interventions.

## 2. Autonomy Uplift Metric
- The success of the framework is measured by **Uplift%**.
- **Formula**: `Uplift% = ((Total Task Cycles - Manual Interventions) / Total Task Cycles) * 100`
- **Target**: Achieve 60% Uplift within the first 4 weeks.
- **Pitfall Mandate**: The agent MUST formalize a new "Pitfall" KI whenever a manual intervention is required for the same underlying issue twice in a 7-day period. This is the primary driver for "Crystallization".

## 3. Mandatory Tracking
- Every `/retro` execution must calculate and log the current session's `manual_interventions` and `autonomous_wins`.
- If `Uplift%` drops below 40%, the agent must trigger a "Governance Audit" via the `/para-knowledge` workflow.

## 4. Pre-emptive Pitfall Analysis
- **Rule:** Before any "Fix" implementation, the agent MUST check `.agents/knowledge/pitfalls/` for existing blockers.
- **Extraction Gate:** Any manual intervention that resolves a recurring blocker (2+ hits) MUST be drafted as a new Pitfall KI during the `/retro` phase.

## 5. Skill Promotion Gate
- A skill can only be promoted to "Always-Equip" status if it maintains 100% compliance with L0 Foundational Rules under pressure-test conditions.
- Failure to comply triggers a "3-Strike Escalation" as defined in `02-planning-memory.md`.

## 6. Autonomy Uplift Dashboard
- **Rule:** EVERY `walkthrough.md` artifact MUST contain an "Autonomy Uplift Dashboard" section before the conclusion.
- **Dashboard Schema:**
    - `Session Uplift%`: Calculation based on total actions vs. manual overrides.
    - `Pitfalls Identified`: List of new Pitfall KIs or candidates extracted.
    - `Manual Interventions Avoided`: Count of times a Pitfall KI successfully prevented a failure.
- **Verification:** The `/retro` workflow must enforce the presence of this dashboard.
