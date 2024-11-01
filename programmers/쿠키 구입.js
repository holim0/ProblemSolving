function solution(cookie) {
  var answer = -1;
  let acc = [0, cookie[0]];

  for (let i = 1; i < cookie.length; i++) {
    acc.push(acc[acc.length - 1] + cookie[i]);
  }

  for (let m = 1; m < acc.length - 1; m++) {
    let l = 1;
    let r = acc.length - 1;

    while (l <= m && m < r) {
      let leftSum = acc[m] - acc[l - 1];
      let rightSum = acc[r] - acc[m];

      if (leftSum < rightSum) {
        r -= 1;
      } else if (leftSum > rightSum) {
        l += 1;
      } else {
        answer = Math.max(answer, leftSum);
        r -= 1;
        l += 1;
      }
    }
  }
  if (answer === -1) return 0;
  return answer;
}
