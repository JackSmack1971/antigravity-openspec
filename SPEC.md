# SPEC — Power-Chain Uplift Breakdown

## 1. Problem Statement
The current Autonomy Uplift metric is an aggregate value that hides variations across different Power-Chains. We lack the visibility to identify which specific workflows (Feature Build, Debug, Security, etc.) require the most human intervention.

## 2. User Scenarios
### Scenario A: Logging a Feature Build
- **Given**: An agent completes a Power-Chain A (Feature Build) session.
- **When**: The agent calls `crystallization-tracker.py 5 1 --chain A`.
- **Then**: The session is recorded with the "A" tag.

### Scenario B: Viewing the Dashboard
- **Given**: Multiple sessions from different Power-Chains have been logged.
- **When**: A user runs `crystallization-tracker.py --dashboard`.
- **Then**: The dashboard shows a table with Uplift% broken down by Chain.

## 3. Technical Requirements
- **CLI update**: `crystallization-tracker.py` must support a `--chain` flag.
- **Data Schema**: Update `metrics.json` session object to include a `chain` field (default "UNKNOWN").
- **Dashboard logic**: Aggregate `wins` and `interventions` per `chain` and display in the dashboard.

## 4. Non-Functional Requirements
- **Backward Compatibility**: Existing "UNKNOWN" sessions must not break the dashboard.
- **Performance**: Dashboard calculation must be fast (<100ms).

## 5. Security & Governance
- **Rule 11**: All paths in the script must be absolute (using script-relative resolution).
- **Rule 03**: No PII or secrets logged in metrics.

## 6. Acceptance Criteria (AC)
- [ ] `crystallization-tracker.py` accepts `--chain [A-G]`.
- [ ] `metrics.json` stores the chain tag.
- [ ] `--dashboard` displays a table: `Chain | Sessions | Uplift%`.
