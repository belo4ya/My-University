// Треугольник. Напишите цикл, выводит такой треугольник.

/**
 * @param {*} data
 * @param {string} end
 * @return {undefined}
 */
const print = (data, end = '\n') => {
  console.log(data + end);
}

const DEFAULT_MARKER = '#';

/**
 * @param {number} n
 * @param {string} marker
 * @return {string}
 */
const triangle = (n, marker = DEFAULT_MARKER) => {
  const stringBuilder = [];
  marker += ' ';
  for (let i = 1; i < n + 1; i++) {
    stringBuilder.push(marker.repeat(i));
  }
  return stringBuilder.join('\n');
}

const square = (n, marker = DEFAULT_MARKER) => {
  const stringBuilder = [];
  marker += ' ';
  for (let i = 1; i < n + 1; i++) {
    stringBuilder.push(marker.repeat(n));
  }
  return stringBuilder.join('\n');
}

const pyramid = (n, marker = DEFAULT_MARKER) => {
  const stringBuilder = [];
  marker += ' ';
  for (let i = 1; i < n + 1; i++) {
    stringBuilder.push((' '.repeat(n - i) + marker.repeat(i)));
  }
  return stringBuilder.join('\n');
}

const rhombus = (n, marker = DEFAULT_MARKER) => {
  const stringBuilder = [];
  marker += ' ';
  for (let i = 1; i < n + 1; i++) {
    stringBuilder.push((' '.repeat(n - i) + marker.repeat(i)));
  }
  stringBuilder.push(...stringBuilder.slice(0, -1).reverse());
  return stringBuilder.join('\n')
}

const hourglass = (n, marker = DEFAULT_MARKER) => {
  const stringBuilder = [];
  marker += ' ';
  for (let i = 1; i < n + 1; i++) {
    stringBuilder.push((' '.repeat(n - i) + marker.repeat(i)));
  }
  return [...stringBuilder.slice(1).reverse(), ...stringBuilder].join('\n')
}

const christmasTree = (n, marker = DEFAULT_MARKER) => {
  const stringBuilder = [];
  marker += '   ';
  for (let i = 1; i < n + 1; i++) {
    stringBuilder.push(('  '.repeat(n - i) + marker.repeat(i)));
  }
  return [...stringBuilder.slice(0, -4), ...stringBuilder.slice(1, -2), ...stringBuilder.slice(1)].join('\n')
}

print(triangle(5));
print(square(5));
print(pyramid(5));
print(rhombus(5))
print(hourglass(5))
print(christmasTree(9))
