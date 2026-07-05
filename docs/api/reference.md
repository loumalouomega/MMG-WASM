# API reference

!!! note
    This page is generated from the MMG public headers (version **5.8.0**) by `scripts/gen_docs_api.py` and is regenerated in CI. Every function hides pointer handling and manual memory management; see [Marshalling](marshalling.md) for how arguments and return values are converted.

**348 functions** across 3 modules (`mmg3d`, `mmg2d`, `mmgs`).

Conventions:

- `MeshHandle` / `SolHandle` are the opaque handles returned by each module's `init()`.
- Functions with output parameters return an **object** keyed by the output names; bulk getters return typed arrays (`Float64Array` / `Int32Array`).
- `status` functions throw a JS `Error` on failure instead of returning 0.

## `mmg3d`

### `mmg3d.addTetrahedron`

```ts
mmg3d.addTetrahedron(mesh: MeshHandle, v0: number, v1: number, v2: number, v3: number, ref: number): void
```

Add a tetrahedron to the mesh. This function adds a tetrahedron with vertices \a v0, \a v1, \a v2, \a v3 and reference \a ref at the first available position of the mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `v0` | `number` |
| `v1` | `number` |
| `v2` | `number` |
| `v3` | `number` |
| `ref` | `number` |

<small>MMG C symbol: `MMG3D_Add_tetrahedron` — return: throws on failure</small>

### `mmg3d.addVertex`

```ts
mmg3d.addVertex(mesh: MeshHandle, c0: number, c1: number, c2: number, ref: number): number
```

Add a vertex to the mesh. This function adds a vertex with coordinates \a c0 \a c1 \a c2 and reference \a ref at the first available position of the mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `c0` | `number` |
| `c1` | `number` |
| `c2` | `number` |
| `ref` | `number` |

<small>MMG C symbol: `MMG3D_Add_vertex` — return: returns the raw integer value</small>

### `mmg3d.chkMeshData`

```ts
mmg3d.chkMeshData(mesh: MeshHandle, met: SolHandle): void
```

Check if the number of given entities match with mesh and sol size Check if the number of given entities match with mesh and sol size (not mandatory) and check mesh datas.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |

<small>MMG C symbol: `MMG3D_Chk_meshData` — return: throws on failure</small>

### `mmg3d.cleanIsoSurf`

```ts
mmg3d.cleanIsoSurf(mesh: MeshHandle): void
```

Clean data (triangles and edges) linked to isosurface.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |

<small>MMG C symbol: `MMG3D_Clean_isoSurf` — return: throws on failure</small>

### `mmg3d.computeEigenv`

```ts
mmg3d.computeEigenv(m: number[] | Float64Array): { value: number; lambda: Float64Array; vp: Float64Array }
```

Compute the real eigenvalues and eigenvectors of a symmetric matrix Compute the real eigenvalues and eigenvectors of a symmetric matrix m whose upper part is provided (m11, m12, m13, m22, m23, m33 in this order). lambda[0] is the eigenvalue associated to the eigenvector ( v[0][0], v[0,1], v[0,2] ) in C and to the eigenvector v(1,:) in fortran lambda[1] is the eigenvalue associated to the eigenvector ( v[1][0], v[1,1], v[1,2] ) in C and to the eigenvector v(2,:) in fortran lambda[2] is the eigenvalue associated to the eigenvector ( v[2][0], v[2,1], v[2,2] ) in C and to the eigenvector v(3,:) in fortran

| Parameter | Type |
|-----------|------|
| `m` | `number[] | Float64Array` |

<small>MMG C symbol: `MMG3D_Compute_eigenv` — return: returns the raw integer value</small>

### `mmg3d.defaultValues`

```ts
mmg3d.defaultValues(mesh: MeshHandle): void
```

Tools for the library */ /** Print the default parameters values.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |

<small>MMG C symbol: `MMG3D_defaultValues` — return: throws on failure</small>

### `mmg3d.freeAll`

```ts
mmg3d.freeAll(mesh: MeshHandle, met: SolHandle, ls: SolHandle | null, disp: SolHandle | null): void
```

Free all allocated structures (fixed-arity shim over the variadic MMG3D_Free_all).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |
| `ls` | `SolHandle | null` |
| `disp` | `SolHandle | null` |

<small>MMG C symbol: `mmgjs_MMG3D_Free_all` — return: throws on failure</small>

### `mmg3d.freeAllSols`

```ts
mmg3d.freeAllSols(mesh: MeshHandle, sol: SolHandle): void
```

Deallocate an array of solution fields

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |

<small>MMG C symbol: `MMG3D_Free_allSols` — return: throws on failure</small>

### `mmg3d.freeNames`

```ts
mmg3d.freeNames(mesh: MeshHandle, met: SolHandle, ls: SolHandle | null, disp: SolHandle | null): void
```

Free file-name strings (shim over MMG3D_Free_names).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |
| `ls` | `SolHandle | null` |
| `disp` | `SolHandle | null` |

<small>MMG C symbol: `mmgjs_MMG3D_Free_names` — return: throws on failure</small>

### `mmg3d.freeSolutions`

```ts
mmg3d.freeSolutions(mesh: MeshHandle, sol: SolHandle): void
```

Free the solution structure of a given mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |

<small>MMG C symbol: `MMG3D_Free_solutions` — return: no return value</small>

### `mmg3d.freeStructures`

```ts
mmg3d.freeStructures(mesh: MeshHandle, met: SolHandle, ls: SolHandle | null, disp: SolHandle | null): void
```

Free mesh/sol arrays but keep the structures (shim over MMG3D_Free_structures).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |
| `ls` | `SolHandle | null` |
| `disp` | `SolHandle | null` |

<small>MMG C symbol: `mmgjs_MMG3D_Free_structures` — return: throws on failure</small>

### `mmg3d.getAdjaTet`

```ts
mmg3d.getAdjaTet(mesh: MeshHandle, kel: number): { listet: Int32Array }
```

Utils */ /** Return adjacent elements of a tetrahedron. Find the indices of the 4 adjacent elements of tetrahedron \a kel. \f$listet[i] = 0\f$ if the \f$i^{th}\f$ face has no adjacent element (so we are on a boundary face).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `kel` | `number` |

<small>MMG C symbol: `MMG3D_Get_adjaTet` — return: throws on failure</small>

### `mmg3d.getByIdxVertex`

```ts
mmg3d.getByIdxVertex(mesh: MeshHandle, idx: number): { c0: number; c1: number; c2: number; ref: number; isCorner: number; isRequired: number }
```

Get the coordinates and reference of a specific vertex in the mesh. Get coordinates \a c0, \a c1, \a c2 and reference \a ref of vertex \a idx of mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `idx` | `number` |

<small>MMG C symbol: `MMG3D_GetByIdx_vertex` — return: throws on failure</small>

### `mmg3d.getEdge`

```ts
mmg3d.getEdge(mesh: MeshHandle): { e0: number; e1: number; ref: number; isRidge: number; isRequired: number }
```

Get the vertices and reference of the next edge in the mesh. This function retrieves the extremities \a e0, \a e1 and reference \a ref of next edge of \a mesh. It is meant to be called in a loop over all edges. When it has been called as many times as there are edges in the mesh, the internal edge counter will be reset.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |

<small>MMG C symbol: `MMG3D_Get_edge` — return: throws on failure</small>

### `mmg3d.getEdges`

```ts
mmg3d.getEdges(mesh: MeshHandle, na: number): { edges: Int32Array; refs: Int32Array; areRidges: Int32Array; areRequired: Int32Array }
```

Get the vertices and references of all edges in a mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `na` | `number (size of the output arrays)` |

<small>MMG C symbol: `MMG3D_Get_edges` — return: throws on failure</small>

### `mmg3d.getIparameter`

```ts
mmg3d.getIparameter(mesh: MeshHandle, iparam: number): void
```

Get the value of an integer parameter of the remesher. Get the value of integer parameter \a iparam.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `iparam` | `number` |

<small>MMG C symbol: `MMG3D_Get_iparameter` — return: throws on failure</small>

### `mmg3d.getIthSolInSolsAtVertices`

```ts
mmg3d.getIthSolInSolsAtVertices(sol: SolHandle, i: number, pos: number, n: number): { s: Float64Array }
```

Get one out of several solutions at a specific vertex. Get values of the ith field of the solution array at vertex \a pos. (pos from 1 to nb_vertices included and \a i from 1 to \a nb_sols). The type of solution is inferred from \a sol.

| Parameter | Type |
|-----------|------|
| `sol` | `SolHandle` |
| `i` | `number` |
| `pos` | `number` |
| `n` | `number (size of the output arrays)` |

<small>MMG C symbol: `MMG3D_Get_ithSol_inSolsAtVertices` — return: throws on failure</small>

### `mmg3d.getIthSolsInSolsAtVertices`

```ts
mmg3d.getIthSolsInSolsAtVertices(sol: SolHandle, i: number, n: number): { s: Float64Array }
```

Get one out of several solutions at all vertices in the mesh. This function retrieves the values of the solution at the ith field of the solution array (\a i from 1 to \a nb_sols).

| Parameter | Type |
|-----------|------|
| `sol` | `SolHandle` |
| `i` | `number` |
| `n` | `number (size of the output arrays)` |

<small>MMG C symbol: `MMG3D_Get_ithSols_inSolsAtVertices` — return: throws on failure</small>

### `mmg3d.getMeshSize`

```ts
mmg3d.getMeshSize(mesh: MeshHandle): { np: number; ne: number; nprism: number; nt: number; nquad: number; na: number }
```

recover data */ /** Get the number of vertices, tetrahedra, prisms, triangles, quadrilaterals and edges of the mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |

<small>MMG C symbol: `MMG3D_Get_meshSize` — return: throws on failure</small>

### `mmg3d.getNonBdyTriangle`

```ts
mmg3d.getNonBdyTriangle(mesh: MeshHandle, idx: number): { v0: number; v1: number; v2: number; ref: number }
```

Get vertices and reference of a non-boundary triangle. Get vertices and reference \a ref of the idx^th non-boundary triangle (for DG methods for example). A tria is boundary if it is located at the interface of 2 domains with different references or if it belongs to one tetra only.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `idx` | `number` |

<small>MMG C symbol: `MMG3D_Get_nonBdyTriangle` — return: throws on failure</small>

### `mmg3d.getNormalAtVertex`

```ts
mmg3d.getNormalAtVertex(mesh: MeshHandle, k: number): { n0: number; n1: number; n2: number }
```

Get the normal orientation at a single mesh vertex. This function retrieves the normal (n0,n1,n2) at vertex \a k.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMG3D_Get_normalAtVertex` — return: throws on failure</small>

### `mmg3d.getNumberOfNonBdyTriangles`

```ts
mmg3d.getNumberOfNonBdyTriangles(mesh: MeshHandle): { nb_tria: number }
```

Get the number of non-boundary triangles. Get the number of non-boundary triangles (for DG methods for example). A triangle is boundary if it is located at the interface of 2 domains with different references or if it belongs to one tetra only. Append these triangles to the list of triangles.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |

<small>MMG C symbol: `MMG3D_Get_numberOfNonBdyTriangles` — return: throws on failure</small>

### `mmg3d.getPrism`

```ts
mmg3d.getPrism(mesh: MeshHandle): { v0: number; v1: number; v2: number; v3: number; v4: number; v5: number; ref: number; isRequired: number }
```

Get the vertices and reference of the next prism in the mesh. This function retrieves the vertices \a v0, \a v1, \a v2, \a v3, \a v4, \a v5 and reference \a ref of the next prism of \a mesh. It is meant to be called in a loop over all prisms. When it has been called as many times as there are prisms, the internal loop counter will be reset.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |

<small>MMG C symbol: `MMG3D_Get_prism` — return: throws on failure</small>

### `mmg3d.getPrisms`

```ts
mmg3d.getPrisms(mesh: MeshHandle, nprism: number): { prisms: Int32Array; refs: Int32Array; areRequired: Int32Array }
```

Get the vertices and references of all prisms in the mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `nprism` | `number (size of the output arrays)` |

<small>MMG C symbol: `MMG3D_Get_prisms` — return: throws on failure</small>

### `mmg3d.getQuadrilateral`

```ts
mmg3d.getQuadrilateral(mesh: MeshHandle): { v0: number; v1: number; v2: number; v3: number; ref: number; isRequired: number }
```

Get the vertices and reference of the next quadrilateral of the mesh. Get the vertices \a v0,\a v1,\a v2,\a v3 and reference \a ref of the next quadrilateral of mesh. This function is meant to be called in a loop over all quadrilaterals. When it has been called as many times as there are quadrilaterals, the internal loop counter will be reset.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |

<small>MMG C symbol: `MMG3D_Get_quadrilateral` — return: throws on failure</small>

### `mmg3d.getQuadrilaterals`

```ts
mmg3d.getQuadrilaterals(mesh: MeshHandle, nquad: number): { quads: Int32Array; refs: Int32Array; areRequired: Int32Array }
```

Get the vertices and references of all quadrilaterals of the mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `nquad` | `number (size of the output arrays)` |

<small>MMG C symbol: `MMG3D_Get_quadrilaterals` — return: throws on failure</small>

### `mmg3d.getScalarSol`

```ts
mmg3d.getScalarSol(met: SolHandle): { s: number }
```

Get the next element of a scalar solution structure defined at vertices. This function retrieves the solution \a s of the next vertex of \a mesh. It is meant to be called in a loop over all vertices. When it has been called as many times as there are vertices in the mesh, the internal loop counter will be reset.

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |

<small>MMG C symbol: `MMG3D_Get_scalarSol` — return: throws on failure</small>

### `mmg3d.getScalarSols`

```ts
mmg3d.getScalarSols(met: SolHandle, np: number): { s: Float64Array }
```

Get all elements of a scalar solution structure defined at vertices.

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |
| `np` | `number (size of the output arrays)` |

<small>MMG C symbol: `MMG3D_Get_scalarSols` — return: throws on failure</small>

### `mmg3d.getSolSize`

```ts
mmg3d.getSolSize(mesh: MeshHandle, sol: SolHandle): { typEntity: number; np: number; typSol: number }
```

Get the number of elements, dimension, and type of a solution structure.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |

<small>MMG C symbol: `MMG3D_Get_solSize` — return: throws on failure</small>

### `mmg3d.getSolsAtVerticesSize`

```ts
mmg3d.getSolsAtVerticesSize(mesh: MeshHandle, sol: SolHandle): { nsols: number; nentities: number; typSol: Int32Array }
```

Get the number of elements, type, and dimensions of several solutions defined on vertices.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |

<small>MMG C symbol: `MMG3D_Get_solsAtVerticesSize` — return: throws on failure</small>

### `mmg3d.getTensorSol`

```ts
mmg3d.getTensorSol(met: SolHandle): { m11: number; m12: number; m13: number; m22: number; m23: number; m33: number }
```

Get the next element of a tensor solution structure. This function retrieves the next element \f$(m_{11},m_{12},m_{13},m_{22},m_{23},m_{33})\f$ of a tensor-valued solution field. It is meant to be called in a loop over all vertices. When it has been called as many times as there are elements in the solution, the internal loop counter will be reset.

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |

<small>MMG C symbol: `MMG3D_Get_tensorSol` — return: throws on failure</small>

### `mmg3d.getTensorSols`

```ts
mmg3d.getTensorSols(met: SolHandle, np: number): { sols: Float64Array }
```

Get all elements of a tensor solution field.

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |
| `np` | `number (size of the output arrays)` |

<small>MMG C symbol: `MMG3D_Get_tensorSols` — return: throws on failure</small>

### `mmg3d.getTetFromTria`

```ts
mmg3d.getTetFromTria(mesh: MeshHandle, ktri: number): { ktet: number; iface: number }
```

Get a tetrahedron given one of its triangles and the index by which it refers to this triangle (DEPRECATED). Fill \a ktet by the index of a tetrahedron to which belongs a boundary triangle and \a iface by the index of the triangle in the tetra.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `ktri` | `number` |

<small>MMG C symbol: `MMG3D_Get_tetFromTria` — return: throws on failure</small>

### `mmg3d.getTetrahedra`

```ts
mmg3d.getTetrahedra(mesh: MeshHandle, ne: number): { tetra: Int32Array; refs: Int32Array; areRequired: Int32Array }
```

Get the vertices and reference of all tetrahedra in the mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `ne` | `number (size of the output arrays)` |

<small>MMG C symbol: `MMG3D_Get_tetrahedra` — return: throws on failure</small>

### `mmg3d.getTetrahedron`

```ts
mmg3d.getTetrahedron(mesh: MeshHandle): { v0: number; v1: number; v2: number; v3: number; ref: number; isRequired: number }
```

Get the vertices and reference of the next tetrahedron in the mesh. This function retrieves the vertices \a v0, \a v1, \a v2, \a v3 and reference \a ref of the next tetrahedron of \a mesh. It is meant to be called in a loop over all tetrahedra. When it has been called as many times as there are tetrahedra, the internal loop counter will be reset.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |

<small>MMG C symbol: `MMG3D_Get_tetrahedron` — return: throws on failure</small>

### `mmg3d.getTetrahedronQuality`

```ts
mmg3d.getTetrahedronQuality(mesh: MeshHandle, met: SolHandle, k: number): number
```

Get the quality measure of a single tetrahedron in the mesh. This function returns the quality measure of tetrahedron \a k. Quality values range from 0 (degenerate) to 1 (best attainable). The function returns 0 if the tetrahedron is flat or has a negative volume, and also if \a k is out of range. In the latter case it will also print a diagnostic message to standard output.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMG3D_Get_tetrahedronQuality` — return: returns the raw double value</small>

### `mmg3d.getTetsFromTria`

```ts
mmg3d.getTetsFromTria(mesh: MeshHandle, ktri: number): { ktet: Int32Array; iface: Int32Array }
```

Get two tetrahedra given a triangle and face indices. Fill \a ktet by the indices of the tetrahedra that have a boundary triangle and \a iface by the indices of the faces of the tetras that correspond to the triangle. Fill ktet[1] and iface[1] by 0 if the triangle belongs to 1 tetrahedron only.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `ktri` | `number` |

<small>MMG C symbol: `MMG3D_Get_tetsFromTria` — return: throws on failure</small>

### `mmg3d.getTriangle`

```ts
mmg3d.getTriangle(mesh: MeshHandle): { v0: number; v1: number; v2: number; ref: number; isRequired: number }
```

Get the vertices and reference of the next triangle in the mesh. This function retrieves the vertices \a v0, \a v1, \a v2, and reference \a ref of the next triangle of \a mesh. It is meant to be called in a loop over all triangles. When it has been called as many times as there are triangles, the internal loop counter will be reset.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |

<small>MMG C symbol: `MMG3D_Get_triangle` — return: throws on failure</small>

### `mmg3d.getTriangles`

```ts
mmg3d.getTriangles(mesh: MeshHandle, nt: number): { tria: Int32Array; refs: Int32Array; areRequired: Int32Array }
```

Get the vertices and references of all triangles in the mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `nt` | `number (size of the output arrays)` |

<small>MMG C symbol: `MMG3D_Get_triangles` — return: throws on failure</small>

### `mmg3d.getVectorSol`

```ts
mmg3d.getVectorSol(met: SolHandle): { vx: number; vy: number; vz: number }
```

Get the next element of a vector solution structure. This function retrieves the next vector-valued element \f$(v_x,v_y,vz)\f$ of the solution. It is meant to be called in a loop over all elements. When it has been called as many times as there are elements in the solution, the internal loop counter will be reset.

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |

<small>MMG C symbol: `MMG3D_Get_vectorSol` — return: throws on failure</small>

### `mmg3d.getVectorSols`

```ts
mmg3d.getVectorSols(met: SolHandle, np: number): { sols: Float64Array }
```

Get all elements of a vector solution structure. Get vectorial solutions at mesh vertices

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |
| `np` | `number (size of the output arrays)` |

<small>MMG C symbol: `MMG3D_Get_vectorSols` — return: throws on failure</small>

### `mmg3d.getVertex`

```ts
mmg3d.getVertex(mesh: MeshHandle): { c0: number; c1: number; c2: number; ref: number; isCorner: number; isRequired: number }
```

Get the coordinates \a c0, \a c1,\a c2 and reference \a ref of the next vertex of \a mesh. This function retrieves the coordinates \a c0, \a c1,\a c2 and reference \a ref of the next vertex of a mesh. It is meant to be used in a loop over all vertices. When this function has been called as many times as there are vertices, the internal loop counter will be reset. To obtain data for a specific vertex, the \ref MMG3D_GetByIdx_vertex function can be used instead.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |

<small>MMG C symbol: `MMG3D_Get_vertex` — return: throws on failure</small>

### `mmg3d.getVertices`

```ts
mmg3d.getVertices(mesh: MeshHandle, np: number): { vertices: Float64Array; refs: Int32Array; areCorners: Int32Array; areRequired: Int32Array }
```

Get the coordinates and references of all vertices in the mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `np` | `number (size of the output arrays)` |

<small>MMG C symbol: `MMG3D_Get_vertices` — return: throws on failure</small>

### `mmg3d.hashTetra`

```ts
mmg3d.hashTetra(mesh: MeshHandle, pack: number): void
```

Compute the length of an edge according to the size prescription. Compute the length of edge \f$[ca,cb]\f$ (with \a ca and \a cb coordinates of edge endpoints) according to the size prescription. / LIBMMG3D_EXPORT extern double (*MMG3D_lenedgCoor)(double *ca,double *cb,double *sa,double *sb); /** Create array of adjacency. Create array of adjacency. Set pack variable to 0 for a compact mesh and to 1 for a mesh that need to be packed.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `pack` | `number` |

<small>MMG C symbol: `MMG3D_hashTetra` — return: throws on failure</small>

### `mmg3d.initFileNames`

```ts
mmg3d.initFileNames(mesh: MeshHandle, sol: SolHandle): void
```

Initialize file names to their default values. This function initializes all file names to their default values.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |

<small>MMG C symbol: `MMG3D_Init_fileNames` — return: no return value</small>

### `mmg3d.initMesh`

```ts
mmg3d.initMesh(mesh: MeshHandle, met: SolHandle, ls: SolHandle | null, disp: SolHandle | null): void
```

Allocate and initialize the mesh and solution structures (fixed-arity shim over the variadic MMG3D_Init_mesh).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |
| `ls` | `SolHandle | null` |
| `disp` | `SolHandle | null` |

<small>MMG C symbol: `mmgjs_MMG3D_Init_mesh` — return: throws on failure</small>

### `mmg3d.initParameters`

```ts
mmg3d.initParameters(mesh: MeshHandle): void
```

Initialize parameters to their default values Initialization of the input parameters (stored in the Info structure).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |

<small>MMG C symbol: `MMG3D_Init_parameters` — return: no return value</small>

### `mmg3d.loadAllSols`

```ts
mmg3d.loadAllSols(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Load one or more solutions in a solution file in medit file format.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG3D_loadAllSols` — return: throws on failure</small>

### `mmg3d.loadGenericMesh`

```ts
mmg3d.loadGenericMesh(mesh: MeshHandle, met: SolHandle, sol: SolHandle, filename: string): void
```

Read mesh data in a format determined by the filename extension.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG3D_loadGenericMesh` — return: throws on failure</small>

### `mmg3d.loadMesh`

```ts
mmg3d.loadMesh(mesh: MeshHandle, filename: string): void
```

Load a mesh (in .mesh/.mesb format) from file. Read mesh data.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG3D_loadMesh` — return: throws on failure</small>

### `mmg3d.loadMshMesh`

```ts
mmg3d.loadMshMesh(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Load a mesh and possibly a solution in .msh format from file. This function reads a mesh and 0 or 1 data fields in MSH file format (.msh extension). We read only low-order vertices, edges, triangles, quadrangles, tetrahedra and prisms.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG3D_loadMshMesh` — return: throws on failure</small>

### `mmg3d.loadMshMeshAndAllData`

```ts
mmg3d.loadMshMeshAndAllData(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Load a mesh and all data from a file in MSH format. Read mesh and a list of data in MSH file format (.msh extension). We read only low-order vertices, edges, tria, quadra, tetra and prisms.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG3D_loadMshMesh_and_allData` — return: throws on failure</small>

### `mmg3d.loadSol`

```ts
mmg3d.loadSol(mesh: MeshHandle, met: SolHandle, filename: string): void
```

Load a metric field (or other solution). Load metric field. The solution file must contains only 1 solution: the metric

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG3D_loadSol` — return: throws on failure</small>

### `mmg3d.loadVtkMesh`

```ts
mmg3d.loadVtkMesh(mesh: MeshHandle, met: SolHandle, sol: SolHandle, filename: string): void
```

Load a mesh and possibly a solution from a file in VTK format. This function reads a mesh and 0 or 1 data fields in VTK file format (.vtu extension). We read only low-order vertices, edges, tria, quadra, tetra and prisms. Point and cell references must be stored in PointData or CellData whose names contain the "medit:ref" keyword.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG3D_loadVtkMesh` — return: throws on failure</small>

### `mmg3d.loadVtkMeshAndAllData`

```ts
mmg3d.loadVtkMeshAndAllData(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Load a mesh and multiple solutions from a file in VTK format. Read mesh and a list of data in VTK file format (.vtu extension). We read only low-order vertices, edges, tria, quadra, tetra and prisms. Point and cell references must be stored in PointData or CellData whose names contains the "medit:ref" keyword.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG3D_loadVtkMesh_and_allData` — return: throws on failure</small>

### `mmg3d.loadVtuMesh`

```ts
mmg3d.loadVtuMesh(mesh: MeshHandle, met: SolHandle, sol: SolHandle, filename: string): void
```

Load a mesh and possibly a solution in VTU (VTK) format from file. This function reads a mesh and 0 or 1 data field in VTU (VTK) file format (.vtu extension). We read only low-order vertices, edges, tria, quadra, tetra and prisms. Point and cell references must be stored in PointData or CellData whose names contain the "medit:ref" keyword.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG3D_loadVtuMesh` — return: throws on failure</small>

### `mmg3d.loadVtuMeshAndAllData`

```ts
mmg3d.loadVtuMeshAndAllData(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Load a mesh and multiple solutions in VTU (VTK) format from file. This functionreads a mesh and a list of data in VTU file format (.vtu extension). We read only low-order vertices, edges, tria, quadra, tetra and prisms. Point and cell references must be stored in PointData or CellData whose names contains the "medit:ref" keyword.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG3D_loadVtuMesh_and_allData` — return: throws on failure</small>

### `mmg3d.mmg3dlib`

```ts
mmg3d.mmg3dlib(mesh: MeshHandle, met: SolHandle): number
```

Main "program" for the mesh adaptation library.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |

<small>MMG C symbol: `MMG3D_mmg3dlib` — return: returns `MMG5_SUCCESS`/`MMG5_LOWFAILURE`; throws on `MMG5_STRONGFAILURE` — alias: `mmg3d.remesh()`</small>

### `mmg3d.mmg3dls`

```ts
mmg3d.mmg3dls(mesh: MeshHandle, sol: SolHandle, met: SolHandle): number
```

Main "program" for the level-set discretization library. Main program for the level-set discretization library. If a metric \a met is provided, use it to adapt the mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `met` | `SolHandle` |

<small>MMG C symbol: `MMG3D_mmg3dls` — return: returns `MMG5_SUCCESS`/`MMG5_LOWFAILURE`; throws on `MMG5_STRONGFAILURE` — alias: `mmg3d.levelset()`</small>

### `mmg3d.mmg3dmov`

```ts
mmg3d.mmg3dmov(mesh: MeshHandle, met: SolHandle, disp: SolHandle): number
```

Main program for the rigid-body movement library.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |
| `disp` | `SolHandle` |

<small>MMG C symbol: `MMG3D_mmg3dmov` — return: returns `MMG5_SUCCESS`/`MMG5_LOWFAILURE`; throws on `MMG5_STRONGFAILURE` — alias: `mmg3d.move()`</small>

### `mmg3d.saveAllSols`

```ts
mmg3d.saveAllSols(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Save 1 or more solutions in medit solution file format

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG3D_saveAllSols` — return: throws on failure</small>

### `mmg3d.saveGenericMesh`

```ts
mmg3d.saveGenericMesh(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Save mesh data in a file whose format depends on the filename extension.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG3D_saveGenericMesh` — return: throws on failure</small>

### `mmg3d.saveMesh`

```ts
mmg3d.saveMesh(mesh: MeshHandle, filename: string): void
```

Save a mesh in .mesh/.meshb format.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG3D_saveMesh` — return: throws on failure</small>

### `mmg3d.saveMshMesh`

```ts
mmg3d.saveMshMesh(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Save a mesh in MSH format, ascii or binary depending on the filename extension. Write mesh and 0 or 1 data in MSH file format (.msh extension). Write binary file for .mshb extension and ASCII for .msh one.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG3D_saveMshMesh` — return: throws on failure</small>

### `mmg3d.saveMshMeshAndAllData`

```ts
mmg3d.saveMshMeshAndAllData(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Save a mesh and data in MSH format, ascii or binary depending on the filename extension. Write mesh and a list of data fields (that are considered as solutions and not metrics, thus, we do nothing over the ridge vertices) in MSH file format (.msh extension). Save file in ASCII format for .msh extension, in binary format for .mshb one.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG3D_saveMshMesh_and_allData` — return: throws on failure</small>

### `mmg3d.saveSol`

```ts
mmg3d.saveSol(mesh: MeshHandle, met: SolHandle, filename: string): void
```

Write isotropic or anisotropic metric.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG3D_saveSol` — return: throws on failure</small>

### `mmg3d.saveTetgenMesh`

```ts
mmg3d.saveTetgenMesh(arg0: MeshHandle, arg1: string): void
```

Save data in Tetgen's Triangle format. Save mesh data in Triangle (or equivalent to Tetgen in 3D) file format.

| Parameter | Type |
|-----------|------|
| `arg0` | `MeshHandle` |
| `arg1` | `string` |

<small>MMG C symbol: `MMG3D_saveTetgenMesh` — return: throws on failure</small>

### `mmg3d.saveVtkMesh`

```ts
mmg3d.saveVtkMesh(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Save a mesh and optionally one solution in VTK format. Write mesh and 0 or 1 data in Vtk file format (.vtk extension).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG3D_saveVtkMesh` — return: throws on failure</small>

### `mmg3d.saveVtkMeshAndAllData`

```ts
mmg3d.saveVtkMeshAndAllData(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Save a mesh and multiple data fields in VTK format. Write mesh and a list of data fields in Vtk file format (.vtk extension).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG3D_saveVtkMesh_and_allData` — return: throws on failure</small>

### `mmg3d.saveVtuMesh`

```ts
mmg3d.saveVtuMesh(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Save a mesh and optionally one data field in VTU format. Write mesh and 0 or 1 data in vtu Vtk file format (.vtu extension).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG3D_saveVtuMesh` — return: throws on failure</small>

### `mmg3d.saveVtuMeshAndAllData`

```ts
mmg3d.saveVtuMeshAndAllData(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Save a mesh and multiple data fields in VTU format. Write mesh and a list of data fields in vtu Vtk file format (.vtu extension).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG3D_saveVtuMesh_and_allData` — return: throws on failure</small>

### `mmg3d.setCommonFunc`

```ts
mmg3d.setCommonFunc(): void
```

Set common pointer functions between mmgs and mmg3d to the matching mmg3d functions.

<small>MMG C symbol: `MMG3D_Set_commonFunc` — return: no return value</small>

### `mmg3d.setConstantSize`

```ts
mmg3d.setConstantSize(mesh: MeshHandle, met: SolHandle): void
```

Compute isotropic size map according to the mean of the length of the edges passing through a vertex. / LIBMMG3D_EXPORT extern int (*MMG3D_doSol)(MMG5_pMesh mesh,MMG5_pSol met); /** Compute a constant size map according to the hsiz, hmin and hmax parameters. This function computes a constant size map according to mesh->info.hsiz, mesh->info.hmin and mesh->info.hmax. It updates these 3 values if not compatible.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |

<small>MMG C symbol: `MMG3D_Set_constantSize` — return: throws on failure</small>

### `mmg3d.setCorner`

```ts
mmg3d.setCorner(mesh: MeshHandle, k: number): void
```

Assign the "corner" attribute to a vertex. Set the "corner" attribute at vertex \a k. This affects how the vertex is treated during remeshing.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMG3D_Set_corner` — return: throws on failure</small>

### `mmg3d.setDparameter`

```ts
mmg3d.setDparameter(mesh: MeshHandle, sol: SolHandle, dparam: number, val: number): void
```

set a real-valued parameter of the remesher This function sets the double parameter \a dparam to value \a val.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `dparam` | `number` |
| `val` | `number` |

<small>MMG C symbol: `MMG3D_Set_dparameter` — return: throws on failure</small>

### `mmg3d.setEdge`

```ts
mmg3d.setEdge(mesh: MeshHandle, v0: number, v1: number, ref: number, pos: number): void
```

Set the vertices and reference of a single edge in a mesh. Set edges of extremities \a v0, \a v1 and reference \a ref at position \a pos in mesh structure (from 1 to nb_edges included)

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `v0` | `number` |
| `v1` | `number` |
| `ref` | `number` |
| `pos` | `number` |

<small>MMG C symbol: `MMG3D_Set_edge` — return: throws on failure</small>

### `mmg3d.setEdges`

```ts
mmg3d.setEdges(mesh: MeshHandle, edges: number[] | Int32Array, refs: number[] | Int32Array | null): void
```

Set the vertices and references of all edges in a mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `edges` | `number[] | Int32Array` |
| `refs` | `number[] | Int32Array | null` |

<small>MMG C symbol: `MMG3D_Set_edges` — return: throws on failure</small>

### `mmg3d.setHandGivenMesh`

```ts
mmg3d.setHandGivenMesh(mesh: MeshHandle): void
```

Finish providing mesh data without using the API functions. To mark as ended a mesh given without using the API functions (for example, mesh given by mesh->point[i] = 0 ...). This function performs verifications, e.g. to make sure that all tetrahedra are consistently oriented.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |

<small>MMG C symbol: `MMG3D_Set_handGivenMesh` — return: no return value</small>

### `mmg3d.setInputMeshName`

```ts
mmg3d.setInputMeshName(mesh: MeshHandle, meshin: string): void
```

Set the name of input mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `meshin` | `string` |

<small>MMG C symbol: `MMG3D_Set_inputMeshName` — return: throws on failure</small>

### `mmg3d.setInputParamName`

```ts
mmg3d.setInputParamName(mesh: MeshHandle, fparamin: string): void
```

Set the name of the input parameter file.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `fparamin` | `string` |

<small>MMG C symbol: `MMG3D_Set_inputParamName` — return: throws on failure</small>

### `mmg3d.setInputSolName`

```ts
mmg3d.setInputSolName(mesh: MeshHandle, sol: SolHandle, solin: string): void
```

Set the name of input solution file.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `solin` | `string` |

<small>MMG C symbol: `MMG3D_Set_inputSolName` — return: throws on failure</small>

### `mmg3d.setIparameter`

```ts
mmg3d.setIparameter(mesh: MeshHandle, sol: SolHandle, iparam: number, val: number): void
```

set an integer parameter of the remesher This function sets the integer parameter \a iparam to value \a val.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `iparam` | `number` |
| `val` | `number` |

<small>MMG C symbol: `MMG3D_Set_iparameter` — return: throws on failure</small>

### `mmg3d.setIthSolInSolsAtVertices`

```ts
mmg3d.setIthSolInSolsAtVertices(sol: SolHandle, i: number, s: number[] | Float64Array, pos: number): void
```

Set a single element of one out of multiple solution fields that are defined on vertices. Set values of the solution at the ith field of the solution array and at position \a pos (\a pos from 1 to \a nb_vertices included and \a i from 1 to \a nb_sols).

| Parameter | Type |
|-----------|------|
| `sol` | `SolHandle` |
| `i` | `number` |
| `s` | `number[] | Float64Array` |
| `pos` | `number` |

<small>MMG C symbol: `MMG3D_Set_ithSol_inSolsAtVertices` — return: throws on failure</small>

### `mmg3d.setIthSolsInSolsAtVertices`

```ts
mmg3d.setIthSolsInSolsAtVertices(sol: SolHandle, i: number, s: number[] | Float64Array): void
```

Set all elements of one out of multiple solution fields that are defined on vertices. Set values of the ith field of the solution array by array (\a i from 1 to \a nb_sols).

| Parameter | Type |
|-----------|------|
| `sol` | `SolHandle` |
| `i` | `number` |
| `s` | `number[] | Float64Array` |

<small>MMG C symbol: `MMG3D_Set_ithSols_inSolsAtVertices` — return: throws on failure</small>

### `mmg3d.setLocalParameter`

```ts
mmg3d.setLocalParameter(mesh: MeshHandle, sol: SolHandle, typ: number, ref: number, hmin: number, hmax: number, hausd: number): void
```

set a local parameter Set local parameters: set the Hausdorff distance, minimum edge length, and maximum edge length for all entities of type \a typ and reference \a ref.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `typ` | `number` |
| `ref` | `number` |
| `hmin` | `number` |
| `hmax` | `number` |
| `hausd` | `number` |

<small>MMG C symbol: `MMG3D_Set_localParameter` — return: throws on failure</small>

### `mmg3d.setLsBaseReference`

```ts
mmg3d.setLsBaseReference(mesh: MeshHandle, sol: SolHandle, br: number): void
```

Set a new level-set base reference. Set a new level-set base reference of ref \a br in LS discretization mode. Base references are boundary conditions to which implicit domains can be attached. All implicit volumes that are not attached to listed base references are deleted as spurious volumes by the \a rmc option.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `br` | `number` |

<small>MMG C symbol: `MMG3D_Set_lsBaseReference` — return: throws on failure</small>

### `mmg3d.setMeshSize`

```ts
mmg3d.setMeshSize(mesh: MeshHandle, np: number, ne: number, nprism: number, nt: number, nquad: number, na: number): void
```

Set the number of vertices, tetrahedra, prisms, triangles, quadrilaterals, and edges of a mesh. This function sets the number of vertices, tetrahedra, prisms, triangles, quadrilaterals and edges of the mesh and allocates the associated arrays. If called again, it will reset the whole mesh to reallocate it at the new size

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `np` | `number` |
| `ne` | `number` |
| `nprism` | `number` |
| `nt` | `number` |
| `nquad` | `number` |
| `na` | `number` |

<small>MMG C symbol: `MMG3D_Set_meshSize` — return: throws on failure</small>

### `mmg3d.setMultiMat`

```ts
mmg3d.setMultiMat(mesh: MeshHandle, sol: SolHandle, ref: number, split: number, rmin: number, rplus: number): void
```

Set the reference mapping for the elements of reference \a ref in level-set discretization mode. With this function you can determine which references will be given to the tetrahedra on both sides of the level set, after discretization. Negative and positive here refer to volumes where the function is smaller or larger, respectively, than the isovalue of the level set.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `ref` | `number` |
| `split` | `number` |
| `rmin` | `number` |
| `rplus` | `number` |

<small>MMG C symbol: `MMG3D_Set_multiMat` — return: throws on failure</small>

### `mmg3d.setNormalAtVertex`

```ts
mmg3d.setNormalAtVertex(mesh: MeshHandle, k: number, n0: number, n1: number, n2: number): void
```

Set the normal orientation at a single vertex. Set normal (n0,n1,n2) at vertex \a k.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |
| `n0` | `number` |
| `n1` | `number` |
| `n2` | `number` |

<small>MMG C symbol: `MMG3D_Set_normalAtVertex` — return: throws on failure</small>

### `mmg3d.setOutputMeshName`

```ts
mmg3d.setOutputMeshName(mesh: MeshHandle, meshout: string): void
```

Set the name of output mesh file.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `meshout` | `string` |

<small>MMG C symbol: `MMG3D_Set_outputMeshName` — return: throws on failure</small>

### `mmg3d.setOutputSolName`

```ts
mmg3d.setOutputSolName(mesh: MeshHandle, sol: SolHandle, solout: string): void
```

Set the name of the output solution file.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `solout` | `string` |

<small>MMG C symbol: `MMG3D_Set_outputSolName` — return: throws on failure</small>

### `mmg3d.setParallelTriangle`

```ts
mmg3d.setParallelTriangle(mesh: MeshHandle, k: number): void
```

Assign the "parallel" attribute to a single triangle. Set triangle \a k as parallel (triangle at the interface between two processors, ie, this triangle is required). (\a k from 1 to nb_tria included).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMG3D_Set_parallelTriangle` — return: throws on failure</small>

### `mmg3d.setParallelTriangles`

```ts
mmg3d.setParallelTriangles(mesh: MeshHandle, parIdx: number[] | Int32Array, npar: number): void
```

Assign the "parallel" attribute to multiple triangles. Set the parallel triangles (triangles at the interface between processors, i.e. these triangles are required).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `parIdx` | `number[] | Int32Array` |
| `npar` | `number` |

<small>MMG C symbol: `MMG3D_Set_parallelTriangles` — return: throws on failure</small>

### `mmg3d.setPrism`

```ts
mmg3d.setPrism(mesh: MeshHandle, v0: number, v1: number, v2: number, v3: number, v4: number, v5: number, ref: number, pos: number): void
```

Set the vertices and reference of a single prism in a mesh. This function sets the six vertices \a v0, \a v1,\a v2,\a v3,\a v4,\a v5 and reference \a ref for the prism at position \a pos in the mesh structure (from 1 to nb_prisms included).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `v0` | `number` |
| `v1` | `number` |
| `v2` | `number` |
| `v3` | `number` |
| `v4` | `number` |
| `v5` | `number` |
| `ref` | `number` |
| `pos` | `number` |

<small>MMG C symbol: `MMG3D_Set_prism` — return: throws on failure</small>

### `mmg3d.setPrisms`

```ts
mmg3d.setPrisms(mesh: MeshHandle, prisms: number[] | Int32Array, refs: number[] | Int32Array | null): void
```

Set the vertices and references of all prisms in a mesh. This function sets the vertices and references of all prisms in a mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `prisms` | `number[] | Int32Array` |
| `refs` | `number[] | Int32Array | null` |

<small>MMG C symbol: `MMG3D_Set_prisms` — return: throws on failure</small>

### `mmg3d.setQuadrilateral`

```ts
mmg3d.setQuadrilateral(mesh: MeshHandle, v0: number, v1: number, v2: number, v3: number, ref: number, pos: number): void
```

Set the vertices and reference of a single quadrilateral in a mesh. Set a quadrilateral of vertices \a v0, \a v1, \a v2, \a v3 and reference \a ref at position \a pos in mesh structure (from 1 to nb_quadrangles included).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `v0` | `number` |
| `v1` | `number` |
| `v2` | `number` |
| `v3` | `number` |
| `ref` | `number` |
| `pos` | `number` |

<small>MMG C symbol: `MMG3D_Set_quadrilateral` — return: throws on failure</small>

### `mmg3d.setQuadrilaterals`

```ts
mmg3d.setQuadrilaterals(mesh: MeshHandle, quads: number[] | Int32Array, refs: number[] | Int32Array | null): void
```

Set the vertices and references of all quadrilaterals in a mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `quads` | `number[] | Int32Array` |
| `refs` | `number[] | Int32Array | null` |

<small>MMG C symbol: `MMG3D_Set_quadrilaterals` — return: throws on failure</small>

### `mmg3d.setRequiredEdge`

```ts
mmg3d.setRequiredEdge(mesh: MeshHandle, k: number): void
```

Assign the "required" attribute to a single edge. Set edge \a k as required.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMG3D_Set_requiredEdge` — return: throws on failure</small>

### `mmg3d.setRequiredTetrahedra`

```ts
mmg3d.setRequiredTetrahedra(mesh: MeshHandle, reqIdx: number[] | Int32Array, nreq: number): void
```

Assign the "required" attribute to multiple tetrahedra. Determine which tetrahedra have the "required" attribute.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `reqIdx` | `number[] | Int32Array` |
| `nreq` | `number` |

<small>MMG C symbol: `MMG3D_Set_requiredTetrahedra` — return: throws on failure</small>

### `mmg3d.setRequiredTetrahedron`

```ts
mmg3d.setRequiredTetrahedron(mesh: MeshHandle, k: number): void
```

Assign the "required" attribute to a tetrahedron. Set element \a k as required (\a k from 1 to nb_tetra included).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMG3D_Set_requiredTetrahedron` — return: throws on failure</small>

### `mmg3d.setRequiredTriangle`

```ts
mmg3d.setRequiredTriangle(mesh: MeshHandle, k: number): void
```

Assign the "required" attribute to a single triangle. Set triangle \a k as required (\a k from 1 to nb_tria included).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMG3D_Set_requiredTriangle` — return: throws on failure</small>

### `mmg3d.setRequiredTriangles`

```ts
mmg3d.setRequiredTriangles(mesh: MeshHandle, reqIdx: number[] | Int32Array, nreq: number): void
```

Assign the "required" attribute to multiple triangles.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `reqIdx` | `number[] | Int32Array` |
| `nreq` | `number` |

<small>MMG C symbol: `MMG3D_Set_requiredTriangles` — return: throws on failure</small>

### `mmg3d.setRequiredVertex`

```ts
mmg3d.setRequiredVertex(mesh: MeshHandle, k: number): void
```

Assign the "required" attribute to a vertex. Set vertex \a k as required (\a k from 1 to nb_vertices included). This prevents the remesher from moving the vertex.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMG3D_Set_requiredVertex` — return: throws on failure</small>

### `mmg3d.setRidge`

```ts
mmg3d.setRidge(mesh: MeshHandle, k: number): void
```

Assign the "ridge" attribute to a single edge. Set the "ridge" attribute at edge \a k. This affects how the remesher treats the edge and the adjacent triangles or tetrahedra.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMG3D_Set_ridge` — return: throws on failure</small>

### `mmg3d.setScalarSol`

```ts
mmg3d.setScalarSol(met: SolHandle, s: number, pos: number): void
```

Set a single element of a scalar solution structure. Set scalar value \a s at position \a pos in solution structure (pos from 1 to nb_vertices included).

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |
| `s` | `number` |
| `pos` | `number` |

<small>MMG C symbol: `MMG3D_Set_scalarSol` — return: throws on failure</small>

### `mmg3d.setScalarSols`

```ts
mmg3d.setScalarSols(met: SolHandle, s: number[] | Float64Array): void
```

Set the values of all elements of a scalar solution structure. Set scalar solutions at mesh vertices.

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |
| `s` | `number[] | Float64Array` |

<small>MMG C symbol: `MMG3D_Set_scalarSols` — return: throws on failure</small>

### `mmg3d.setSolSize`

```ts
mmg3d.setSolSize(mesh: MeshHandle, sol: SolHandle, typEntity: number, np: number, typSol: number): void
```

Initialize a solution field. Initialize a solution field: set dimension, types and number of data. To use to initialize a metric, a level-set or a displacement field.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `typEntity` | `number` |
| `np` | `number` |
| `typSol` | `number` |

<small>MMG C symbol: `MMG3D_Set_solSize` — return: throws on failure</small>

### `mmg3d.setSolsAtVerticesSize`

```ts
mmg3d.setSolsAtVerticesSize(mesh: MeshHandle, sol: SolHandle, nsols: number, nentities: number, typSol: number[] | Int32Array): void
```

Initialize an array of solution values defined at vertices Initialize a solution field defined at vertices: set dimension, types and number of data values. (not used by Mmg itself).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `nsols` | `number` |
| `nentities` | `number` |
| `typSol` | `number[] | Int32Array` |

<small>MMG C symbol: `MMG3D_Set_solsAtVerticesSize` — return: throws on failure</small>

### `mmg3d.setTensorSol`

```ts
mmg3d.setTensorSol(met: SolHandle, m11: number, m12: number, m13: number, m22: number, m23: number, m33: number, pos: number): void
```

Set a single element of a tensor solution structure. Set tensorial values at position \a pos in solution structure. (pos from 1 to nb_vertices included).

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |
| `m11` | `number` |
| `m12` | `number` |
| `m13` | `number` |
| `m22` | `number` |
| `m23` | `number` |
| `m33` | `number` |
| `pos` | `number` |

<small>MMG C symbol: `MMG3D_Set_tensorSol` — return: throws on failure</small>

### `mmg3d.setTensorSols`

```ts
mmg3d.setTensorSols(met: SolHandle, sols: number[] | Float64Array): void
```

Set all elements of a tensor solution structure. Set tensorial values by array.

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |
| `sols` | `number[] | Float64Array` |

<small>MMG C symbol: `MMG3D_Set_tensorSols` — return: throws on failure</small>

### `mmg3d.setTetrahedra`

```ts
mmg3d.setTetrahedra(mesh: MeshHandle, tetra: number[] | Int32Array, refs: number[] | Int32Array | null): void
```

Set the vertices and references of all tetrahedra in a mesh structure This function sets the vertices and references of all tetrahedra in a mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `tetra` | `number[] | Int32Array` |
| `refs` | `number[] | Int32Array | null` |

<small>MMG C symbol: `MMG3D_Set_tetrahedra` — return: throws on failure</small>

### `mmg3d.setTetrahedron`

```ts
mmg3d.setTetrahedron(mesh: MeshHandle, v0: number, v1: number, v2: number, v3: number, ref: number, pos: number): void
```

set a single tetrahedron's vertices Assign the vertices \a v0, \a v1,\a v2,\a v3 and reference \a ref to the tetrahedron at position \a pos in the mesh structure. \a pos ranges from 1 to nb_tetra included.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `v0` | `number` |
| `v1` | `number` |
| `v2` | `number` |
| `v3` | `number` |
| `ref` | `number` |
| `pos` | `number` |

<small>MMG C symbol: `MMG3D_Set_tetrahedron` — return: throws on failure</small>

### `mmg3d.setTriangle`

```ts
mmg3d.setTriangle(mesh: MeshHandle, v0: number, v1: number, v2: number, ref: number, pos: number): void
```

Set the vertices and reference of a single triangle in a mesh. This function defines a triangle of vertices \a v0, \a v1, \a v2 and reference \a ref at position \a pos in mesh structure (from 1 to nb_triangle included).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `v0` | `number` |
| `v1` | `number` |
| `v2` | `number` |
| `ref` | `number` |
| `pos` | `number` |

<small>MMG C symbol: `MMG3D_Set_triangle` — return: throws on failure</small>

### `mmg3d.setTriangles`

```ts
mmg3d.setTriangles(mesh: MeshHandle, tria: number[] | Int32Array, refs: number[] | Int32Array | null): void
```

Set the vertices and references of all triangles in a mesh. This function sets the vertices and references of all triangles in a mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `tria` | `number[] | Int32Array` |
| `refs` | `number[] | Int32Array | null` |

<small>MMG C symbol: `MMG3D_Set_triangles` — return: throws on failure</small>

### `mmg3d.setVectorSol`

```ts
mmg3d.setVectorSol(met: SolHandle, vx: number, vy: number, vz: number, pos: number): void
```

Set a single element of a vector solution structure. Set vectorial value \f$(v_x,v_y,v_z)\f$ at position \a pos in solution structure. (pos from 1 to nb_vertices included).

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |
| `vx` | `number` |
| `vy` | `number` |
| `vz` | `number` |
| `pos` | `number` |

<small>MMG C symbol: `MMG3D_Set_vectorSol` — return: throws on failure</small>

### `mmg3d.setVectorSols`

```ts
mmg3d.setVectorSols(met: SolHandle, sols: number[] | Float64Array): void
```

Set all elements of a vector solution structure. Set vectorial solutions at mesh vertices

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |
| `sols` | `number[] | Float64Array` |

<small>MMG C symbol: `MMG3D_Set_vectorSols` — return: throws on failure</small>

### `mmg3d.setVertex`

```ts
mmg3d.setVertex(mesh: MeshHandle, c0: number, c1: number, c2: number, ref: number, pos: number): void
```

Set the coordinates of a single vertex. This function sets the coordinates of a vertex \a c0, \a c1,\a c2 and reference \a ref at position \a pos in mesh structure (from 1 to nb_vertices included).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `c0` | `number` |
| `c1` | `number` |
| `c2` | `number` |
| `ref` | `number` |
| `pos` | `number` |

<small>MMG C symbol: `MMG3D_Set_vertex` — return: throws on failure</small>

### `mmg3d.setVertices`

```ts
mmg3d.setVertices(mesh: MeshHandle, vertices: number[] | Float64Array, refs: number[] | Int32Array | null): void
```

Set all vertex coordinates and references in a mesh structure This function sets the coordinates and references of all vertices in a mesh structure. The number of vertices in the mesh must have been set before.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `vertices` | `number[] | Float64Array` |
| `refs` | `number[] | Int32Array | null` |

<small>MMG C symbol: `MMG3D_Set_vertices` — return: throws on failure</small>

### `mmg3d.setfunc`

```ts
mmg3d.setfunc(mesh: MeshHandle, met: SolHandle): void
```

To associate function pointers without calling MMG3D_mmg3dlib */ /** Set function pointers for caltet, lenedg, lenedgCoor defsiz, gradsiz... depending if the metric that was read is anisotropic or isotropic

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |

<small>MMG C symbol: `MMG3D_setfunc` — return: no return value</small>

### `mmg3d.switchMetricStorage`

```ts
mmg3d.switchMetricStorage(mesh: MeshHandle, met: SolHandle): void
```

Swap the m22 and m23 values of the metric. Switch the m22 and m23 value of the metric to allow to pass from the API storage to the medit storage.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |

<small>MMG C symbol: `MMG3D_switch_metricStorage` — return: throws on failure</small>

### `mmg3d.unsetCorner`

```ts
mmg3d.unsetCorner(mesh: MeshHandle, k: number): void
```

Remove the "corner" attribute from a vertex. Remove corner attribute from vertex \a k (from 1 to the number of vertices included).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMG3D_Unset_corner` — return: throws on failure</small>

### `mmg3d.unsetParallelTriangle`

```ts
mmg3d.unsetParallelTriangle(mesh: MeshHandle, k: number): void
```

Remove the "parallel" attribute from a single triangle. Remove parallel attribute from triangle \a k (i.e. triangles aren't preserved anymore). (\a k from 1 to nb_tria included).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMG3D_Unset_parallelTriangle` — return: throws on failure</small>

### `mmg3d.unsetParallelTriangles`

```ts
mmg3d.unsetParallelTriangles(mesh: MeshHandle, parIdx: number[] | Int32Array, npar: number): void
```

Remove the "parallel" attribute from multiple triangles. Remove parallel attributes from triangles (i.e. triangles aren't preserved anymore).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `parIdx` | `number[] | Int32Array` |
| `npar` | `number` |

<small>MMG C symbol: `MMG3D_Unset_parallelTriangles` — return: throws on failure</small>

### `mmg3d.unsetRequiredEdge`

```ts
mmg3d.unsetRequiredEdge(mesh: MeshHandle, k: number): void
```

Remove the "required" attribute from a single edge. Remove required attribute from edge \a k.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMG3D_Unset_requiredEdge` — return: throws on failure</small>

### `mmg3d.unsetRequiredTetrahedra`

```ts
mmg3d.unsetRequiredTetrahedra(mesh: MeshHandle, reqIdx: number[] | Int32Array, nreq: number): void
```

Remove the "required" attribute from multiple tetrahedra. Remove required attribute from a list of Tetra whose indices are contained in array \a reqIdx.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `reqIdx` | `number[] | Int32Array` |
| `nreq` | `number` |

<small>MMG C symbol: `MMG3D_Unset_requiredTetrahedra` — return: throws on failure</small>

### `mmg3d.unsetRequiredTetrahedron`

```ts
mmg3d.unsetRequiredTetrahedron(mesh: MeshHandle, k: number): void
```

Remove the "required" attribute from a tetrahedron. Remove required attribute from element \a k (\a k from 1 to nb_tetra included).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMG3D_Unset_requiredTetrahedron` — return: throws on failure</small>

### `mmg3d.unsetRequiredTriangle`

```ts
mmg3d.unsetRequiredTriangle(mesh: MeshHandle, k: number): void
```

Remove the "required" attribute from a single triangle. Remove required attribute from triangle \a k.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMG3D_Unset_requiredTriangle` — return: throws on failure</small>

### `mmg3d.unsetRequiredTriangles`

```ts
mmg3d.unsetRequiredTriangles(mesh: MeshHandle, reqIdx: number[] | Int32Array, nreq: number): void
```

Remove the "required" attribute from multiple triangles.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `reqIdx` | `number[] | Int32Array` |
| `nreq` | `number` |

<small>MMG C symbol: `MMG3D_Unset_requiredTriangles` — return: throws on failure</small>

### `mmg3d.unsetRequiredVertex`

```ts
mmg3d.unsetRequiredVertex(mesh: MeshHandle, k: number): void
```

Remove required attribute from a vertex. This function removes the required attribute from vertex \a k.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMG3D_Unset_requiredVertex` — return: throws on failure</small>

### `mmg3d.unsetRidge`

```ts
mmg3d.unsetRidge(mesh: MeshHandle, k: number): void
```

Remove the "ridge" attribute from a single edge. Remove ridge attribute at edge \a k.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMG3D_Unset_ridge` — return: throws on failure</small>

### `mmg3d.usage`

```ts
mmg3d.usage(prog: string): void
```

Print help for mmg3d options.

| Parameter | Type |
|-----------|------|
| `prog` | `string` |

<small>MMG C symbol: `MMG3D_usage` — return: throws on failure</small>

## `mmg2d`

### `mmg2d.chkMeshData`

```ts
mmg2d.chkMeshData(mesh: MeshHandle, met: SolHandle): void
```

Check if the number of given entities match with mesh and sol size Check if the number of given entities match with mesh and sol size (not mandatory) and check mesh datas.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |

<small>MMG C symbol: `MMG2D_Chk_meshData` — return: throws on failure</small>

### `mmg2d.computeEigenv`

```ts
mmg2d.computeEigenv(m: number[] | Float64Array): { value: number; lambda: Float64Array; vp: Float64Array }
```

Compute the real eigenvalues and eigenvectors of a symmetric matrix This function computes the real eigenvalues and eigenvectors of a symmetric matrix m whose upper part is provided (m11, m12, m22, in this order). lambda[0] is the eigenvalue associated to the eigenvector ( v[0][0], v[0,1] ) in C and to the eigenvector v(1,:) in fortran lambda[1] is the eigenvalue associated to the eigenvector ( v[1][0], v[1,1] ) in C and to the eigenvector v(2,:) in fortran

| Parameter | Type |
|-----------|------|
| `m` | `number[] | Float64Array` |

<small>MMG C symbol: `MMG2D_Compute_eigenv` — return: returns the raw integer value</small>

### `mmg2d.defaultValues`

```ts
mmg2d.defaultValues(mesh: MeshHandle): void
```

Print the default parameters values.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |

<small>MMG C symbol: `MMG2D_defaultValues` — return: throws on failure</small>

### `mmg2d.freeAll`

```ts
mmg2d.freeAll(mesh: MeshHandle, met: SolHandle, ls: SolHandle | null, disp: SolHandle | null): void
```

Free all allocated structures (fixed-arity shim over the variadic MMG2D_Free_all).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |
| `ls` | `SolHandle | null` |
| `disp` | `SolHandle | null` |

<small>MMG C symbol: `mmgjs_MMG2D_Free_all` — return: throws on failure</small>

### `mmg2d.freeAllSols`

```ts
mmg2d.freeAllSols(mesh: MeshHandle, sol: SolHandle): void
```

Deallocate an array of solution fields

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |

<small>MMG C symbol: `MMG2D_Free_allSols` — return: throws on failure</small>

### `mmg2d.freeEdges`

```ts
mmg2d.freeEdges(mesh: MeshHandle): void
```

Free the mesh edges (and the associated xpoints).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |

<small>MMG C symbol: `MMG2D_Free_edges` — return: no return value</small>

### `mmg2d.freeNames`

```ts
mmg2d.freeNames(mesh: MeshHandle, met: SolHandle, ls: SolHandle | null, disp: SolHandle | null): void
```

Free file-name strings (shim over MMG2D_Free_names).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |
| `ls` | `SolHandle | null` |
| `disp` | `SolHandle | null` |

<small>MMG C symbol: `mmgjs_MMG2D_Free_names` — return: throws on failure</small>

### `mmg2d.freeSolutions`

```ts
mmg2d.freeSolutions(mesh: MeshHandle, sol: SolHandle): void
```

Free the solution.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |

<small>MMG C symbol: `MMG2D_Free_solutions` — return: no return value</small>

### `mmg2d.freeStructures`

```ts
mmg2d.freeStructures(mesh: MeshHandle, met: SolHandle, ls: SolHandle | null, disp: SolHandle | null): void
```

Free mesh/sol arrays but keep the structures (shim over MMG2D_Free_structures).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |
| `ls` | `SolHandle | null` |
| `disp` | `SolHandle | null` |

<small>MMG C symbol: `mmgjs_MMG2D_Free_structures` — return: throws on failure</small>

### `mmg2d.freeTriangles`

```ts
mmg2d.freeTriangles(mesh: MeshHandle): void
```

Free the mesh elements (and the adjacency information).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |

<small>MMG C symbol: `MMG2D_Free_triangles` — return: no return value</small>

### `mmg2d.getAdjaTri`

```ts
mmg2d.getAdjaTri(mesh: MeshHandle, kel: number): { listri: Int32Array }
```

Return adjacent elements of a triangle. Find the indices of the 3 adjacent elements of triangle \a kel. \f$v_i = 0\f$ if the \f$i^{th}\f$ face has no adjacent element (so we are on a boundary face).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `kel` | `number` |

<small>MMG C symbol: `MMG2D_Get_adjaTri` — return: throws on failure</small>

### `mmg2d.getAdjaVertices`

```ts
mmg2d.getAdjaVertices(mesh: MeshHandle, ip: number): { value: number; lispoi: Int32Array }
```

Return adjacent vertices of a triangle. Find the indices of the adjacent vertices of the vertex \a ip.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `ip` | `number` |

<small>MMG C symbol: `MMG2D_Get_adjaVertices` — return: returns the raw integer value</small>

### `mmg2d.getAdjaVerticesFast`

```ts
mmg2d.getAdjaVerticesFast(mesh: MeshHandle, ip: number, start: number): { value: number; lispoi: Int32Array }
```

Return adjacent vertices of a triangle. Find the indices of the adjacent vertices of the vertex \a ip of the triangle \a start.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `ip` | `number` |
| `start` | `number` |

<small>MMG C symbol: `MMG2D_Get_adjaVerticesFast` — return: returns the raw integer value</small>

### `mmg2d.getByIdxVertex`

```ts
mmg2d.getByIdxVertex(mesh: MeshHandle, idx: number): { c0: number; c1: number; ref: number; isCorner: number; isRequired: number }
```

Get the coordinates and reference of a specific vertex in the mesh. Get coordinates \a c0, \a c1 and reference \a ref of vertex \a idx of mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `idx` | `number` |

<small>MMG C symbol: `MMG2D_GetByIdx_vertex` — return: throws on failure</small>

### `mmg2d.getEdge`

```ts
mmg2d.getEdge(mesh: MeshHandle): { e0: number; e1: number; ref: number; isRidge: number; isRequired: number }
```

Get the vertices and reference of the next edge in the mesh. This function retrieves the extremities \a e0, \a e1 and reference \a ref of next edge of \a mesh. It is meant to be called in a loop over all edges. When it has been called as many times as there are edges in the mesh, the internal edge counter will be reset.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |

<small>MMG C symbol: `MMG2D_Get_edge` — return: throws on failure</small>

### `mmg2d.getEdges`

```ts
mmg2d.getEdges(mesh: MeshHandle, na: number): { edges: Int32Array; refs: Int32Array; areRidges: Int32Array; areRequired: Int32Array }
```

Get the vertices and references of all edges in a mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `na` | `number (size of the output arrays)` |

<small>MMG C symbol: `MMG2D_Get_edges` — return: throws on failure</small>

### `mmg2d.getIthSolInSolsAtVertices`

```ts
mmg2d.getIthSolInSolsAtVertices(sol: SolHandle, i: number, pos: number, n: number): { s: Float64Array }
```

Get one out of several scalar solutions at a specific vertex. Get values of the ith field of the solution array at vertex \a pos. (pos from 1 to the number of vertices included and \a i from 1 to the number of solutions).

| Parameter | Type |
|-----------|------|
| `sol` | `SolHandle` |
| `i` | `number` |
| `pos` | `number` |
| `n` | `number (size of the output arrays)` |

<small>MMG C symbol: `MMG2D_Get_ithSol_inSolsAtVertices` — return: throws on failure</small>

### `mmg2d.getIthSolsInSolsAtVertices`

```ts
mmg2d.getIthSolsInSolsAtVertices(sol: SolHandle, i: number, n: number): { s: Float64Array }
```

Get one out of several scalar solutions at all vertices in the mesh. Get values of the solution at the ith field of the solution array. (\a i from 1 to \a nb_sols)

| Parameter | Type |
|-----------|------|
| `sol` | `SolHandle` |
| `i` | `number` |
| `n` | `number (size of the output arrays)` |

<small>MMG C symbol: `MMG2D_Get_ithSols_inSolsAtVertices` — return: throws on failure</small>

### `mmg2d.getMeshSize`

```ts
mmg2d.getMeshSize(mesh: MeshHandle): { np: number; nt: number; nquad: number; na: number }
```

recover datas */ /** Get the number of vertices, triangles and edges of the mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |

<small>MMG C symbol: `MMG2D_Get_meshSize` — return: throws on failure</small>

### `mmg2d.getNonBdyEdge`

```ts
mmg2d.getNonBdyEdge(mesh: MeshHandle, idx: number): { e0: number; e1: number; ref: number }
```

Get vertices and reference of a non-boundary edge. This function returns the extremities \a e0, \a e1 and reference \a ref of the idx^th non boundary edge (for DG methods for example). An edge is boundary if it is located at the interface of 2 domains with different references, if it belongs to one triangle only or if it is a singular edge (ridge or required).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `idx` | `number` |

<small>MMG C symbol: `MMG2D_Get_nonBdyEdge` — return: throws on failure</small>

### `mmg2d.getNumberOfNonBdyEdges`

```ts
mmg2d.getNumberOfNonBdyEdges(mesh: MeshHandle): { nb_edges: number }
```

Get the number of non-boundary edges. This function extracts the number of non boundary edges (for DG methods for example). An edge is boundary if it is located at the interface of two domains with different references, if it belongs to one triangle only or if it is a singular edge (ridge or required). Append these edges to the list of edges.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |

<small>MMG C symbol: `MMG2D_Get_numberOfNonBdyEdges` — return: throws on failure</small>

### `mmg2d.getQuadrilateral`

```ts
mmg2d.getQuadrilateral(mesh: MeshHandle): { v0: number; v1: number; v2: number; v3: number; ref: number; isRequired: number }
```

Get the vertices and reference of the next quadrangle of the mesh. Get the vertices \a v0,\a v1,\a v2,\a v3 and reference \a ref of the next quadrangle of mesh. This function is meant to be called in a loop over all quadrangles. When it has been called as many times as there are quadrangles, the internal loop counter will be reset.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |

<small>MMG C symbol: `MMG2D_Get_quadrilateral` — return: throws on failure</small>

### `mmg2d.getQuadrilaterals`

```ts
mmg2d.getQuadrilaterals(mesh: MeshHandle, nquad: number): { quadra: Int32Array; refs: Int32Array; areRequired: Int32Array }
```

Get the vertices and references of all quadrangles of the mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `nquad` | `number (size of the output arrays)` |

<small>MMG C symbol: `MMG2D_Get_quadrilaterals` — return: throws on failure</small>

### `mmg2d.getScalarSol`

```ts
mmg2d.getScalarSol(met: SolHandle): { s: number }
```

Get the scalar solution value \a s of next element of a solution. This function is meant to be called in a loop over all elements. When it has been called as many times as there are elements in the solution, the internal counter will be reset.

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |

<small>MMG C symbol: `MMG2D_Get_scalarSol` — return: throws on failure</small>

### `mmg2d.getScalarSols`

```ts
mmg2d.getScalarSols(met: SolHandle, np: number): { s: Float64Array }
```

Get all elements of a scalar sol structure.

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |
| `np` | `number (size of the output arrays)` |

<small>MMG C symbol: `MMG2D_Get_scalarSols` — return: throws on failure</small>

### `mmg2d.getSolSize`

```ts
mmg2d.getSolSize(mesh: MeshHandle, sol: SolHandle): { typEntity: number; np: number; typSol: number }
```

Get the number of solutions, their dimension and their type.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |

<small>MMG C symbol: `MMG2D_Get_solSize` — return: throws on failure</small>

### `mmg2d.getSolsAtVerticesSize`

```ts
mmg2d.getSolsAtVerticesSize(mesh: MeshHandle, sol: SolHandle): { nsols: number; nentities: number; typSol: Int32Array }
```

Get the number of elements and dimension of a solution defined on vertices.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |

<small>MMG C symbol: `MMG2D_Get_solsAtVerticesSize` — return: throws on failure</small>

### `mmg2d.getTensorSol`

```ts
mmg2d.getTensorSol(met: SolHandle): { m11: number; m12: number; m22: number }
```

Get the next element of a tensor sol structure. This function is meant to be called in a loop over all elements. When it has been called as many times as there are elements in the solution, the internal counter will be reset.

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |

<small>MMG C symbol: `MMG2D_Get_tensorSol` — return: throws on failure</small>

### `mmg2d.getTensorSols`

```ts
mmg2d.getTensorSols(met: SolHandle, np: number): { sols: Float64Array }
```

Get all elements of a tensor sol structure.

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |
| `np` | `number (size of the output arrays)` |

<small>MMG C symbol: `MMG2D_Get_tensorSols` — return: throws on failure</small>

### `mmg2d.getTriFromEdge`

```ts
mmg2d.getTriFromEdge(mesh: MeshHandle, ked: number): { ktri: number; ied: number }
```

Find a triangle given an adjacent triangle and an edge number. Fill \a ktri by the index of the triangle to which belong a boundary edge and \a ied by the index of the edge of the triangle that correspond to the edge.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `ked` | `number` |

<small>MMG C symbol: `MMG2D_Get_triFromEdge` — return: throws on failure</small>

### `mmg2d.getTriangle`

```ts
mmg2d.getTriangle(mesh: MeshHandle): { v0: number; v1: number; v2: number; ref: number; isRequired: number }
```

Get the vertices and reference of the next triangle in the mesh. This function retrieves the vertices \a v0, \a v1, \a v2, and reference \a ref of the next triangle of \a mesh. It is meant to be called in a loop over all triangles. When it has been called as many times as there are triangles, the internal loop counter will be reset.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |

<small>MMG C symbol: `MMG2D_Get_triangle` — return: throws on failure</small>

### `mmg2d.getTriangleQuality`

```ts
mmg2d.getTriangleQuality(mesh: MeshHandle, met: SolHandle, k: number): number
```

Get the quality measure of a single triangle in the mesh. Get quality of triangle \a k.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMG2D_Get_triangleQuality` — return: returns the raw double value</small>

### `mmg2d.getTriangles`

```ts
mmg2d.getTriangles(mesh: MeshHandle, nt: number): { tria: Int32Array; refs: Int32Array; areRequired: Int32Array }
```

Get the vertices and references of all triangles in the mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `nt` | `number (size of the output arrays)` |

<small>MMG C symbol: `MMG2D_Get_triangles` — return: throws on failure</small>

### `mmg2d.getTrisFromEdge`

```ts
mmg2d.getTrisFromEdge(mesh: MeshHandle, ked: number): { ktri: Int32Array; ied: Int32Array }
```

Find two triangles given the edge that they share. Fill \a ktri by the indices of the triangles to which belong a boundary edge and \a ied by the indices of the matching edge in each triangle. If \a ked belongs to one triangle only, ktri[1] = ied[1] = 0.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `ked` | `number` |

<small>MMG C symbol: `MMG2D_Get_trisFromEdge` — return: throws on failure</small>

### `mmg2d.getVectorSol`

```ts
mmg2d.getVectorSol(met: SolHandle): { vx: number; vy: number }
```

Get the next element of a vector sol structure. This function retrieves vectorial solution \f$(v_x,v_y)\f$ of the next element of \a met. It is meant to be called in a loop over all elements. When it has been called as many times as there are elements in the solution, the internal counter will be reset.

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |

<small>MMG C symbol: `MMG2D_Get_vectorSol` — return: throws on failure</small>

### `mmg2d.getVectorSols`

```ts
mmg2d.getVectorSols(met: SolHandle, np: number): { sols: Float64Array }
```

Get all elements of a vector sol structure.

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |
| `np` | `number (size of the output arrays)` |

<small>MMG C symbol: `MMG2D_Get_vectorSols` — return: throws on failure</small>

### `mmg2d.getVertex`

```ts
mmg2d.getVertex(mesh: MeshHandle): { c0: number; c1: number; ref: number; isCorner: number; isRequired: number }
```

Get the coordinates and reference ref of the next vertex of a mesh. This function retrieves the coordinates \a c0 and \a c1, and reference \a ref of the next vertex of a mesh. It is meant to be used in a loop over all vertices. When this function has been called as many times as there are vertices, the internal loop counter will be reset. To obtain data for a specific vertex, the \ref MMG2D_GetByIdx_vertex function can be used instead.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |

<small>MMG C symbol: `MMG2D_Get_vertex` — return: throws on failure</small>

### `mmg2d.getVertices`

```ts
mmg2d.getVertices(mesh: MeshHandle, np: number): { vertices: Float64Array; refs: Int32Array; areCorners: Int32Array; areRequired: Int32Array }
```

Get the coordinates and references of all vertices in the mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `np` | `number (size of the output arrays)` |

<small>MMG C symbol: `MMG2D_Get_vertices` — return: throws on failure</small>

### `mmg2d.initFileNames`

```ts
mmg2d.initFileNames(mesh: MeshHandle, sol: SolHandle): void
```

Initialize file names to their default values.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |

<small>MMG C symbol: `MMG2D_Init_fileNames` — return: no return value</small>

### `mmg2d.initMesh`

```ts
mmg2d.initMesh(mesh: MeshHandle, met: SolHandle, ls: SolHandle | null, disp: SolHandle | null): void
```

Allocate and initialize the mesh and solution structures (fixed-arity shim over the variadic MMG2D_Init_mesh).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |
| `ls` | `SolHandle | null` |
| `disp` | `SolHandle | null` |

<small>MMG C symbol: `mmgjs_MMG2D_Init_mesh` — return: throws on failure</small>

### `mmg2d.initParameters`

```ts
mmg2d.initParameters(mesh: MeshHandle): void
```

Initialize the input parameters (stored in the Info structure).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |

<small>MMG C symbol: `MMG2D_Init_parameters` — return: no return value</small>

### `mmg2d.loadAllSols`

```ts
mmg2d.loadAllSols(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Load one or more solutions in a solution file in medit file format. Load 1 or more solutions in a solution file in medit file format

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG2D_loadAllSols` — return: throws on failure</small>

### `mmg2d.loadGenericMesh`

```ts
mmg2d.loadGenericMesh(mesh: MeshHandle, met: SolHandle, sol: SolHandle, filename: string): void
```

Read mesh data in a format determined by the filename extension.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG2D_loadGenericMesh` — return: throws on failure</small>

### `mmg2d.loadMesh`

```ts
mmg2d.loadMesh(mesh: MeshHandle, filename: string): void
```

Load a mesh (in .mesh/.mesb format) from file.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG2D_loadMesh` — return: throws on failure</small>

### `mmg2d.loadMshMesh`

```ts
mmg2d.loadMshMesh(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Load a mesh and possibly a solution in .msh format from file. This function reads a mesh and 0 or 1 data fields in MSH file format (.msh extension). We read only low-order vertices, edges, triangles, and quadrangles.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG2D_loadMshMesh` — return: throws on failure</small>

### `mmg2d.loadMshMeshAndAllData`

```ts
mmg2d.loadMshMeshAndAllData(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Load a mesh and all data from a file in MSH format. This function reads a mesh and all data fields from a file in MSH file format (.msh extension). We read only low-order vertices, edges, triangles, quadrangles, tetrahedra and prisms.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG2D_loadMshMesh_and_allData` — return: throws on failure</small>

### `mmg2d.loadSol`

```ts
mmg2d.loadSol(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Load a metric field (or other solution) in medit's .sol format. This function loads a metric field. The file in medit format must contain 1 solution: the metric.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG2D_loadSol` — return: throws on failure</small>

### `mmg2d.loadVtkMesh`

```ts
mmg2d.loadVtkMesh(mesh: MeshHandle, met: SolHandle, sol: SolHandle, filename: string): void
```

Load a mesh and possibly data in VTK format from file. Read mesh and 0 or 1 data fields in VTK file format (.vtk extension). We read only low-order vertices, edges, triangles and quadrangles.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG2D_loadVtkMesh` — return: throws on failure</small>

### `mmg2d.loadVtkMeshAndAllData`

```ts
mmg2d.loadVtkMeshAndAllData(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Load a mesh and multiple solutions in VTK format from file. This function reads a mesh and a list of data fields in VTK file format (.vtk extension). We read only low-order vertices, edges, triangles and quadrangles.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG2D_loadVtkMesh_and_allData` — return: throws on failure</small>

### `mmg2d.loadVtpMesh`

```ts
mmg2d.loadVtpMesh(mesh: MeshHandle, met: SolHandle, sol: SolHandle, filename: string): void
```

Load a mesh and possibly a solution in VTP (VTK) format from file. Read a mesh and 0 or 1 data fields in VTK vtp file format (.vtp extension). We read only low-order vertices, edges, triangles and quadrangles.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG2D_loadVtpMesh` — return: throws on failure</small>

### `mmg2d.loadVtpMeshAndAllData`

```ts
mmg2d.loadVtpMeshAndAllData(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Load a mesh and multiple solutions in VTP (VTK) format from file. Read a mesh and a list of data fields in VTK vtp file format (.vtp extension). We read only low-order vertices, edges, triangles and quadrangles.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG2D_loadVtpMesh_and_allData` — return: throws on failure</small>

### `mmg2d.loadVtuMesh`

```ts
mmg2d.loadVtuMesh(mesh: MeshHandle, met: SolHandle, sol: SolHandle, filename: string): void
```

Load a mesh and possibly data in VTU (VTK) format from file. Read a mesh and 0 or 1 data fields in VTK vtu file format (.vtu extension). We read only low-order vertices, edges, triangles and quadrangles.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG2D_loadVtuMesh` — return: throws on failure</small>

### `mmg2d.loadVtuMeshAndAllData`

```ts
mmg2d.loadVtuMeshAndAllData(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Load a mesh and multiple solutions in VTU (VTK) format from file. Read a mesh and a list of data fields in VTK vtu file format (.vtu extension). We read only low-order vertices, edges, triangles and quadrangles.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG2D_loadVtuMesh_and_allData` — return: throws on failure</small>

### `mmg2d.mmg2dlib`

```ts
mmg2d.mmg2dlib(mesh: MeshHandle, sol: SolHandle): number
```

Main "program" for the mesh adaptation library. This function adapts a given mesh, trying to improve the quality, under the given metric and parameters.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |

<small>MMG C symbol: `MMG2D_mmg2dlib` — return: returns `MMG5_SUCCESS`/`MMG5_LOWFAILURE`; throws on `MMG5_STRONGFAILURE` — alias: `mmg2d.remesh()`</small>

### `mmg2d.mmg2dls`

```ts
mmg2d.mmg2dls(mesh: MeshHandle, sol: SolHandle, met: SolHandle): number
```

Main "program" for the level-set discretization library. This is the main program for the level-set discretization library. If a metric \a met is provided, it is used to adapt the mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `met` | `SolHandle` |

<small>MMG C symbol: `MMG2D_mmg2dls` — return: returns `MMG5_SUCCESS`/`MMG5_LOWFAILURE`; throws on `MMG5_STRONGFAILURE` — alias: `mmg2d.levelset()`</small>

### `mmg2d.mmg2dmesh`

```ts
mmg2d.mmg2dmesh(mesh: MeshHandle, sol: SolHandle): number
```

Main "program" for the mesh generation library. FIXME: This function creates a triangular mesh from a given polygon, right?

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |

<small>MMG C symbol: `MMG2D_mmg2dmesh` — return: returns `MMG5_SUCCESS`/`MMG5_LOWFAILURE`; throws on `MMG5_STRONGFAILURE` — alias: `mmg2d.generate()`</small>

### `mmg2d.mmg2dmov`

```ts
mmg2d.mmg2dmov(mesh: MeshHandle, met: SolHandle, disp: SolHandle): number
```

Main "program" for the rigid-body movement library.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |
| `disp` | `SolHandle` |

<small>MMG C symbol: `MMG2D_mmg2dmov` — return: returns `MMG5_SUCCESS`/`MMG5_LOWFAILURE`; throws on `MMG5_STRONGFAILURE` — alias: `mmg2d.move()`</small>

### `mmg2d.resetVerticestags`

```ts
mmg2d.resetVerticestags(mesh: MeshHandle): void
```

Reset the vertex tags. This function resets the tags of all vertices. Be careful: all the tags are deleted.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |

<small>MMG C symbol: `MMG2D_Reset_verticestags` — return: no return value</small>

### `mmg2d.saveAllSols`

```ts
mmg2d.saveAllSols(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Save one or more solutions in a solution file in medit file format.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG2D_saveAllSols` — return: throws on failure</small>

### `mmg2d.saveGenericMesh`

```ts
mmg2d.saveGenericMesh(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Save mesh data in a file whose format depends on the filename extension.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG2D_saveGenericMesh` — return: throws on failure</small>

### `mmg2d.saveMesh`

```ts
mmg2d.saveMesh(arg0: MeshHandle, arg1: string): void
```

Save a mesh in .mesh/.meshb format.

| Parameter | Type |
|-----------|------|
| `arg0` | `MeshHandle` |
| `arg1` | `string` |

<small>MMG C symbol: `MMG2D_saveMesh` — return: throws on failure</small>

### `mmg2d.saveMshMesh`

```ts
mmg2d.saveMshMesh(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Save a mesh and optionally one data field in MSH format, ascii or binary depending on the filename extension. This function writes a mesh and optionally one data field in MSH file format (.msh extension). It uses ASCII format for .msh extension, binary format for .msb extension.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG2D_saveMshMesh` — return: throws on failure</small>

### `mmg2d.saveMshMeshAndAllData`

```ts
mmg2d.saveMshMeshAndAllData(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Save a mesh and multiple data fields in MSH format, ascii or binary depending on the filename extension. This function writes a mesh and a list of data fields in MSH file format (.msh extension). It uses ASCII format for .msh extension, binary format for .mshb extension.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG2D_saveMshMesh_and_allData` — return: throws on failure</small>

### `mmg2d.saveSol`

```ts
mmg2d.saveSol(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Save metric field in medit solution file format.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG2D_saveSol` — return: throws on failure</small>

### `mmg2d.saveTetgenMesh`

```ts
mmg2d.saveTetgenMesh(arg0: MeshHandle, arg1: string): void
```

Save data in Tetgen's Triangle format. This function saves mesh data in Triangle (or equivalent to Tetgen in 2D) file format.

| Parameter | Type |
|-----------|------|
| `arg0` | `MeshHandle` |
| `arg1` | `string` |

<small>MMG C symbol: `MMG2D_saveTetgenMesh` — return: throws on failure</small>

### `mmg2d.saveVtkMesh`

```ts
mmg2d.saveVtkMesh(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Save a mesh and optionally one solution in VTK format. This function writes a mesh and 0 or 1 data fields in Vtk file format (.vtk extension).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG2D_saveVtkMesh` — return: throws on failure</small>

### `mmg2d.saveVtkMeshAndAllData`

```ts
mmg2d.saveVtkMeshAndAllData(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Save a mesh and multiple data fields in VTK format. This function writes a mesh and a list of data fields in Vtk file format (.vtk extension).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG2D_saveVtkMesh_and_allData` — return: throws on failure</small>

### `mmg2d.saveVtpMesh`

```ts
mmg2d.saveVtpMesh(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Save a mesh and optionally one data field in VTP format. This function writes a mesh and optionally one data field in polydata Vtk file format (.vtp extension).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG2D_saveVtpMesh` — return: throws on failure</small>

### `mmg2d.saveVtpMeshAndAllData`

```ts
mmg2d.saveVtpMeshAndAllData(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Save a mesh and multiple data fields in VTP format. This function writes a mesh and a list of data fields in polydata Vtk file format (.vtp extension).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG2D_saveVtpMesh_and_allData` — return: throws on failure</small>

### `mmg2d.saveVtuMesh`

```ts
mmg2d.saveVtuMesh(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Save a mesh and optionally one data field in VTU format. This function writes a mesh and 0 or 1 data fields in vtu Vtk file format (.vtu extension).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG2D_saveVtuMesh` — return: throws on failure</small>

### `mmg2d.saveVtuMeshAndAllData`

```ts
mmg2d.saveVtuMeshAndAllData(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Save a mesh and multiple data fields in VTU format. This function writes a mesh and a list of data fields in vtu Vtk file format (.vtu extension).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMG2D_saveVtuMesh_and_allData` — return: throws on failure</small>

### `mmg2d.setCommonFunc`

```ts
mmg2d.setCommonFunc(): void
```

Set common function pointers between mmgs and mmg2d to the matching mmg2d functions.

<small>MMG C symbol: `MMG2D_Set_commonFunc` — return: no return value</small>

### `mmg2d.setConstantSize`

```ts
mmg2d.setConstantSize(mesh: MeshHandle, met: SolHandle): void
```

Compute unit tensor according to the lengths of the edges passing through a vertex. / LIBMMG2D_EXPORT extern int (*MMG2D_doSol)(MMG5_pMesh mesh ,MMG5_pSol met ); /** Compute a constant size map according to the hsiz, hmin and hmax parameters. This function computes a constant size map according to mesh->info.hsiz, mesh->info.hmin and mesh->info.hmax. It updates these 3 values if not compatible.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |

<small>MMG C symbol: `MMG2D_Set_constantSize` — return: throws on failure</small>

### `mmg2d.setCorner`

```ts
mmg2d.setCorner(mesh: MeshHandle, k: number): void
```

Assign the "corner" attribute to a vertex. Set the "corner" attribute at vertex \a k. This affects how the vertex is treated during remeshing.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMG2D_Set_corner` — return: throws on failure</small>

### `mmg2d.setDparameter`

```ts
mmg2d.setDparameter(mesh: MeshHandle, sol: SolHandle, dparam: number, val: number): void
```

Set double parameter \a dparam to value \a val.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `dparam` | `number` |
| `val` | `number` |

<small>MMG C symbol: `MMG2D_Set_dparameter` — return: throws on failure</small>

### `mmg2d.setEdge`

```ts
mmg2d.setEdge(mesh: MeshHandle, v0: number, v1: number, ref: number, pos: number): void
```

Define a single edge. Define an edge with vertices \a v0, \a v1 and reference \a ref at position \a pos in the mesh structure (\a pos from 1 to the number of edges included).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `v0` | `number` |
| `v1` | `number` |
| `ref` | `number` |
| `pos` | `number` |

<small>MMG C symbol: `MMG2D_Set_edge` — return: throws on failure</small>

### `mmg2d.setEdges`

```ts
mmg2d.setEdges(mesh: MeshHandle, edges: number[] | Int32Array, refs: number[] | Int32Array | null): void
```

Set the vertices and references of all edges in a mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `edges` | `number[] | Int32Array` |
| `refs` | `number[] | Int32Array | null` |

<small>MMG C symbol: `MMG2D_Set_edges` — return: throws on failure</small>

### `mmg2d.setInputMeshName`

```ts
mmg2d.setInputMeshName(mesh: MeshHandle, meshin: string): void
```

Set the name of the input mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `meshin` | `string` |

<small>MMG C symbol: `MMG2D_Set_inputMeshName` — return: throws on failure</small>

### `mmg2d.setInputParamName`

```ts
mmg2d.setInputParamName(mesh: MeshHandle, fparamin: string): void
```

Set the name of the input parameter file.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `fparamin` | `string` |

<small>MMG C symbol: `MMG2D_Set_inputParamName` — return: throws on failure</small>

### `mmg2d.setInputSolName`

```ts
mmg2d.setInputSolName(mesh: MeshHandle, sol: SolHandle, solin: string): void
```

Set the name of the input solution file.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `solin` | `string` |

<small>MMG C symbol: `MMG2D_Set_inputSolName` — return: throws on failure</small>

### `mmg2d.setIparameter`

```ts
mmg2d.setIparameter(mesh: MeshHandle, sol: SolHandle, iparam: number, val: number): void
```

Set integer parameter \a iparam to value \a val.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `iparam` | `number` |
| `val` | `number` |

<small>MMG C symbol: `MMG2D_Set_iparameter` — return: throws on failure</small>

### `mmg2d.setIthSolInSolsAtVertices`

```ts
mmg2d.setIthSolInSolsAtVertices(sol: SolHandle, i: number, s: number[] | Float64Array, pos: number): void
```

Set a single element of one out of multiple solution fields that are defined on vertices. Set values of the solution at the ith field of the solution array. (\a pos from 1 to \a nb_vertices included and \a i from 1 to \a nb_sols).

| Parameter | Type |
|-----------|------|
| `sol` | `SolHandle` |
| `i` | `number` |
| `s` | `number[] | Float64Array` |
| `pos` | `number` |

<small>MMG C symbol: `MMG2D_Set_ithSol_inSolsAtVertices` — return: throws on failure</small>

### `mmg2d.setIthSolsInSolsAtVertices`

```ts
mmg2d.setIthSolsInSolsAtVertices(sol: SolHandle, i: number, s: number[] | Float64Array): void
```

Set all elements of one out of multiple solution fields that are defined on vertices. Set scalar values of the solution at the ith field of the solution array. (\a i from 1 to \a nb_sols)

| Parameter | Type |
|-----------|------|
| `sol` | `SolHandle` |
| `i` | `number` |
| `s` | `number[] | Float64Array` |

<small>MMG C symbol: `MMG2D_Set_ithSols_inSolsAtVertices` — return: throws on failure</small>

### `mmg2d.setLocalParameter`

```ts
mmg2d.setLocalParameter(mesh: MeshHandle, sol: SolHandle, typ: number, ref: number, hmin: number, hmax: number, hausd: number): void
```

Set local parameters. Set local parameters: set the Hausdorff distance, minimal desired edge length, and maximal desired edge length for all entities of type \a typ and reference \a ref.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `typ` | `number` |
| `ref` | `number` |
| `hmin` | `number` |
| `hmax` | `number` |
| `hausd` | `number` |

<small>MMG C symbol: `MMG2D_Set_localParameter` — return: throws on failure</small>

### `mmg2d.setLsBaseReference`

```ts
mmg2d.setLsBaseReference(mesh: MeshHandle, sol: SolHandle, br: number): void
```

Set level-set base reference. Set a new level-set base reference of ref \a br in ls discretization mode. Based references are boundary conditions to which implicit domain can be attached. All implicit volumes that are not attached to listed base references are deleted as spurious volumes by the \a rmc option.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `br` | `number` |

<small>MMG C symbol: `MMG2D_Set_lsBaseReference` — return: throws on failure</small>

### `mmg2d.setMeshSize`

```ts
mmg2d.setMeshSize(mesh: MeshHandle, np: number, nt: number, nquad: number, na: number): void
```

Set the numbers of entities in the mesh. Set the number of vertices, triangles, quadrangles and edges of the mesh and allocate the associated tables. If call twice, reset the whole mesh to realloc it at the new size

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `np` | `number` |
| `nt` | `number` |
| `nquad` | `number` |
| `na` | `number` |

<small>MMG C symbol: `MMG2D_Set_meshSize` — return: throws on failure</small>

### `mmg2d.setMultiMat`

```ts
mmg2d.setMultiMat(mesh: MeshHandle, sol: SolHandle, ref: number, split: number, rmin: number, rplus: number): void
```

Set the reference mapping for the elements of ref \a ref in LS discretization mode. With this function you can determine which references will be given to the triangles on both sides of the level set, after discretization. Negative and positive here refer to areas where the function is smaller or larger, respectively, than the isovalue of the level set.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `ref` | `number` |
| `split` | `number` |
| `rmin` | `number` |
| `rplus` | `number` |

<small>MMG C symbol: `MMG2D_Set_multiMat` — return: throws on failure</small>

### `mmg2d.setOutputMeshName`

```ts
mmg2d.setOutputMeshName(mesh: MeshHandle, meshout: string): void
```

Set the name of the output mesh file.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `meshout` | `string` |

<small>MMG C symbol: `MMG2D_Set_outputMeshName` — return: throws on failure</small>

### `mmg2d.setOutputSolName`

```ts
mmg2d.setOutputSolName(mesh: MeshHandle, sol: SolHandle, solout: string): void
```

Set the name of the output solution file.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `solout` | `string` |

<small>MMG C symbol: `MMG2D_Set_outputSolName` — return: throws on failure</small>

### `mmg2d.setParallelEdge`

```ts
mmg2d.setParallelEdge(mesh: MeshHandle, k: number): void
```

Give edge \a k the "parallel" attribute.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMG2D_Set_parallelEdge` — return: throws on failure</small>

### `mmg2d.setQuadrilateral`

```ts
mmg2d.setQuadrilateral(mesh: MeshHandle, v0: number, v1: number, v2: number, v3: number, ref: number, pos: number): void
```

Set the vertices and reference of a single quadrangle in a mesh. Define a quadrangle with vertices \a v0, \a v1,\a v2,\a v3 and reference \a ref at position \a pos in mesh structure (from 1 to nb_quad included).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `v0` | `number` |
| `v1` | `number` |
| `v2` | `number` |
| `v3` | `number` |
| `ref` | `number` |
| `pos` | `number` |

<small>MMG C symbol: `MMG2D_Set_quadrilateral` — return: throws on failure</small>

### `mmg2d.setQuadrilaterals`

```ts
mmg2d.setQuadrilaterals(mesh: MeshHandle, quadra: number[] | Int32Array, refs: number[] | Int32Array | null): void
```

Set the vertices and references of all quadrangles in a mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `quadra` | `number[] | Int32Array` |
| `refs` | `number[] | Int32Array | null` |

<small>MMG C symbol: `MMG2D_Set_quadrilaterals` — return: throws on failure</small>

### `mmg2d.setRequiredEdge`

```ts
mmg2d.setRequiredEdge(mesh: MeshHandle, k: number): void
```

Give edge \a k the "required" attribute.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMG2D_Set_requiredEdge` — return: throws on failure</small>

### `mmg2d.setRequiredTriangle`

```ts
mmg2d.setRequiredTriangle(mesh: MeshHandle, k: number): void
```

Give triangle \a k the "required" attribute.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMG2D_Set_requiredTriangle` — return: throws on failure</small>

### `mmg2d.setRequiredVertex`

```ts
mmg2d.setRequiredVertex(mesh: MeshHandle, k: number): void
```

Assign the "required" attribute to a vertex. Set vertex \a k as required (\a k from 1 to the number of vertices included). This prevents the remesher from moving the vertex.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMG2D_Set_requiredVertex` — return: throws on failure</small>

### `mmg2d.setScalarSol`

```ts
mmg2d.setScalarSol(met: SolHandle, s: number, pos: number): void
```

Set a single value of a sol structure. Set scalar value \a s at position \a pos in solution structure. (pos from 1 to nb_vertices included).

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |
| `s` | `number` |
| `pos` | `number` |

<small>MMG C symbol: `MMG2D_Set_scalarSol` — return: throws on failure</small>

### `mmg2d.setScalarSols`

```ts
mmg2d.setScalarSols(met: SolHandle, s: number[] | Float64Array): void
```

Set all values of a scalar sol structure.

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |
| `s` | `number[] | Float64Array` |

<small>MMG C symbol: `MMG2D_Set_scalarSols` — return: throws on failure</small>

### `mmg2d.setSolSize`

```ts
mmg2d.setSolSize(mesh: MeshHandle, sol: SolHandle, typEntity: number, np: number, typSol: number): void
```

Set the size and type of a solution field. Initialize an array of solution field: set dimension, types and number of data. To use to initialize an array of solution fields (not used by Mmg itself).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `typEntity` | `number` |
| `np` | `number` |
| `typSol` | `number` |

<small>MMG C symbol: `MMG2D_Set_solSize` — return: throws on failure</small>

### `mmg2d.setSolsAtVerticesSize`

```ts
mmg2d.setSolsAtVerticesSize(mesh: MeshHandle, sol: SolHandle, nsols: number, nentities: number, typSol: number[] | Int32Array): void
```

Initialize an array of solutions field defined at vertices Initialize an array of solutions field defined at vertices: set dimension, types and number of data. To use to initialize an array of solution fields (not used by Mmg itself).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `nsols` | `number` |
| `nentities` | `number` |
| `typSol` | `number[] | Int32Array` |

<small>MMG C symbol: `MMG2D_Set_solsAtVerticesSize` — return: throws on failure</small>

### `mmg2d.setTensorSol`

```ts
mmg2d.setTensorSol(met: SolHandle, m11: number, m12: number, m22: number, pos: number): void
```

Set a single element of a tensor sol structure. Set tensor value \a s at position \a pos in solution structure (\a pos from 1 to nb_vertices included).

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |
| `m11` | `number` |
| `m12` | `number` |
| `m22` | `number` |
| `pos` | `number` |

<small>MMG C symbol: `MMG2D_Set_tensorSol` — return: throws on failure</small>

### `mmg2d.setTensorSols`

```ts
mmg2d.setTensorSols(met: SolHandle, sols: number[] | Float64Array): void
```

Set all elements of a tensor sol structure. Set tensorial values at position \a pos in solution structure.

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |
| `sols` | `number[] | Float64Array` |

<small>MMG C symbol: `MMG2D_Set_tensorSols` — return: throws on failure</small>

### `mmg2d.setTriangle`

```ts
mmg2d.setTriangle(mesh: MeshHandle, v0: number, v1: number, v2: number, ref: number, pos: number): void
```

Set the vertices and reference of a single triangle in a mesh. This function defines a triangle with vertices \a v0, \a v1, \a v2 and reference \a ref at position \a pos in mesh structure (from 1 to the number of triangles included).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `v0` | `number` |
| `v1` | `number` |
| `v2` | `number` |
| `ref` | `number` |
| `pos` | `number` |

<small>MMG C symbol: `MMG2D_Set_triangle` — return: throws on failure</small>

### `mmg2d.setTriangles`

```ts
mmg2d.setTriangles(mesh: MeshHandle, tria: number[] | Int32Array, refs: number[] | Int32Array | null): void
```

Set the vertices and references of all triangles in a mesh. This function sets the vertices and references of all triangles in a mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `tria` | `number[] | Int32Array` |
| `refs` | `number[] | Int32Array | null` |

<small>MMG C symbol: `MMG2D_Set_triangles` — return: throws on failure</small>

### `mmg2d.setVectorSol`

```ts
mmg2d.setVectorSol(met: SolHandle, vx: number, vy: number, pos: number): void
```

Set a single vector value in a sol structure. Set vectorial value \f$(v_x,v_y)\f$ at position \a pos in solution structure. ( pos from 1 to nb_vertices included).

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |
| `vx` | `number` |
| `vy` | `number` |
| `pos` | `number` |

<small>MMG C symbol: `MMG2D_Set_vectorSol` — return: throws on failure</small>

### `mmg2d.setVectorSols`

```ts
mmg2d.setVectorSols(met: SolHandle, sols: number[] | Float64Array): void
```

Set all values in a vector sol structure. Set vectorial solutions at mesh vertices

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |
| `sols` | `number[] | Float64Array` |

<small>MMG C symbol: `MMG2D_Set_vectorSols` — return: throws on failure</small>

### `mmg2d.setVertex`

```ts
mmg2d.setVertex(mesh: MeshHandle, c0: number, c1: number, ref: number, pos: number): void
```

Set the coordinates and reference of a single vertex. Set vertex of coordinates \a c0, \a c1 and reference \a ref at position \a pos in mesh structure (from 1 to nb_vertices included).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `c0` | `number` |
| `c1` | `number` |
| `ref` | `number` |
| `pos` | `number` |

<small>MMG C symbol: `MMG2D_Set_vertex` — return: throws on failure</small>

### `mmg2d.setVertices`

```ts
mmg2d.setVertices(mesh: MeshHandle, vertices: number[] | Float64Array, refs: number[] | Int32Array | null): void
```

Set the coordinates and references of all vertices in the mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `vertices` | `number[] | Float64Array` |
| `refs` | `number[] | Int32Array | null` |

<small>MMG C symbol: `MMG2D_Set_vertices` — return: throws on failure</small>

### `mmg2d.setfunc`

```ts
mmg2d.setfunc(mesh: MeshHandle, met: SolHandle): void
```

Set function pointers for length, caltri... depending if case is iso or aniso

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |

<small>MMG C symbol: `MMG2D_setfunc` — return: no return value</small>

### `mmg2d.unsetCorner`

```ts
mmg2d.unsetCorner(mesh: MeshHandle, k: number): void
```

Remove the "corner" attribute from a vertex. Remove corner attribute from vertex \a k (from 1 to the number of vertices included).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMG2D_Unset_corner` — return: throws on failure</small>

### `mmg2d.unsetRequiredEdge`

```ts
mmg2d.unsetRequiredEdge(mesh: MeshHandle, k: number): void
```

Remove the "required" attribute from edge \a k.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMG2D_Unset_requiredEdge` — return: throws on failure</small>

### `mmg2d.unsetRequiredTriangle`

```ts
mmg2d.unsetRequiredTriangle(mesh: MeshHandle, k: number): void
```

Remove the "required" attribute from triangle \a k.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMG2D_Unset_requiredTriangle` — return: throws on failure</small>

### `mmg2d.unsetRequiredVertex`

```ts
mmg2d.unsetRequiredVertex(mesh: MeshHandle, k: number): void
```

Remove the "required" attribute from a vertex. This function removes the "required" attribute from vertex \a k.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMG2D_Unset_requiredVertex` — return: throws on failure</small>

### `mmg2d.usage`

```ts
mmg2d.usage(prog: string): void
```

Print help for mmg2d options.

| Parameter | Type |
|-----------|------|
| `prog` | `string` |

<small>MMG C symbol: `MMG2D_usage` — return: throws on failure</small>

## `mmgs`

### `mmgs.chkMeshData`

```ts
mmgs.chkMeshData(mesh: MeshHandle, met: SolHandle): void
```

Check if the numbers of given entities match with mesh and solution size and check mesh data. This function checks if the numbers of given entities match with the mesh and solution sizes and checks the mesh data. Use of this function is not mandatory.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |

<small>MMG C symbol: `MMGS_Chk_meshData` — return: throws on failure</small>

### `mmgs.cleanIsoSurf`

```ts
mmgs.cleanIsoSurf(mesh: MeshHandle): void
```

Clean data (triangles and edges) linked to isosurface.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |

<small>MMG C symbol: `MMGS_Clean_isoSurf` — return: throws on failure</small>

### `mmgs.computeEigenv`

```ts
mmgs.computeEigenv(m: number[] | Float64Array): { value: number; lambda: Float64Array; vp: Float64Array }
```

Compute the real eigenvalues and eigenvectors of a symmetric matrix Compute the real eigenvalues and eigenvectors of a symmetric matrix m whose upper part is provided (m11, m12, m13, m22, m23, m33 in this order). lambda[0] is the eigenvalue associated to the eigenvector ( v[0][0], v[0,1], v[0,2] ) in C and to the eigenvector v(1,:) in fortran lambda[1] is the eigenvalue associated to the eigenvector ( v[1][0], v[1,1], v[1,2] ) in C and to the eigenvector v(2,:) in fortran lambda[2] is the eigenvalue associated to the eigenvector ( v[2][0], v[2,1], v[2,2] ) in C and to the eigenvector v(3,:) in fortran

| Parameter | Type |
|-----------|------|
| `m` | `number[] | Float64Array` |

<small>MMG C symbol: `MMGS_Compute_eigenv` — return: returns the raw integer value</small>

### `mmgs.defaultValues`

```ts
mmgs.defaultValues(mesh: MeshHandle): void
```

Print the default parameter values.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |

<small>MMG C symbol: `MMGS_defaultValues` — return: throws on failure</small>

### `mmgs.freeAll`

```ts
mmgs.freeAll(mesh: MeshHandle, met: SolHandle, ls: SolHandle | null): void
```

Free all allocated structures (fixed-arity shim over the variadic MMGS_Free_all).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |
| `ls` | `SolHandle | null` |

<small>MMG C symbol: `mmgjs_MMGS_Free_all` — return: throws on failure</small>

### `mmgs.freeAllSols`

```ts
mmgs.freeAllSols(mesh: MeshHandle, sol: SolHandle): void
```

Deallocate an array of solution fields

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |

<small>MMG C symbol: `MMGS_Free_allSols` — return: throws on failure</small>

### `mmgs.freeNames`

```ts
mmgs.freeNames(mesh: MeshHandle, met: SolHandle, ls: SolHandle | null): void
```

Free file-name strings (shim over MMGS_Free_names).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |
| `ls` | `SolHandle | null` |

<small>MMG C symbol: `mmgjs_MMGS_Free_names` — return: throws on failure</small>

### `mmgs.freeSolutions`

```ts
mmgs.freeSolutions(mesh: MeshHandle, sol: SolHandle): void
```

Free a solution.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |

<small>MMG C symbol: `MMGS_Free_solutions` — return: no return value</small>

### `mmgs.freeStructures`

```ts
mmgs.freeStructures(mesh: MeshHandle, met: SolHandle, ls: SolHandle | null): void
```

Free mesh/sol arrays but keep the structures (shim over MMGS_Free_structures).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |
| `ls` | `SolHandle | null` |

<small>MMG C symbol: `mmgjs_MMGS_Free_structures` — return: throws on failure</small>

### `mmgs.getAdjaTri`

```ts
mmgs.getAdjaTri(mesh: MeshHandle, kel: number): { listri: Int32Array }
```

Return adjacent triangles of a triangle. Find the indices of the 3 adjacent elements of triangle \a kel. \f$v_i = 0\f$ if the \f$i^{th}\f$ face has no adjacent element (so we are on a boundary face).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `kel` | `number` |

<small>MMG C symbol: `MMGS_Get_adjaTri` — return: throws on failure</small>

### `mmgs.getAdjaVerticesFast`

```ts
mmgs.getAdjaVerticesFast(mesh: MeshHandle, ip: number, start: number): { value: number; lispoi: Int32Array }
```

Find adjacent vertices of a triangle. Find the indices of the adjacent vertices of the vertex \a ip of the triangle \a start.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `ip` | `number` |
| `start` | `number` |

<small>MMG C symbol: `MMGS_Get_adjaVerticesFast` — return: returns the raw integer value</small>

### `mmgs.getByIdxVertex`

```ts
mmgs.getByIdxVertex(mesh: MeshHandle, idx: number): { c0: number; c1: number; c2: number; ref: number; isCorner: number; isRequired: number }
```

Get the coordinates and reference of a specific vertex in the mesh. This function retrieves the coordinates \a c0, \a c1, \a c2 and reference \a ref of vertex \a idx of mesh, as well as its "corner" and "required" attributes.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `idx` | `number` |

<small>MMG C symbol: `MMGS_GetByIdx_vertex` — return: throws on failure</small>

### `mmgs.getEdge`

```ts
mmgs.getEdge(mesh: MeshHandle): { e0: number; e1: number; ref: number; isRidge: number; isRequired: number }
```

Get the vertices, reference, and attributes of the next edge in the mesh. This function retrieves the extremities \a e0, \a e1, reference \a ref, and attributes of the next edge of \a mesh. It is meant to be called in a loop over all edges. When it has been called as many times as there are edges in the mesh, the internal edge counter will be reset.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |

<small>MMG C symbol: `MMGS_Get_edge` — return: throws on failure</small>

### `mmgs.getEdges`

```ts
mmgs.getEdges(mesh: MeshHandle, na: number): { edges: Int32Array; refs: Int32Array; areRidges: Int32Array; areRequired: Int32Array }
```

Get vertices, references and attributes of all edges in the mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `na` | `number (size of the output arrays)` |

<small>MMG C symbol: `MMGS_Get_edges` — return: throws on failure</small>

### `mmgs.getIparameter`

```ts
mmgs.getIparameter(mesh: MeshHandle, iparam: number): void
```

Get the value of an integer parameter of the remesher. This function retrieves the value of integer parameter \a iparam (see \ref MMGS_Param for a list of parameters). It returns the value of the parameter, or zero if the value of \a iparam is not recognized.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `iparam` | `number` |

<small>MMG C symbol: `MMGS_Get_iparameter` — return: throws on failure</small>

### `mmgs.getIthSolInSolsAtVertices`

```ts
mmgs.getIthSolInSolsAtVertices(sol: SolHandle, i: number, pos: number, n: number): { s: Float64Array }
```

Get one out of several solutions at a specific vertex. This function retreives the value of field \a i of the solution array at vertex \a pos. (\a pos from 1 to the number of vertices included and \a i from 1 to the number of solutions). It works for any type of solution; the types are inferred from \a sol.

| Parameter | Type |
|-----------|------|
| `sol` | `SolHandle` |
| `i` | `number` |
| `pos` | `number` |
| `n` | `number (size of the output arrays)` |

<small>MMG C symbol: `MMGS_Get_ithSol_inSolsAtVertices` — return: throws on failure</small>

### `mmgs.getIthSolsInSolsAtVertices`

```ts
mmgs.getIthSolsInSolsAtVertices(sol: SolHandle, i: number, n: number): { s: Float64Array }
```

Get one out of several solutions at all vertices in the mesh. This function retrieves the values of field \a i of the solution array \a sol (\a i from 1 to \a the number of solutions). It works for any type of solution; the type is inferred from \a sol.

| Parameter | Type |
|-----------|------|
| `sol` | `SolHandle` |
| `i` | `number` |
| `n` | `number (size of the output arrays)` |

<small>MMG C symbol: `MMGS_Get_ithSols_inSolsAtVertices` — return: throws on failure</small>

### `mmgs.getMeshSize`

```ts
mmgs.getMeshSize(mesh: MeshHandle): { np: number; nt: number; na: number }
```

recover data */ /** Get the number of vertices, triangles, and edges of the mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |

<small>MMG C symbol: `MMGS_Get_meshSize` — return: throws on failure</small>

### `mmgs.getNonBdyEdge`

```ts
mmgs.getNonBdyEdge(mesh: MeshHandle, idx: number): { e0: number; e1: number; ref: number }
```

Get vertices and reference of a non-boundary edge. This function returns the vertices \a e0, \a e1 and reference \a ref of the non boundary edge \a idx. An edge is boundary if it is located at the interface of 2 domains with different references, if it belongs to one triangle only or if it is a singular edge (ridge or required).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `idx` | `number` |

<small>MMG C symbol: `MMGS_Get_nonBdyEdge` — return: throws on failure</small>

### `mmgs.getNormalAtVertex`

```ts
mmgs.getNormalAtVertex(mesh: MeshHandle, k: number): { n0: number; n1: number; n2: number }
```

Get the normal orientation at an edge. This function retrieves the normal (n0,n1,n2) at vertex \a k.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMGS_Get_normalAtVertex` — return: throws on failure</small>

### `mmgs.getNumberOfNonBdyEdges`

```ts
mmgs.getNumberOfNonBdyEdges(mesh: MeshHandle): { nb_edges: number }
```

Get the number of non-boundary edges. Get the number of non-boundary edges (for DG methods for example). An edge is boundary if it is located at the interface of 2 domains with different references, if it belongs to one triangle only or if it is a singular edge (ridge or required). Append these edges to the list of edges.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |

<small>MMG C symbol: `MMGS_Get_numberOfNonBdyEdges` — return: throws on failure</small>

### `mmgs.getScalarSol`

```ts
mmgs.getScalarSol(met: SolHandle): { s: number }
```

Get the next element of a scalar solution structure. This function retrieves the next element \a s of the solution field \a met. It is meant to be called in a loop over all elements. When it has been called as many times as there are elements in the solution, the internal loop counter will be reset.

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |

<small>MMG C symbol: `MMGS_Get_scalarSol` — return: throws on failure</small>

### `mmgs.getScalarSols`

```ts
mmgs.getScalarSols(met: SolHandle, np: number): { s: Float64Array }
```

Get all elements of a scalar solution structure.

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |
| `np` | `number (size of the output arrays)` |

<small>MMG C symbol: `MMGS_Get_scalarSols` — return: throws on failure</small>

### `mmgs.getSolSize`

```ts
mmgs.getSolSize(mesh: MeshHandle, sol: SolHandle): { typEntity: number; np: number; typSol: number }
```

Get the number of elements, dimension, and type of a solution.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |

<small>MMG C symbol: `MMGS_Get_solSize` — return: throws on failure</small>

### `mmgs.getSolsAtVerticesSize`

```ts
mmgs.getSolsAtVerticesSize(mesh: MeshHandle, sol: SolHandle): { nsols: number; nentities: number; typSol: Int32Array }
```

Get the number of elements, type, and dimensions of several solutions defined on vertices.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |

<small>MMG C symbol: `MMGS_Get_solsAtVerticesSize` — return: throws on failure</small>

### `mmgs.getTensorSol`

```ts
mmgs.getTensorSol(met: SolHandle): { m11: number; m12: number; m13: number; m22: number; m23: number; m33: number }
```

Get the next element of a tensor solution structure. This function retrieves the next element \f$(m_{11},m_{12},m_{13},m_{22},m_{23},m_{33})\f$ of a tensor-valued solution field. It is meant to be called in a loop over all vertices. When it has been called as many times as there are elements in the solution, the internal loop counter will be reset.

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |

<small>MMG C symbol: `MMGS_Get_tensorSol` — return: throws on failure</small>

### `mmgs.getTensorSols`

```ts
mmgs.getTensorSols(met: SolHandle, np: number): { sols: Float64Array }
```

Get all elements of a tensor solution field.

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |
| `np` | `number (size of the output arrays)` |

<small>MMG C symbol: `MMGS_Get_tensorSols` — return: throws on failure</small>

### `mmgs.getTriangle`

```ts
mmgs.getTriangle(mesh: MeshHandle): { v0: number; v1: number; v2: number; ref: number; isRequired: number }
```

Get the vertices, reference, and required attribute of the next triangle in the mesh. This function retrieves the vertices \a v0, \a v1, \a v2, reference \a ref, and required attribute \a isRequired of the next triangle of \a mesh. It is meant to be called in a loop over all triangles. When it has been called as many times as there are triangles, the internal loop counter will be reset.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |

<small>MMG C symbol: `MMGS_Get_triangle` — return: throws on failure</small>

### `mmgs.getTriangles`

```ts
mmgs.getTriangles(mesh: MeshHandle, nt: number): { tria: Int32Array; refs: Int32Array; areRequired: Int32Array }
```

Get the vertices, references, and required attributes of all triangles in the mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `nt` | `number (size of the output arrays)` |

<small>MMG C symbol: `MMGS_Get_triangles` — return: throws on failure</small>

### `mmgs.getVectorSol`

```ts
mmgs.getVectorSol(met: SolHandle): { vx: number; vy: number; vz: number }
```

Get the next element of a vector solution structure. This function retrieves the next vector-valued element \f$(v_x,v_y,vz)\f$ of a solution field. It is meant to be called in a loop over all elements. When it has been called as many times as there are elements in the solution, the internal loop counter will be reset.

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |

<small>MMG C symbol: `MMGS_Get_vectorSol` — return: throws on failure</small>

### `mmgs.getVectorSols`

```ts
mmgs.getVectorSols(met: SolHandle, np: number): { sols: Float64Array }
```

Get all elements of a vector solution structure. This function retrieves all elements of a vector-valued solution field.

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |
| `np` | `number (size of the output arrays)` |

<small>MMG C symbol: `MMGS_Get_vectorSols` — return: throws on failure</small>

### `mmgs.getVertex`

```ts
mmgs.getVertex(mesh: MeshHandle): { c0: number; c1: number; c2: number; ref: number; isCorner: number; isRequired: number }
```

Get the coordinates \a c0, \a c1,\a c2 and reference \a ref of the next vertex of \a mesh. This function retrieves the coordinates \a c0, \a c1,\a c2, reference \a ref, and attributes of the next vertex of a mesh. It is meant to be used in a loop over all vertices. When this function has been called as many times as there are vertices, the internal loop counter will be reset. To obtain data for a specific vertex, the \ref MMGS_GetByIdx_vertex function can be used instead.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |

<small>MMG C symbol: `MMGS_Get_vertex` — return: throws on failure</small>

### `mmgs.getVertices`

```ts
mmgs.getVertices(mesh: MeshHandle, np: number): { vertices: Float64Array; refs: Int32Array; areCorners: Int32Array; areRequired: Int32Array }
```

Get the coordinates, references and attributes of all vertices in the mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `np` | `number (size of the output arrays)` |

<small>MMG C symbol: `MMGS_Get_vertices` — return: throws on failure</small>

### `mmgs.initFileNames`

```ts
mmgs.initFileNames(mesh: MeshHandle, sol: SolHandle): void
```

Initialize file names to their default values.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |

<small>MMG C symbol: `MMGS_Init_fileNames` — return: no return value</small>

### `mmgs.initMesh`

```ts
mmgs.initMesh(mesh: MeshHandle, met: SolHandle, ls: SolHandle | null): void
```

Allocate and initialize the mesh and solution structures (fixed-arity shim over the variadic MMGS_Init_mesh).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |
| `ls` | `SolHandle | null` |

<small>MMG C symbol: `mmgjs_MMGS_Init_mesh` — return: throws on failure</small>

### `mmgs.initParameters`

```ts
mmgs.initParameters(mesh: MeshHandle): void
```

Initialize the input parameters. Initialization of the input parameters (stored in the Info structure).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |

<small>MMG C symbol: `MMGS_Init_parameters` — return: no return value</small>

### `mmgs.loadAllSols`

```ts
mmgs.loadAllSols(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Load one or more solutions in a solution file in medit file format.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMGS_loadAllSols` — return: throws on failure</small>

### `mmgs.loadGenericMesh`

```ts
mmgs.loadGenericMesh(mesh: MeshHandle, met: SolHandle, sol: SolHandle, filename: string): void
```

Load a mesh and all data from a file. The format will be guessed from the filename extension.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMGS_loadGenericMesh` — return: throws on failure</small>

### `mmgs.loadMesh`

```ts
mmgs.loadMesh(mesh: MeshHandle, filename: string): void
```

Load a mesh (in .mesh/.mesb format) from file. This function reads .mesh (ASCII) and .meshb (binary) files. If the name contains ".mesh" the file will be read as an ASCII file and if the name contains .meshb it be read as a binary file. If the file contains neither of these strings the function will first try to open "[filename].meshb" and if this fails it will try "[filename].mesh".

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMGS_loadMesh` — return: throws on failure</small>

### `mmgs.loadMshMesh`

```ts
mmgs.loadMshMesh(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Load a mesh and possibly a solution in .msh format from file. Read a mesh and optionally one data field in MSH file format (.msh extension). We read only low-order vertices, edges, triangles, quadrangles, tetrahedra and prisms.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMGS_loadMshMesh` — return: throws on failure</small>

### `mmgs.loadMshMeshAndAllData`

```ts
mmgs.loadMshMeshAndAllData(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Load a mesh and all data from a file in MSH format. Read a mesh and multiple data in MSH file format (.msh extension). We read only low-order vertices, edges, triangles, quadrangles, tetrahedra and prisms.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMGS_loadMshMesh_and_allData` — return: throws on failure</small>

### `mmgs.loadSol`

```ts
mmgs.loadSol(mesh: MeshHandle, met: SolHandle, filename: string): void
```

Load a metric field (or other solution) in medit's .sol format. Load metric field. The solution file (in medit file format) must contain only 1 solution: the metric.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMGS_loadSol` — return: throws on failure</small>

### `mmgs.loadVtkMesh`

```ts
mmgs.loadVtkMesh(mesh: MeshHandle, met: SolHandle, sol: SolHandle, filename: string): void
```

Load a mesh and possibly data in VTK format from file. Read a mesh and optionally one data field in VTK vtk file format (.vtk extension). We read only low-order vertices, edges, triangles and quadrangles.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMGS_loadVtkMesh` — return: throws on failure</small>

### `mmgs.loadVtkMeshAndAllData`

```ts
mmgs.loadVtkMeshAndAllData(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Load a mesh and multiple solutions in VTK format from file. Read a mesh and multiple data field in VTK vtk file format (.vtk extension). We read only low-order vertices, edges, triangles and quadrangles.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMGS_loadVtkMesh_and_allData` — return: throws on failure</small>

### `mmgs.loadVtpMesh`

```ts
mmgs.loadVtpMesh(mesh: MeshHandle, met: SolHandle, sol: SolHandle, filename: string): void
```

Load a mesh and optionally a solution in VTP (VTK) format from file. This function reads a mesh and optionally one data field in VTK vtp file format (.vtp extension). We read only low-order vertices, edges, triangles and quadrangles.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMGS_loadVtpMesh` — return: throws on failure</small>

### `mmgs.loadVtpMeshAndAllData`

```ts
mmgs.loadVtpMeshAndAllData(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Load a mesh and multiple solutions in VTP (VTK) format from file. Read a mesh and multiple data fields in VTK vtp file format (.vtp extension). We read only low-order vertices, edges, triangles and quadrangles.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMGS_loadVtpMesh_and_allData` — return: throws on failure</small>

### `mmgs.loadVtuMesh`

```ts
mmgs.loadVtuMesh(mesh: MeshHandle, met: SolHandle, sol: SolHandle, filename: string): void
```

Load a mesh and possibly data in VTU (VTK) format from file. Read a mesh and optionally one data field in VTK vtu file format (.vtu extension). We read only low-order vertices, edges, triangles and quadrangles.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMGS_loadVtuMesh` — return: throws on failure</small>

### `mmgs.loadVtuMeshAndAllData`

```ts
mmgs.loadVtuMeshAndAllData(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Load a mesh and multiple solutions in VTU (VTK) format from file. Read a mesh and multiple data field in VTK vtu file format (.vtu extension). We read only low-order vertices, edges, triangles and quadrangles.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMGS_loadVtuMesh_and_allData` — return: throws on failure</small>

### `mmgs.mmgslib`

```ts
mmgs.mmgslib(mesh: MeshHandle, met: SolHandle): number
```

Main "program" for mesh adaptation. Main program for the library.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |

<small>MMG C symbol: `MMGS_mmgslib` — return: returns `MMG5_SUCCESS`/`MMG5_LOWFAILURE`; throws on `MMG5_STRONGFAILURE` — alias: `mmgs.remesh()`</small>

### `mmgs.mmgsls`

```ts
mmgs.mmgsls(mesh: MeshHandle, sol: SolHandle, met: SolHandle): number
```

Main "program" for level-set discretization. Main program for level set discretization library. If a metric \a met is provided, use it to adapt the mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `met` | `SolHandle` |

<small>MMG C symbol: `MMGS_mmgsls` — return: returns `MMG5_SUCCESS`/`MMG5_LOWFAILURE`; throws on `MMG5_STRONGFAILURE` — alias: `mmgs.levelset()`</small>

### `mmgs.saveAllSols`

```ts
mmgs.saveAllSols(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Save one or more solutions in a solution file in medit file format.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMGS_saveAllSols` — return: throws on failure</small>

### `mmgs.saveGenericMesh`

```ts
mmgs.saveGenericMesh(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Save mesh data in a file whose format depends on the filename extension.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMGS_saveGenericMesh` — return: throws on failure</small>

### `mmgs.saveMesh`

```ts
mmgs.saveMesh(mesh: MeshHandle, filename: string): void
```

Save a mesh in .mesh or .meshb format. This function saves a mesh in .mesh or .meshb format (depending on the filename extension).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMGS_saveMesh` — return: throws on failure</small>

### `mmgs.saveMshMesh`

```ts
mmgs.saveMshMesh(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Write mesh and optionally one data field in MSH file format (.msh extension). The file is saved in ASCII format for .msh extension, an in binary format for a .mshb extension.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMGS_saveMshMesh` — return: throws on failure</small>

### `mmgs.saveMshMeshAndAllData`

```ts
mmgs.saveMshMeshAndAllData(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Save a mesh and multiple data fields in MSH format, ascii or binary depending on the filename extension. This function saves a mesh and multiple data fields (that are considered as solutions and not metrics, thus, we do nothing over the ridge vertices) in MSH file format (.msh extension). The file is saved in ASCII format for .msh extension and in binary format for a .mshb extension.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMGS_saveMshMesh_and_allData` — return: throws on failure</small>

### `mmgs.saveSol`

```ts
mmgs.saveSol(mesh: MeshHandle, met: SolHandle, filename: string): void
```

Write an isotropic or anisotropic metric in medit file format.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMGS_saveSol` — return: throws on failure</small>

### `mmgs.saveVtkMesh`

```ts
mmgs.saveVtkMesh(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Write mesh and optionally one data field in Vtk file format (.vtk extension).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMGS_saveVtkMesh` — return: throws on failure</small>

### `mmgs.saveVtkMeshAndAllData`

```ts
mmgs.saveVtkMeshAndAllData(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Save a mesh and multiple data fields in VTK format. This function writes a mesh and a list of data fields in Vtk file format (.vtk extension).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMGS_saveVtkMesh_and_allData` — return: throws on failure</small>

### `mmgs.saveVtpMesh`

```ts
mmgs.saveVtpMesh(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Save a mesh and optionally one data field in VTP format. This function writes a mesh and optionally one data in polydata Vtk file format (.vtp extension).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMGS_saveVtpMesh` — return: throws on failure</small>

### `mmgs.saveVtpMeshAndAllData`

```ts
mmgs.saveVtpMeshAndAllData(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Save a mesh and multiple data fields in VTP format. This function writes a mesh and multiple data fields in polydata Vtk file format (.vtp extension).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMGS_saveVtpMesh_and_allData` — return: throws on failure</small>

### `mmgs.saveVtuMesh`

```ts
mmgs.saveVtuMesh(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Write mesh and optionally one data field vtu Vtk file format (.vtu extension).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMGS_saveVtuMesh` — return: throws on failure</small>

### `mmgs.saveVtuMeshAndAllData`

```ts
mmgs.saveVtuMeshAndAllData(mesh: MeshHandle, sol: SolHandle, filename: string): void
```

Write a mesh and multiple data fields in vtu Vtk file format (.vtu extension).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `filename` | `string` |

<small>MMG C symbol: `MMGS_saveVtuMesh_and_allData` — return: throws on failure</small>

### `mmgs.setCommonFunc`

```ts
mmgs.setCommonFunc(): void
```

Set common function pointers between mmgs and mmg3d to the matching mmgs functions.

<small>MMG C symbol: `MMGS_Set_commonFunc` — return: no return value</small>

### `mmgs.setConstantSize`

```ts
mmgs.setConstantSize(mesh: MeshHandle, met: SolHandle): void
```

Compute an isotropic size map according to the mean of the length of the edges passing through a vertex. / LIBMMGS_EXPORT extern int (*MMGS_doSol)(MMG5_pMesh mesh,MMG5_pSol met); /** Compute a constant size map. This function computes a constant size map according to mesh->info.hsiz, mesh->info.hmin and mesh->info.hmax. It updates these 3 values if they are not compatible.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |

<small>MMG C symbol: `MMGS_Set_constantSize` — return: throws on failure</small>

### `mmgs.setCorner`

```ts
mmgs.setCorner(mesh: MeshHandle, k: number): void
```

Assign the "corner" attribute to a vertex. This function sets the corner attribute at vertex \a pos (\a pos from 1 to the number of vertices included).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMGS_Set_corner` — return: throws on failure</small>

### `mmgs.setDparameter`

```ts
mmgs.setDparameter(mesh: MeshHandle, sol: SolHandle, dparam: number, val: number): void
```

set a real-valued parameter of the remesher This function sets the double parameter \a dparam to value \a val.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `dparam` | `number` |
| `val` | `number` |

<small>MMG C symbol: `MMGS_Set_dparameter` — return: throws on failure</small>

### `mmgs.setEdge`

```ts
mmgs.setEdge(mesh: MeshHandle, v0: number, v1: number, ref: number, pos: number): void
```

Set the vertices and reference of one edge in the mesh. Assigns vertices \a v0, \a v1 and reference \a ref to the edge at position \a pos in the mesh structure (\a pos from 1 to the number of edges included).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `v0` | `number` |
| `v1` | `number` |
| `ref` | `number` |
| `pos` | `number` |

<small>MMG C symbol: `MMGS_Set_edge` — return: throws on failure</small>

### `mmgs.setEdges`

```ts
mmgs.setEdges(mesh: MeshHandle, edges: number[] | Int32Array, refs: number[] | Int32Array | null): void
```

Set the vertices and references of all edges in a mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `edges` | `number[] | Int32Array` |
| `refs` | `number[] | Int32Array | null` |

<small>MMG C symbol: `MMGS_Set_edges` — return: throws on failure</small>

### `mmgs.setInputMeshName`

```ts
mmgs.setInputMeshName(mesh: MeshHandle, meshin: string): void
```

Set the name of the input mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `meshin` | `string` |

<small>MMG C symbol: `MMGS_Set_inputMeshName` — return: throws on failure</small>

### `mmgs.setInputParamName`

```ts
mmgs.setInputParamName(mesh: MeshHandle, fparamin: string): void
```

Set the name of the input parameter file.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `fparamin` | `string` |

<small>MMG C symbol: `MMGS_Set_inputParamName` — return: throws on failure</small>

### `mmgs.setInputSolName`

```ts
mmgs.setInputSolName(mesh: MeshHandle, sol: SolHandle, solin: string): void
```

Set the name of the input solution file.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `solin` | `string` |

<small>MMG C symbol: `MMGS_Set_inputSolName` — return: throws on failure</small>

### `mmgs.setIparameter`

```ts
mmgs.setIparameter(mesh: MeshHandle, sol: SolHandle, iparam: number, val: number): void
```

functions to set parameters */ /** set an integer parameter of the remesher This function sets integer parameter \a iparam to value \a val.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `iparam` | `number` |
| `val` | `number` |

<small>MMG C symbol: `MMGS_Set_iparameter` — return: throws on failure</small>

### `mmgs.setIthSolInSolsAtVertices`

```ts
mmgs.setIthSolInSolsAtVertices(sol: SolHandle, i: number, s: number[] | Float64Array, pos: number): void
```

Set a single element of one out of multiple solution fields that are defined on vertices. Set values of the solution at field \a i of the solution array and at position \pos (\a pos from 1 to the number of vertices included and \a i from 1 to the number of solutions). The type of solution is determined from \a sol.

| Parameter | Type |
|-----------|------|
| `sol` | `SolHandle` |
| `i` | `number` |
| `s` | `number[] | Float64Array` |
| `pos` | `number` |

<small>MMG C symbol: `MMGS_Set_ithSol_inSolsAtVertices` — return: throws on failure</small>

### `mmgs.setIthSolsInSolsAtVertices`

```ts
mmgs.setIthSolsInSolsAtVertices(sol: SolHandle, i: number, s: number[] | Float64Array): void
```

Set all elements of one out of multiple solution fields that are defined on vertices. Set values of the solution at field \a i of the solution array (\a i from 1 to the number of solutions). The type of solution is determined from \a sol.

| Parameter | Type |
|-----------|------|
| `sol` | `SolHandle` |
| `i` | `number` |
| `s` | `number[] | Float64Array` |

<small>MMG C symbol: `MMGS_Set_ithSols_inSolsAtVertices` — return: throws on failure</small>

### `mmgs.setLocalParameter`

```ts
mmgs.setLocalParameter(mesh: MeshHandle, sol: SolHandle, typ: number, ref: number, hmin: number, hmax: number, hausd: number): void
```

set a local parameter Set local parameters: set the hausdorff distance at \a hausd, the minmal edge length at \a hmin and the maximal edge length at \a hmax for all elements of type \a typ and reference \a ref.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `typ` | `number` |
| `ref` | `number` |
| `hmin` | `number` |
| `hmax` | `number` |
| `hausd` | `number` |

<small>MMG C symbol: `MMGS_Set_localParameter` — return: throws on failure</small>

### `mmgs.setLsBaseReference`

```ts
mmgs.setLsBaseReference(mesh: MeshHandle, sol: SolHandle, br: number): void
```

Set a new level-set base reference. Set a new level-set base reference of ref \a br in level-set discretization mode. Base references are boundary conditions to which an implicit domain can be attached. All implicit volumes that are not attached to listed base references are deleted as spurious volumes by the \a rmc option.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `br` | `number` |

<small>MMG C symbol: `MMGS_Set_lsBaseReference` — return: throws on failure</small>

### `mmgs.setMeshSize`

```ts
mmgs.setMeshSize(mesh: MeshHandle, np: number, nt: number, na: number): void
```

Set the number of vertices, triangles and edges of the mesh and allocate the associated tables. If called again, this function resets the whole mesh to reallocate it at the new size

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `np` | `number` |
| `nt` | `number` |
| `na` | `number` |

<small>MMG C symbol: `MMGS_Set_meshSize` — return: throws on failure</small>

### `mmgs.setMultiMat`

```ts
mmgs.setMultiMat(mesh: MeshHandle, sol: SolHandle, ref: number, split: number, rmin: number, rplus: number): void
```

Set the reference mapping for the elements of reference \a ref in level-set discretization mode. With this function you can determine which references will be given to the triangles on both sides of the level set, after discretization. Negative and positive here refer to areas where the function is smaller or larger, respectively, than the isovalue of the level set.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `ref` | `number` |
| `split` | `number` |
| `rmin` | `number` |
| `rplus` | `number` |

<small>MMG C symbol: `MMGS_Set_multiMat` — return: throws on failure</small>

### `mmgs.setNormalAtVertex`

```ts
mmgs.setNormalAtVertex(mesh: MeshHandle, k: number, n0: number, n1: number, n2: number): void
```

Set the normal orientation at a single vertex. Set normal (n0,n1,n2) at vertex \a k.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |
| `n0` | `number` |
| `n1` | `number` |
| `n2` | `number` |

<small>MMG C symbol: `MMGS_Set_normalAtVertex` — return: throws on failure</small>

### `mmgs.setOutputMeshName`

```ts
mmgs.setOutputMeshName(mesh: MeshHandle, meshout: string): void
```

Set the name of the output mesh file.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `meshout` | `string` |

<small>MMG C symbol: `MMGS_Set_outputMeshName` — return: throws on failure</small>

### `mmgs.setOutputSolName`

```ts
mmgs.setOutputSolName(mesh: MeshHandle, sol: SolHandle, solout: string): void
```

Set the name of the output solution file.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `solout` | `string` |

<small>MMG C symbol: `MMGS_Set_outputSolName` — return: throws on failure</small>

### `mmgs.setRequiredEdge`

```ts
mmgs.setRequiredEdge(mesh: MeshHandle, k: number): void
```

Assign the "required" attribute to an edge. This function makes edge \a k a required edge. Required edges will not be modified by the remesher.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMGS_Set_requiredEdge` — return: throws on failure</small>

### `mmgs.setRequiredTriangle`

```ts
mmgs.setRequiredTriangle(mesh: MeshHandle, k: number): void
```

Assign the "required" attribute to a triangle. This function sets the required attribute at triangle \a k.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMGS_Set_requiredTriangle` — return: throws on failure</small>

### `mmgs.setRequiredVertex`

```ts
mmgs.setRequiredVertex(mesh: MeshHandle, k: number): void
```

Assign the "required" attribute to a vertex. This function sets the required attribute at vertex \a k. Vertices with this attribute will not be modified by the remesher.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMGS_Set_requiredVertex` — return: throws on failure</small>

### `mmgs.setRidge`

```ts
mmgs.setRidge(mesh: MeshHandle, k: number): void
```

Assign the "ridge" attribute to an edge. This function gives the ridge attribute to edge \a k. This influences how this edge is treated by the remesher.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMGS_Set_ridge` — return: throws on failure</small>

### `mmgs.setScalarSol`

```ts
mmgs.setScalarSol(met: SolHandle, s: number, pos: number): void
```

Get the quality measure of a triangle. / double MMGS_Get_triangleQuality(MMG5_pMesh mesh, MMG5_pSol met, MMG5_int k); /** Set a single element of a scalar solution structure. This function sets the scalar value \a s at position \a pos in the solution structure (\a pos from 1 to the number of vertices included).

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |
| `s` | `number` |
| `pos` | `number` |

<small>MMG C symbol: `MMGS_Set_scalarSol` — return: throws on failure</small>

### `mmgs.setScalarSols`

```ts
mmgs.setScalarSols(met: SolHandle, s: number[] | Float64Array): void
```

Set the values of all elements of a scalar solution structure.

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |
| `s` | `number[] | Float64Array` |

<small>MMG C symbol: `MMGS_Set_scalarSols` — return: throws on failure</small>

### `mmgs.setSolSize`

```ts
mmgs.setSolSize(mesh: MeshHandle, sol: SolHandle, typEntity: number, np: number, typSol: number): void
```

Initialize an array of solution fields: set dimension, types and number of fields. To use to initialize an array of solution fields (not used by Mmg itself).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `typEntity` | `number` |
| `np` | `number` |
| `typSol` | `number` |

<small>MMG C symbol: `MMGS_Set_solSize` — return: throws on failure</small>

### `mmgs.setSolsAtVerticesSize`

```ts
mmgs.setSolsAtVerticesSize(mesh: MeshHandle, sol: SolHandle, nsols: number, nentities: number, typSol: number[] | Int32Array): void
```

Initialize an array of solution fields defined at vertices: set dimension, types and number of fields. To use to initialize an array of solution fields (not used by Mmg itself).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `sol` | `SolHandle` |
| `nsols` | `number` |
| `nentities` | `number` |
| `typSol` | `number[] | Int32Array` |

<small>MMG C symbol: `MMGS_Set_solsAtVerticesSize` — return: throws on failure</small>

### `mmgs.setTensorSol`

```ts
mmgs.setTensorSol(met: SolHandle, m11: number, m12: number, m13: number, m22: number, m23: number, m33: number, pos: number): void
```

Set a single element of a tensor solution structure. This function sets a tensor value at position \a pos in solution structure (\a pos from 1 to the number of vertices included).

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |
| `m11` | `number` |
| `m12` | `number` |
| `m13` | `number` |
| `m22` | `number` |
| `m23` | `number` |
| `m33` | `number` |
| `pos` | `number` |

<small>MMG C symbol: `MMGS_Set_tensorSol` — return: throws on failure</small>

### `mmgs.setTensorSols`

```ts
mmgs.setTensorSols(met: SolHandle, sols: number[] | Float64Array): void
```

Set all elements of a tensor solution structure.

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |
| `sols` | `number[] | Float64Array` |

<small>MMG C symbol: `MMGS_Set_tensorSols` — return: throws on failure</small>

### `mmgs.setTriangle`

```ts
mmgs.setTriangle(mesh: MeshHandle, v0: number, v1: number, v2: number, ref: number, pos: number): void
```

Set the coordinates and reference of a single triangle. This function sets a triangle with vertices \a v0, \a v1, \a v2 and reference \a ref at position \a pos in the mesh structure (\a pos from 1 to the number of triangles included).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `v0` | `number` |
| `v1` | `number` |
| `v2` | `number` |
| `ref` | `number` |
| `pos` | `number` |

<small>MMG C symbol: `MMGS_Set_triangle` — return: throws on failure</small>

### `mmgs.setTriangles`

```ts
mmgs.setTriangles(mesh: MeshHandle, tria: number[] | Int32Array, refs: number[] | Int32Array | null): void
```

Set the vertices and references of all triangles in the mesh.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `tria` | `number[] | Int32Array` |
| `refs` | `number[] | Int32Array | null` |

<small>MMG C symbol: `MMGS_Set_triangles` — return: throws on failure</small>

### `mmgs.setVectorSol`

```ts
mmgs.setVectorSol(met: SolHandle, vx: number, vy: number, vz: number, pos: number): void
```

Set a single element of a vector solution structure. This function sets the vectorial value \f$(v_x,v_y,v_z)\f$ at position \a pos in the solution structure (\a pos from 1 to the number of vertices included).

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |
| `vx` | `number` |
| `vy` | `number` |
| `vz` | `number` |
| `pos` | `number` |

<small>MMG C symbol: `MMGS_Set_vectorSol` — return: throws on failure</small>

### `mmgs.setVectorSols`

```ts
mmgs.setVectorSols(met: SolHandle, sols: number[] | Float64Array): void
```

Set all elements of a vector solution structure. This function sets a vector-valued solution at each element of solution structure.

| Parameter | Type |
|-----------|------|
| `met` | `SolHandle` |
| `sols` | `number[] | Float64Array` |

<small>MMG C symbol: `MMGS_Set_vectorSols` — return: throws on failure</small>

### `mmgs.setVertex`

```ts
mmgs.setVertex(mesh: MeshHandle, c0: number, c1: number, c2: number, ref: number, pos: number): void
```

Set the coordinates of a single vertex. Set vertex coordinates \a c0, \a c1,\a c2 and reference \a ref at position \a pos in the mesh structure (\a pos from 1 to the number of vertices included).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `c0` | `number` |
| `c1` | `number` |
| `c2` | `number` |
| `ref` | `number` |
| `pos` | `number` |

<small>MMG C symbol: `MMGS_Set_vertex` — return: throws on failure</small>

### `mmgs.setVertices`

```ts
mmgs.setVertices(mesh: MeshHandle, vertices: number[] | Float64Array, refs: number[] | Int32Array | null): void
```

Set the coordinates and references of all vertices in a mesh

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `vertices` | `number[] | Float64Array` |
| `refs` | `number[] | Int32Array | null` |

<small>MMG C symbol: `MMGS_Set_vertices` — return: throws on failure</small>

### `mmgs.setfunc`

```ts
mmgs.setfunc(mesh: MeshHandle, met: SolHandle): void
```

To associate function pointers without calling MMGS_mmgslib */ /** Set function pointers for caltet, lenedg, defsiz and gradsiz.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `met` | `SolHandle` |

<small>MMG C symbol: `MMGS_setfunc` — return: no return value</small>

### `mmgs.unsetCorner`

```ts
mmgs.unsetCorner(mesh: MeshHandle, k: number): void
```

Remove the "corner" attribute from a vertex. This function removes the corner attribute from vertex \a pos (from 1 to the number of vertices included).

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMGS_Unset_corner` — return: throws on failure</small>

### `mmgs.unsetRequiredEdge`

```ts
mmgs.unsetRequiredEdge(mesh: MeshHandle, k: number): void
```

Remove the "required" attribute from an edge. This function removes the "required" attribute from edge \a k.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMGS_Unset_requiredEdge` — return: throws on failure</small>

### `mmgs.unsetRequiredTriangle`

```ts
mmgs.unsetRequiredTriangle(mesh: MeshHandle, k: number): void
```

Remove the "required" attribute from a vertex. This function removes the required attribute from triangle \a k.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMGS_Unset_requiredTriangle` — return: throws on failure</small>

### `mmgs.unsetRequiredVertex`

```ts
mmgs.unsetRequiredVertex(mesh: MeshHandle, k: number): void
```

Remove the "required" attribute from a vertex. This function removes the required attribute from vertex \a k.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMGS_Unset_requiredVertex` — return: throws on failure</small>

### `mmgs.unsetRidge`

```ts
mmgs.unsetRidge(mesh: MeshHandle, k: number): void
```

Remove the "ridge" attribute from an edge. This function removes the ridge attribute from edge \a k.

| Parameter | Type |
|-----------|------|
| `mesh` | `MeshHandle` |
| `k` | `number` |

<small>MMG C symbol: `MMGS_Unset_ridge` — return: throws on failure</small>

### `mmgs.usage`

```ts
mmgs.usage(prog: string): void
```

Print help for mmgs options.

| Parameter | Type |
|-----------|------|
| `prog` | `string` |

<small>MMG C symbol: `MMGS_usage` — return: throws on failure</small>

## Unsupported functions

These C API entry points are not exposed to JavaScript:

| C symbol | Reason |
|----------|--------|
| `MMG3D_parsar` | explicitly unsupported (struct ptr / CLI-only) |
| `MMG3D_parsop` | explicitly unsupported (struct ptr / CLI-only) |
| `MMG3D_stockOptions` | explicitly unsupported (struct ptr / CLI-only) |
| `MMG3D_destockOptions` | explicitly unsupported (struct ptr / CLI-only) |
| `MMG3D_mmg3dcheck` | explicitly unsupported (struct ptr / CLI-only) |
| `MMG3D_searchqua` | explicitly unsupported (struct ptr / CLI-only) |
| `MMG3D_searchlen` | explicitly unsupported (struct ptr / CLI-only) |
| `MMG2D_loadVect` | explicitly unsupported (struct ptr / CLI-only) |
| `MMG2D_saveVect` | explicitly unsupported (struct ptr / CLI-only) |
| `MMG2D_parsar` | explicitly unsupported (struct ptr / CLI-only) |
| `MMG2D_parsop` | explicitly unsupported (struct ptr / CLI-only) |
| `MMG2D_scaleMesh` | explicitly unsupported (struct ptr / CLI-only) |
| `MMGS_parsar` | explicitly unsupported (struct ptr / CLI-only) |
| `MMGS_stockOptions` | explicitly unsupported (struct ptr / CLI-only) |
| `MMGS_destockOptions` | explicitly unsupported (struct ptr / CLI-only) |
