/**
 * @param {number[]} nums
 * @param {number} limit
 * @return {number[]}
 */
var lexicographicallySmallestArray = function (nums, limit) {
  const n = nums.length;
  const indices = [];

  // Create an array of indices
  for (let i = 0; i < n; i++) {
    indices.push([nums[i], i]);
  }

  // Sort indices based on the values in nums
  indices.sort((a, b) => a[0] - b[0]);

  const result = new Array(n);
  let i = 0;

  while (i < n) {
    let j = i + 1;

    // Find the range of indices that can be swapped with each other
    while (j < n && indices[j][0] - indices[j - 1][0] <= limit) {
      j++;
    }

    // Extract the current group of indices
    const currentGroup = indices.slice(i, j);

    // Sort indices (positions) and values within the group
    const sortedPositions = currentGroup
      .map((cur) => cur[1])
      .sort((a, b) => a - b);
    const sortedValues = currentGroup
      .map((cur) => cur[0])
      .sort((a, b) => a - b);

    // Place the sorted values in the result array
    for (let k = 0; k < currentGroup.length; k++) {
      result[sortedPositions[k]] = sortedValues[k];
    }

    // Move to the next group
    i = j;
  }

  return result;
};
