# Browser usage

The package is plain ESM + a single `.wasm` asset; any bundler (Vite,
webpack, Rollup) or even no bundler at all works. The build is
single-threaded, so **no COOP/COEP headers or SharedArrayBuffer** are
required.

## With a bundler (Vite)

```js
import initialize from '@loumalouomega/mmg-wasm';

const mmg = await initialize();
```

Bundlers that rewrite asset URLs usually pick up `mmg-core.wasm`
automatically (it sits next to `mmg.mjs` and is referenced relatively). If
yours does not, resolve the wasm explicitly:

```js
import wasmUrl from '@loumalouomega/mmg-wasm/mmg-core.wasm?url';

const mmg = await initialize({
  locateFile: (file) => (file.endsWith('.wasm') ? wasmUrl : file),
});
```

`locateFile` is the standard Emscripten override and receives every asset
the runtime requests.

## Without a bundler

Serve `dist/` (or the installed package directory) statically and import
the entry directly — this is exactly what
[`examples/browser/index.html`](https://github.com/loumalouomega/MMG-WASM/blob/master/examples/browser/index.html)
does:

```html
<script type="module">
  import initialize from './node_modules/@loumalouomega/mmg-wasm/dist/mmg.mjs';
  const mmg = await initialize();
  // ...
</script>
```

The server must send `application/wasm` for `.wasm` files (any competent
static server does).

## Keeping the UI responsive

Remeshing is CPU-bound and synchronous. For non-trivial meshes run it in a
**Web Worker**:

```js
// worker.js
import initialize from '@loumalouomega/mmg-wasm';
const mmg = await initialize();
self.onmessage = ({ data }) => {
  const { mmg3d } = mmg;
  const h = mmg3d.init();
  mmg3d.setMeshSize(h.mesh, data.np, data.ne, 0, data.nt, 0, 0);
  mmg3d.setVertices(h.mesh, data.coords, null);
  mmg3d.setTetrahedra(h.mesh, data.tetra, null);
  mmg3d.remesh(h.mesh, h.met);
  const { np, ne } = mmg3d.getMeshSize(h.mesh);
  const out = {
    coords: mmg3d.getVertices(h.mesh, np).vertices,
    tetra: mmg3d.getTetrahedra(h.mesh, ne).tetra,
  };
  mmg3d.free(h);
  self.postMessage(out, [out.coords.buffer, out.tetra.buffer]);
};
```

Typed arrays returned by the bulk getters are copies owned by JS, so they
can be transferred (zero-copy) out of the worker.

## Memory

The instance starts at 64 MB and grows on demand up to 4 GB. A failed
growth (huge meshes on 32-bit budgets) surfaces as an `abort`; catch it at
the `initialize()`/call level if you handle untrusted input sizes.
