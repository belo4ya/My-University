/* 13. Every и some.
Напишите функции every и some, которые работают так же, как эти
методы, только принимают массив в качестве аргумента.
 */

const some = (arr, predicate) => {
  for (const item of arr) {
    if (predicate(item)) return true;
  }
  return false;
}

const every = (arr, predicate) => {
  for (const item of arr) {
    if (!predicate(item)) return false;
  }
  return true;
}

console.log(every([NaN, NaN, NaN], isNaN));
console.log(every([NaN, NaN, 4], isNaN));
console.log(some([NaN, 3, 4], isNaN));
console.log(some([2, 3, 4], isNaN));
