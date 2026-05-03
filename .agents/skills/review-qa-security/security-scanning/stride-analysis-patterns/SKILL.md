---
name: stride-analysis-patterns
description: Core security analysis pattern using the STRIDE methodology. Use to identify threats in components across Spoofing, Tampering, Repudiation, Information Disclosure, DoS, and Elevation of Privilege categories.
version: 1.0.0
triggers: ["STRIDE", "threat model", "security analysis"]
---

# stride-analysis-patterns

## Purpose
Evaluate a system or feature against all 6 STRIDE categories to identify potential vulnerabilities before implementation.

## Output Structure
Generate a `ThreatModel.md` file with a populated threat matrix:
- **Rows**: Threat Categories (S, T, R, I, D, E)
- **Columns**: System Components

## Data Model (Python Reference)
```python
class Threat:
    def __init__(self, id, category, description, component, impact, likelihood):
        self.id = id
        self.category = category
        self.description = description
        self.component = component
        self.impact = impact # 1-5
        self.likelihood = likelihood # 1-5

class ThreatModel:
    def __init__(self, threats=[]):
        self.threats = threats
    
    def generate_matrix(self):
        # returns markdown table representation
        pass
```

## Rules
- **Category Completeness**: ALL 6 STRIDE categories must be documented. If any category is skipped or partial, the analysis must be marked as **HOLD**.
- **Impact Assessment**: Every identified threat must have a defined impact and likelihood score.
