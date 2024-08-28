/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function (nums) {
  if (nums.length === 1) return true;
  if (nums[0] === 0) return false;
  const check = new Array(nums.length).fill(false);
  check[0] = true;
  for (let i = 0; i < nums.length; i++) {
    let dist = nums[i];
    if (dist === 0 || !check[i]) continue;
    for (let j = i + 1; j < nums.length; j++) {
      if (i + dist >= j) {
        check[j] = true;
      } else {
        break;
      }
    }
  }

  return check[nums.length - 1];
};
