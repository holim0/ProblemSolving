let info = [];
let emojSize = 0;
let baseDiscount = [10, 20, 30, 40];
let emoj = [];
let userList = [];

function getInfo(curDis) {
  let userCnt = 0;
  let sell = 0;

  userList.forEach((u) => {
    let [targetDis, maxCost] = u;
    let curCost = 0;
    for (let i = 0; i < emojSize; i++) {
      let [dis, cost] = [curDis[i], emoj[i]];
      if (dis >= targetDis) {
        curCost += (cost * (100 - dis)) / 100;
      }
    }

    if (curCost >= maxCost) {
      userCnt += 1;
    } else {
      sell += curCost;
    }
  });
  info.push([userCnt, sell]);
}

function getJohab(curDis) {
  if (curDis.length === emojSize) {
    getInfo(curDis);
    return;
  }

  baseDiscount.forEach((dis) => {
    curDis.push(dis);
    getJohab(curDis);
    curDis.pop();
  });
}

function solution(users, emoticons) {
  let answer = [];

  userList = [...users];
  emojSize = emoticons.length;
  emoj = [...emoticons];

  getJohab([]);

  info.sort((a, b) => b[0] - a[0] || b[1] - a[1]);
  answer = info[0];
  return answer;
}
