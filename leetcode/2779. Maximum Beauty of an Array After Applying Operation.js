/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maximumBeauty = function (nums, k) {
  const len = nums.length;
  nums.sort((a, b) => a - b);
  let i = 0,
    j = 0;
  answer = 0;
  while (i <= j && i < len && j < len) {
    if (nums[j] - nums[i] <= 2 * k) {
      answer = Math.max(answer, j - i + 1);
      j += 1;
    } else {
      i += 1;
    }
  }

  return answer;
};
