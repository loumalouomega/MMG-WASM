# mmg-wasm

**[MMG](https://www.mmgtools.org/)** — the open-source surface and volume
remeshers — compiled to **WebAssembly** with a typed JavaScript/TypeScript
API. Run mesh adaptation, isotropic/anisotropic remeshing, level-set
discretization and 2D mesh generation directly in Node.js or the browser,
with no native binaries.

- **All three modules**: `mmg2d` (planar meshes), `mmgs` (3D surface meshes),
  `mmg3d` (tetrahedral volume meshes).
- **~350 typed functions** generated from the upstream MMG v5.8 headers:
  the full in-memory `Set_*`/`Get_*` API, parameter control, and the
  `mmg*lib`/`mmg*ls`/`mmg*mov` entry points.
- **In-memory or file-based**: build meshes programmatically from arrays, or
  read/write Medit `.mesh`/`.sol` and Gmsh `.msh` files through an in-memory
  filesystem (MEMFS).
- **Dual ESM + CJS** package sharing a single `.wasm`, with TypeScript
  declarations. Works in Node ≥ 18 and modern browsers, single-threaded.
- Handles, return codes and pointer marshalling are hidden behind a typed
  wrapper: failed calls throw JavaScript `Error`s.

## Quick taste

```js
import initialize from '@loumalouomega/mmg-wasm';

const mmg = await initialize();
const { mmg3d } = mmg;

const h = mmg3d.init();                       // MMG5_pMesh + MMG5_pSol handles
mmg3d.setMeshSize(h.mesh, np, ne, 0, nt, 0, 0);
mmg3d.setVertices(h.mesh, coords, refs);      // bulk Float64Array/Int32Array
mmg3d.setTetrahedra(h.mesh, tetra, tetRefs);
mmg3d.setDparameter(h.mesh, h.met, mmg3d.DPARAM_hausd, 0.01);
mmg3d.remesh(h.mesh, h.met);                  // MMG3D_mmg3dlib
const { np: npOut } = mmg3d.getMeshSize(h.mesh);
mmg3d.free(h);
```

## Where next

- [Getting started](getting-started.md) — install and first remesh.
- [Concepts](guide/concepts.md) — handles, modules, and the data flow.
- [API reference](api/reference.md) — every generated function.
- [Building from source](building.md) — reproduce the WASM build.

## Relationship to upstream MMG

mmg-wasm compiles the unmodified [MmgTools/mmg](https://github.com/MmgTools/mmg)
sources (pinned as a git submodule) with Emscripten and generates JS bindings
from its public headers. It is a community port, **not** affiliated with or
endorsed by the Mmg consortium. Scientific credit belongs to the MMG
authors — see [Licensing](licensing.md) for citation and license details.
