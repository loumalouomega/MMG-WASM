# Licensing

## LGPL-3.0-or-later

MMG is distributed under the **GNU Lesser General Public License v3 or
later** (see upstream `mmg/LICENSE` and `COPYING.LESSER`). mmg-wasm
statically links MMG into `mmg-core.wasm` and is distributed under the same
license: **LGPL-3.0-or-later** for the whole package (wrapper scripts,
runtime, generated bindings included).

## What this means for you

Using `@loumalouomega/mmg-wasm` from npm in an application (even a
proprietary one) is the standard LGPL "combined work" situation. The
practical obligations:

- keep the license and copyright notices (the npm package ships `LICENSE`);
- tell your users the app uses MMG/mmg-wasm under LGPL and where to get the
  source (this repository);
- allow relinking with a modified library: because the library is a
  self-contained npm package, swapping `node_modules/@loumalouomega/mmg-wasm`
  (or the served `dist/` files) for a rebuilt version satisfies this — the
  full recipe to rebuild `mmg-core.wasm` from source is in
  [Building from source](building.md).

If you modify mmg-wasm or MMG itself and distribute the result, those
modifications must be published under LGPL-3.0-or-later.

!!! note
    This page is a good-faith summary, not legal advice. Read the
    [LGPL-3.0 text](https://www.gnu.org/licenses/lgpl-3.0.html) for the
    authoritative terms.

## Citing MMG

mmg-wasm is a packaging effort; the science is upstream. If you use it in
academic work, cite the MMG platform paper and the relevant module papers —
see [mmgtools.org](https://www.mmgtools.org/) for the current citation
list. C. Dapogny, C. Dobrzynski and P. Frey,
*Three-dimensional adaptive domain remeshing, implicit domain meshing, and
applications to free and moving boundary problems*, JCP, 2014, is the
standard reference for mmg3d.

## Not affiliated

mmg-wasm is a community project and is not affiliated with, or endorsed
by, the Mmg consortium, Inria, or the MMG authors.
