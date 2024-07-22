function solution(n) {
  let answer = 0;
  let curSum = 0;
  let window = [];
  let p = 0;
  let curNum = 1;

  let idx = 1;

  while (curNum <= n) {
    if (curSum <= n) {
      if (curSum == n) {
        answer += 1;
      }
      curSum += curNum;
      window.push(curNum);
      curNum += 1;
    } else {
      curSum -= window[p];
      p += 1;
    }
  }

  return answer + 1;
}
