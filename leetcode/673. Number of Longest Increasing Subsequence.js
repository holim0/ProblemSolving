/**
 * @param {number[]} nums
 * @return {number}
 */
var findNumberOfLIS = function (nums) {
  const dp = new Array(nums.length).fill(1);
  const cnt = new Array(nums.length).fill(1);

  let max_len = 1;
  dp[0] = 1;
  for (let i = 1; i < nums.length; i++) {
    for (let j = 0; j < i; j++) {
      if (nums[j] < nums[i]) {
        if (dp[i] < dp[j] + 1) {
          dp[i] = dp[j] + 1;
          cnt[i] = cnt[j];
          max_len = Math.max(max_len, dp[i]);
        } else if (dp[i] === dp[j] + 1) {
          cnt[i] += cnt[j];
        }
      }
    }
  }
  let answer = 0;
  for (let i = 0; i < nums.length; i++) {
    if (dp[i] === max_len) {
      answer += cnt[i];
    }
  }
  return answer;
};
