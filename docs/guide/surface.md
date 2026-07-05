# Surface remeshing (mmgs)

`mmgs` remeshes triangulated surfaces embedded in 3D: quality improvement,
refinement to a size map, and geometric approximation control, while
preserving (or detecting) sharp features.

## Basic surface remesh

```js
const h = mmgs.init();
// np vertices, nt triangles, na edges
mmgs.setMeshSize(h.mesh, np, nt, 0);
mmgs.setVertices(h.mesh, coords /* Float64Array 3*np */, null);
mmgs.setTriangles(h.mesh, tria /* Int32Array 3*nt */, null);

mmgs.setDparameter(h.mesh, h.met, mmgs.DPARAM_hausd, 0.005);
mmgs.remesh(h.mesh, h.met);           // MMGS_mmgslib

const { np: npo, nt: nto } = mmgs.getMeshSize(h.mesh);
const out = mmgs.getVertices(h.mesh, npo);
mmgs.free(h);
```

Triangles must be consistently oriented (outward normals for a closed
surface).

## Feature preservation

- Ridge/sharp-edge detection is on by default; tune with
  `DPARAM_angleDetection` (degrees) or disable with `IPARAM_angle = 0`.
- Mark features explicitly: `setCorner(mesh, i)`, `setRidge(mesh, e)`,
  `setRequiredVertex/Triangle/Edge`.
- Prescribe normals at vertices with `setNormalAtVertex(mesh, i, nx, ny, nz)`
  (useful when the triangulation under-samples the true geometry).

## Size maps

Exactly as in [3D adaptation](adaptation-3d.md), on `h.met`: scalar sizes
(`MMG5_Scalar`) or anisotropic 3×3 tensors (`MMG5_Tensor`, 6 values per
vertex) via `setScalarSols` / `setTensorSols`.

## Level-sets on surfaces

`mmgs.levelset(mesh, sol, met)` (`MMGS_mmgsls`) discretizes the zero
isoline of a scalar field defined on the surface — see
[Level-set & Lagrangian motion](levelset.md). `mmgs` has no Lagrangian
motion entry point (and therefore `mmgs.init()` accepts only
`{ levelset }`, not `{ displacement }`).
