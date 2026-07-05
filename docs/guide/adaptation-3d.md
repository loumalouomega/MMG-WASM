# 3D adaptation (mmg3d)

`mmg3d` adapts tetrahedral meshes: refinement/coarsening to a size map,
boundary approximation control, quality optimization.

## Building the input mesh

```js
const h = mmg3d.init();

// np vertices, ne tetrahedra, nprism prisms, nt triangles, nquad quads, na edges
mmg3d.setMeshSize(h.mesh, np, ne, 0, nt, 0, 0);
```

Per-entity (1-based positions):

```js
mmg3d.setVertex(h.mesh, x, y, z, ref, i);          // i in 1..np
mmg3d.setTetrahedron(h.mesh, v0, v1, v2, v3, ref, k); // k in 1..ne
mmg3d.setTriangle(h.mesh, v0, v1, v2, ref, t);     // boundary triangles
```

Or bulk, with typed arrays (fastest across the JS/WASM boundary):

```js
mmg3d.setVertices(h.mesh, coords /* Float64Array 3*np */, refs /* Int32Array np or null */);
mmg3d.setTetrahedra(h.mesh, tetra /* Int32Array 4*ne */, tetRefs);
mmg3d.setTriangles(h.mesh, tria /* Int32Array 3*nt */, triRefs);
```

## Size maps (metrics)

Attach the metric to `h.met`:

```js
// isotropic: one target edge length per vertex
mmg3d.setSolSize(h.mesh, h.met, mmg.MMG5_Vertex, np, mmg.MMG5_Scalar);
mmg3d.setScalarSols(h.met, sizes /* Float64Array np */);

// anisotropic: one symmetric 3x3 tensor (6 values) per vertex
mmg3d.setSolSize(h.mesh, h.met, mmg.MMG5_Vertex, np, mmg.MMG5_Tensor);
mmg3d.setTensorSols(h.met, tensors /* Float64Array 6*np */);
```

Without a metric, MMG computes one from the geometry and the `hausd` /
`hmin` / `hmax` / `hgrad` parameters. `setConstantSize(h.mesh, h.met)`
fills an isotropic metric with a constant size (`DPARAM_hsiz`).

## Running

```js
mmg3d.setDparameter(h.mesh, h.met, mmg3d.DPARAM_hausd, 0.01);
mmg3d.setDparameter(h.mesh, h.met, mmg3d.DPARAM_hgrad, 1.3);
const code = mmg3d.remesh(h.mesh, h.met);   // MMG3D_mmg3dlib
```

`remesh` returns `MMG5_SUCCESS` or `MMG5_LOWFAILURE` (usable-but-imperfect
result) and throws on `MMG5_STRONGFAILURE`.

Useful switches: `IPARAM_optim` (optimize keeping sizes), `IPARAM_noinsert`
/ `IPARAM_noswap` / `IPARAM_nomove` (freeze topology aspects),
`IPARAM_nosurf` (do not modify the surface), `IPARAM_angle` +
`DPARAM_angleDetection` (sharp-edge detection).

## Reading the result

```js
const { np, ne, nt } = mmg3d.getMeshSize(h.mesh);
const { vertices, refs, areCorners, areRequired } = mmg3d.getVertices(h.mesh, np);
const { tetra, refs: tetRefs } = mmg3d.getTetrahedra(h.mesh, ne);
const { tria } = mmg3d.getTriangles(h.mesh, nt);
mmg3d.free(h);
```

Bulk getters take the entity count as their last argument (MMG cannot size
JS arrays itself) and return typed arrays.

Quality/adjacency helpers: `getTetrahedronQuality(mesh, met, k)`,
`getAdjaTet(mesh, k)` (the 4 neighbours), `getTetFromTria` /
`getTetsFromTria` (tetra adjacent to a boundary triangle).

## Required entities

Freeze specific entities so the remesher preserves them:

```js
mmg3d.setRequiredVertex(h.mesh, i);
mmg3d.setRequiredTetrahedron(h.mesh, k);
mmg3d.setRequiredTriangle(h.mesh, t);
mmg3d.setRequiredTetrahedra(h.mesh, new Int32Array([...ks]), ks.length);
```
