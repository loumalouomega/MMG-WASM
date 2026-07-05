# Level-set discretization & Lagrangian motion

## Level-set discretization

Given a scalar field φ at the vertices, the `levelset` entry points remesh
so the isosurface φ = 0 (adjustable via `DPARAM_ls`) becomes an explicit,
conforming internal boundary — the basis of implicit-domain meshing.

```js
const { mmg3d } = mmg;
const h = mmg3d.init({ levelset: true });   // adds h.ls

// build the mesh as usual (setMeshSize, setVertices, setTetrahedra, ...)

// φ values at the vertices, e.g. distance to the x = 0.75 plane
mmg3d.setSolSize(h.mesh, h.ls, mmg.MMG5_Vertex, np, mmg.MMG5_Scalar);
mmg3d.setScalarSols(h.ls, phi /* Float64Array np */);

mmg3d.setIparameter(h.mesh, h.ls, mmg3d.IPARAM_iso, 1);   // enable ls mode
const code = mmg3d.levelset(h.mesh, h.ls, null);          // MMG3D_mmg3dls
```

The third argument is an optional metric (`null` for none; pass `h.met`
after filling it to control sizes along the interface).

Options:

- `IPARAM_iso` — volume + surface discretization; `IPARAM_isosurf` —
  surfaces only (mmg3d).
- `DPARAM_ls` — the isovalue to extract (default 0).
- `IPARAM_isoref` — reference assigned to the created interface.
- `DPARAM_rmc` — remove small connected components of the negative domain.
- Multi-material domain assignment via `setMultiMat(mesh, sol, ref,
  split, rin, rex)` and `IPARAM_numberOfMat`.
- Base references that must not be merged: `setLsBaseReference` +
  `IPARAM_numberOfLSBaseReferences`.

`mmg2d.levelset` and `mmgs.levelset` work the same way on planar meshes and
surfaces.

## Lagrangian motion (not functional in WASM)

`mmg3d.move(mesh, met, disp)` / `mmg2d.move` (`MMG*_mmg*mov`) displace the
mesh according to a vector field in `h.disp` (from
`init({ displacement: true })`), remeshing as needed. Upstream MMG only
enables this when built against the **LinearElasticity** (`USE_ELAS`)
library, which is not part of the WASM build — calling `move` fails at
runtime with `IPARAM_lag` rejected. The bindings exist so the API surface
matches upstream; treat them as reserved.
