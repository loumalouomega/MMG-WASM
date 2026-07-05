# 2D meshing (mmg2d)

`mmg2d` works on planar triangular meshes and has one extra trick: it can
**generate** a triangulation from a boundary alone.

## Adaptation of an existing mesh

```js
const h = mmg2d.init();
// np vertices, nt triangles, nquad quads, na edges
mmg2d.setMeshSize(h.mesh, 4, 2, 0, 4);
[[0,0],[1,0],[1,1],[0,1]].forEach(([x, y], i) =>
  mmg2d.setVertex(h.mesh, x, y, 0, i + 1));
mmg2d.setTriangle(h.mesh, 1, 2, 3, 1, 1);
mmg2d.setTriangle(h.mesh, 1, 3, 4, 1, 2);
[[1,2],[2,3],[3,4],[4,1]].forEach(([a, b], i) =>
  mmg2d.setEdge(h.mesh, a, b, 1, i + 1));

mmg2d.setDparameter(h.mesh, h.met, mmg2d.DPARAM_hmax, 0.2);
mmg2d.remesh(h.mesh, h.met);          // MMG2D_mmg2dlib

const { np, nt } = mmg2d.getMeshSize(h.mesh);
const { vertices } = mmg2d.getVertices(h.mesh, np);   // 2 doubles per vertex
const { tria } = mmg2d.getTriangles(h.mesh, nt);
mmg2d.free(h);
```

Note that 2D vertices have **2 coordinates**: `setVertex(mesh, x, y, ref,
pos)` and `getVertices` returns a `Float64Array` of length `2 * np`.

## Mesh generation from a boundary

Give only vertices and boundary edges (no triangles) and call `generate`:

```js
const h = mmg2d.init();
mmg2d.setMeshSize(h.mesh, 4, 0, 0, 4);        // nt = 0
[[0,0],[1,0],[1,1],[0,1]].forEach(([x, y], i) =>
  mmg2d.setVertex(h.mesh, x, y, 0, i + 1));
[[1,2],[2,3],[3,4],[4,1]].forEach(([a, b], i) =>
  mmg2d.setEdge(h.mesh, a, b, 1, i + 1));

mmg2d.setDparameter(h.mesh, h.met, mmg2d.DPARAM_hmax, 0.1);
mmg2d.generate(h.mesh, h.met);        // MMG2D_mmg2dmesh
```

The boundary must form closed loop(s); holes are supported (inner loops
oriented opposite to the outer one).

## Level-set and Lagrangian motion

`mmg2d.levelset(mesh, sol, met)` (`MMG2D_mmg2dls`) discretizes an implicit
curve, and `mmg2d.move(mesh, met, disp)` (`MMG2D_mmg2dmov`) follows a
displacement field — see [Level-set & Lagrangian motion](levelset.md); the
Lagrangian entry point requires the `USE_ELAS` build option and is **not
functional in mmg-wasm** (it fails at runtime, as it does in any MMG build
without the LinearElasticity library).

## 2D specifics

- `IPARAM_3dMedit`: read/write 2D meshes embedded in 3D Medit files.
- Quadrilaterals are supported as input/output data
  (`setQuadrilateral` / `getQuadrilaterals`).
- `getNumberOfNonBdyEdges` / `getNonBdyEdge` enumerate internal edges.
