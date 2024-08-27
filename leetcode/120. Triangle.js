/**
 * @param {number[][]} triangle
 * @return {number}
 */
var minimumTotal = function (triangle) {
  const dp = [];
  const h = triangle.length;
  let answer = Infinity;
  const maxSize = triangle[h - 1].length;
  for (let i = 0; i < h; i++) {
    dp.push(new Array(maxSize).fill(Infinity));
  }
  dp[0][0] = triangle[0][0];
  for (let i = 1; i < h; i++) {
    let w = triangle[i].length;
    for (let j = 0; j < w; j++) {
      if (j === 0) {
        dp[i][j] = Math.min(dp[i][j], triangle[i][j] + dp[i - 1][0]);
      } else if (j === w - 1) {
        dp[i][j] = Math.min(dp[i][j], triangle[i][j] + dp[i - 1][w - 2]);
      } else {
        dp[i][j] = Math.min(
          dp[i][j],
          triangle[i][j] + dp[i - 1][j - 1],
          triangle[i][j] + dp[i - 1][j]
        );
      }
    }
  }

  for (let i = 0; i < maxSize; i++) {
    answer = Math.min(answer, dp[h - 1][i]);
  }
  return answer;
};
