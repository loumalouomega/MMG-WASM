# CLAUDE.md

Guidance for working in this repository with Claude Code. Keep it short;
record only what isn't obvious. On every code change, check whether `docs/`,
`README.md`, and this file need updating.

## What this is

`mmg-wasm` compiles the MMG remeshers (mmg2d, mmgs, mmg3d — the `mmg/`
submodule, unmodified) to WebAssembly with Emscripten and wraps the flat C
API in a typed JS/TS package (`@loumalouomega/mmg-wasm`). Node + browser,
single-threaded, MEMFS for file I/O. No VTK/SCOTCH/ELAS.

## Architecture (how a change flows)

```
mmg/src/*/libmmg*.h → scripts/gen_js.py (+ scripts/mmg_overrides.py)
                    → generated/{exported_functions.json, mmg-api.json, mmg.d.ts}
scripts/build-wasm.sh → emcmake mmg → libmmg.a → emcc (+ src/mmgjs_glue.c)
                      → dist/mmg-core.{mjs,cjs,wasm}
scripts/assemble.mjs → dist/mmg.{mjs,cjs} + runtime + descriptor + .d.ts
scripts/gen_docs_api.py → docs/api/reference.md
```

- `src/runtime.mjs` is the ONLY marshalling location; the generator emits
  data, never code. Never hand-edit `generated/`.
- Handles are addresses of 4-byte heap slots boxing MMG5_pMesh/MMG5_pSol;
  kind `handle` dereferences the slot, `handleref` passes the slot itself.
- `src/mmgjs_glue.c` holds the only C additions: fixed-arity shims for the
  12 variadic `MMG5_ARG_*` functions.

## Key commands

| Command | What |
|---------|------|
| `npm run setup` | install pinned emsdk into `.emsdk/` |
| `npm run build:wasm` | full build → `dist/` |
| `npm run gen` | regenerate `generated/` from headers (no emcc needed) |
| `npm test` | node smoke + typed API tests |
| `npm run test:browser` | Playwright headless Chromium |
| `npm run docs:build` | regen API reference + `mkdocs build` |

emsdk is not on PATH; scripts source `scripts/env.sh` and call
`activate_emsdk`. `EMSDK_DIR=<path>` reuses an existing SDK.

## Repo conventions

- `generated/` is committed; CI regenerates and `git diff --exit-code`s it.
- `dist/`, `build/`, `.emsdk/`, `site/`, `node_modules/` are gitignored.
- Public API: `initialize()` loads the wasm and returns the api; lifecycle
  is per-mesh via `mmg3d.init()` / `mmg3d.free(handles)` (no global
  init/finalize).
- Classification gaps go in `scripts/mmg_overrides.py` (BULK / RETMODE /
  UNSUPPORTED / ALIASES), never as special cases in the runtime.

## Gotchas (learned the hard way)

- **`-sSTACK_SIZE=8MB` is required**: mmg overflows Emscripten's 64 KB
  default stack during remeshing ("memory access out of bounds" after
  PHASE 1 output).
- mmg's CMake `find_library(m)` fails in the emscripten sysroot — preset
  `-DM_LIB=m`.
- Pass `-DCMAKE_DISABLE_FIND_PACKAGE_Perl=ON` and build only the
  `libmmg_a` target, or mmg tries to build+run a `genheader` host tool
  (a wasm binary) for Fortran headers.
- MMG headers have **no `\param[out]`** annotations: out-detection is
  name-based (`Get_*`) plus the BULK table. gen_js.py warns on drift.
- `MMG3D_Param` is ONE enum: `DPARAM_*` values continue after the 26
  `IPARAM_*` entries (e.g. `DPARAM_hausd` = 30). Never hardcode; use the
  generated constants.
- `MMG2D_loadVect/saveVect/scaleMesh` are declared in the header but not
  defined in the library — exporting them breaks the link (kept in
  UNSUPPORTED).
- This package's `package.json` has `"type": "module"`, so emcc's classic
  (non-ES6) output must be named `.cjs` to run under node.
- VTK entry points are declared and bound but fail at runtime (built
  without VTK) — documented, not a bug.
- Builds take minutes; run them in the background.

## Decisions (fixed for v1)

LGPL-3.0-or-later (matches mmg; root LICENSE = mmg/COPYING.LESSER).
`MMG5_INT=int32_t`. emmalloc. `-fexceptions` (mmg's C++ I/O). MODULARIZE +
EXPORT_ES6 for the ESM core. All three modules in one wasm. MEMFS I/O on.
