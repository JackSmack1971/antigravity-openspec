import os
import sys
import re

# Rule 11.5: Use script-relative absolute path to prevent CWD-dependent failures on Windows.
# Path: workspace/.agents/scripts/this_script.py
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))  # .../scripts
_AGENTS_DIR = os.path.dirname(_SCRIPT_DIR)                 # .../.agents
_WORKSPACE_ROOT = os.path.dirname(_AGENTS_DIR)             # workspace root
_TASK_PLAN = os.path.join(_WORKSPACE_ROOT, "task_plan.md")

def check_complete():
    if not os.path.exists(_TASK_PLAN):
        print("[SKIP] No task_plan.md found.")
        return True

    with open(_TASK_PLAN, "r") as f:
        content = f.read()

    # Find all unchecked tasks [ ]
    unchecked = re.findall(r"- \[ \]", content)

    if unchecked:
        print(f"[WARNING] {len(unchecked)} tasks remain incomplete in task_plan.md.")
        print("[FAIL] Mandatory /retro loop blocked by incomplete tasks.")
        return False

    print("[SUCCESS] All tasks completed. Proceeding to /retro.")
    return True

if __name__ == "__main__":
    if not check_complete():
        sys.exit(1)
    sys.exit(0)
