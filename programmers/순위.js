function solution(n, results) {
  var answer = 0;

  let order = [];
  let cnt = new Array(n + 1).fill(0);
  let g = {};
  let check = [];
  for (let i = 0; i < n + 1; i++) {
    check.push(new Array(n + 1).fill(0));
  }

  results.forEach((r) => {
    let [a, b] = r;
    check[a][b] = 1;
    check[b][a] = -1;
  });
  for (let k = 1; k <= n; k++) {
    for (let i = 1; i <= n; i++) {
      for (let j = 1; j <= n; j++) {
        if (i === j) {
          continue;
        }

        if (check[i][k] == 1 && check[k][j] == 1) {
          check[i][j] = 1;
        } else if (check[i][k] == -1 && check[k][j] == -1) {
          check[i][j] = -1;
        }
      }
    }
  }
  for (let i = 1; i <= n; i++) {
    let zero = 0;
    for (let j = 1; j <= n; j++) {
      if (check[i][j] == 0) {
        zero += 1;
      }
    }
    if (zero === 1) {
      answer += 1;
    }
  }

  return answer;
}
