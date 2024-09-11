/**
 * @param {number[][]} grid1
 * @param {number[][]} grid2
 * @return {number}
 */
var countSubIslands = function (grid1, grid2) {
  const check = [];
  const m = grid1[0].length;
  const n = grid1.length;
  let answer = 0;
  for (let i = 0; i < n; i++) {
    check.push(new Array(m).fill(0));
  }
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (grid1[i][j] === 1) {
        check[i][j] = 1;
      }
    }
  }

  let q = [];
  const dir = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1],
  ];
  const grid2Check = [];
  for (let i = 0; i < n; i++) {
    grid2Check.push(new Array(m).fill(false));
  }
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (grid2[i][j] === 0 || grid2Check[i][j]) continue;

      q = [[i, j]];
      check[i][j] += 1;
      let isSubIsLand = true;
      if (check[i][j] < 2) {
        isSubIsLand = false;
      }

      grid2Check[i][j] = true;
      while (q.length) {
        let [cx, cy] = q.shift();
        for (let k = 0; k < 4; k++) {
          let [nx, ny] = [cx + dir[k][0], cy + dir[k][1]];

          if (
            nx >= 0 &&
            nx < n &&
            ny >= 0 &&
            ny < m &&
            grid2[nx][ny] === 1 &&
            !grid2Check[nx][ny]
          ) {
            check[nx][ny] += 1;
            q.push([nx, ny]);
            grid2Check[nx][ny] = true;
            if (check[nx][ny] < 2) {
              isSubIsLand = false;
            }
          }
        }
      }
      if (isSubIsLand) {
        answer += 1;
      }
    }
  }
  return answer;
};
