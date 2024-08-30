/**
 * @param {string} s1
 * @param {string} s2
 * @param {string} s3
 * @return {boolean}
 */
var isInterleave = function (s1, s2, s3) {
  const dp = [];
  s1 = " " + s1;
  s2 = " " + s2;
  s3 = " " + s3;
  for (let i = 0; i < s1.length + 1; i++) {
    dp.push(new Array(s2.length + 1).fill(false));
  }
  dp[0][0] = true;
  for (let i = 1; i <= s1.length; i++) {
    dp[i][0] = dp[i - 1][0] && s1[i] === s3[i];
  }
  for (let i = 1; i <= s2.length; i++) {
    dp[0][i] = dp[0][i - 1] && s2[i] === s3[i];
  }

  for (let i = 1; i <= s1.length; i++) {
    for (let j = 1; j <= s2.length; j++) {
      dp[i][j] =
        (dp[i - 1][j] && s1[i] === s3[i + j]) ||
        (dp[i][j - 1] && s2[j] === s3[i + j]);
    }
  }
  return dp[s1.length][s2.length];
};
