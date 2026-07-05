# Troubleshooting

## "RuntimeError: memory access out of bounds" / stack overflow

The shipped build uses an 8 MB stack precisely because MMG recurses deeply;
if you rebuilt locally without `-sSTACK_SIZE=8MB` you will hit this on the
first remesh. Rebuild with the stock `scripts/build-wasm.sh` flags.

## `remesh` returned 1 (`MMG5_LOWFAILURE`)

Not an exception: MMG produced a usable mesh but could not satisfy
everything (often boundary approximation vs. `hausd`, or bad input
elements). Inspect with `IPARAM_verbose ≥ 5`; validate the input first with
`chkMeshData(mesh, met)`.

## Calls throw "`MMG3D_Set_vertex failed (returned 0)`"

The C function reported failure. The usual causes, in order:

1. `setMeshSize` not called (or called with smaller counts than you then
   set) — MMG refuses out-of-range positions;
2. 0-based indices — MMG entities are **1-based**;
3. solution size mismatch — `setSolSize` count must equal the mesh vertex
   count when remeshing.

MMG prints details to the console unless verbosity is silenced
(`IPARAM_verbose = -1`).

## `loadVtkMesh` / `saveVtuMesh` fail

Expected: the WASM build compiles MMG without VTK. Use Medit
(`.mesh`/`.sol`) or Gmsh (`.msh`) formats — see [File I/O](guide/file-io.md).

## `move` / `IPARAM_lag` rejected

Lagrangian motion needs MMG's optional LinearElasticity dependency
(`USE_ELAS`), which is not in the WASM build. See
[Level-set & Lagrangian motion](guide/levelset.md).

## Browser: `.wasm` fails to load / MIME error

Serve `mmg-core.wasm` with `Content-Type: application/wasm`, or pass a
`locateFile` override pointing at the correct URL — see
[Browser usage](guide/browser.md).

## Node: `require()` / `import` mismatch

The package is dual: `import` gets `dist/mmg.mjs`, `require` gets
`dist/mmg.cjs` via the `exports` map. If a bundler resolves the wrong one,
pin the condition (`"node"`/`"import"`) or import the file explicitly.

## Output looks noisy

MMG logs to stdout/stderr by default. Silence per mesh with
`setIparameter(h.mesh, h.met, <mod>.IPARAM_verbose, -1)`, or capture the
streams via the Emscripten overrides:

```js
const mmg = await initialize({ print: (s) => {}, printErr: (s) => {} });
```

## Memory keeps growing

WASM memory never shrinks. Free meshes (`free(h)`), unlink MEMFS files
(`FS.unlink`), and for long-lived apps consider re-running `initialize()`
to start a fresh instance for large one-off jobs.
