const reverseArray = (arr) => {
  const length = arr.length;
  return Array.from({length: length}, (v, k) => arr[length - 1 - k]);
}

const reverseArrayInPlace = (arr) => {
  const length = arr.length;
  for (let i = 0; i < length / 2; i++) {
    [arr[i], arr[length - 1 - i]] = [arr[length - 1 - i], arr[i]];
  }
}


const arr = [1, 2, -3, -5, 7, 10]
console.log(reverseArray(arr));
reverseArrayInPlace(arr);
console.log(arr);
