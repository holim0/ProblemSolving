/**
 * @param {number[]} nums
 * @return {number}
 */
var findScore = function (nums) {
  let score = 0;
  const len = nums.length;
  const check = new Array(len).fill(false);
  const checkList = [];
  const numsWithIdx = nums.map((num, idx) => [num, idx]);
  numsWithIdx.sort((a, b) => b[0] - a[0] || b[1] - a[1]);

  while (checkList.length < len) {
    const [curMin, idx] = numsWithIdx.pop();

    if (check[idx]) {
      continue;
    }

    score += curMin;
    check[idx] = true;
    checkList.push(idx);
    if (idx - 1 >= 0 && !check[idx - 1]) {
      check[idx - 1] = true;
      checkList.push(idx - 1);
    }
    if (idx + 1 < len && !check[idx + 1]) {
      check[idx + 1] = true;
      checkList.push(idx + 1);
    }
  }

  return score;
};
