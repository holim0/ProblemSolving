/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function (nums) {
  if (nums.length !== 1) {
    let i = 0;
    let j = 1;

    while (i < j && j < nums.length) {
      let v1 = nums[i];
      let v2 = nums[j];
      if (v1 === 0 && v2 === 0) {
        j += 1;
        continue;
      }
      if (v1 === 0 && v2 !== 0) {
        nums[i] = v2;
        nums[j] = 0;
        i += 1;
        j += 1;
        continue;
      }
      if (v1 !== 0) {
        i += 1;
        j += 1;
        continue;
      }
    }
  }
};
