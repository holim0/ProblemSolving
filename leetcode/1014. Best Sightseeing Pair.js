/**
 * @param {number[]} values
 * @return {number}
 */
var maxScoreSightseeingPair = function (values) {
  const size = values.length;
  let answer = -Infinity;

  let maxPrev = values[0];

  for (let i = 1; i < size; i++) {
    answer = Math.max(answer, maxPrev + values[i] - i);
    maxPrev = Math.max(maxPrev, values[i] + i);
  }

  return answer;
};
