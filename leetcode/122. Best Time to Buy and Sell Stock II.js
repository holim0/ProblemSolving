/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  const size = prices.length;
  if (size === 1) return 0;
  const dp = new Array(size).fill(0);
  let answer = 0;
  if (prices[0] < prices[1]) {
    dp[1] = prices[1] - prices[0];
    answer = dp[1];
  }

  for (let i = 2; i < size; i++) {
    let curValue = prices[i];
    let prevValue = prices[i - 1];
    if (curValue > prevValue) {
      dp[i] = Math.max(dp[i], dp[i - 1] + curValue - prevValue);
      answer = Math.max(answer, dp[i]);
    } else {
      dp[i] = dp[i - 1];
      answer = Math.max(answer, dp[i]);
    }
  }

  return answer;
};
