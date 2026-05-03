#!/usr/bin/env python3
"""
ce-plan :: Plan Validator (Black-Box Script)
Agent: execute with --help for usage. NEVER read or modify internals.
Exit 0 = valid. Exit 1 = errors in JSON stdout.
"""

import sys
import re
import json
import argparse

REQUIRED_SECTIONS = [
    "Overview",
    "Implementation Units",
    "Dependencies",
    "Risks",
    "Test Scenarios",
    "Acceptance Criteria",
]

ABSOLUTE_PATH_PATTERN = re.compile(
    r'(?:^|[\s`"\'])(/(?:home|usr|etc|var|opt|root|tmp)|~/)', re.MULTILINE
)
CONFIDENCE_PATTERN = re.compile(r'CS:\s*(\d+)%|Confidence:\s*(\d+)%', re.IGNORECASE)
IU_BLOCK_PATTERN = re.compile(
    r'#+\s*IU\d*|#+\s*Implementation Unit', re.IGNORECASE
)
AC_PATTERN = re.compile(r'AC:|Acceptance Criteria', re.IGNORECASE)


def validate(filepath: str) -> list[str]:
    errors = []

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        return [f"ERROR: Plan file not found at '{filepath}'."]
    except OSError as e:
        return [f"ERROR: Cannot read '{filepath}': {e}"]

    # S1 — Required sections present
    for section in REQUIRED_SECTIONS:
        pattern = re.compile(rf'#+\s*{re.escape(section)}', re.IGNORECASE)
        if not pattern.search(content):
            errors.append(f"ERROR: Required section missing: '{section}'.")

    # S2 — No absolute paths
    abs_matches = ABSOLUTE_PATH_PATTERN.findall(content)
    if abs_matches:
        errors.append(
            f"ERROR: Absolute path(s) detected ({len(abs_matches)} occurrence(s)). "
            "All file refs must be repo-relative."
        )

    # S3 — Confidence Score present and >= 70
    cs_match = CONFIDENCE_PATTERN.search(content)
    if not cs_match:
        errors.append("ERROR: No Confidence Score (CS) found. Required format: 'CS: 85%'.")
    else:
        score_str = cs_match.group(1) or cs_match.group(2)
        score = int(score_str)
        if score < 70:
            errors.append(
                f"ERROR: CS {score}% is below handoff threshold (70%). "
                "Return to Phase 1 with gap identification."
            )

    # S4 — Each IU block contains AC
    iu_blocks = IU_BLOCK_PATTERN.split(content)
    # First block is pre-IU preamble; check subsequent blocks
    for i, block in enumerate(iu_blocks[1:], start=1):
        if not AC_PATTERN.search(block):
            errors.append(
                f"ERROR: Implementation Unit #{i} is missing Acceptance Criteria (AC)."
            )

    # S5 — Plan file must not be empty
    if len(content.strip()) < 100:
        errors.append("ERROR: Plan file appears empty or severely truncated.")

    return errors


def main():
    parser = argparse.ArgumentParser(
        description="ce-plan validator — checks plan structure, path hygiene, and confidence gate."
    )
    parser.add_argument("plan_file", help="Path to the plan Markdown file to validate.")
    args = parser.parse_args()

    errors = validate(args.plan_file)

    if errors:
        print(json.dumps({"status": "failed", "error_count": len(errors), "errors": errors}, indent=2))
        sys.exit(1)
    else:
        print(json.dumps({"status": "passed", "message": "Plan validation successful. Ready for handoff."}))
        sys.exit(0)


if __name__ == "__main__":
    main()

