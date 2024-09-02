/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  let map = {};
  const answer = [];

  strs.forEach((s) => {
    let sorted_s = s.split("").sort().join("");
    if (!map[sorted_s]) {
      map[sorted_s] = [s];
    } else {
      map[sorted_s].push(s);
    }
  });
  Object.keys(map).forEach((key) => {
    answer.push(map[key]);
  });
  return answer;
};
