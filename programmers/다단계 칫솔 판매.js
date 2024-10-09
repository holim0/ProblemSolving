function solution(enroll, referral, seller, amount) {
  var answer = [];
  const enrollSize = enroll.length;
  let g = {};
  let earn = {};
  for (let i = 0; i < enrollSize; i++) {
    earn[enroll[i]] = 0;
  }

  for (let i = 0; i < enrollSize; i++) {
    let curName = enroll[i];
    let curReferral = referral[i];

    if (curReferral === "-") {
      g[curName] = null;
    } else {
      g[curName] = curReferral;
    }
  }

  const addEarn = (cur, curEarn) => {
    if (cur === null) {
      return;
    }

    let fee = curEarn * 0.1;

    if (fee < 1) {
      earn[cur] += curEarn;
      return;
    } else {
      fee = Math.floor(fee);

      earn[cur] += curEarn - fee;

      addEarn(g[cur], fee);
    }
  };

  for (let i = 0; i < seller.length; i++) {
    let curSeller = seller[i];
    let curEarn = amount[i] * 100;

    addEarn(curSeller, curEarn);
  }

  for (let i = 0; i < enroll.length; i++) {
    let name = enroll[i];
    answer.push(earn[name]);
  }

  return answer;
}
