/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {boolean[]}
 */
var isArraySpecial = function (nums, queries) {
  let split = [];

  let tmp = [];

  for (let i = 0; i < nums.length; i++) {
    if (tmp.length === 0) {
      tmp.push(i);
      continue;
    }

    const curValue = nums[i];
    const tmpLast = nums[tmp[tmp.length - 1]];

    if (
      (curValue % 2 === 1 && tmpLast % 2 === 0) ||
      (curValue % 2 === 0 && tmpLast % 2 === 1)
    ) {
      tmp.push(i);
    } else {
      split.push(tmp);
      tmp = [i];
    }
  }

  if (tmp.length) {
    split.push(tmp);
  }
  split = split.map((cur) => [cur[0], cur[cur.length - 1]]);
  const answer = new Array(queries.length).fill(false);

  for (let i = 0; i < queries.length; i++) {
    let [s, e] = queries[i];

    let l = 0,
      r = split.length - 1;
    let candi = [];
    while (l <= r) {
      let mid = Math.floor((l + r) / 2);

      let curStart = split[mid][0];
      let curEnd = split[mid][1];
      if (curStart <= s) {
        if (curEnd >= e) {
          answer[i] = true;
          break;
        }
        l = mid + 1;
      } else {
        r = mid - 1;
      }
    }
  }
  return answer;
};
