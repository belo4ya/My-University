export const deepEqual = (a, b) => {
  if (a === b) return true;

  else if (a && b && typeof a === 'object' && typeof b === 'object') {
    if (Object.keys(a).length !== Object.keys(b).length) return false;
    for (const key in a) {
      if (!(key in b)) return false;
      if (!deepEqual(a[key], b[key])) return false;
    }
    return true;
  }

  return false;
}
