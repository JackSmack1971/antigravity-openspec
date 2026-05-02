import os
import sys

def main():
    plan_path = 'task_plan.md'
    if not os.path.exists(plan_path):
        print("No task_plan.md found. Skipping complete check.")
        return

    try:
        with open(plan_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error reading {plan_path}: {e}")
        return

    incomplete_tasks = []
    for i, line in enumerate(lines):
        if '- [ ]' in line or '- [/]' in line:
            incomplete_tasks.append(f"Line {i+1}: {line.strip()}")

    if incomplete_tasks:
        print("WARNING: Incomplete workflow chains detected in task_plan.md!")
        for task in incomplete_tasks:
            print(f"  {task}")
        print("\nPlease complete or explicitly defer these tasks before closing the session.")
        sys.exit(1)
    else:
        print("All tasks in task_plan.md appear complete. You MUST proceed to /retro.")
        print("Ensure the KNOWLEDGE SUBAGENT is triggered to extract KIs before closing the session.")
        sys.exit(0)

if __name__ == "__main__":
    main()
