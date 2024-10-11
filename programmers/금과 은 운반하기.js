function solution(a, b, g, s, w, t) {
  var answer = -1;
  let listSize = g.length;
  const calGoldandSilver = (curTime) => {
    let gold = 0;
    let silver = 0;
    let total = 0;
    for (let i = 0; i < listSize; i++) {
      let maxMoveCnt = Math.floor(curTime / (2 * t[i]));
      if (curTime % (2 * t[i]) >= t[i]) maxMoveCnt += 1;

      let curGoldCnt = Math.min(g[i], maxMoveCnt * w[i]);
      let curSilverCnt = Math.min(s[i], maxMoveCnt * w[i]);
      let curTotalCnt = Math.min(g[i] + s[i], maxMoveCnt * w[i]);

      gold += curGoldCnt;
      silver += curSilverCnt;
      total += curTotalCnt;
    }

    if (gold >= a && silver >= b && total >= a + b) {
      return true;
    }
    return false;
  };

  let l = 0;
  let r = Math.pow(10, 16);
  answer = r;
  while (l <= r) {
    let mid = Math.floor((l + r) / 2);

    if (calGoldandSilver(mid)) {
      answer = Math.min(answer, mid);
      r = mid - 1;
    } else {
      l = mid + 1;
    }
  }

  return answer;
}
