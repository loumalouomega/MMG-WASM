#!/usr/bin/env bash
# Regenerate the JS binding artifacts (generated/) from the MMG headers.
# Pure Python; does not need emsdk.

set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
python3 scripts/gen_js.py
