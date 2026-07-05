# Concepts

## The three modules

MMG is three remeshers sharing one infrastructure; mmg-wasm builds all of
them into a single WASM binary:

| Module | Mesh type | Entry points |
|--------|-----------|--------------|
| `mmg2d` | planar triangular (+ quads) | `remesh` (mmg2dlib), `generate` (mmg2dmesh), `levelset` (mmg2dls), `move` (mmg2dmov) |
| `mmgs`  | triangulated surfaces in 3D | `remesh` (mmgslib), `levelset` (mmgsls) |
| `mmg3d` | tetrahedral volumes (+ prisms) | `remesh` (mmg3dlib), `levelset` (mmg3dls), `move` (mmg3dmov) |

Each module namespace carries its full generated API
(`mmg3d.setVertex`, `mmg2d.getTriangles`, …) plus its parameter constants
(`mmg3d.IPARAM_verbose`, `mmg3d.DPARAM_hausd`, …). Shared constants
(`MMG5_SUCCESS`, `MMG5_Scalar`, `MMG5_Vertex`, format codes) live on the
root API object.

## Handles

The MMG C API works on two structures:

- `MMG5_pMesh` — the mesh: vertices, elements, adjacency, parameters;
- `MMG5_pSol` — a solution field: metric (size map), level-set values, or
  displacement vectors.

In JavaScript these are **opaque numeric handles** (branded as `MeshHandle` /
`SolHandle` in TypeScript). You never touch their contents; you pass them to
API functions. A handle is technically the address of a small heap slot
holding the C struct pointer, which lets MMG's own free functions NULL the
pointer exactly as they do in C — but you can treat it as an opaque token.

## Lifecycle

```js
const h = mmg3d.init();                    // { mesh, met }
const h2 = mmg3d.init({ levelset: true }); // { mesh, met, ls }
const h3 = mmg3d.init({ displacement: true }); // { mesh, met, disp }
// ... use ...
mmg3d.free(h);                             // MMG3D_Free_all + release handles
```

- `init()` wraps the (variadic) `MMG3D_Init_mesh` C call through a fixed
  shim; it allocates and initializes the structures.
- `free()` wraps `MMG3D_Free_all` and releases the handle slots. Always call
  it — WASM memory is not garbage-collected.
- Multiple concurrent handle sets are fine; the WASM instance is shared but
  each mesh is independent.

There is **no** global `initialize`/`finalize` pair like Gmsh has: after
`await initialize()` (which only loads the WASM), lifecycle is entirely
per-mesh.

## Data flow

Every workflow is the same three phases, mirroring the C API:

1. **Describe**: `setMeshSize` (allocates), then per-entity setters
   (`setVertex`, `setTetrahedron`, …) or bulk setters (`setVertices`,
   `setTetrahedra`, … with typed arrays). Optionally attach a solution:
   `setSolSize` + `setScalarSol`/`setTensorSol`/… on `h.met` (metric) or
   `h.ls` (level-set).
2. **Run**: set parameters (`setIparameter`/`setDparameter`), then call an
   entry point (`remesh`/`levelset`/`move`/`generate`).
3. **Harvest**: `getMeshSize`, then per-entity getters (`getVertex`) or bulk
   getters (`getVertices(h.mesh, np)` → typed arrays).

!!! warning "Indices are 1-based"
    MMG numbers vertices and elements from 1, and bulk arrays are laid out
    accordingly (the first vertex occupies `vertices[0..2]` but is *vertex
    1* when referenced from a tetrahedron).

## Parameters

Integer parameters via `setIparameter(mesh, sol, IPARAM_*, value)`, real
parameters via `setDparameter(mesh, sol, DPARAM_*, value)`. The most used:

| Parameter | Meaning |
|-----------|---------|
| `IPARAM_verbose` | verbosity, `-1` silences all output |
| `DPARAM_hausd` | Hausdorff distance controlling boundary approximation |
| `DPARAM_hmin` / `DPARAM_hmax` | min/max edge lengths |
| `DPARAM_hsiz` | constant target edge length |
| `DPARAM_hgrad` | mesh gradation |
| `IPARAM_iso` | enable level-set discretization mode |
| `IPARAM_optim` | optimize while keeping edge sizes |

The full per-module lists are on each module object (every `IPARAM_*` /
`DPARAM_*` enum entry) and in the [API reference](../api/reference.md).

## Solutions (metrics, level-sets, displacements)

A `MMG5_pSol` stores per-vertex values whose meaning depends on the entry
point: for `remesh` it is the metric (scalar isotropic size or tensor
anisotropic metric), for `levelset` the implicit function values, for `move`
the displacement vectors. Declare with
`setSolSize(mesh, sol, MMG5_Vertex, np, MMG5_Scalar | MMG5_Vector | MMG5_Tensor)`
then fill with the matching setters.
