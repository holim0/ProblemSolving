/**
 * @param {string[]} words
 * @param {number[][]} queries
 * @return {number[]}
 */
var vowelStrings = function (words, queries) {
  const wlen = words.length;
  const answer = [];
  const vowel = {
    a: true,
    e: true,
    i: true,
    o: true,
    u: true,
  };
  const cnt = new Array(wlen + 1).fill(0);

  for (let [i, w] of words.entries()) {
    let start = w[0],
      end = w[w.length - 1];

    if (vowel[start] && vowel[end]) {
      cnt[i + 1] += 1;
    }
  }
  const acc = [0];
  for (let i = 1; i <= wlen; i++) {
    acc.push(acc[acc.length - 1] + cnt[i]);
  }

  for (let q of queries) {
    let [i, j] = q;
    let curCnt = acc[j + 1] - acc[i];
    answer.push(curCnt);
  }

  return answer;
};
