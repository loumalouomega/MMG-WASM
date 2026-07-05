# Contributing

Issues and pull requests are welcome at
[loumalouomega/MMG-WASM](https://github.com/loumalouomega/MMG-WASM).

## Ground rules

- **Never edit `generated/`** — it is codegen output (`npm run gen`); CI
  fails if it is out of sync with the headers and scripts.
- **All marshalling lives in `src/runtime.mjs`.** If you are tempted to
  hand-write conversion code for one function, extend the descriptor
  vocabulary and the runtime instead.
- Classification fixes (a mis-detected out-parameter, a bulk array) belong
  in `scripts/mmg_overrides.py`.
- The `mmg/` submodule is upstream, unmodified. Fixes to MMG itself go to
  [MmgTools/mmg](https://github.com/MmgTools/mmg).

## Dev loop

```bash
npm run setup                # once
npm run build:wasm           # full build (fast after the first time)
npm test                     # node tests
npm run test:browser         # playwright
npm run gen                  # bindings only (no emcc needed)
npm run docs:serve           # live docs preview (pip install -r docs/requirements.txt)
```

For a debug build: `OPT="-O0 -g" npm run build:wasm`.

## Checklist for PRs

1. `npm test` and `npm run test:browser` pass.
2. `npm run gen` leaves `git status generated/` clean (commit regenerated
   files if your change affects them).
3. New behaviour has a test in `test/api.test.mjs`.
4. Docs updated when the public API or build changes (`docs/`, `README.md`).
5. `mkdocs build --strict` succeeds if you touched docs.

## Release (maintainers)

1. Bump `version` in `package.json`, commit.
2. Tag `vX.Y.Z` and push the tag.
3. CI builds, tests, verifies tag == package version, and publishes to npm
   with provenance. A `workflow_dispatch` run with `dry_run: true`
   rehearses the pipeline without publishing.
