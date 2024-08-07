function solution(sticker) {
  let answer = 0;
  let n = sticker.length;
  if (n === 1) {
    return sticker[0];
  }
  sticker.unshift(-1);

  let dp = new Array(sticker.length + 1).fill(0);
  dp[1] = sticker[1];
  for (let i = 2; i <= sticker.length - 1; i++) {
    dp[i] = Math.max(dp[i], dp[i - 1]);
    dp[i] = Math.max(dp[i], dp[i - 2] + sticker[i]);
  }
  let pickOne = dp[n - 1];
  dp = new Array(sticker.length + 1).fill(0);

  dp[1] = 0;
  for (let i = 2; i <= sticker.length; i++) {
    dp[i] = Math.max(dp[i], dp[i - 1]);
    dp[i] = Math.max(dp[i], dp[i - 2] + sticker[i]);
  }

  let pickLast = dp[n];
  console.log(pickLast, pickOne);
  answer = Math.max(pickLast, pickOne);
  return answer;
}
