# File I/O

MMG's file readers/writers are compiled in and operate on an **in-memory
filesystem** (Emscripten MEMFS) exposed as `mmg.FS`. Nothing touches the
real disk: you copy bytes in, let MMG read them, and copy results out.

## Formats

| Format | Load | Save |
|--------|------|------|
| Medit ASCII/binary (`.mesh`/`.meshb`) | `loadMesh` | `saveMesh` |
| Medit solutions (`.sol`/`.solb`) | `loadSol`, `loadAllSols` | `saveSol`, `saveAllSols` |
| Gmsh (`.msh`, v2) | `loadMshMesh`, `loadMshMesh_and_allData` | `saveMshMesh`, `saveMshMesh_and_allData` |
| Format auto-detection | `loadGenericMesh` | `saveGenericMesh` |
| Tetgen (`.node`/`.ele`...) | — | `saveTetgenMesh` (mmg3d) |
| VTK (`.vtk`/`.vtu`/`.vtp`) | declared, **fails at runtime** | declared, **fails at runtime** |

!!! warning "VTK entry points"
    The `loadVtkMesh`/`saveVtuMesh`/... functions exist in the API (they are
    part of MMG's headers) but the WASM build compiles MMG **without VTK**,
    so they return an error at runtime. Use Medit or Gmsh formats instead.

## Round trip example

```js
const mmg = await initialize();
const { mmg3d, FS } = mmg;

// bring a mesh file into the sandbox (Node example)
import { readFile } from 'node:fs/promises';
FS.writeFile('/input.mesh', await readFile('input.mesh'));

const h = mmg3d.init();
mmg3d.loadMesh(h.mesh, '/input.mesh');
mmg3d.setDparameter(h.mesh, h.met, mmg3d.DPARAM_hausd, 0.01);
mmg3d.remesh(h.mesh, h.met);
mmg3d.saveMesh(h.mesh, '/output.mesh');
mmg3d.free(h);

const bytes = FS.readFile('/output.mesh');            // Uint8Array
const text = FS.readFile('/output.mesh', { encoding: 'utf8' });
```

In the browser, fetch the input instead:

```js
const buf = new Uint8Array(await (await fetch('part.mesh')).arrayBuffer());
FS.writeFile('/part.mesh', buf);
```

## Solutions

```js
mmg3d.loadSol(h.mesh, h.met, '/metric.sol');   // metric / level-set values
mmg3d.saveSol(h.mesh, h.met, '/out.sol');
```

`loadAllSols`/`saveAllSols` handle multi-field `.sol` files together with
`setSolsAtVerticesSize`/`getSolsAtVerticesSize` and the
`*ithSol_inSolsAtVertices` accessors.

## File names inside the structures

`setInputMeshName`/`setOutputMeshName` (and the `Sol` variants) store
default file names in the structures; `saveMesh(mesh, null)` then uses the
stored name. Passing an explicit path is usually simpler.

## MEMFS notes

- Paths are POSIX-style, rooted at `/`; `FS.mkdir('/data')` creates
  directories.
- Contents live in WASM memory: delete big files with `FS.unlink` when done.
- MEMFS is per-`initialize()` call and vanishes with the instance.
