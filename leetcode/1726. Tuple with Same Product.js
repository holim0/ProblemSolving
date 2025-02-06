/**
 * @param {number[]} nums
 * @return {number}
 */
var tupleSameProduct = function (nums) {
  nums.sort((a, b) => a - b);
  let answer = 0;
  const productMap = {};
  const size = nums.length;

  for (let i = 0; i < size; i++) {
    for (let j = i + 1; j < size; j++) {
      const [a, b] = [nums[i], nums[j]];

      const curProductValue = a * b;

      if (!productMap[curProductValue]) {
        productMap[curProductValue] = [];
      }
      productMap[curProductValue].push([a, b]);
    }
  }
  const keys = Object.keys(productMap);
  for (let i = 0; i < keys.length; i++) {
    const keyValue = keys[i];
    const value = productMap[keyValue];
    const valueSize = value.length;
    if (valueSize <= 1) continue;
    answer += valueSize * (valueSize - 1) * 4;
  }

  return answer;
};
