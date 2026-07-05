# Getting started

## Install

```bash
npm install @loumalouomega/mmg-wasm
```

The package ships prebuilt WASM — consumers never need Emscripten, CMake or
a C compiler.

## Load the module

=== "ESM"

    ```js
    import initialize from '@loumalouomega/mmg-wasm';
    const mmg = await initialize();
    ```

=== "CommonJS"

    ```js
    const initialize = require('@loumalouomega/mmg-wasm');
    initialize().then((mmg) => { /* ... */ });
    ```

`initialize()` loads and instantiates the WASM binary and returns the API
object with the three modules (`mmg.mmg3d`, `mmg.mmg2d`, `mmg.mmgs`), the
shared constants, and `mmg.FS` (the in-memory filesystem).

!!! tip "One WASM instance, many meshes"
    Unlike libraries with global state, MMG is handle-based: call
    `initialize()` once and create as many independent mesh/solution pairs
    as you need via each module's `init()`.

## First remesh: adapt a tetrahedral cube

The canonical MMG "hello world" (upstream `adaptation_example0`): build a
two-material cube of 12 vertices / 12 tetrahedra / 20 boundary triangles,
then adapt it with a Hausdorff distance of 0.1.

```js
import initialize from '@loumalouomega/mmg-wasm';

const mmg = await initialize();
const { mmg3d } = mmg;

// 1) allocate the MMG5_pMesh / MMG5_pSol structures
const h = mmg3d.init();

// 2) describe the input mesh
mmg3d.setMeshSize(h.mesh, 12, 12, 0, 20, 0, 0);
vertices.forEach(([x, y, z], i) => mmg3d.setVertex(h.mesh, x, y, z, 0, i + 1));
tetrahedra.forEach(([a, b, c, d, ref], i) =>
  mmg3d.setTetrahedron(h.mesh, a, b, c, d, ref, i + 1));
triangles.forEach(([a, b, c, ref], i) =>
  mmg3d.setTriangle(h.mesh, a, b, c, ref, i + 1));

// 3) optional size map (scalar metric: target edge length per vertex)
mmg3d.setSolSize(h.mesh, h.met, mmg.MMG5_Vertex, 12, mmg.MMG5_Scalar);
for (let k = 1; k <= 12; k++) mmg3d.setScalarSol(h.met, 0.5, k);

// 4) parameters and remeshing
mmg3d.setDparameter(h.mesh, h.met, mmg3d.DPARAM_hausd, 0.1);
const code = mmg3d.remesh(h.mesh, h.met);   // alias of mmg3dlib
if (code === mmg.MMG5_LOWFAILURE) console.warn('remeshed with warnings');

// 5) read the adapted mesh back
const { np, ne } = mmg3d.getMeshSize(h.mesh);
const { vertices: coords, refs } = mmg3d.getVertices(h.mesh, np);
const { tetra } = mmg3d.getTetrahedra(h.mesh, ne);

// 6) release everything
mmg3d.free(h);
```

Entity indices are **1-based**, exactly as in the MMG C API.

## Error handling

- `Set_*`/`Get_*`/`load*`/`save*` style functions throw a JavaScript `Error`
  when MMG reports failure (C return ≠ 1).
- The remeshing entry points (`remesh`, `levelset`, `move`, `generate`)
  return the MMG library code — `mmg.MMG5_SUCCESS` (0) or
  `mmg.MMG5_LOWFAILURE` (1) — and only throw on `MMG5_STRONGFAILURE`.

```js
try {
  mmg3d.setVertex(h.mesh, 0, 0, 0, 0, 999999); // out of range -> throws
} catch (e) {
  console.error(e.message); // "MMG3D_Set_vertex failed (returned 0)"
}
```

## Next steps

- [Concepts](guide/concepts.md) — the handle model and per-module lifecycle.
- [3D adaptation](guide/adaptation-3d.md), [2D meshing](guide/meshing-2d.md),
  [surface remeshing](guide/surface.md), [level-sets](guide/levelset.md).
- [File I/O](guide/file-io.md) — Medit/Gmsh files through MEMFS.
