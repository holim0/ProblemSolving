/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
  const strLen = s.length;
  let maxLen = 1;
  let answer = s[0];
  const dp = [];
  for (let i = 0; i < strLen; i++) {
    dp.push(new Array(strLen).fill(false));
  }
  for (let i = 0; i < strLen; i++) {
    dp[i][i] = true;
  }
  for (let l = 2; l <= strLen; l++) {
    for (let i = 0; i <= strLen - l; i++) {
      if (l == 2) {
        if (s[i] === s[i + l - 1]) {
          dp[i][i + 1] = true;
          if (maxLen < l) {
            maxLen = l;
            answer = s.slice(i, i + l);
          }
        }
      } else {
        if (s[i] === s[i + l - 1] && dp[i + 1][i + l - 2]) {
          dp[i][i + l - 1] = true;
          if (maxLen < l) {
            maxLen = l;
            answer = s.slice(i, i + l);
          }
        }
      }
    }
  }
  return answer;
};
