function solution(s) {
  let answer = 1;
  const size = s.length;
  if (size === 1) return 1;
  const dp = [];

  for (let i = 0; i < size; i++) {
    dp.push(new Array(size).fill(false));
  }

  for (let i = 0; i < size; i++) {
    dp[i][i] = true;
  }
  for (let i = 0; i < size - 1; i++) {
    if (s[i] === s[i + 1]) {
      dp[i][i + 1] = true;
      answer = 2;
    }
  }

  for (let l = 3; l <= size; l++) {
    for (let i = 0; i <= size - l; i++) {
      const left = s[i];
      const right = s[i + l - 1];

      if (left === right && dp[i + 1][i + l - 2]) {
        dp[i][i + l - 1] = true;
        answer = Math.max(answer, l);
      }
    }
  }

  return answer;

  return answer;
}
