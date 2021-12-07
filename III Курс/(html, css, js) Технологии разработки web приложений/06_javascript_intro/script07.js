/* 7. Обращаем массив вспять.
Напишите две функции, reverseArray и reverseArrayInPlace.
Первая получает массив как аргумент и выдаёт новый массив,
с обратным порядком элементов. Вторая работает как
оригинальный метод reverse – она меняет порядок элементов на
обратный в том массиве, который был ей передан в качестве аргумента.
Не используйте стандартный метод reverse.
 */

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
