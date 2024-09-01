/**
 * @param {character[][]} matrix
 * @return {number}
 */
var maximalSquare = function (matrix) {
  let answer = 0;
  let m = matrix[0].length;
  let n = matrix.length;
  const dp = [];
  for (let i = 0; i < n; i++) {
    dp.push(new Array(m).fill(0));
  }
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (matrix[i][j] === "1") {
        dp[i][j] = 1;
        answer = 1;
      }
    }
  }

  for (let i = 1; i < n; i++) {
    for (let j = 1; j < m; j++) {
      let cur = matrix[i][j];
      if (cur === "1") {
        let minSize = Math.min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]);
        if (minSize !== 0) {
          dp[i][j] = Math.max(dp[i][j], minSize + 1);
          answer = Math.max(dp[i][j], answer);
        }
      }
    }
  }
  return answer * answer;
};
