/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
var canCompleteCircuit = function (gas, cost) {
  let gasSum = 0;
  let costSum = 0;
  gas.forEach((g) => {
    gasSum += g;
  });
  cost.forEach((c) => {
    costSum += c;
  });
  if (costSum > gasSum) {
    return -1;
  }

  const gasWithCost = [];

  for (let i = 0; i < gas.length; i++) {
    gasWithCost.push([gas[i], cost[i], i]);
  }

  gasWithCost.sort((a, b) => a[1] - b[1] || b[0] - a[0]);
  let totalSize = gasWithCost.length;
  let cnt = new Array(totalSize).fill(0);

  const getSol = (curIdx, curGas) => {
    if (cnt[curIdx] === 2) {
      return true;
    }

    let needCost = cost[curIdx];
    let filledGas = curGas + gas[curIdx];
    if (needCost <= filledGas) {
      let nextIdx = (curIdx + 1) % totalSize;
      cnt[nextIdx] += 1;
      if (getSol(nextIdx, filledGas - needCost)) {
        return true;
      }
      cnt[nextIdx] -= 1;
    }

    return false;
  };

  for (let i = 0; i < gasWithCost.length; i++) {
    let [g, c, idx] = gasWithCost[i];
    cnt[idx] += 1;
    if (getSol(idx, 0)) {
      return idx;
    }
    cnt[idx] -= 1;
  }
};

// 그리디 형식으로 다시 풀어보기 필요
