/* 6. Сумма диапазона.
Напишите функцию range, принимающую два
аргумента, начало и конец диапазона, и возвращающую массив,
который содержит все числа из него, включая начальное и
конечное. Затем напишите функцию sum, принимающую массив чисел
и возвращающую их сумму. Запустите указанную выше инструкцию и
убедитесь, что она возвращает 55.В качестве бонуса дополните
функцию range, чтобы она могла принимать необязательный третий
аргумент – шаг для построения массива. Если он не задан, шаг равен
единице. Вызов функции range(1, 10, 2) должен будет вернуть [1, 3, 5,
7, 9]. Убедитесь, что она работает с отрицательным шагом так, что
вызов range(5, 2, -1) возвращает [5, 4, 3, 2].
 */

const equals = (arrA, arrB) => {
  return JSON.stringify(arrA) === JSON.stringify(arrB);
}


function* range(start, end, step = 1) {
  if (step === 0) {
    throw `Invalid step value: step=${step}`;
  }
  const predicate = step > 0 ? (start, end) => start <= end : (start, end) => start >= end;
  while (predicate(start, end)) {
    yield start;
    start += step;
  }
}

console.log(Array.from(range(1, 10)).reduce((a, b) => a + b, 0));
console.log(Array.from(range(1, 10, 2)));
console.log(Array.from(range(5, 2, -1)));

let [start, end, step] = [];

[start, end] = [2, 10];
console.assert(
  equals(Array.from(range(start, end)), [2, 3, 4, 5, 6, 7, 8, 9, 10]),
  `start=${start}, end=${end}`
);

[start, end, step] = [2, 10, 2];
console.assert(
  equals(Array.from(range(start, end, step)), [2, 4, 6, 8, 10]),
  `start=${start}, end=${end}, step=${step}`
);

[start, end, step] = [-4, 7, 3];
console.assert(
  equals(Array.from(range(start, end, step)), [-4, -1, 2, 5]),
  `start=${start}, end=${end}, step=${step}`
);

[start, end, step] = [5, 2, -1];
console.assert(
  equals(Array.from(range(start, end, step)), [5, 4, 3, 2]),
  `start=${start}, end=${end}, step=${step}`
);

[start, end, step] = [10, -5, -3];
console.assert(
  equals(Array.from(range(start, end, step)), [10, 7, 4, 1, -2, -5]),
  `start=${start}, end=${end}, step=${step}`
);

try {
  console.log(Array.from(range(2, 10, 0)));
} catch (e) {
  console.assert(e === 'Invalid step value: step=0');
}
