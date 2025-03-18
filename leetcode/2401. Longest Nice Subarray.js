/**
 * @param {number[]} nums
 * @return {number}
 */
var longestNiceSubarray = function (nums) {
  const size = nums.length;
  let answer = 1;
  let l = 0,
    r = 1;

  while (l <= r && r < size) {
    const cur = nums[r];

    const start = l;

    for (let i = start; i < r; i++) {
      const and = cur & nums[i];

      if (and !== 0) {
        l = i + 1;
      }
    }

    answer = Math.max(answer, r - l + 1);

    r += 1;
  }
  return answer;
};
