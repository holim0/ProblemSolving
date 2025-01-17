/**
 * @param {number[]} A
 * @param {number[]} B
 * @return {number[]}
 */
var findThePrefixCommonArray = function (A, B) {
  const common_cnt = [];
  const size = A.length;
  const checkSet = new Set();
  if (A[0] === B[0]) {
    checkSet.add(A[0]);
    common_cnt.push(1);
  } else {
    checkSet.add(A[0]);
    checkSet.add(B[0]);
    common_cnt.push(0);
  }

  for (let i = 1; i < size; i++) {
    const lastValue = common_cnt[common_cnt.length - 1];
    if (A[i] === B[i]) {
      common_cnt.push(lastValue + 1);
    } else {
      let cnt = 0;
      if (checkSet.has(A[i])) {
        cnt += 1;
      }

      if (checkSet.has(B[i])) {
        cnt += 1;
      }
      common_cnt.push(lastValue + cnt);
    }

    checkSet.add(A[i]);
    checkSet.add(B[i]);
  }

  return common_cnt;
};
