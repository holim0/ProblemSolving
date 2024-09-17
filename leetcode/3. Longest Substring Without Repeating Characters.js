/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  if (s === "") return 0;
  let answer = 1;
  let check = {};

  let curLang = 0;

  for (let i = 0; i < s.length; i++) {
    let cur = s[i];
    if (check[cur] === undefined) {
      check[cur] = i;
      curLang += 1;
    } else {
      answer = Math.max(answer, curLang);
      curLang = i - check[cur];
      answer = Math.max(answer, curLang);
      Object.keys(check).forEach((key) => {
        if (check[key] < check[cur]) {
          check[key] = undefined;
        }
      });
      check[cur] = i;
    }
  }
  answer = Math.max(answer, curLang);
  return answer;
};
