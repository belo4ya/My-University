/* 4. Минимум.
Напишите функцию min, принимающую два аргумента,
и возвращающую минимальный из них.
 */

const min = (a, b) => {
  return a < b ? a : b;
}

const minHack = (a, b) => {
  return (a + b - Math.abs(a - b)) / 2
}

console.log(min(5, 2));
console.log(minHack(10, 11));
