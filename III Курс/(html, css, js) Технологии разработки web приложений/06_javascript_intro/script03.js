/* 3. Шахматная доска.
Напишите программу, создающую строку,
содержащую решётку 8х8, в которой линии разделяются символами
новой строки. На каждой позиции либо пробел, либо #. В результате
должна получиться шахматная доска
 */

const chessBoard = (marker = '#') => {
  const oddRow = (marker + ' ').repeat(4);
  const evenRow = (' ' + marker).repeat(4);

  const stringBuilder = [];
  for (let i = 0; i < 8; i++) {
    if (i % 2 === 0) {
      stringBuilder.push(oddRow);
    } else {
      stringBuilder.push(evenRow);
    }
  }

  return stringBuilder.join('\n');
}

console.log(chessBoard());
