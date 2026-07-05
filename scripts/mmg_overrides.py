"""Hand-maintained classification tables consumed by gen_js.py.

MMG's headers have no machine-readable in/out annotations (no \\param[out]),
so anything the name-based rules cannot classify is listed here. Keep these
tables small: only bulk-array functions, return-mode exceptions and the
force-unsupported list live here. Everything else is derived from the
prototypes. gen_js.py validates every key against the parsed headers and
warns on drift.

BULK entry shapes (keyed by C symbol, then by C arg name -- names must match
the header exactly):
  input  arrays: ("iarraydouble",) / ("iarrayint",) / (..., "nullable")
  output arrays, caller-sized: ("oarraydouble", per, countParam[, "nullable"])
     per        = components per entity (3D vertex -> 3 doubles, tetra -> 4
                  ints); byte size allocated = per * <countParam> * elemsize.
     countParam = name of the extra JS parameter giving the entity count
                  (mmg cannot report array sizes itself; callers know them
                  from getMeshSize / getSolSize).
  output arrays, fixed-size:   ("oarraydouble", count)  e.g. eigenvectors.
"""

# The 9 remeshing entry points: return MMG5_SUCCESS(0)/LOWFAILURE(1)/
# STRONGFAILURE(2); the wrapper throws only on STRONGFAILURE.
LIBCODE = {
    "MMG3D_mmg3dlib", "MMG3D_mmg3dls", "MMG3D_mmg3dmov",
    "MMG2D_mmg2dlib", "MMG2D_mmg2dmesh", "MMG2D_mmg2dls", "MMG2D_mmg2dmov",
    "MMGS_mmgslib", "MMGS_mmgsls",
}

# Functions whose int/MMG5_int return is a value (index, count, order...) and
# not a 1-ok status. double returns are auto-detected.
RETMODE = {
    "MMG3D_Add_vertex": "int",           # returns new vertex index (0 on error)
    "MMG2D_Get_adjaVertices": "int",     # returns number of adjacent vertices
    "MMG2D_Get_adjaVerticesFast": "int",
    "MMGS_Get_adjaVerticesFast": "int",
    "MMG2D_Compute_eigenv": "int",       # returns eigenvalue order
    "MMG3D_Compute_eigenv": "int",
    "MMGS_Compute_eigenv": "int",
}

# Force-unsupported: struct pointers, CLI plumbing and diagnostics that make
# no sense from JS. Kept in the descriptor (unsupported: true) for docs.
UNSUPPORTED = {
    "MMG3D_stockOptions", "MMG3D_destockOptions",
    "MMGS_stockOptions", "MMGS_destockOptions",
    "MMG3D_parsar", "MMG2D_parsar", "MMGS_parsar",
    "MMG3D_parsop", "MMG2D_parsop",       # read CLI option *files*
    "MMG3D_mmg3dcheck", "MMG3D_searchqua", "MMG3D_searchlen",  # diagnostics
    # declared in libmmg2d.h but never defined anywhere in the library
    "MMG2D_loadVect", "MMG2D_saveVect", "MMG2D_scaleMesh",
}

# Friendly aliases: extra JS names bound to the same C symbol.
ALIASES = {
    "MMG3D_mmg3dlib": "remesh",
    "MMG3D_mmg3dls": "levelset",
    "MMG3D_mmg3dmov": "move",
    "MMG2D_mmg2dlib": "remesh",
    "MMG2D_mmg2dmesh": "generate",
    "MMG2D_mmg2dls": "levelset",
    "MMG2D_mmg2dmov": "move",
    "MMGS_mmgslib": "remesh",
    "MMGS_mmgsls": "levelset",
}

BULK = {}

for _mod in ("MMG3D", "MMG2D", "MMGS"):
    # vertices: coordinate dim (2 in mmg2d); vector sol dim matches.
    _vdim = 2 if _mod == "MMG2D" else 3
    _tdim = 3 if _mod == "MMG2D" else 6   # tensor components
    BULK.update({
        f"{_mod}_Set_vertices": {
            "vertices": ("iarraydouble",),
            "refs": ("iarrayint", "nullable"),
        },
        f"{_mod}_Get_vertices": {
            "vertices": ("oarraydouble", _vdim, "np"),
            "refs": ("oarrayint", 1, "np", "nullable"),
            "areCorners": ("oarrayint", 1, "np", "nullable"),
            "areRequired": ("oarrayint", 1, "np", "nullable"),
        },
        f"{_mod}_Set_triangles": {
            "tria": ("iarrayint",),
            "refs": ("iarrayint", "nullable"),
        },
        f"{_mod}_Get_triangles": {
            "tria": ("oarrayint", 3, "nt"),
            "refs": ("oarrayint", 1, "nt", "nullable"),
            "areRequired": ("oarrayint", 1, "nt", "nullable"),
        },
        f"{_mod}_Set_edges": {
            "edges": ("iarrayint",),
            "refs": ("iarrayint", "nullable"),
        },
        f"{_mod}_Get_edges": {
            "edges": ("oarrayint", 2, "na"),
            "refs": ("oarrayint", 1, "na", "nullable"),
            "areRidges": ("oarrayint", 1, "na", "nullable"),
            "areRequired": ("oarrayint", 1, "na", "nullable"),
        },
        # solution values, one entity block per vertex; count params are the
        # number of entities (from getSolSize).
        f"{_mod}_Set_scalarSols": {"s": ("iarraydouble",)},
        f"{_mod}_Get_scalarSols": {"s": ("oarraydouble", 1, "np")},
        f"{_mod}_Set_vectorSols": {"sols": ("iarraydouble",)},
        f"{_mod}_Get_vectorSols": {"sols": ("oarraydouble", _vdim, "np")},
        f"{_mod}_Set_tensorSols": {"sols": ("iarraydouble",)},
        f"{_mod}_Get_tensorSols": {"sols": ("oarraydouble", _tdim, "np")},
        # multi-solution fields: `n` = total number of scalar values of the
        # ith field (nentities * field size).
        f"{_mod}_Set_ithSol_inSolsAtVertices": {"s": ("iarraydouble",)},
        f"{_mod}_Get_ithSol_inSolsAtVertices": {"s": ("oarraydouble", 1, "n")},
        f"{_mod}_Set_ithSols_inSolsAtVertices": {"s": ("iarraydouble",)},
        f"{_mod}_Get_ithSols_inSolsAtVertices": {"s": ("oarraydouble", 1, "n")},
        # multi-solution setup: typSol is an int array of length nsols
        # (MMG5_NSOLS_MAX = 100 max); on Get it is filled up to nsols entries.
        f"{_mod}_Set_solsAtVerticesSize": {"typSol": ("iarrayint",)},
        f"{_mod}_Get_solsAtVerticesSize": {"typSol": ("oarrayint", 100)},
        # eigen decomposition of a metric tensor: m is input, lambda/vp out.
        f"{_mod}_Compute_eigenv": {
            "m": ("iarraydouble",),
            "lambda": ("oarraydouble", _vdim),
            "vp": ("oarraydouble", _vdim * _vdim),
        },
    })

BULK.update({
    "MMG3D_Set_tetrahedra": {
        "tetra": ("iarrayint",),
        "refs": ("iarrayint", "nullable"),
    },
    "MMG3D_Get_tetrahedra": {
        "tetra": ("oarrayint", 4, "ne"),
        "refs": ("oarrayint", 1, "ne", "nullable"),
        "areRequired": ("oarrayint", 1, "ne", "nullable"),
    },
    "MMG3D_Set_prisms": {
        "prisms": ("iarrayint",),
        "refs": ("iarrayint", "nullable"),
    },
    "MMG3D_Get_prisms": {
        "prisms": ("oarrayint", 6, "nprism"),
        "refs": ("oarrayint", 1, "nprism", "nullable"),
        "areRequired": ("oarrayint", 1, "nprism", "nullable"),
    },
    "MMG3D_Set_quadrilaterals": {
        "quads": ("iarrayint",),
        "refs": ("iarrayint", "nullable"),
    },
    "MMG3D_Get_quadrilaterals": {
        "quads": ("oarrayint", 4, "nquad"),
        "refs": ("oarrayint", 1, "nquad", "nullable"),
        "areRequired": ("oarrayint", 1, "nquad", "nullable"),
    },
    "MMG2D_Set_quadrilaterals": {
        "quadra": ("iarrayint",),
        "refs": ("iarrayint", "nullable"),
    },
    "MMG2D_Get_quadrilaterals": {
        "quadra": ("oarrayint", 4, "nquad"),
        "refs": ("oarrayint", 1, "nquad", "nullable"),
        "areRequired": ("oarrayint", 1, "nquad", "nullable"),
    },
    # required/parallel entity index lists (input arrays of length nreq/npar)
    "MMG3D_Set_requiredTetrahedra": {"reqIdx": ("iarrayint",)},
    "MMG3D_Unset_requiredTetrahedra": {"reqIdx": ("iarrayint",)},
    "MMG3D_Set_requiredTriangles": {"reqIdx": ("iarrayint",)},
    "MMG3D_Unset_requiredTriangles": {"reqIdx": ("iarrayint",)},
    "MMG3D_Set_parallelTriangles": {"parIdx": ("iarrayint",)},
    "MMG3D_Unset_parallelTriangles": {"parIdx": ("iarrayint",)},
})

# Fixed-size Compute_eigenv arrays: mmg2d works on 2x2 metrics (m has 3
# entries), mmg3d/mmgs on 3x3 (m has 6). Adjust the input sizes emitted above
# (only lambda/vp sizes differ per module and are set in the loop).
BULK["MMG2D_Compute_eigenv"]["m"] = ("iarraydouble",)
