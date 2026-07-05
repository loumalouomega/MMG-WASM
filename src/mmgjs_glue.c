/*
 * Fixed-arity shims over MMG's variadic init/free functions.
 *
 * MMG5_ARG_* keyword varargs (MMG3D_Init_mesh(MMG5_ARG_start, ...)) cannot be
 * called from JavaScript through a wasm table signature, so each variadic
 * entry point gets a fixed-arity wrapper taking the pointer slots directly.
 * A NULL ls/disp slot omits that keyword from the underlying variadic call.
 *
 * mmg3d and mmg2d accept ppMesh/ppMet/ppLs/ppDisp; mmgs has no Lagrangian
 * motion and only accepts ppMesh/ppMet/ppLs.
 *
 * Everything else JS needs (heap slots for the handles) is plain _malloc from
 * the runtime; no other C glue exists.
 */

#include "mmg/libmmg.h"

/* Dispatch on which optional slots are present (4 combinations). */
#define MMGJS_CALL4(FN, mesh, met, ls, disp)                                   \
  do {                                                                         \
    if ((ls) && (disp))                                                        \
      return FN(MMG5_ARG_start, MMG5_ARG_ppMesh, (mesh), MMG5_ARG_ppMet,       \
                (met), MMG5_ARG_ppLs, (ls), MMG5_ARG_ppDisp, (disp),           \
                MMG5_ARG_end);                                                 \
    if (ls)                                                                    \
      return FN(MMG5_ARG_start, MMG5_ARG_ppMesh, (mesh), MMG5_ARG_ppMet,       \
                (met), MMG5_ARG_ppLs, (ls), MMG5_ARG_end);                     \
    if (disp)                                                                  \
      return FN(MMG5_ARG_start, MMG5_ARG_ppMesh, (mesh), MMG5_ARG_ppMet,       \
                (met), MMG5_ARG_ppDisp, (disp), MMG5_ARG_end);                 \
    return FN(MMG5_ARG_start, MMG5_ARG_ppMesh, (mesh), MMG5_ARG_ppMet, (met),  \
              MMG5_ARG_end);                                                   \
  } while (0)

#define MMGJS_CALL3(FN, mesh, met, ls)                                         \
  do {                                                                         \
    if (ls)                                                                    \
      return FN(MMG5_ARG_start, MMG5_ARG_ppMesh, (mesh), MMG5_ARG_ppMet,       \
                (met), MMG5_ARG_ppLs, (ls), MMG5_ARG_end);                     \
    return FN(MMG5_ARG_start, MMG5_ARG_ppMesh, (mesh), MMG5_ARG_ppMet, (met),  \
              MMG5_ARG_end);                                                   \
  } while (0)

/* ------------------------------ mmg3d ---------------------------------- */

int mmgjs_MMG3D_Init_mesh(MMG5_pMesh *mesh, MMG5_pSol *met, MMG5_pSol *ls,
                          MMG5_pSol *disp) {
  MMGJS_CALL4(MMG3D_Init_mesh, mesh, met, ls, disp);
}

int mmgjs_MMG3D_Free_all(MMG5_pMesh *mesh, MMG5_pSol *met, MMG5_pSol *ls,
                         MMG5_pSol *disp) {
  MMGJS_CALL4(MMG3D_Free_all, mesh, met, ls, disp);
}

int mmgjs_MMG3D_Free_structures(MMG5_pMesh *mesh, MMG5_pSol *met,
                                MMG5_pSol *ls, MMG5_pSol *disp) {
  MMGJS_CALL4(MMG3D_Free_structures, mesh, met, ls, disp);
}

int mmgjs_MMG3D_Free_names(MMG5_pMesh *mesh, MMG5_pSol *met, MMG5_pSol *ls,
                           MMG5_pSol *disp) {
  MMGJS_CALL4(MMG3D_Free_names, mesh, met, ls, disp);
}

/* ------------------------------ mmg2d ---------------------------------- */

int mmgjs_MMG2D_Init_mesh(MMG5_pMesh *mesh, MMG5_pSol *met, MMG5_pSol *ls,
                          MMG5_pSol *disp) {
  MMGJS_CALL4(MMG2D_Init_mesh, mesh, met, ls, disp);
}

int mmgjs_MMG2D_Free_all(MMG5_pMesh *mesh, MMG5_pSol *met, MMG5_pSol *ls,
                         MMG5_pSol *disp) {
  MMGJS_CALL4(MMG2D_Free_all, mesh, met, ls, disp);
}

int mmgjs_MMG2D_Free_structures(MMG5_pMesh *mesh, MMG5_pSol *met,
                                MMG5_pSol *ls, MMG5_pSol *disp) {
  MMGJS_CALL4(MMG2D_Free_structures, mesh, met, ls, disp);
}

int mmgjs_MMG2D_Free_names(MMG5_pMesh *mesh, MMG5_pSol *met, MMG5_pSol *ls,
                           MMG5_pSol *disp) {
  MMGJS_CALL4(MMG2D_Free_names, mesh, met, ls, disp);
}

/* ------------------------------ mmgs ----------------------------------- */

int mmgjs_MMGS_Init_mesh(MMG5_pMesh *mesh, MMG5_pSol *met, MMG5_pSol *ls) {
  MMGJS_CALL3(MMGS_Init_mesh, mesh, met, ls);
}

int mmgjs_MMGS_Free_all(MMG5_pMesh *mesh, MMG5_pSol *met, MMG5_pSol *ls) {
  MMGJS_CALL3(MMGS_Free_all, mesh, met, ls);
}

int mmgjs_MMGS_Free_structures(MMG5_pMesh *mesh, MMG5_pSol *met,
                               MMG5_pSol *ls) {
  MMGJS_CALL3(MMGS_Free_structures, mesh, met, ls);
}

int mmgjs_MMGS_Free_names(MMG5_pMesh *mesh, MMG5_pSol *met, MMG5_pSol *ls) {
  MMGJS_CALL3(MMGS_Free_names, mesh, met, ls);
}
