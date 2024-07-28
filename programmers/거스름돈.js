function solution(n, money) {
  var answer = 0;
  const MOD = 1000000007;
  let dp = new Array(n + 1).fill(0);

  dp[0] = 1;
  for (let i = 0; i < money.length; i++) {
    for (let j = 1; j <= n + 1; j++) {
      if (j - money[i] >= 0) {
        dp[j] += dp[j - money[i]];
      }
    }
  }
  answer = dp[n] % MOD;
  return answer;
}
