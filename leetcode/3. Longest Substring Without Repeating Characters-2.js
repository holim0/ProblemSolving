/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  if (s === "") return 0;
  let tmp = [];
  let check = {};
  let answer = 1;
  for (let i = 0; i < s.length; i++) {
    let cur = s[i];
    if (!check[cur]) {
      check[cur] = true;
      tmp.push(cur);
    } else {
      answer = Math.max(answer, tmp.length);
      while (true) {
        if (check[cur] === false) break;
        let front = tmp.shift();
        check[front] = false;
      }
      tmp.push(cur);
      check[cur] = true;
    }
  }
  answer = Math.max(answer, tmp.length);
  return answer;
};
