# Marshalling

The wrapper is a single generic marshaller (`src/runtime.mjs`) driven by a
generated descriptor: each C argument carries a *kind* that says how to
convert it. This page documents those kinds — useful when reading the
[reference](reference.md) or the descriptor itself.

## Input kinds

| Kind | C type | JS type | Notes |
|------|--------|---------|-------|
| `iint` | `int`, `MMG5_int`, enums | `number` | truncated to int32 |
| `idouble` | `double` | `number` | |
| `istring` | `const char*` | `string \| null` | copied into the heap for the call; `null` passes `NULL` |
| `handle` | `MMG5_pMesh`, `MMG5_pSol` (by value) | `MeshHandle` / `SolHandle` | the boxed struct pointer is dereferenced |
| `handleref` | `MMG5_pMesh*`, `MMG5_pSol*` | `MeshHandle` / `SolHandle` | the box itself is passed (init/free shims, `loadAllSols`, ...) |
| `iarrayint` | `MMG5_int*`, `int*` (bulk) | `number[] \| Int32Array \| null` | copied in; MMG reads the length from prior `set*Size` calls |
| `iarraydouble` | `double*` (bulk) | `number[] \| Float64Array \| null` | copied in |

## Output kinds

| Kind | C type | JS result | Notes |
|------|--------|-----------|-------|
| `oint` | `int*`, `MMG5_int*` | `number` | scalar out-param |
| `odouble` | `double*` | `number` | scalar out-param |
| `oarrayint` | `MMG5_int*`, `int*` | `Int32Array` | buffer allocated by the wrapper, copied out |
| `oarraydouble` | `double*` | `Float64Array` | buffer allocated by the wrapper, copied out |

Output array sizes come from one of:

- a **trailing count argument** you pass (e.g.
  `getVertices(mesh, np)` allocates `3*np` doubles + `np`-sized int arrays;
  the count name is shown in the reference), or
- a **fixed size** from the C declaration (e.g. `getAdjaTet` fills
  `listet[4]`, `computeEigenv` returns `lambda[3]` and `vp[9]`).

## Return shape

- No outputs → the scalar return (`libcode`/`int`/`double` modes) or
  `undefined`.
- Outputs → an object keyed by the C parameter names; a meaningful scalar
  return is added as `value`.

```js
const r = mmg2d.getAdjaVertices(h.mesh, ip);
// -> { value: count, lispoi: Int32Array(1024) } (first `count` entries valid)
```

## Memory discipline

Every call is transactional: input copies and output buffers are
`malloc`ed before the call and freed in a `finally` block; returned typed
arrays are **JS-owned copies**, never views into WASM memory (safe against
memory growth and later frees). The only persistent allocations are the
4-byte handle boxes created by `init()` and released by `free()`.

## Heap views and memory growth

The WASM memory starts at 64 MB and grows on demand (`ALLOW_MEMORY_GROWTH`);
the marshaller re-fetches `HEAP*` views on every access, so growth never
invalidates a call in progress.
