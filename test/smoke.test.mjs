// Smoke test against the raw emcc core (dist/mmg-core.mjs): replicates
// mmg's libexamples/mmg3d/adaptation_example0/example0_b (hand-built
// two-material cube) through the raw C exports, without the typed wrapper.

import test from 'node:test';
import assert from 'node:assert/strict';
import initMmg from '../dist/mmg-core.mjs';
import { makeHelpers } from './raw-helpers.mjs';

// Cube data from mmg/libexamples/mmg3d/adaptation_example0/example0_b/main.c
const VERTICES = [
  [0, 0, 0, 0], [0.5, 0, 0, 0], [0.5, 0, 1, 0], [0, 0, 1, 0],
  [0, 1, 0, 0], [0.5, 1, 0, 0], [0.5, 1, 1, 0], [0, 1, 1, 0],
  [1, 0, 0, 0], [1, 1, 0, 0], [1, 0, 1, 0], [1, 1, 1, 0],
];
const TETRA = [
  [1, 4, 2, 8, 1], [8, 3, 2, 7, 1], [5, 2, 6, 8, 1], [5, 8, 1, 2, 1],
  [7, 2, 8, 6, 1], [2, 4, 3, 8, 1], [9, 2, 3, 7, 2], [7, 11, 9, 12, 2],
  [6, 9, 10, 7, 2], [6, 7, 2, 9, 2], [12, 9, 7, 10, 2], [9, 3, 11, 7, 2],
];
const TRIA = [
  [1, 4, 8, 3], [1, 2, 4, 3], [8, 3, 7, 3], [5, 8, 6, 3], [5, 6, 2, 3],
  [5, 2, 1, 3], [5, 1, 8, 3], [7, 6, 8, 3], [4, 3, 8, 3], [2, 3, 4, 3],
  [9, 3, 2, 4], [11, 9, 12, 4], [7, 11, 12, 4], [6, 7, 10, 4], [6, 10, 9, 4],
  [6, 9, 2, 4], [12, 10, 7, 4], [12, 9, 10, 4], [3, 11, 7, 4], [9, 11, 3, 4],
];

const MMG5_Vertex = 1;
const MMG5_Scalar = 1;
const MMG5_STRONGFAILURE = 2;
const MMG3D_IPARAM_verbose = 0;
const MMG3D_DPARAM_hausd = 30; // 26 IPARAM_* entries precede the DPARAM_* block

test('raw exports: cube adaptation (example0_b)', async () => {
  const Module = await initMmg();
  const H = makeHelpers(Module);

  // Handle boxes: 4-byte slots holding MMG5_pMesh / MMG5_pSol.
  const meshSlot = H.slot();
  const solSlot = H.slot();

  H.checked('Init_mesh', () =>
    Module._mmgjs_MMG3D_Init_mesh(meshSlot, solSlot, 0, 0));
  const mesh = H.readInt(meshSlot);
  const sol = H.readInt(solSlot);
  assert.ok(mesh > 0 && sol > 0, 'mesh/sol structs allocated');

  H.checked('Set_iparameter verbose', () =>
    Module._MMG3D_Set_iparameter(mesh, sol, MMG3D_IPARAM_verbose, -1));

  H.checked('Set_meshSize', () =>
    Module._MMG3D_Set_meshSize(mesh, 12, 12, 0, 20, 0, 0));
  VERTICES.forEach(([x, y, z, ref], i) => {
    H.checked(`Set_vertex ${i + 1}`, () =>
      Module._MMG3D_Set_vertex(mesh, x, y, z, ref, i + 1));
  });
  TETRA.forEach(([a, b, c, d, ref], i) => {
    H.checked(`Set_tetrahedron ${i + 1}`, () =>
      Module._MMG3D_Set_tetrahedron(mesh, a, b, c, d, ref, i + 1));
  });
  TRIA.forEach(([a, b, c, ref], i) => {
    H.checked(`Set_triangle ${i + 1}`, () =>
      Module._MMG3D_Set_triangle(mesh, a, b, c, ref, i + 1));
  });

  H.checked('Set_solSize', () =>
    Module._MMG3D_Set_solSize(mesh, sol, MMG5_Vertex, 12, MMG5_Scalar));
  for (let k = 1; k <= 12; k++) {
    H.checked(`Set_scalarSol ${k}`, () =>
      Module._MMG3D_Set_scalarSol(sol, 0.5, k));
  }
  H.checked('Chk_meshData', () => Module._MMG3D_Chk_meshData(mesh, sol));

  H.checked('Set_dparameter hausd', () =>
    Module._MMG3D_Set_dparameter(mesh, sol, MMG3D_DPARAM_hausd, 0.1));

  const ier = Module._MMG3D_mmg3dlib(mesh, sol);
  assert.notEqual(ier, MMG5_STRONGFAILURE, 'mmg3dlib must not fail strongly');

  // Output mesh must have been refined (input: 12 vertices).
  const npP = H.slot(), neP = H.slot(), nprismP = H.slot(),
        ntP = H.slot(), nquadP = H.slot(), naP = H.slot();
  H.checked('Get_meshSize', () =>
    Module._MMG3D_Get_meshSize(mesh, npP, neP, nprismP, ntP, nquadP, naP));
  const np = H.readInt(npP), ne = H.readInt(neP);
  assert.ok(np > 12, `refined mesh has more vertices than input (np=${np})`);
  assert.ok(ne > 12, `refined mesh has more tetrahedra than input (ne=${ne})`);

  // Round-trip a vertex through Get_vertex out-pointers.
  const cx = H.malloc(8), cy = H.malloc(8), cz = H.malloc(8);
  const ref = H.slot();
  H.checked('Get_vertex', () =>
    Module._MMG3D_Get_vertex(mesh, cx, cy, cz, ref, 0, 0));
  const x = H.readDouble(cx);
  assert.ok(Number.isFinite(x), 'vertex coordinate is finite');

  // Save to MEMFS and check the Medit header round-trips.
  const out = H.cstr('/out.mesh');
  H.checked('saveMesh', () => Module._MMG3D_saveMesh(mesh, out));
  const text = Module.FS.readFile('/out.mesh', { encoding: 'utf8' });
  assert.match(text, /MeshVersionFormatted/);
  assert.match(text, /Vertices/);

  H.checked('Free_all', () =>
    Module._mmgjs_MMG3D_Free_all(meshSlot, solSlot, 0, 0));
  assert.equal(H.readInt(meshSlot), 0, 'mesh pointer NULLed by Free_all');
});
