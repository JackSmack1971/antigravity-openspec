---
name: threat-mitigation-mapping
description: Map identified threats to security controls and compute overall mitigation coverage.
version: 1.0.0
triggers: ["mitigate", "controls", "mitigation plan"]
---

# threat-mitigation-mapping

## Purpose
Ensure that every identified threat has an associated control or a documented risk acceptance decision.

## Coverage Scoring
Compute a coverage score between `0.0` and `1.0`.
- **GATE**: If coverage < `0.8`, execution must **HOLD /ship**.
- Generate fix recommendations for missing controls and re-run analysis after implementation.

## Risk Acceptance
For any unmitigated or under-mitigated threat, an explicit **RISK-ACCEPT** decision is required. The user must explicitly approve these decisions.

## Output
`MitigationPlan.md` including:
- Overall Coverage Score.
- Gap Analysis Table (identifying control gaps per threat category).

## Data Model (Python Reference)
```python
class SecurityControl:
    def __init__(self, id, threat_id, control_type, effectiveness):
        self.id = id
        self.threat_id = threat_id
        self.control_type = control_type # Preventive, Detective, Corrective
        self.effectiveness = effectiveness # 0.0 - 1.0

class MitigationPlan:
    def __init__(self, controls=[]):
        self.controls = controls
    
    def compute_coverage(self):
        # returns aggregate score
        pass
```

## Rules
- **Gap Identification**: The gap analysis must list every threat category from the STRIDE phase that lacks 100% effective coverage.
- **Mandatory User Gate**: Coverage < 0.8 blocks release.
