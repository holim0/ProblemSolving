/**
 * @param {string} s
 * @param {number} repeatLimit
 * @return {string}
 */
var repeatLimitedString = function (s, repeatLimit) {
  let answer = [];
  const check = {};
  const remainCnt = {};
  const char = [];
  for (let ss of s) {
    if (!check[ss]) {
      check[ss] = true;
      char.push(ss);
    }
    remainCnt[ss] = (remainCnt[ss] ?? 0) + 1;
  }

  char.sort((a, b) => b.localeCompare(a));
  let curSequenceCnt = 0;
  let p = 0;

  while (true) {
    while (p < char.length && remainCnt[char[p]] === 0) {
      p += 1;
    }

    if (p >= char.length) break;

    if (char[p] !== answer[answer.length - 1]) {
      curSequenceCnt = 0;
    }

    if (curSequenceCnt <= repeatLimit - 1) {
      answer.push(char[p]);
      remainCnt[char[p]] -= 1;
      curSequenceCnt += 1;
      p = 0;
    } else {
      p += 1;
      curSequenceCnt = 0;
    }
  }
  return answer.join("");
};
