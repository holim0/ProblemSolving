/**
 * @param {string} s
 * @return {number}
 */
var numDecodings = function (s) {
  if (s[0] === "0") return 0;
  s = " " + s;
  const dp = new Array(s.length).fill(0);
  dp[0] = 1;
  dp[1] = 1;

  for (let i = 2; i <= s.length; i++) {
    if (s[i] !== "0") {
      dp[i] += dp[i - 1];
    }
    if (s[i - 1] !== "0") {
      let value = parseInt(s[i - 1] + s[i]);
      if (value <= 26) {
        dp[i] += dp[i - 2];
      }
    }
  }
  return dp[s.length - 1];
};
