import os
import sys

# Rule 11.5: Use script-relative absolute path to prevent CWD-dependent failures on Windows.
# Path: workspace/.agents/scripts/this_script.py
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))  # .../scripts
_AGENTS_DIR = os.path.dirname(_SCRIPT_DIR)                 # .../.agents
_WORKSPACE_ROOT = os.path.dirname(_AGENTS_DIR)             # workspace root

def catchup():
    print("APEX Session Catchup...")
    nucleus_files = ["task_plan.md", "findings.md", "progress.md"]
    found = []
    for fname in nucleus_files:
        fpath = os.path.join(_WORKSPACE_ROOT, fname)
        if os.path.exists(fpath):
            found.append(fname)
            print(f"[FOUND] {fname}")
        else:
            print(f"[MISSING] {fname}")

    if "task_plan.md" in found:
        task_plan_path = os.path.join(_WORKSPACE_ROOT, "task_plan.md")
        with open(task_plan_path, "r") as f:
            print("\n--- Current Plan Summary (first 20 lines) ---")
            for i, line in enumerate(f):
                if i < 20:
                    print(line.strip())
                else:
                    break

    # Check for in-progress tasks
    if "task_plan.md" in found:
        task_plan_path = os.path.join(_WORKSPACE_ROOT, "task_plan.md")
        with open(task_plan_path, "r") as f:
            content = f.read()
        import re
        in_progress = re.findall(r"- \[/\]", content)
        unchecked = re.findall(r"- \[ \]", content)
        if in_progress or unchecked:
            print(f"\n[RESUME] {len(in_progress)} in-progress, {len(unchecked)} pending tasks found.")
            print("[ACTION] Read task_plan.md and resume from the first [/] item.")
        else:
            print("\n[CLEAN] No active tasks. System is at rest.")

    print("\n[READY] Context re-oriented. Proceed with next action.")

if __name__ == "__main__":
    catchup()
