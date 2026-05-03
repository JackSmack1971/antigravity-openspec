#!/usr/bin/env bash
# gitignore-check.sh — verify .gitignore before worktree creation
# Usage: bash gitignore-check.sh
set -euo pipefail
REPO_ROOT=$(git rev-parse --show-toplevel)
cd "$REPO_ROOT"
echo "=== GITIGNORE VERIFICATION ==="
SENSITIVE_PATTERNS=(".env" ".env.local" "*.key" "*.pem" "secrets/" "node_modules/" ".agents/artifacts/")
MISSING=()
for pattern in "${SENSITIVE_PATTERNS[@]}"; do
  if ! grep -qF "$pattern" .gitignore 2>/dev/null; then
    MISSING+=("$pattern")
  fi
done
if [ ${#MISSING[@]} -gt 0 ]; then
  echo "FAIL: Missing .gitignore entries:"
  for m in "${MISSING[@]}"; do echo "  - $m"; done
  exit 1
fi
echo "PASS: All sensitive patterns covered."
exit 0
