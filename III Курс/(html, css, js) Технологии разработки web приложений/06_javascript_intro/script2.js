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
