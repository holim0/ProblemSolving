/**
 * @param {number[]} arr
 * @param {number[][]} mat
 * @return {number}
 */
var firstCompleteIndex = function (arr, mat) {
  const rowSize = mat.length;
  const colSize = mat[0].length;

  const rowCnt = new Array(rowSize).fill(0);
  const colCnt = new Array(colSize).fill(0);

  const pos = {};

  for (let i = 0; i < rowSize; i++) {
    for (let j = 0; j < colSize; j++) {
      let value = mat[i][j];
      pos[value] = [i, j];
    }
  }

  let answer = -1;

  for (let i = 0; i < arr.length; i++) {
    const value = arr[i];
    const [x, y] = pos[value];

    rowCnt[x] += 1;
    colCnt[y] += 1;

    if (rowCnt[x] === colSize || colCnt[y] === rowSize) {
      answer = i;
      break;
    }
  }

  return answer;
};
