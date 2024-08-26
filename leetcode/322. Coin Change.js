/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function (coins, amount) {
  if (amount === 0) return 0;
  const dp = new Array(amount + 1).fill(Infinity);
  for (let i = 1; i <= amount; i++) {
    if (coins.includes(i)) {
      dp[i] = 1;
    }
  }

  coins.forEach((c) => {
    for (let i = 1; i <= amount; i++) {
      if (i - c >= 0) {
        dp[i] = Math.min(dp[i], dp[i - c] + 1);
      }
    }
  });

  if (dp[amount] === Infinity) return -1;
  return dp[amount];
};
