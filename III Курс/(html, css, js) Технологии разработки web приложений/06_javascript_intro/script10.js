const naiveFlatten = (arr) => {
  return arr.reduce((prev, curr) => prev.concat(curr), []);
}

function* flatten(arr) {
  for (const item of arr) {
    if (Array.isArray(item)) {
      for (const i of flatten(item)) {
        yield i;
      }
    } else {
      yield item;
    }
  }
}


const arr = [1, 2, 3, 4, [1, 3, 5, 4], 3, [1, 2], [1, 2, [5, 4, [0]]]];
console.log(naiveFlatten(arr));
console.log(Array.from(flatten(arr)));
