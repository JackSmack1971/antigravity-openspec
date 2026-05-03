---
name: security-requirement-extraction
description: Map identified threats to actionable security requirements using Given/When/Then format. Ensures traceability from threat to test case.
version: 1.0.0
triggers: ["security requirements", "requirement extraction"]
---

# security-requirement-extraction

## Purpose
Convert abstract threats identified in the STRIDE phase into concrete, testable security requirements.

## Output Structure
Generate a `SecurityRequirements.md` file containing a `RequirementSet`.

## Traceability Mandate
Every requirement MUST link through the following chain:
`threat_id` → `requirement_id` → `test_case_id`

## Data Model (Python Reference)
```python
class SecurityRequirement:
    def __init__(self, id, threat_id, given, when, then, test_case_id):
        self.id = id
        self.threat_id = threat_id
        self.given = given
        self.when = when
        self.then = then
        self.test_case_id = test_case_id

class RequirementSet:
    def __init__(self, requirements=[]):
        self.requirements = requirements
    
    def validate_traceability(self):
        # returns True if no orphans (all have valid threat_id)
        return all(r.threat_id is not None for r in self.requirements)
```

## Rules
- **No Orphans**: Any requirement without a valid `threat_id` is invalid.
- **Actionability**: Use Given/When/Then format to ensure requirements can be directly converted into automated tests.
