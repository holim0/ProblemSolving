function solution(land) {
  var answer = 0;
  const n = land.length;

  for (let i = 1; i < n; i++) {
    for (let j = 0; j < 4; j++) {
      let maxValue = 0;
      for (let k = 0; k < 4; k++) {
        if (k != j) {
          maxValue = Math.max(maxValue, land[i - 1][k]);
        }
      }
      land[i][j] += maxValue;
    }
  }

  for (let k = 0; k < 4; k++) {
    answer = Math.max(answer, land[n - 1][k]);
  }

  return answer;
}
