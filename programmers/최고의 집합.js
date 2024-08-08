function solution(n, s) {
  var answer = [];
  let number = [];

  let mok = Math.floor(s / n);
  if (mok === 0) {
    return [-1];
  }
  let rest = s % n;

  for (let i = 0; i < n; i++) {
    if (rest > 0) {
      answer.push(mok + 1);
      rest -= 1;
    } else {
      answer.push(mok);
    }
  }

  answer.sort((a, b) => a - b);

  return answer;
}
