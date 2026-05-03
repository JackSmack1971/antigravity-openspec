---
name: attack-tree-construction
description: Construct attack trees to visualize and analyze potential attack paths for high-risk threats.
version: 1.0.0
triggers: ["attack tree", "attack paths", "threat paths"]
---

# attack-tree-construction

## Purpose
Deconstruct the top 3 highest-risk threats into component attack steps to identify the most likely or dangerous paths an attacker might take.

## Path Analysis
Compute exactly 3 paths per tree:
1. **Easiest**: Lowest required skill level.
2. **Cheapest**: Lowest resource cost for the attacker.
3. **Stealthiest**: Lowest probability of detection.

## Output
- `AttackTree.json`: Machine-readable representation of the tree.
- `attack-tree-visualization.md`: Human-readable markdown tree diagram.

## Data Model (Python Reference)
```python
class AttackNode:
    def __init__(self, id, description, cost, skill_level, detectability):
        self.id = id
        self.description = description
        self.cost = cost # 1-5
        self.skill_level = skill_level # 1-5
        self.detectability = detectability # 1-5 (5 is most detectable)

class AttackTree:
    def __init__(self, root):
        self.root = root
    
    def add_node(self, parent_id, node):
        pass
    
    def find_paths(self, mode):
        # mode: 'easiest', 'cheapest', 'stealthiest'
        pass
```

## Workflow
1. Use the **Builder Pattern**: construct the tree incrementally node-by-node.
2. Perform path analysis.
3. Export JSON and generate markdown visualization.
