/**
 * @param {number[]} nums
 * @return {number}
 */

var rob = function (nums) {
  const houseCnt = nums.length;
  let answer = 0;
  if (houseCnt === 1) return nums[0];
  if (houseCnt === 2) return Math.max(nums[0], nums[1]);

  const dp = new Array(houseCnt + 1).fill(0);
  dp[0] = nums[0];
  dp[1] = Math.max(nums[0], nums[1]);

  for (let i = 2; i < houseCnt; i++) {
    dp[i] = Math.max(dp[i - 1], nums[i] + dp[i - 2]);
  }

  return dp[houseCnt - 1];
};
