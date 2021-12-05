const reverseArray = (arr) => {
  const length = arr.length;
  return Array.from({length: length}, (v, k) => arr[length - 1 - k]);
}

const reverseArrayInPlace = (arr) => {
  const length = arr.length;
  for (let i = 0, j = length; i < length / 2; i++, j--) {
    [arr[i], arr[j - 1]] = [arr[j - 1], arr[i]];
  }
}


const arr = [1, 2, -3, -5, 7, 10];
console.log(reverseArray(arr));
reverseArrayInPlace(arr);
console.log(arr);
