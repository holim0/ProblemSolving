/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
  if (nums.length === 1) return nums[0];
  let answer = 0;
  let dp = new Array(nums.length).fill(0);
  dp[0] = nums[0];
  dp[1] = nums[1];
  answer = Math.max(nums[0], nums[1]);

  for (let i = 2; i < nums.length - 1; i++) {
    let maxValue = 0;
    for (let j = 0; j < i - 1; j++) {
      maxValue = Math.max(maxValue, dp[j]);
    }
    dp[i] = Math.max(dp[i], maxValue + nums[i]);
    answer = Math.max(dp[i], answer);
  }
  dp = new Array(nums.length).fill(0);
  dp[0] = nums[0];
  dp[1] = nums[1];

  for (let i = 2; i < nums.length; i++) {
    let maxValue = 0;
    for (let j = 1; j < i - 1; j++) {
      maxValue = Math.max(maxValue, dp[j]);
    }
    dp[i] = Math.max(dp[i], maxValue + nums[i]);
    answer = Math.max(dp[i], answer);
  }

  return answer;
};
