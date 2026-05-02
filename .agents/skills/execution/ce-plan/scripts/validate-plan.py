#!/usr/bin/env python3
import sys
import os
import re

def validate_plan(filepath):
    if not os.path.exists(filepath):
        print("FAIL: Plan file does not exist.")
        sys.exit(1)
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    required_sections = ["Overview", "Implementation Units", "Dependencies", "Risks", "Test Scenarios", "Acceptance Criteria"]
    missing = [sec for sec in required_sections if not re.search(rf'#+\s+{sec}', content, re.IGNORECASE) and not re.search(rf'#+\s+.*{sec}.*', content, re.IGNORECASE)]
    
    if missing:
        print(f"FAIL: Missing required sections: {', '.join(missing)}")
        sys.exit(1)
        
    # Arbitrary confidence score logic based on detail length
    cs = min(100, 50 + (len(content) // 100))
    if cs < 70:
        print(f"FAIL: Plan lacks sufficient detail. Confidence Score: {cs}")
        sys.exit(1)
        
    print(f"PASS: Plan validated successfully. Confidence Score: {cs}")
    sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate-plan.py <path_to_plan.md>")
        sys.exit(1)
    validate_plan(sys.argv[1])
