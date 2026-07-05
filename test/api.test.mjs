// Tests for the typed wrapper (dist/mmg.mjs): 3D adaptation (scalar +
// bulk-array paths), 2D adaptation + generation, surface remeshing, 3D
// level-set discretization, MEMFS file I/O round-trip, and error paths.

import test from 'node:test';
import assert from 'node:assert/strict';
import initialize from '../dist/mmg.mjs';

// Two-material cube from mmg/libexamples/mmg3d/adaptation_example0/example0_b.
const CUBE_VERTS = [
  [0, 0, 0], [0.5, 0, 0], [0.5, 0, 1], [0, 0, 1],
  [0, 1, 0], [0.5, 1, 0], [0.5, 1, 1], [0, 1, 1],
  [1, 0, 0], [1, 1, 0], [1, 0, 1], [1, 1, 1],
];
const CUBE_TETRA = [
  [1, 4, 2, 8, 1], [8, 3, 2, 7, 1], [5, 2, 6, 8, 1], [5, 8, 1, 2, 1],
  [7, 2, 8, 6, 1], [2, 4, 3, 8, 1], [9, 2, 3, 7, 2], [7, 11, 9, 12, 2],
  [6, 9, 10, 7, 2], [6, 7, 2, 9, 2], [12, 9, 7, 10, 2], [9, 3, 11, 7, 2],
];
const CUBE_TRIA = [
  [1, 4, 8, 3], [1, 2, 4, 3], [8, 3, 7, 3], [5, 8, 6, 3], [5, 6, 2, 3],
  [5, 2, 1, 3], [5, 1, 8, 3], [7, 6, 8, 3], [4, 3, 8, 3], [2, 3, 4, 3],
  [9, 3, 2, 4], [11, 9, 12, 4], [7, 11, 12, 4], [6, 7, 10, 4], [6, 10, 9, 4],
  [6, 9, 2, 4], [12, 10, 7, 4], [12, 9, 10, 4], [3, 11, 7, 4], [9, 11, 3, 4],
];

function buildCube(mmg, h) {
  mmg.setIparameter(h.mesh, h.met, mmg.IPARAM_verbose, -1);
  mmg.setMeshSize(h.mesh, 12, 12, 0, 20, 0, 0);
  CUBE_VERTS.forEach(([x, y, z], i) =>
    mmg.setVertex(h.mesh, x, y, z, 0, i + 1));
  CUBE_TETRA.forEach(([a, b, c, d, ref], i) =>
    mmg.setTetrahedron(h.mesh, a, b, c, d, ref, i + 1));
  CUBE_TRIA.forEach(([a, b, c, ref], i) =>
    mmg.setTriangle(h.mesh, a, b, c, ref, i + 1));
}

let api;
test.before(async () => { api = await initialize(); });

test('constants: return codes and parameter enums', () => {
  assert.equal(api.MMG5_SUCCESS, 0);
  assert.equal(api.MMG5_LOWFAILURE, 1);
  assert.equal(api.MMG5_STRONGFAILURE, 2);
  assert.equal(api.MMG5_Scalar, 1);
  assert.equal(api.MMG5_Vertex, 1);
  assert.equal(api.mmg3d.IPARAM_verbose, 0);
  assert.equal(typeof api.mmg3d.DPARAM_hausd, 'number');
  assert.equal(typeof api.mmg2d.IPARAM_verbose, 'number');
  assert.equal(typeof api.mmgs.DPARAM_hausd, 'number');
});

test('mmg3d: cube adaptation via scalar setters + metric', () => {
  const { mmg3d } = api;
  const h = mmg3d.init();
  buildCube(mmg3d, h);

  mmg3d.setSolSize(h.mesh, h.met, api.MMG5_Vertex, 12, api.MMG5_Scalar);
  for (let k = 1; k <= 12; k++) mmg3d.setScalarSol(h.met, 0.5, k);
  mmg3d.chkMeshData(h.mesh, h.met);
  mmg3d.setDparameter(h.mesh, h.met, mmg3d.DPARAM_hausd, 0.1);

  const code = mmg3d.remesh(h.mesh, h.met); // alias of mmg3dlib
  assert.notEqual(code, api.MMG5_STRONGFAILURE);

  const size = mmg3d.getMeshSize(h.mesh);
  assert.ok(size.np > 12, `adapted mesh refined (np=${size.np})`);
  assert.ok(size.ne > 12, `adapted mesh refined (ne=${size.ne})`);

  // scalar getter with out-params
  const v = mmg3d.getVertex(h.mesh);
  assert.ok(Number.isFinite(v.c0) && Number.isFinite(v.c1) && Number.isFinite(v.c2));

  // bulk getter: trailing count argument sizes the output buffers
  const bulk = mmg3d.getVertices(h.mesh, size.np);
  assert.equal(bulk.vertices.length, 3 * size.np);
  assert.ok(bulk.vertices instanceof Float64Array);
  assert.ok(bulk.refs instanceof Int32Array);
  const tets = mmg3d.getTetrahedra(h.mesh, size.ne);
  assert.equal(tets.tetra.length, 4 * size.ne);
  for (const idx of tets.tetra) assert.ok(idx >= 1 && idx <= size.np);

  mmg3d.free(h);
});

test('mmg3d: bulk setters (setVertices / setTetrahedra)', () => {
  const { mmg3d } = api;
  const h = mmg3d.init();
  mmg3d.setIparameter(h.mesh, h.met, mmg3d.IPARAM_verbose, -1);
  mmg3d.setMeshSize(h.mesh, 12, 12, 0, 20, 0, 0);

  const coords = new Float64Array(CUBE_VERTS.flat());
  const vrefs = new Int32Array(12);
  mmg3d.setVertices(h.mesh, coords, vrefs);

  const tetra = new Int32Array(CUBE_TETRA.flatMap((t) => t.slice(0, 4)));
  const trefs = new Int32Array(CUBE_TETRA.map((t) => t[4]));
  mmg3d.setTetrahedra(h.mesh, tetra, trefs);

  const tria = new Int32Array(CUBE_TRIA.flatMap((t) => t.slice(0, 3)));
  const trirefs = new Int32Array(CUBE_TRIA.map((t) => t[3]));
  mmg3d.setTriangles(h.mesh, tria, trirefs);

  mmg3d.setDparameter(h.mesh, h.met, mmg3d.DPARAM_hausd, 0.1);
  const code = mmg3d.remesh(h.mesh, h.met);
  assert.notEqual(code, api.MMG5_STRONGFAILURE);
  assert.ok(mmg3d.getMeshSize(h.mesh).np > 12);
  mmg3d.free(h);
});

test('mmg3d: level-set discretization (mmg3dls)', () => {
  const { mmg3d } = api;
  const h = mmg3d.init({ levelset: true });
  buildCube(mmg3d, h);

  // level-set: signed distance to the x = 0.75 plane
  mmg3d.setSolSize(h.mesh, h.ls, api.MMG5_Vertex, 12, api.MMG5_Scalar);
  CUBE_VERTS.forEach(([x], i) => mmg3d.setScalarSol(h.ls, x - 0.75, i + 1));

  mmg3d.setIparameter(h.mesh, h.ls, mmg3d.IPARAM_iso, 1);
  const code = mmg3d.levelset(h.mesh, h.ls, null); // mmg3dls, met = NULL
  assert.notEqual(code, api.MMG5_STRONGFAILURE);
  assert.ok(mmg3d.getMeshSize(h.mesh).np > 12);
  mmg3d.free(h);
});

test('mmg2d: unit-square adaptation', () => {
  const { mmg2d } = api;
  const h = mmg2d.init();
  mmg2d.setIparameter(h.mesh, h.met, mmg2d.IPARAM_verbose, -1);
  // 4 vertices, 2 triangles, 0 quads, 4 boundary edges
  mmg2d.setMeshSize(h.mesh, 4, 2, 0, 4);
  const sq = [[0, 0], [1, 0], [1, 1], [0, 1]];
  sq.forEach(([x, y], i) => mmg2d.setVertex(h.mesh, x, y, 0, i + 1));
  mmg2d.setTriangle(h.mesh, 1, 2, 3, 1, 1);
  mmg2d.setTriangle(h.mesh, 1, 3, 4, 1, 2);
  [[1, 2], [2, 3], [3, 4], [4, 1]].forEach(([a, b], i) =>
    mmg2d.setEdge(h.mesh, a, b, 1, i + 1));

  mmg2d.setDparameter(h.mesh, h.met, mmg2d.DPARAM_hmax, 0.2);
  const code = mmg2d.remesh(h.mesh, h.met); // alias of mmg2dlib
  assert.notEqual(code, api.MMG5_STRONGFAILURE);
  const size = mmg2d.getMeshSize(h.mesh);
  assert.ok(size.np > 4, `2d adaptation refined (np=${size.np})`);
  mmg2d.free(h);
});

test('mmg2d: mesh generation from a boundary (mmg2dmesh)', () => {
  const { mmg2d } = api;
  const h = mmg2d.init();
  mmg2d.setIparameter(h.mesh, h.met, mmg2d.IPARAM_verbose, -1);
  // boundary only: 4 vertices, no triangles, 4 edges
  mmg2d.setMeshSize(h.mesh, 4, 0, 0, 4);
  const sq = [[0, 0], [1, 0], [1, 1], [0, 1]];
  sq.forEach(([x, y], i) => mmg2d.setVertex(h.mesh, x, y, 0, i + 1));
  [[1, 2], [2, 3], [3, 4], [4, 1]].forEach(([a, b], i) =>
    mmg2d.setEdge(h.mesh, a, b, 1, i + 1));

  mmg2d.setDparameter(h.mesh, h.met, mmg2d.DPARAM_hmax, 0.3);
  const code = mmg2d.generate(h.mesh, h.met); // alias of mmg2dmesh
  assert.notEqual(code, api.MMG5_STRONGFAILURE);
  const size = mmg2d.getMeshSize(h.mesh);
  assert.ok(size.nt > 0, `triangulation generated (nt=${size.nt})`);
  mmg2d.free(h);
});

test('mmgs: cube-surface remeshing', () => {
  const { mmgs } = api;
  const h = mmgs.init();
  mmgs.setIparameter(h.mesh, h.met, mmgs.IPARAM_verbose, -1);
  // reuse the cube boundary: 12 vertices, 20 triangles, 0 edges
  mmgs.setMeshSize(h.mesh, 12, 20, 0);
  CUBE_VERTS.forEach(([x, y, z], i) => mmgs.setVertex(h.mesh, x, y, z, 0, i + 1));
  CUBE_TRIA.forEach(([a, b, c, ref], i) => mmgs.setTriangle(h.mesh, a, b, c, ref, i + 1));

  mmgs.setDparameter(h.mesh, h.met, mmgs.DPARAM_hmax, 0.25);
  const code = mmgs.remesh(h.mesh, h.met); // alias of mmgslib
  assert.notEqual(code, api.MMG5_STRONGFAILURE);
  const size = mmgs.getMeshSize(h.mesh);
  assert.ok(size.np > 12, `surface refined (np=${size.np})`);
  mmgs.free(h);
});

test('file I/O through MEMFS: saveMesh -> loadMesh round-trip', () => {
  const { mmg3d, FS } = api;

  // adapt the cube and save it
  const h1 = mmg3d.init();
  buildCube(mmg3d, h1);
  mmg3d.setDparameter(h1.mesh, h1.met, mmg3d.DPARAM_hausd, 0.1);
  mmg3d.remesh(h1.mesh, h1.met);
  const saved = mmg3d.getMeshSize(h1.mesh);
  mmg3d.saveMesh(h1.mesh, '/adapted.mesh');
  mmg3d.free(h1);

  const text = FS.readFile('/adapted.mesh', { encoding: 'utf8' });
  assert.match(text, /MeshVersionFormatted/);
  assert.match(text, /Vertices/);

  // load it back into a fresh pair of structures
  const h2 = mmg3d.init();
  mmg3d.setIparameter(h2.mesh, h2.met, mmg3d.IPARAM_verbose, -1);
  mmg3d.loadMesh(h2.mesh, '/adapted.mesh');
  const loaded = mmg3d.getMeshSize(h2.mesh);
  assert.equal(loaded.np, saved.np, 'vertex count round-trips');
  assert.equal(loaded.ne, saved.ne, 'tetra count round-trips');
  mmg3d.free(h2);
  FS.unlink('/adapted.mesh');
});

test('gmsh-format export (saveMshMesh)', () => {
  const { mmg3d, FS } = api;
  const h = mmg3d.init();
  buildCube(mmg3d, h);
  mmg3d.saveMshMesh(h.mesh, h.met, '/cube.msh');
  const text = FS.readFile('/cube.msh', { encoding: 'utf8' });
  assert.match(text, /\$MeshFormat/);
  mmg3d.free(h);
  FS.unlink('/cube.msh');
});

test('error paths: failed status calls throw', () => {
  const { mmg3d } = api;
  const h = mmg3d.init();
  mmg3d.setIparameter(h.mesh, h.met, mmg3d.IPARAM_verbose, -1);
  // setVertex before setMeshSize: mmg returns 0 -> wrapper throws
  assert.throws(() => mmg3d.setVertex(h.mesh, 0, 0, 0, 0, 1),
    /MMG3D_Set_vertex failed/);
  // missing file
  assert.throws(() => mmg3d.loadMesh(h.mesh, '/no-such-file.mesh'),
    /MMG3D_loadMesh failed/);
  mmg3d.free(h);
});

test('unsupported functions are not exposed', () => {
  assert.equal(api.mmg3d.parsar, undefined);
  assert.equal(api.mmg3d.stockOptions, undefined);
  assert.equal(api.mmg2d.loadVect, undefined);
});
