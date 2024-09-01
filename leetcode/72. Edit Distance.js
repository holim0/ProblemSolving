/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var minDistance = function (word1, word2) {
  const w1Len = word1.length;
  const w2Len = word2.length;
  word1 = " " + word1;
  word2 = " " + word2;
  const dp = [];
  for (let i = 0; i <= w1Len; i++) {
    dp.push(new Array(w2Len + 1).fill(Infinity));
  }
  for (let i = 0; i <= w1Len; i++) {
    dp[i][0] = i;
  }
  for (let i = 0; i <= w2Len; i++) {
    dp[0][i] = i;
  }
  for (let i = 1; i <= w1Len; i++) {
    for (let j = 1; j <= w2Len; j++) {
      if (word1[i] === word2[j]) {
        dp[i][j] = dp[i - 1][j - 1];
      } else {
        dp[i][j] = Math.min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1;
      }
    }
  }
  return dp[w1Len][w2Len];
};
