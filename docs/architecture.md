# Architecture

mmg-wasm follows a strict "generator emits data, one runtime interprets it"
design (shared with its sibling project
[gmsh-wasm](https://github.com/loumalouomega/GMSH-JS)): there is no
per-function binding code anywhere.

```
mmg/src/{mmg3d,mmg2d,mmgs}/libmmg*.h      mmg/ (submodule, unmodified)
        │  parsed by
        ▼
scripts/gen_js.py  ◄── scripts/mmg_overrides.py (bulk arrays, ret modes)
        │
        ├─► generated/exported_functions.json   (emcc export list)
        ├─► generated/mmg-api.json              (descriptor table)
        └─► generated/mmg.d.ts                  (TypeScript declarations)

scripts/build-wasm.sh
        │  emcmake cmake mmg → build/mmg/lib/libmmg.a
        │  emcc  libmmg.a + src/mmgjs_glue.c  (×2: ESM, CJS)
        ▼
dist/mmg-core.{mjs,cjs,wasm}

scripts/assemble.mjs
        │  + src/runtime.mjs (the ONLY marshalling code)
        │  + generated/mmg-api.json (inlined)
        ▼
dist/mmg.{mjs,cjs}, dist/runtime.{mjs,cjs}, dist/mmg-descriptor.{mjs,cjs},
dist/mmg.d.ts

scripts/gen_docs_api.py ──► docs/api/reference.md
```

## Why header parsing?

Gmsh ships a declarative API definition that its own bindings are generated
from; MMG does not — its ground truth is the doxygen-annotated public
headers. `gen_js.py` parses the `LIBMMG*_EXPORT` prototypes with a small
recognizer. MMG's headers carry no machine-readable in/out annotations, so
direction is inferred from names (`Get_*` → out-pointers) plus an explicit
table (`scripts/mmg_overrides.py`) for the ~40 bulk-array functions; the
generator warns when the tables drift from the headers.

## The C shim layer

Exactly one C file is added on top of MMG: `src/mmgjs_glue.c`, fixed-arity
wrappers over the 12 variadic `MMG5_ARG_*` functions (`Init_mesh`,
`Free_all`, `Free_structures`, `Free_names` × 3 modules), because varargs
cannot cross the JS/WASM boundary. Everything else calls MMG symbols
directly.

## The handle model

A JS handle is the address of a 4-byte heap slot holding the
`MMG5_pMesh`/`MMG5_pSol` struct pointer:

- kind `handle` (C takes the struct by value): the runtime passes
  `HEAPU32[h>>2]`;
- kind `handleref` (C takes `MMG5_pMesh*`): the runtime passes `h` itself,
  so MMG's own NULL-ing of freed pointers works untouched.

Handles stay plain numbers in JS (branded in TypeScript); there are no
wrapper objects and no finalizers — `free()` is explicit.

## Descriptor-driven runtime

`src/runtime.mjs` walks `generated/mmg-api.json` once at `initialize()`
time, producing a closure per function that: writes inputs into the heap,
allocates output buffers, invokes the raw export, applies the return-mode
policy (`status` throws on ≠1, `libcode` throws on STRONGFAILURE), copies
outputs into JS-owned typed arrays, and frees everything in `finally`.

Adding a new upstream function usually requires **zero code**: re-run
`npm run gen`, rebuild, done (plus one `mmg_overrides.py` line if it has a
bulk-array parameter).

## Testing strategy

- `test/smoke.test.mjs` drives the **raw exports** (no wrapper) through the
  canonical cube example — proves compilation, exceptions, memory.
- `test/api.test.mjs` exercises the typed wrapper across all three modules,
  the bulk paths, level-sets, MEMFS I/O and the error mapping.
- `test/browser.test.mjs` loads the real ESM package in headless Chromium.
