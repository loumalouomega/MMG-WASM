#!/usr/bin/env python3
"""Generate the markdown API reference (docs/api/reference.md) from the same
descriptor that drives the runtime, so the docs cannot drift from the build.

Each function is rendered with its ergonomic JS call form, the underlying MMG
C symbol, a typed parameter table, the return shape, and the upstream doc
text, grouped by module (mmg3d, mmg2d, mmgs). Unsupported functions are
listed at the end with the reason.
"""

import os
import sys
import json

ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from gen_js import ts_signature, INPUT_TS, HANDLE_TS  # reuse .d.ts mapping

GEN = os.path.join(ROOT, "generated", "mmg-api.json")
OUT = os.path.join(ROOT, "docs", "api", "reference.md")


def input_params(fn):
    """[(name, ts_type)] for the caller-visible inputs (+ count params)."""
    rows = []
    for a in fn["args"]:
        if a.get("output"):
            continue
        kind = a["kind"]
        if kind in ("handle", "handleref"):
            ts = HANDLE_TS[a["handleType"]]
        else:
            ts = INPUT_TS.get(kind, "number")
        if a.get("nullable"):
            ts += " | null"
        rows.append((a["name"], ts))
    for cp in fn.get("counts", []):
        rows.append((cp, "number (size of the output arrays)"))
    return rows


RET_DOC = {
    "status": "throws on failure",
    "libcode": "returns `MMG5_SUCCESS`/`MMG5_LOWFAILURE`; throws on "
               "`MMG5_STRONGFAILURE`",
    "int": "returns the raw integer value",
    "double": "returns the raw double value",
    "void": "no return value",
}


def main():
    data = json.load(open(GEN))
    funcs = [f for f in data["functions"] if not f.get("unsupported")]
    unsupported = [f for f in data["functions"] if f.get("unsupported")]
    aliases = data.get("aliases", {})

    groups = {}
    for f in funcs:
        groups.setdefault(f["path"][0], []).append(f)

    lines = [
        "# API reference",
        "",
        "!!! note",
        "    This page is generated from the MMG public headers "
        f"(version **{data['version']}**) by `scripts/gen_docs_api.py` and is "
        "regenerated in CI. Every function hides pointer handling and manual "
        "memory management; see [Marshalling](marshalling.md) for how "
        "arguments and return values are converted.",
        "",
        f"**{len(funcs)} functions** across {len(groups)} modules "
        "(`mmg3d`, `mmg2d`, `mmgs`).",
        "",
        "Conventions:",
        "",
        "- `MeshHandle` / `SolHandle` are the opaque handles returned by each "
        "module's `init()`.",
        "- Functions with output parameters return an **object** keyed by the "
        "output names; bulk getters return typed arrays "
        "(`Float64Array` / `Int32Array`).",
        "- `status` functions throw a JS `Error` on failure instead of "
        "returning 0.",
        "",
    ]

    for mod in ("mmg3d", "mmg2d", "mmgs"):
        fns = sorted(groups.get(mod, []), key=lambda f: f["js"])
        lines.append(f"## `{mod}`")
        lines.append("")
        for fn in fns:
            params, ret = ts_signature(fn)
            call = f"{mod}.{fn['js']}({', '.join(params)})"
            lines.append(f"### `{mod}.{fn['js']}`")
            lines.append("")
            lines.append("```ts")
            lines.append(f"{call}: {ret}")
            lines.append("```")
            lines.append("")
            if fn["doc"]:
                lines.append(fn["doc"])
                lines.append("")
            rows = input_params(fn)
            if rows:
                lines.append("| Parameter | Type |")
                lines.append("|-----------|------|")
                for name, ts in rows:
                    lines.append(f"| `{name}` | `{ts}` |")
                lines.append("")
            notes = [f"MMG C symbol: `{fn['c']}`",
                     f"return: {RET_DOC[fn['ret']]}"]
            if aliases.get(fn["c"]):
                notes.append(f"alias: `{mod}.{aliases[fn['c']]}()`")
            lines.append(f"<small>{' — '.join(notes)}</small>")
            lines.append("")

    lines.append("## Unsupported functions")
    lines.append("")
    lines.append("These C API entry points are not exposed to JavaScript:")
    lines.append("")
    lines.append("| C symbol | Reason |")
    lines.append("|----------|--------|")
    for f in unsupported:
        lines.append(f"| `{f['c']}` | {f['reason']} |")
    lines.append("")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        f.write("\n".join(lines))
    print(f"wrote {OUT}: {len(funcs)} functions, {len(groups)} modules, "
          f"{len(unsupported)} unsupported")


if __name__ == "__main__":
    main()
