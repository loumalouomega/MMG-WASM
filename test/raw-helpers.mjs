// Minimal manual marshalling helpers for the raw MMG C API, used by the
// smoke test *before* the generated typed wrapper exists. wasm32: pointers
// are 4 bytes.

export function makeHelpers(Module) {
  const I32 = 'i32';

  const malloc = (n) => Module._malloc(n);
  const free = (p) => Module._free(p);

  // Allocate a zeroed 4-byte slot (handle box or int out-param).
  function slot() {
    const p = malloc(4);
    Module.setValue(p, 0, I32);
    return p;
  }
  const readInt = (p) => Module.getValue(p, I32);
  const readDouble = (p) => Module.getValue(p, 'double');

  // JS string -> NUL-terminated UTF8 in the heap.
  function cstr(s) {
    const n = Module.lengthBytesUTF8(s) + 1;
    const p = malloc(n);
    Module.stringToUTF8(s, p, n);
    return p;
  }

  // Call fn; MMG Set_/Get_ style functions return 1 on success.
  function checked(name, fn) {
    const r = fn();
    if (r !== 1) throw new Error(`${name} failed (returned ${r})`);
    return r;
  }

  return { malloc, free, slot, readInt, readDouble, cstr, checked };
}
