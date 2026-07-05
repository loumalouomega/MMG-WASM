#!/usr/bin/env python3
"""Generate the JavaScript/TypeScript binding artifacts for mmg-wasm from the
MMG public C headers (mmg has no declarative API definition, so the headers
are parsed directly; classification gaps live in scripts/mmg_overrides.py).

Outputs (into generated/):
  - exported_functions.json : Emscripten -sEXPORTED_FUNCTIONS list (all bound
                              C symbols + the variadic shims + malloc/free).
  - mmg-api.json            : descriptor table consumed by src/runtime.mjs --
                              one entry per function (module path, JS name, C
                              symbol, return mode, typed args) + constants.
  - mmg.d.ts                : TypeScript declarations for the typed wrapper.

We do NOT hand-marshal per function: the runtime interprets the descriptor.
"""

import os
import re
import sys
import json

ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
MMG_SRC = os.path.join(ROOT, "mmg", "src")
OUT_DIR = os.path.join(ROOT, "generated")

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
from mmg_overrides import BULK, RETMODE, UNSUPPORTED, ALIASES, LIBCODE  # noqa: E402

HEADERS = [
    ("mmg3d", os.path.join(MMG_SRC, "mmg3d", "libmmg3d.h"), "MMG3D"),
    ("mmg2d", os.path.join(MMG_SRC, "mmg2d", "libmmg2d.h"), "MMG2D"),
    ("mmgs", os.path.join(MMG_SRC, "mmgs", "libmmgs.h"), "MMGS"),
]
TYPES_HEADER = os.path.join(MMG_SRC, "common", "libmmgtypes.h")

INT_TYPES = {"int", "MMG5_int", "int8_t", "const int", "const MMG5_int"}


# ---------------------------------------------------------------------------
# Header parsing
# ---------------------------------------------------------------------------
def strip_comments(text):
    text = re.sub(r"/\*.*?\*/", " ", text, flags=re.S)
    text = re.sub(r"//[^\n]*", " ", text)
    return text


def extract_docs(text):
    """Map C function name -> cleaned doc prose (from its doxygen block)."""
    docs = {}
    pat = re.compile(
        r"/\*\*(.*?)\*/\s*\n\s*LIBMMG\w*_EXPORT\s+(?:extern\s+)?[\w\s]+?[\s\*]"
        r"(MMG(?:3D|2D|S|5)_\w+)\s*\(",
        re.S,
    )
    for m in pat.finditer(text):
        raw, name = m.groups()
        lines = []
        skipping = False
        for line in raw.splitlines():
            line = line.strip().lstrip("*").strip()
            if line.startswith(("\\param", "\\return", "\\remark", "\\ref",
                                "\\warning", "\\todo", ">")):
                skipping = True
                continue
            if line.startswith("\\brief"):
                skipping = False
                line = line[len("\\brief"):].strip()
            elif line == "":
                skipping = False
                continue
            if skipping:
                continue
            lines.append(line)
        doc = " ".join(" ".join(lines).split())
        docs[name] = doc
    return docs


def split_args(argstr):
    """Split a C argument list on top-level commas."""
    args, depth, cur = [], 0, ""
    for ch in argstr:
        if ch in "([":
            depth += 1
        elif ch in ")]":
            depth -= 1
        if ch == "," and depth == 0:
            args.append(cur.strip())
            cur = ""
        else:
            cur += ch
    if cur.strip():
        args.append(cur.strip())
    return args


ARG_RE = re.compile(
    r"^(?P<type>.+?)\s*(?P<name>\w+)?\s*(?P<arr>(?:\[[^\]]*\])*)$"
)

# Types that can appear as a bare unnamed argument (e.g. `MMG5_pMesh ,`);
# the lazy ARG_RE would otherwise split the type itself into type+name.
BARE_TYPES = {"MMG5_pMesh", "MMG5_pSol", "int", "double", "MMG5_int",
              "int8_t", "void"}


def parse_arg(raw):
    """-> (base_type, name, array_dims) e.g. ('MMG5_int', 'listet', [4])."""
    raw = " ".join(raw.split())
    m = ARG_RE.match(raw)
    base, name, arr = m.group("type"), m.group("name"), m.group("arr")
    dims = re.findall(r"\[([^\]]*)\]", arr or "")
    # unnamed arg whose type got split by the lazy regex ('M' + 'MG5_pMesh')
    if name and not arr and (base + name) in BARE_TYPES:
        base, name = base + name, None
    # `double *sols` vs `double* sols` vs `double *`
    base = base.replace(" *", "*").replace("* ", "*").strip()
    return base, name, dims


def parse_prototypes(header, export_macro):
    text = open(header).read()
    docs = extract_docs(text)
    clean = strip_comments(text)
    protos = []
    for m in re.finditer(export_macro + r"\s+([^;]+?);", clean, flags=re.S):
        p = " ".join(m.group(1).split())
        if p.startswith("extern") and "(*" in p:
            continue  # exported function-pointer variables (MMG2D_doSol...)
        pm = re.match(
            r"(?:extern\s+)?(?P<ret>[\w\s]+?)\s*[\s\*]\s*"
            r"(?P<name>MMG(?:3D|2D|S|5)_\w+)\s*\((?P<args>.*)\)$",
            p,
        )
        if not pm:
            print(f"WARNING: unparsed prototype in {header}: {p[:80]}",
                  file=sys.stderr)
            continue
        ret = pm.group("ret").strip()
        name = pm.group("name")
        args = pm.group("args").strip()
        variadic = "..." in args
        arglist = []
        if args not in ("void", "") and not variadic:
            arglist = [parse_arg(a) for a in split_args(args)]
        protos.append({
            "c": name, "ret_ctype": ret, "cargs": arglist,
            "variadic": variadic, "doc": docs.get(name, ""),
        })
    return protos


# ---------------------------------------------------------------------------
# Constants / enums
# ---------------------------------------------------------------------------
def parse_enum(text, enum_name, strip_prefix):
    m = re.search(r"enum\s+" + enum_name + r"\s*\{(.*?)\}", text, flags=re.S)
    if not m:
        return {}
    body = strip_comments(m.group(1))
    out, next_val = {}, 0
    for entry in body.split(","):
        entry = entry.strip()
        if not entry:
            continue
        if "=" in entry:
            name, val = [x.strip() for x in entry.split("=", 1)]
            next_val = int(val, 0)
        else:
            name = entry
        if name.startswith(strip_prefix):
            key = name[len(strip_prefix):]
        else:
            key = name
        out[key] = next_val
        next_val += 1
    return out


def parse_defines(text, names):
    out = {}
    for n in names:
        m = re.search(r"#define\s+" + n + r"\s+(-?\d+)", text)
        if m:
            out[n] = int(m.group(1))
    return out


def collect_constants():
    types_text = open(TYPES_HEADER).read()
    root = {}
    root.update(parse_defines(types_text, [
        "MMG5_SUCCESS", "MMG5_LOWFAILURE", "MMG5_STRONGFAILURE",
    ]))
    # keep the full enum-entry names at root level (MMG5_Scalar, MMG5_Vertex...)
    root.update(parse_enum(types_text, "MMG5_type", ""))
    root.update(parse_enum(types_text, "MMG5_entities", ""))
    root.update(parse_enum(types_text, "MMG5_Format", ""))
    consts = {"root": root}
    for mod, header, macro in HEADERS:
        text = open(header).read()
        enum_name = macro + "_Param" if macro != "MMGS" else "MMGS_Param"
        consts[mod] = parse_enum(text, enum_name, macro + "_")
    return consts


# ---------------------------------------------------------------------------
# Classification: C prototype -> descriptor entry
# ---------------------------------------------------------------------------
def apply_bulk_spec(entry, spec):
    """Fill a descriptor arg from a BULK override tuple; see mmg_overrides."""
    kind = spec[0]
    entry["kind"] = kind
    if kind.startswith("oarray"):
        entry["output"] = True
        if len(spec) >= 3 and isinstance(spec[2], str):
            entry["per"], entry["countParam"] = spec[1], spec[2]
        else:
            entry["count"] = spec[1]          # fixed-size output
        entry["nullable"] = "nullable" in spec
    else:
        entry["nullable"] = "nullable" in spec
    return kind


def classify_function(proto, mod):
    c = proto["c"]
    unsupported_reason = None
    args = []
    bulk = BULK.get(c, {})
    is_get = re.search(r"_Get(?:ByIdx)?_", c) is not None

    for i, (base, name, dims) in enumerate(proto["cargs"]):
        base_np = base.replace("const ", "")
        name = name or f"arg{i}"
        entry = {"name": name}
        kind = None
        if dims:
            # fixed-size array arg: MMG5_int listet[4], double m[6]...
            total = 1
            for d in dims:
                if d in ("MMG2D_LMAX", "MMGS_LMAX"):
                    total *= 1024
                elif d.isdigit():
                    total *= int(d)
                else:
                    unsupported_reason = f"array dim {d}"
            elem = "int" if base_np.replace("*", "") in INT_TYPES else "double"
            if name in bulk:
                kind = apply_bulk_spec(entry, bulk[name])
                entry.setdefault("count", total)
            elif is_get:
                kind = "oarray" + elem
                entry["count"] = total
                entry["output"] = True
            else:
                unsupported_reason = f"fixed array {name}[{total}] " \
                                     "with unknown direction"
        elif base_np in ("MMG5_pMesh", "MMG5_pSol"):
            kind = "handle"
            entry["handleType"] = "mesh" if base_np == "MMG5_pMesh" else "sol"
        elif base_np in ("MMG5_pMesh*", "MMG5_pSol*"):
            kind = "handleref"
            entry["handleType"] = "mesh" if "pMesh" in base_np else "sol"
        elif base_np in INT_TYPES:
            kind = "iint"
        elif base_np == "double":
            kind = "idouble"
        elif base_np in ("char*", "const char*"):
            kind = "istring"
        elif base_np in ("int*", "MMG5_int*", "double*"):
            elem = "double" if base_np == "double*" else "int"
            if name in bulk:
                kind = apply_bulk_spec(entry, bulk[name])
            elif is_get:
                kind = "o" + elem
                entry["output"] = True
            else:
                unsupported_reason = f"unclassified pointer arg {base} {name}"
        else:
            unsupported_reason = f"unhandled type {base}"
        entry["kind"] = kind
        args.append(entry)

    # extra JS params for caller-sized output arrays, in appearance order
    counts = []
    for a in args:
        cp = a.get("countParam")
        if cp and cp not in counts:
            counts.append(cp)

    # return mode
    rt = proto["ret_ctype"]
    if c in LIBCODE:
        ret = "libcode"
    elif c in RETMODE:
        ret = RETMODE[c]
    elif rt == "void":
        ret = "void"
    elif rt == "double":
        ret = "double"
    else:
        ret = "status"

    if c in UNSUPPORTED:
        unsupported_reason = "explicitly unsupported (struct ptr / CLI-only)"

    entry = {
        "path": [mod],
        "js": js_name(c),
        "c": c,
        "ret": ret,
        "args": args,
        "doc": proto["doc"],
    }
    if counts:
        entry["counts"] = counts
    if unsupported_reason:
        entry["unsupported"] = True
        entry["reason"] = unsupported_reason
    return entry


def js_name(c):
    """MMG3D_Set_vertex -> setVertex; MMG3D_mmg3dlib -> mmg3dlib."""
    stem = re.sub(r"^MMG(?:3D|2D|S|5)_", "", c)
    parts = stem.split("_")
    first = parts[0][0].lower() + parts[0][1:]
    rest = [p[0].upper() + p[1:] if p else p for p in parts[1:]]
    return first + "".join(rest)


# ---------------------------------------------------------------------------
# Variadic shims (hand-authored entries; C lives in src/mmgjs_glue.c)
# ---------------------------------------------------------------------------
def shim_entries():
    entries = []
    for mod, macro in (("mmg3d", "MMG3D"), ("mmg2d", "MMG2D"), ("mmgs", "MMGS")):
        has_disp = macro != "MMGS"
        for op, doc in (
            ("Init_mesh", "Allocate and initialize the mesh and solution "
                          "structures (fixed-arity shim over the variadic "
                          f"{macro}_Init_mesh)."),
            ("Free_all", "Free all allocated structures (fixed-arity shim "
                         f"over the variadic {macro}_Free_all)."),
            ("Free_structures", "Free mesh/sol arrays but keep the "
                                "structures (shim over "
                                f"{macro}_Free_structures)."),
            ("Free_names", "Free file-name strings (shim over "
                           f"{macro}_Free_names)."),
        ):
            args = [
                {"name": "mesh", "kind": "handleref", "handleType": "mesh"},
                {"name": "met", "kind": "handleref", "handleType": "sol"},
                {"name": "ls", "kind": "handleref", "handleType": "sol",
                 "nullable": True},
            ]
            if has_disp:
                args.append({"name": "disp", "kind": "handleref",
                             "handleType": "sol", "nullable": True})
            entries.append({
                "path": [mod],
                "js": js_name(macro + "_" + op),
                "c": f"mmgjs_{macro}_{op}",
                "ret": "status",
                "args": args,
                "doc": doc,
                "shim": True,
            })
    return entries


# ---------------------------------------------------------------------------
# TypeScript declaration emitter
# ---------------------------------------------------------------------------
INPUT_TS = {
    "iint": "number",
    "idouble": "number",
    "istring": "string",
    "handle": None,  # resolved from handleType
    "handleref": None,
    "iarrayint": "number[] | Int32Array",
    "iarraydouble": "number[] | Float64Array",
}
OUTPUT_TS = {
    "oint": "number",
    "odouble": "number",
    "oarrayint": "Int32Array",
    "oarraydouble": "Float64Array",
}
HANDLE_TS = {"mesh": "MeshHandle", "sol": "SolHandle"}
RET_TS = {"status": None, "void": None, "libcode": "number",
          "int": "number", "double": "number"}


def ts_signature(fn):
    params = []
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
        params.append(f"{a['name']}: {ts}")
    for cp in fn.get("counts", []):
        params.append(f"{cp}: number")

    outputs = [a for a in fn["args"] if a.get("output")]
    ret_scalar = RET_TS.get(fn["ret"])
    if outputs:
        fields = [f"{o['name']}: {OUTPUT_TS[o['kind']]}" for o in outputs]
        if ret_scalar:
            fields.insert(0, f"value: {ret_scalar}")
        ret = "{ " + "; ".join(fields) + " }"
    elif ret_scalar:
        ret = ret_scalar
    else:
        ret = "void"
    return params, ret


def emit_ts(funcs, constants, version):
    lines = [
        "// AUTO-GENERATED by scripts/gen_js.py from the MMG public headers.",
        "// Do not edit by hand.",
        f"// MMG version {version}.",
        "",
        "export type MeshHandle = number & { readonly __mmg: 'mesh' };",
        "export type SolHandle = number & { readonly __mmg: 'sol' };",
        "",
        "export interface MmgFS {",
        "  writeFile(path: string, data: Uint8Array | string): void;",
        "  readFile(path: string, opts?: { encoding?: 'utf8' }): Uint8Array | string;",
        "  unlink(path: string): void;",
        "  mkdir(path: string): void;",
        "  readdir(path: string): string[];",
        "}",
        "",
        "export interface MmgHandles {",
        "  mesh: MeshHandle;",
        "  met: SolHandle;",
        "  ls?: SolHandle;",
        "  disp?: SolHandle;",
        "}",
        "",
    ]
    for mod, _, macro in HEADERS:
        iface = "Mmg" + mod[3:].upper() if False else mod.capitalize()
        lines.append(f"export interface {iface} {{")
        lines.append("  /** Allocate mesh + met (+ optional ls/disp) handle "
                     "boxes and initialize the structures. */")
        opts = "{ levelset?: boolean; displacement?: boolean }" \
            if macro != "MMGS" else "{ levelset?: boolean }"
        lines.append(f"  init(options?: {opts}): MmgHandles;")
        lines.append("  /** Free the structures and the handle boxes "
                     "allocated by init(). */")
        lines.append("  free(handles: MmgHandles): void;")
        for fn in funcs:
            if fn["path"][0] != mod or fn.get("unsupported"):
                continue
            params, ret = ts_signature(fn)
            doc = fn["doc"] or fn["c"]
            lines.append(f"  /** {doc} */")
            lines.append(f"  {fn['js']}({', '.join(params)}): {ret};")
            alias = ALIASES.get(fn["c"])
            if alias:
                lines.append(f"  /** Alias of {fn['js']}. */")
                lines.append(f"  {alias}({', '.join(params)}): {ret};")
        for k in sorted(constants[mod]):
            lines.append(f"  readonly {k}: number;")
        lines.append("}")
        lines.append("")
    lines.append("export interface Mmg {")
    lines.append("  mmg3d: Mmg3d;")
    lines.append("  mmg2d: Mmg2d;")
    lines.append("  mmgs: Mmgs;")
    lines.append("  FS: MmgFS;")
    lines.append("  module: Record<string, unknown>;")
    for k in sorted(constants["root"]):
        lines.append(f"  readonly {k}: number;")
    lines.append("}")
    lines += [
        "",
        "export declare function initialize(",
        "  moduleOverrides?: Record<string, unknown>",
        "): Promise<Mmg>;",
        "",
        "export default initialize;",
        "",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
def read_version():
    cml = open(os.path.join(ROOT, "mmg", "CMakeLists.txt")).read()
    parts = []
    for comp in ("MAJOR", "MINOR", "PATCH"):
        m = re.search(r'CMAKE_RELEASE_VERSION_' + comp + r'\s+"?(\d+)"?', cml)
        parts.append(m.group(1) if m else "?")
    return ".".join(parts)


def validate_overrides(funcs):
    """Warn when override tables drift from the parsed headers."""
    by_c = {f["c"]: f for f in funcs}
    for table, name in ((BULK, "BULK"), (RETMODE, "RETMODE"),
                        (UNSUPPORTED, "UNSUPPORTED"), (ALIASES, "ALIASES"),
                        (LIBCODE, "LIBCODE")):
        for c in table:
            if c not in by_c:
                print(f"WARNING: {name} entry {c} not found in headers",
                      file=sys.stderr)
    for c, spec in BULK.items():
        fn = by_c.get(c)
        if not fn:
            continue
        argnames = {a["name"] for a in fn["args"]}
        for arg in spec:
            if arg not in argnames:
                print(f"WARNING: BULK {c} names unknown arg '{arg}' "
                      f"(header has {sorted(argnames)})", file=sys.stderr)


def main():
    version = read_version()
    funcs = []
    for mod, header, macro in HEADERS:
        for proto in parse_prototypes(header, "LIB" + macro + "_EXPORT"):
            if proto["variadic"]:
                continue  # replaced by the mmgjs_* shims
            funcs.append(classify_function(proto, mod))
    validate_overrides(funcs)
    funcs += shim_entries()

    constants = collect_constants()
    os.makedirs(OUT_DIR, exist_ok=True)

    supported = [f for f in funcs if not f.get("unsupported")]
    symbols = sorted({"_" + f["c"] for f in supported} | {"_malloc", "_free"})
    with open(os.path.join(OUT_DIR, "exported_functions.json"), "w") as f:
        json.dump(symbols, f, indent=0)
        f.write("\n")

    with open(os.path.join(OUT_DIR, "mmg-api.json"), "w") as f:
        json.dump({
            "version": version,
            "functions": funcs,
            "constants": constants,
            "aliases": ALIASES,
        }, f, indent=1)
        f.write("\n")

    with open(os.path.join(OUT_DIR, "mmg.d.ts"), "w") as f:
        f.write(emit_ts(funcs, constants, version))

    unsup = [f for f in funcs if f.get("unsupported")]
    print(f"mmg-wasm bindings: {len(funcs)} functions, "
          f"{len(supported)} bound ({len(symbols)} exported symbols), "
          f"{len(unsup)} unsupported.")
    for f in unsup:
        print(f"  unsupported: {f['c']}: {f['reason']}")


if __name__ == "__main__":
    main()
