/**
 * @param {string} s
 * @return {number}
 */
var maximumLength = function (s) {
  let answer = 0;
  const slen = s.length;
  let l = 0,
    r = 0;

  const countChar = (curStr) => {
    const curStrLen = curStr.length;
    let cnt = 0;
    for (let i = 0; i < slen - curStrLen + 1; i++) {
      let targetStr = s.slice(i, i + curStrLen);
      if (curStr === targetStr) {
        cnt += 1;
      }
    }

    return cnt;
  };

  while (l <= r && l < slen && r < slen) {
    if (s[l] !== s[r]) {
      l = r;
    }

    const curStr = s.slice(l, r + 1);

    const curCnt = countChar(curStr);
    if (curCnt >= 3) {
      answer = Math.max(answer, r - l + 1);
    }

    r += 1;
  }

  if (answer === 0) {
    return -1;
  } else {
    return answer;
  }
};
