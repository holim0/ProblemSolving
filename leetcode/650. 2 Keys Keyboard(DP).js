/**
 * @param {number} n
 * @return {number}
 */

var minSteps = function (n) {
  const dp = new Array(n + 1).fill(Infinity);
  dp[1] = 0;

  for (let i = 2; i <= n; i++) {
    for (let j = 1; j * j <= i; j++) {
      if (i % j == 0) {
        dp[i] = Math.min(dp[i], dp[j] + i / j);

        if (j !== 1) {
          dp[i] = Math.min(dp[i], dp[i / j] + j);
        }
      }
    }
  }

  return dp[n];
};
