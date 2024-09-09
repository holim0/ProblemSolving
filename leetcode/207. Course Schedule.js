/**
 * @param {number} numCourses
 * @param {number[][]} pre
 * @return {boolean}
 */
var canFinish = function (numCourses, pre) {
  const g = {};
  const degree = new Array(numCourses).fill(0);
  let cnt = 0;
  pre.forEach((p) => {
    let [a, b] = p;
    degree[a] += 1;
    if (!g[b]) {
      g[b] = [a];
    } else {
      g[b].push(a);
    }
  });

  const start = [];
  for (let i = 0; i < numCourses; i++) {
    if (degree[i] === 0) {
      start.push(i);
    }
  }

  while (start.length) {
    let cur = start.shift();
    cnt += 1;
    if (!g[cur]) {
      continue;
    }
    g[cur].forEach((nxt) => {
      degree[nxt] -= 1;
      if (degree[nxt] === 0) {
        start.push(nxt);
      }
    });
  }
  return cnt === numCourses;
};
