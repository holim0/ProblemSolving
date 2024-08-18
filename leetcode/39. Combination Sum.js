/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */

var combinationSum = function (candidates, target) {
  const answer = [];
  const getSol = (idx, curNumber, curList) => {
    if (curNumber === target) {
      answer.push(curList);
      return;
    }

    for (let i = idx; i < candidates.length; i++) {
      const curCandi = candidates[i];
      if (curCandi + curNumber <= target) {
        getSol(i, curCandi + curNumber, curList.concat([curCandi]));
      }
    }
  };

  getSol(0, 0, []);

  return answer;
};
