#!/usr/bin/env bash
# Shared environment for all build scripts. Source this; do not execute.
# Pins every external toolchain/version for reproducibility (CI + local).

set -euo pipefail

# Repo root (this file lives in <root>/scripts)
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# --- Pinned versions -------------------------------------------------------
# Emscripten SDK. Bump deliberately; CI caches keyed on this.
EMSDK_VERSION="${EMSDK_VERSION:-3.1.74}"

# --- Locations -------------------------------------------------------------
EMSDK_DIR="${EMSDK_DIR:-$ROOT/.emsdk}"
BUILD_DIR="$ROOT/build"
MMG_SRC="$ROOT/mmg"
MMG_BUILD="$BUILD_DIR/mmg"
DIST="$ROOT/dist"

export ROOT EMSDK_VERSION EMSDK_DIR BUILD_DIR MMG_SRC MMG_BUILD DIST

# Activate emsdk if present (emcc/emcmake on PATH, EMSDK set).
activate_emsdk() {
  if [ -f "$EMSDK_DIR/emsdk_env.sh" ]; then
    # shellcheck disable=SC1091
    source "$EMSDK_DIR/emsdk_env.sh" >/dev/null 2>&1
  else
    echo "emsdk not found at $EMSDK_DIR — run scripts/setup-emsdk.sh first" >&2
    return 1
  fi
}
