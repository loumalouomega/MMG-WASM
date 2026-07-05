# TypeScript

The package ships generated declarations (`mmg.d.ts`) covering every bound
function, the constants, and the lifecycle helpers.

```ts
import initialize, { Mmg, MmgHandles, MeshHandle, SolHandle }
  from '@loumalouomega/mmg-wasm';

const mmg: Mmg = await initialize();
const h: MmgHandles = mmg.mmg3d.init();
```

## Branded handles

`MeshHandle` and `SolHandle` are branded numbers:

```ts
export type MeshHandle = number & { readonly __mmg: 'mesh' };
export type SolHandle = number & { readonly __mmg: 'sol' };
```

They are ordinary numbers at runtime, but the brand stops you from passing
a solution where a mesh is expected (or a random integer as either):

```ts
mmg.mmg3d.setVertex(h.met, 0, 0, 0, 0, 1);
//                  ~~~~~ error: SolHandle is not assignable to MeshHandle
```

## Output objects and typed arrays

Functions with output parameters return an object typed field-by-field;
bulk getters return typed arrays:

```ts
const size = mmg.mmg3d.getMeshSize(h.mesh);
// { np: number; ne: number; nprism: number; nt: number; nquad: number; na: number }

const v = mmg.mmg3d.getVertices(h.mesh, size.np);
// { vertices: Float64Array; refs: Int32Array; areCorners: Int32Array; areRequired: Int32Array }
```

Functions whose C return is a status return `void` (they throw on failure);
the remeshing entry points return `number` (the MMG5 library code).

## Constants

Constants are `readonly number` properties on the API objects, so parameter
calls type-check and autocomplete:

```ts
mmg.mmg3d.setDparameter(h.mesh, h.met, mmg.mmg3d.DPARAM_hausd, 0.01);
mmg.mmg3d.setSolSize(h.mesh, h.met, mmg.MMG5_Vertex, np, mmg.MMG5_Tensor);
```

## Escape hatch

`mmg.module` is the raw Emscripten module (typed as
`Record<string, unknown>`): every exported C symbol is available as
`(mmg.module as any)._MMG3D_Set_vertex(...)` should you ever need to bypass
the wrapper.
