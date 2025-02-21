/**
 * @param {string[]} nums
 * @return {string}
 */
var findDifferentBinaryString = function (nums) {
  const n = nums.length;
  const mapp = {};

  for (let value of nums) {
    mapp[value] = true;
  }
  const answer = [];
  const dfs = (cur) => {
    if (cur.length === n) {
      if (!mapp[cur]) {
        answer.push(cur);
      }
      return;
    }

    dfs(cur + "0");
    dfs(cur + "1");
  };

  dfs("");

  return answer[0];
};
