function solution(n) {
  let answer = 0;
  let mod = 1234567;
  let dp = new Array(n + 1).fill(0);

  dp[1] = 1;
  dp[2] = 2;

  for (let i = 3; i <= n; i++) {
    dp[i] = (dp[i - 1] + dp[i - 2]) % mod;
  }

  answer = dp[n] % mod;

  return answer;
}
