/**
 * @param {number[][]} edges
 * @return {number[]}
 */
var findRedundantConnection = function (edges) {
  const answer = [];
  const size = edges.length;

  const p = new Array(size + 1).fill(0).map((_, idx) => idx);

  const find = (x) => {
    if (x === p[x]) return x;
    return find(p[x]);
  };

  const merge = (a, b) => {
    a = find(a);
    b = find(b);
    if (a > b) {
      p[a] = b;
    } else {
      p[b] = a;
    }
  };

  for (let e of edges) {
    const [a, b] = e;

    if (find(a) !== find(b)) {
      merge(a, b);
    } else {
      answer.push([a, b]);
    }
  }

  return answer[answer.length - 1];
};
