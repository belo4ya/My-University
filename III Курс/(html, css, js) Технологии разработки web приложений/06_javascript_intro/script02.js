/* 2. FizzBuzz.
Напишите программу, которая выводит через console.log все
числа от 1 до 100, с двумя исключениями. Для чисел, нацело
делящихся на 3, она должна выводить ‘Fizz’, а для чисел, делящихся на
5 (но не на 3) – ‘Buzz’. Когда сумеете – исправьте её так, чтобы она
выводила «FizzBuzz» для всех чисел, которые делятся и на 3 и на 5.
 */

const _fizzBuzz = (n) => {
  if (n % 3 === 0 && n % 5 === 0) {
    return 'FizzBuzz'
  }
  if (n % 3 === 0) {
    return 'Fizz';
  }
  if (n % 5 === 0) {
    return 'Buzz';
  }
  return n;
}

const fizzBuzz = (n = 100) => {
  for (let i = 1; i < n + 1; i++) {
    console.log(_fizzBuzz(i));
  }
}

fizzBuzz(100);
