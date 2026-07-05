# API overview

## Naming rule

Every C function maps mechanically to a JS method on its module object:
strip the module prefix, split on `_`, camelCase the remainder.

| C symbol | JS call |
|----------|---------|
| `MMG3D_Set_vertex` | `mmg.mmg3d.setVertex(...)` |
| `MMG3D_Get_meshSize` | `mmg.mmg3d.getMeshSize(...)` |
| `MMG2D_Chk_meshData` | `mmg.mmg2d.chkMeshData(...)` |
| `MMGS_mmgslib` | `mmg.mmgs.mmgslib(...)` |

The nine remeshing entry points additionally get friendly aliases:

| Alias | mmg3d | mmg2d | mmgs |
|-------|-------|-------|------|
| `remesh` | `mmg3dlib` | `mmg2dlib` | `mmgslib` |
| `levelset` | `mmg3dls` | `mmg2dls` | `mmgsls` |
| `move` | `mmg3dmov` | `mmg2dmov` | — |
| `generate` | — | `mmg2dmesh` | — |

The variadic C initializers/finalizers (`MMG*_Init_mesh`, `MMG*_Free_all`,
`Free_structures`, `Free_names`) are exposed through fixed-arity shims as
`initMesh`/`freeAll`/`freeStructures`/`freeNames`, but you normally use the
higher-level `init()` / `free()` helpers instead.

## Error model and return codes

MMG has two return conventions, and the wrapper maps both to JS idioms:

| C convention | Functions | JS behaviour |
|--------------|-----------|--------------|
| `1` ok / `0` fail | `Set_*`, `Get_*`, `load*`, `save*`, `Chk_*`, ... | throws `Error` on failure, returns outputs (or `undefined`) |
| `MMG5_SUCCESS(0)` / `MMG5_LOWFAILURE(1)` / `MMG5_STRONGFAILURE(2)` | `remesh`, `levelset`, `move`, `generate` | returns the code; throws only on `MMG5_STRONGFAILURE` |
| raw value | `getTetrahedronQuality` (double), `addVertex` (new index), `getAdjaVertices` (count) | returned as-is |

`MMG5_LOWFAILURE` means "the remesher hit a problem but the mesh is
usable" — check for it explicitly if you need pristine results.

## Constants

- Root object: `MMG5_SUCCESS`, `MMG5_LOWFAILURE`, `MMG5_STRONGFAILURE`;
  solution types `MMG5_Scalar`/`MMG5_Vector`/`MMG5_Tensor`; entity kinds
  `MMG5_Vertex`/`MMG5_Triangle`/...; file formats `MMG5_FMT_*`.
- Each module: its parameter enum as `IPARAM_*` / `DPARAM_*` properties
  (values match the C `MMG3D_Param`/`MMG2D_Param`/`MMGS_Param` enums).

## Outputs

Functions with C out-pointers return an object keyed by the C parameter
names:

```js
const { np, ne, nprism, nt, nquad, na } = mmg3d.getMeshSize(h.mesh);
const { c0, c1, c2, ref, isCorner, isRequired } = mmg3d.getVertex(h.mesh);
```

Bulk getters need the entity count (from `getMeshSize`/`getSolSize`) as a
trailing argument and return typed arrays — see
[Marshalling](marshalling.md).

## What is not exposed

A handful of C functions are deliberately unbound (CLI plumbing, raw
`MMG5_Info` struct access, diagnostics with unbounded output buffers, and
three symbols declared upstream but never implemented). They are listed at
the bottom of the [reference](reference.md) with reasons.
