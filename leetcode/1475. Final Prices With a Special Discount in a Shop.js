/**
 * @param {number[]} prices
 * @return {number[]}
 */
var finalPrices = function (prices) {
  const answer = new Array(prices.length).fill(0);

  const stack = [[prices[0], 0]];
  const idx = 1;

  for (let i = 1; i < prices.length; i++) {
    const curP = prices[i];

    while (stack.length && stack[stack.length - 1][0] >= curP) {
      const [topP, idx] = stack.pop();
      answer[idx] = topP - curP;
    }

    stack.push([curP, i]);
  }

  while (stack.length) {
    const [topP, idx] = stack.pop();
    answer[idx] = topP;
  }

  return answer;
};
