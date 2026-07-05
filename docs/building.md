# Building from source

Consumers of the npm package never need this — it documents how the `.wasm`
and bindings are produced (locally and in CI).

## Prerequisites

- Linux or macOS, bash, git
- CMake ≥ 3.24, Python 3.10+, Node 18+
- ~2 GB free disk (Emscripten SDK + build trees)

Everything else is pinned and installed by the scripts.

## Steps

```bash
git clone --recurse-submodules https://github.com/loumalouomega/MMG-WASM.git
cd MMG-WASM

npm run setup        # install pinned Emscripten SDK into .emsdk/
npm run build:wasm   # configure mmg, build libmmg.a, link, assemble dist/
npm install          # dev deps (playwright) for the test suite
npm test             # Node smoke + typed API tests
npm run test:browser # headless Chromium (needs: npx playwright install chromium)
```

The build takes a few minutes; the result is a self-contained `dist/`.

## What `build:wasm` does

1. **Configure + compile MMG** with `emcmake cmake` (options:
   `BUILD=MMG`, static lib only, `USE_SCOTCH/USE_ELAS/USE_VTK=OFF`,
   `MMG5_INT=int32_t`, Perl disabled) and build the single `libmmg_a`
   target → `build/mmg/lib/libmmg.a`.
2. **Regenerate bindings**: `scripts/gen_js.py` parses the MMG public
   headers into `generated/{exported_functions.json, mmg-api.json, mmg.d.ts}`.
3. **Link** `libmmg.a` + `src/mmgjs_glue.c` (variadic shims) with `emcc`
   twice — ESM and CJS — sharing one `mmg-core.wasm`.
4. **Assemble**: `scripts/assemble.mjs` writes the public entries
   (`dist/mmg.{mjs,cjs}`), the runtime, the inlined descriptor and the
   typings.

## Key emcc flags

| Flag | Why |
|------|-----|
| `-O3 -fexceptions` | optimized; MMG's C++ I/O files need exceptions |
| `-sMODULARIZE -sEXPORT_NAME=initMmg` | factory function, no globals |
| `-sALLOW_MEMORY_GROWTH -sINITIAL_MEMORY=64MB -sMAXIMUM_MEMORY=4GB` | meshes of unpredictable size |
| `-sSTACK_SIZE=8MB` | **required** — mmg overflows the 64 KB default stack |
| `-sFORCE_FILESYSTEM` | MEMFS for the file I/O API |
| `-sEXPORTED_FUNCTIONS=@generated/exported_functions.json` | the generated C surface |
| `-sENVIRONMENT=node,web` | no shell/worker-specific code paths |

## Build knobs

```bash
OPT="-O0 -g" npm run build:wasm     # debug build
EMSDK_DIR=/path/to/existing/emsdk npm run build:wasm  # reuse an SDK
```

## Regenerating bindings only

```bash
npm run gen          # scripts/gen_js.py -> generated/
git diff generated/  # CI fails if this is non-empty after a build
```

`generated/` is committed so consumers of the repo (and the docs build) can
work without running Emscripten; CI verifies it stays in sync with the
submodule headers.

## Bumping the MMG version

```bash
cd mmg && git fetch && git checkout vX.Y.Z && cd ..
npm run gen                    # regenerate bindings; check the warnings
npm run build:wasm && npm test
git add mmg generated/ && git commit
```

`gen_js.py` warns when override tables in `scripts/mmg_overrides.py` drift
from the headers (renamed args, added pointer parameters) — fix those
before committing.
