/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function (nums, k) {
  let i = 0;
  let j = k - 1;
  const acc = [nums[0]];
  let answer = -Infinity;
  for (let i = 1; i < nums.length; i++) {
    acc.push(acc[acc.length - 1] + nums[i]);
  }

  while (j < nums.length) {
    let curSum = null;
    if (i === 0) {
      curSum = acc[j];
    } else {
      curSum = acc[j] - acc[i - 1];
    }
    let avg = curSum / k;
    answer = Math.max(answer, avg);
    i += 1;
    j += 1;
  }

  return answer;
};
