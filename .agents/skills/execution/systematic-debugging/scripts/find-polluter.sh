#!/usr/bin/env bash
# find-polluter.sh — git bisect wrapper to locate regression commit
# Usage: bash find-polluter.sh <good-commit> <bad-commit> <test-command>
set -euo pipefail
GOOD=$1
BAD=$2
TEST_CMD=$3
if [ -z "$GOOD" ] || [ -z "$BAD" ] || [ -z "$TEST_CMD" ]; then
  echo "Usage: find-polluter.sh <good-commit> <bad-commit> <test-command>"
  exit 1
fi
echo "=== BISECT START: good=$GOOD bad=$BAD ==="
git bisect start
git bisect bad "$BAD"
git bisect good "$GOOD"
git bisect run bash -c "$TEST_CMD"
echo "=== BISECT COMPLETE ==="
git bisect reset
