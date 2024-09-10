/**
 * @param {number} n
 * @return {number}
 */
var totalNQueens = function (n) {
  let answer = 0;
  const check = [];
  for (let i = 0; i < n; i++) {
    check.push(new Array(n).fill(false));
  }
  const isValid = (x, y) => {
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (check[i][j]) {
          if (Math.abs(x - i) === Math.abs(y - j)) {
            return false;
          }
        }
      }
    }
    return true;
  };
  let rowCheck = new Array(n).fill(false);
  let colCheck = new Array(n).fill(false);
  const getSol = (curRow, cnt) => {
    if (cnt === n) {
      answer += 1;
      return;
    }
    for (let i = 0; i < n; i++) {
      if (
        !check[curRow][i] &&
        !rowCheck[curRow] &&
        !colCheck[i] &&
        isValid(curRow, i)
      ) {
        check[curRow][i] = true;
        rowCheck[curRow] = true;
        colCheck[i] = true;
        getSol(curRow + 1, cnt + 1);
        check[curRow][i] = false;
        rowCheck[curRow] = false;
        colCheck[i] = false;
      }
    }
  };
  getSol(0, 0);

  return answer;
};
