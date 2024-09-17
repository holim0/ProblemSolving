/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function (nums, k) {
  const answer = [];
  const size = nums.length;

  let rotateCnt = k % size;
  const tmp = [];
  const rest = [];
  while (rotateCnt) {
    const last = nums.pop();
    tmp.push(last);
    rotateCnt -= 1;
  }

  while (nums.length) {
    rest.push(nums.pop());
  }
  tmp.reverse();
  rest.reverse();
  nums.push(...tmp);
  nums.push(...rest);
};
