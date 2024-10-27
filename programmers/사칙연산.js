function solution(arr) {
  let answer = 0;
  let oper = [];
  let number = [];
  let max_dp = [];
  let min_dp = [];
  for (let i = 0; i < arr.length; i++) {
    max_dp.push(new Array(arr.length).fill(-Infinity));
    min_dp.push(new Array(arr.length).fill(Infinity));
  }

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === "+" || arr[i] === "-") {
      oper.push(arr[i]);
    } else {
      number.push(Number(arr[i]));
    }
  }

  for (let i = 0; i < number.length; i++) {
    max_dp[i][i] = number[i];
    min_dp[i][i] = number[i];
  }
  for (let i = 0; i < number.length - 1; i++) {
    let value = 0;
    if (oper[i] === "+") {
      value = number[i] + number[i + 1];
    } else {
      value = number[i] - number[i + 1];
    }
    max_dp[i][i + 1] = value;
    min_dp[i][i + 1] = value;
  }

  for (let size = 3; size <= number.length; size++) {
    for (let start = 0; start <= number.length - size; start++) {
      let end = start + size - 1;
      for (let idx = start; idx < end; idx++) {
        let curValue = 0;
        if (oper[idx] === "+") {
          max_dp[start][end] = Math.max(
            max_dp[start][end],
            max_dp[start][idx] + max_dp[idx + 1][end]
          );
          min_dp[start][end] = Math.min(
            min_dp[start][end],
            min_dp[start][idx] + min_dp[idx + 1][end]
          );
        } else {
          max_dp[start][end] = Math.max(
            max_dp[start][end],
            max_dp[start][idx] - min_dp[idx + 1][end]
          );
          min_dp[start][end] = Math.min(
            min_dp[start][end],
            min_dp[start][idx] - max_dp[idx + 1][end]
          );
        }
      }
    }
  }

  answer = max_dp[0][number.length - 1];
  return answer;
}
