/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function (height) {
  let left_max = height[0];
  let right_max = height[height.length - 1];

  let l = 0;
  let r = height.length - 1;
  let answer = 0;
  while (l <= r) {
    left_max = Math.max(left_max, height[l]);
    right_max = Math.max(right_max, height[r]);

    if (left_max > right_max) {
      answer += right_max - height[r];
      r -= 1;
    } else {
      answer += left_max - height[l];
      l += 1;
    }
  }

  return answer;
};
