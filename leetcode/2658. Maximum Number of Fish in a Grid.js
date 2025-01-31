/**
 * @param {number[][]} grid
 * @return {number}
 */
var findMaxFish = function (grid) {
  const dir = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1],
  ];
  const n = grid.length;
  const m = grid[0].length;

  let answer = 0;
  let q = [];

  const isInRange = (x, y) => {
    return x >= 0 && x < n && y >= 0 && y < m;
  };

  let check = new Array(n).fill(0).map(() => new Array(m).fill(false));

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (grid[i][j] === 0) continue;

      let curFishCnt = 0;
      check = new Array(n).fill(0).map(() => new Array(m).fill(false));
      q.push([i, j]);
      check[i][j] = true;
      while (q.length) {
        const [x, y] = q.shift();
        curFishCnt += grid[x][y];

        for (let k = 0; k < 4; k++) {
          const [nx, ny] = [x + dir[k][0], y + dir[k][1]];

          if (isInRange(nx, ny) && !check[nx][ny] && grid[nx][ny] !== 0) {
            q.push([nx, ny]);
            check[nx][ny] = true;
          }
        }
      }

      answer = Math.max(answer, curFishCnt);
    }
  }
  return answer;
};
