function solution(target) {
  var answer = [];
  let dp = [];

  for (let i = 0; i <= target; i++) {
    dp.push([Infinity, 0]);
  }
  dp[0] = [0, 0];
  let single = [];
  let doubleTriple = [];
  for (let i = 1; i <= 20; i++) {
    single.push(i);
    doubleTriple.push(i * 2);
    doubleTriple.push(i * 3);
  }
  single.push(50);
  doubleTriple.sort();
  for (let i = 1; i <= target; i++) {
    for (let k = 0; k < single.length; k++) {
      let j = single[k];

      if (i >= j) {
        if (dp[i][0] > dp[i - j][0] + 1) {
          dp[i][0] = dp[i - j][0] + 1;
          dp[i][1] = dp[i - j][1] + 1;
        } else if (dp[i][0] === dp[i - j][0] + 1) {
          dp[i][1] = Math.max(dp[i][1], dp[i - j][1] + 1);
        }
      }
    }
    for (let k = 0; k < doubleTriple.length; k++) {
      let j = doubleTriple[k];

      if (i >= j) {
        if (dp[i][0] > dp[i - j][0] + 1) {
          dp[i][0] = dp[i - j][0] + 1;
          dp[i][1] = dp[i - j][1];
        } else if (dp[i][0] === dp[i - j][0] + 1) {
          dp[i][1] = Math.max(dp[i][1], dp[i - j][1]);
        }
      }
    }
  }
  answer = dp[target];
  return answer;
}
