/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */

var combinationSum2 = function (candidates, target) {
  const answer = [];
  const check = {};

  candidates.forEach((candi) => {
    if (!check[candi]) {
      check[candi] = 1;
    } else {
      check[candi] += 1;
    }
  });
  candidates.sort((a, b) => a - b);
  function getSol(idx, curSum, curArray) {
    if (curSum === target) {
      answer.push(curArray);

      return;
    }

    for (let i = idx; i < candidates.length; i++) {
      const cur = candidates[i];
      if (i != idx && candidates[i] === candidates[i - 1]) continue;
      if (curSum + cur <= target && check[cur] > 0) {
        check[cur] -= 1;
        getSol(i + 1, curSum + cur, [...curArray, cur]);
        check[cur] += 1;
      }
    }
  }
  getSol(0, 0, []);
  return answer;
};
