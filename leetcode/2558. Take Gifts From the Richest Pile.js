/**
 * @param {number[]} gifts
 * @param {number} k
 * @return {number}
 */
var pickGifts = function (gifts, k) {
  while (k) {
    gifts.sort((a, b) => b - a);
    gifts[0] = Math.floor(Math.sqrt(gifts[0]));
    k -= 1;
  }

  const answer = gifts.reduce((acc, cur) => {
    acc += cur;
    return acc;
  }, 0);
  return answer;
};
