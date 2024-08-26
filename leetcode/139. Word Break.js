/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function (s, wordDict) {
  const slen = s.length;
  const dp = new Array(slen).fill(false);
  const wordMap = {};
  wordDict.forEach((word) => {
    wordMap[word] = true;
  });
  if (wordMap[s[0]]) {
    dp[0] = true;
  }

  for (let i = 1; i < slen; i++) {
    const curValue = s.substring(0, i + 1);
    if (wordMap[curValue]) {
      dp[i] = true;
      continue;
    }
    for (let j = 0; j < i; j++) {
      if (dp[j]) {
        const rightStr = s.substring(j + 1, i + 1);
        if (wordMap[rightStr]) {
          dp[i] = true;
        }
      }
    }
  }
  console.log(dp);
  return dp[slen - 1];
};
