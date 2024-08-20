/**
 * @param {number} n
 * @return {boolean}
 */
var divisorGame = function (n) {
  const dp = new Array(n + 1).fill(false);
  for (let i = 2; i <= n; i++) {
    for (let x = 1; x < i; x++) {
      if (i % x === 0 && !dp[i - x]) {
        dp[i] = true;
        break;
      }
    }
  }
  return dp[n];
};
