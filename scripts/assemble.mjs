// Assemble the publishable dist/ from the emcc core + generated descriptor +
// hand-written runtime. Produces dual ESM/CJS entry points that expose the
// ergonomic `initialize()` API, plus the .d.ts.
//
// Inputs (must already exist):
//   dist/mmg-core.mjs, dist/mmg-core.cjs, dist/mmg-core.wasm   (from emcc)
//   generated/mmg-api.json, generated/mmg.d.ts                 (from gen_js.py)
//   src/runtime.mjs                                            (marshaller)
// Outputs:
//   dist/runtime.mjs, dist/runtime.cjs
//   dist/mmg-descriptor.mjs, dist/mmg-descriptor.cjs
//   dist/mmg.mjs, dist/mmg.cjs, dist/mmg.d.ts

import { readFileSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const DIST = join(ROOT, 'dist');
const GEN = join(ROOT, 'generated');

// 1. runtime: emit ESM (as-is) and a mechanically-derived CJS variant.
const runtimeSrc = readFileSync(join(ROOT, 'src', 'runtime.mjs'), 'utf8');
writeFileSync(join(DIST, 'runtime.mjs'), runtimeSrc);
const runtimeCjs = runtimeSrc.replace(
  /export function buildApi/, 'function buildApi'
) + '\nmodule.exports = { buildApi };\n';
writeFileSync(join(DIST, 'runtime.cjs'), runtimeCjs);

// 2. descriptor: inline the JSON as a module (avoids JSON-import/asset issues).
const descriptor = readFileSync(join(GEN, 'mmg-api.json'), 'utf8').trimEnd();
writeFileSync(join(DIST, 'mmg-descriptor.mjs'), `export default ${descriptor};\n`);
writeFileSync(join(DIST, 'mmg-descriptor.cjs'), `module.exports = ${descriptor};\n`);

// 3. typings
writeFileSync(join(DIST, 'mmg.d.ts'), readFileSync(join(GEN, 'mmg.d.ts'), 'utf8'));

// 4. entry points
const esm = `// AUTO-GENERATED entry (ESM). See scripts/assemble.mjs.
import createCore from './mmg-core.mjs';
import { buildApi } from './runtime.mjs';
import descriptor from './mmg-descriptor.mjs';

export async function initialize(moduleOverrides = {}) {
  const Module = await createCore(moduleOverrides);
  const api = buildApi(Module, descriptor);
  api.FS = Module.FS;        // MEMFS access for file I/O
  api.module = Module;       // raw Emscripten module (escape hatch)
  return api;
}

export default initialize;
`;
writeFileSync(join(DIST, 'mmg.mjs'), esm);

const cjs = `// AUTO-GENERATED entry (CJS). See scripts/assemble.mjs.
const createCore = require('./mmg-core.cjs');
const { buildApi } = require('./runtime.cjs');
const descriptor = require('./mmg-descriptor.cjs');

async function initialize(moduleOverrides = {}) {
  const Module = await createCore(moduleOverrides);
  const api = buildApi(Module, descriptor);
  api.FS = Module.FS;
  api.module = Module;
  return api;
}

module.exports = initialize;
module.exports.initialize = initialize;
module.exports.default = initialize;
`;
writeFileSync(join(DIST, 'mmg.cjs'), cjs);

console.log('assembled dist/: mmg.mjs, mmg.cjs, runtime.{mjs,cjs}, mmg-descriptor.{mjs,cjs}, mmg.d.ts');
