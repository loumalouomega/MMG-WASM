#!/usr/bin/env bash
# Build MMG's C API to WebAssembly.
#   1. configure + build libmmg.a (mmg2d + mmgs + mmg3d + common) with emcmake
#   2. regenerate the JS bindings (descriptor / typings / export list)
#   3. emcc-link libmmg.a + the variadic-shim glue into a MODULARIZE'd reactor
#      module, emitted as both ESM (.mjs) and CJS (.cjs) sharing one mmg.wasm
#
# Env knobs:
#   OPT=-O3    (override for faster/debug builds, e.g. OPT="-O0 -g")

set -euo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"
activate_emsdk

OPT="${OPT:--O3}"

mkdir -p "$DIST" "$BUILD_DIR"

# --- 1. Configure + build libmmg.a -----------------------------------------
# - M_LIB=m: mmg does find_library(m), which fails inside the emscripten
#   sysroot (libm is implicit there); presetting the cache var skips the
#   search and emcc treats the resulting -lm as a no-op.
# - CMAKE_DISABLE_FIND_PACKAGE_Perl=ON: otherwise mmg builds a `genheader`
#   host tool (a wasm binary here) and tries to run it for Fortran headers.
# - Only the `libmmg_a` target is built: no executables, no header codegen.
emcmake cmake -S "$MMG_SRC" -B "$MMG_BUILD" \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
  -DBUILD=MMG -DBUILD_SHARED_LIBS=OFF \
  -DUSE_SCOTCH=OFF -DUSE_ELAS=OFF -DUSE_VTK=OFF \
  -DMMG5_INT=int32_t \
  -DCMAKE_DISABLE_FIND_PACKAGE_Perl=ON \
  -DM_LIB=m \
  -DCMAKE_C_FLAGS="$OPT" -DCMAKE_CXX_FLAGS="$OPT -fexceptions"

cmake --build "$MMG_BUILD" --target libmmg_a -- -j"$(nproc)"

LIBMMG="$(find "$MMG_BUILD" -name 'libmmg.a' | head -1)"
[ -n "$LIBMMG" ] || { echo "libmmg.a not produced" >&2; exit 1; }
echo ">> Built $LIBMMG"

# --- 2. Generate bindings + determine exported functions -------------------
# Regenerate the descriptor / typings / export list from the mmg headers so
# the link surface stays in sync with the submodule.
python3 "$ROOT/scripts/gen_js.py" || echo ">> gen_js.py failed; falling back"
EXPORTS="$ROOT/generated/exported_functions.json"
if [ ! -f "$EXPORTS" ]; then
  EXPORTS="$ROOT/scripts/exported_functions.default.json"
  echo ">> Using fallback export list ($EXPORTS)."
fi

# --- 3. Compile glue + emcc link (shared flags) -----------------------------
echo ">> Compiling variadic shims"
emcc "$OPT" -c "$ROOT/src/mmgjs_glue.c" -I"$MMG_BUILD/include" \
  -o "$BUILD_DIR/mmgjs_glue.o"

# STACK_SIZE: mmg overflows emscripten's 64KB default stack during
# remeshing (deep recursion + large locals); 8MB matches native defaults.
common_flags=(
  "$OPT" -fexceptions
  -sMODULARIZE=1 -sEXPORT_NAME=initMmg
  -sALLOW_MEMORY_GROWTH=1 -sINITIAL_MEMORY=64MB -sMAXIMUM_MEMORY=4GB
  -sSTACK_SIZE=8MB
  -sMALLOC=emmalloc
  -sFORCE_FILESYSTEM=1
  -sEXPORTED_RUNTIME_METHODS=FS,ccall,cwrap,getValue,setValue,UTF8ToString,stringToUTF8,lengthBytesUTF8
  -sEXPORTED_FUNCTIONS=@"$EXPORTS"
  -sENVIRONMENT=node,web
)

echo ">> Linking ESM core (dist/mmg-core.mjs)"
emcc "$BUILD_DIR/mmgjs_glue.o" "$LIBMMG" "${common_flags[@]}" \
  -sEXPORT_ES6=1 \
  -o "$DIST/mmg-core.mjs"

echo ">> Linking CJS core (dist/mmg-core.cjs)"
emcc "$BUILD_DIR/mmgjs_glue.o" "$LIBMMG" "${common_flags[@]}" \
  -o "$DIST/mmg-core.cjs"

# Both links emit an identical mmg-core.wasm. Assemble the public entries
# (typed wrapper over the core, dual ESM/CJS) on top.
if [ -f "$ROOT/scripts/assemble.mjs" ]; then
  node "$ROOT/scripts/assemble.mjs"
fi

ls -la "$DIST"
echo ">> Done."
