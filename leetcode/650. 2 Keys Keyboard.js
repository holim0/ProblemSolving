/**
 * @param {number} n
 * @return {number}
 */

var minSteps = function (n) {
  let answer = Infinity;

  const getSol = (times, curLen, copiedLen) => {
    if (curLen === n) {
      answer = Math.min(answer, times);
      return;
    }

    // 복사
    if (curLen != copiedLen) {
      getSol(times + 1, curLen, curLen);
    }

    // 붙여넣기
    if (copiedLen !== 0 && curLen + copiedLen <= n) {
      getSol(times + 1, curLen + copiedLen, copiedLen);
    }
  };

  getSol(0, 1, 0);
  return answer;
};
