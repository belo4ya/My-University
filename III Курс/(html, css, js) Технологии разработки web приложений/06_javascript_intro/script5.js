const countChar = (s, target) => {
  let cnt = 0;
  for (const ch of s) {
    target === ch && cnt++;
  }
  return cnt;
}

console.log(countChar('Hello, world!', 'o'));
