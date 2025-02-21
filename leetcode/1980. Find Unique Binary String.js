/**
 * @param {string[]} nums
 * @return {string}
 */
var findDifferentBinaryString = function (nums) {
  const n = nums.length;
  const binarySet = new Set(nums);
  let result = null;

  const dfs = (current) => {
    if (current.length === n) {
      if (!binarySet.has(current)) {
        result = current;
        return true; // 찾으면 바로 종료
      }
      return false;
    }

    return dfs(current + "0") || dfs(current + "1");
  };

  dfs("");
  return result;
};
