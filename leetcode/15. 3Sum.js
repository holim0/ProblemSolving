/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  nums.sort((a, b) => a - b);
  const answer = [];

  const moveUp = (curIdx) => {
    let newIdx = curIdx;
    while (newIdx < nums.length && nums[newIdx] === nums[newIdx + 1]) {
      newIdx += 1;
    }
    return newIdx + 1;
  };

  const moveDown = (curIdx) => {
    let newIdx = curIdx;
    while (newIdx >= 0 && nums[newIdx] === nums[newIdx - 1]) {
      newIdx -= 1;
    }
    return newIdx - 1;
  };

  for (let i = 0; i < nums.length - 2; i++) {
    if (nums[i - 1] === nums[i]) continue;
    const base = nums[i];
    const targetSum = nums[i] * -1;

    let [l, r] = [i + 1, nums.length - 1];

    while (l < r && r >= 0 && l < nums.length) {
      let curSum = nums[l] + nums[r];

      if (curSum < targetSum) {
        l = moveUp(l);
      } else if (curSum > targetSum) {
        r = moveDown(r);
      } else {
        answer.push([nums[i], nums[l], nums[r]]);
        l = moveUp(l);
        r = moveDown(r);
      }
    }
  }
  return answer;
};
