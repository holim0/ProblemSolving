function solution(players, m, k) {
  let answer = 0;
  const q = [];
  let plusCnt = 0;

  for (let i = 0; i < 24; i++) {
    const [s, e] = [i, i + 1];
    const user = players[i];

    while (q.length && q[0][0] < e) {
      const [curE, cnt] = q.shift();

      plusCnt -= cnt;
    }

    if (user < m) continue;
    const needCnt = Math.floor(user / m) - plusCnt;

    if (needCnt > 0) {
      plusCnt += needCnt;

      q.push([s + k, needCnt]);

      answer += needCnt;
    }
  }
  return answer;
}
