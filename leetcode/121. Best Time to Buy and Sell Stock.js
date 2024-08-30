/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let minBuy = Infinity;
  let answer = 0;
  const dp = new Array(prices.length).fill(0);
  minBuy = prices[0];

  for (let i = 1; i < prices.length; i++) {
    if (minBuy < prices[i]) {
      dp[i] = prices[i] - minBuy;
      answer = Math.max(dp[i], answer);
    } else {
      minBuy = prices[i];
    }
  }

  return answer;
};
