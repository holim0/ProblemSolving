/**
 * @param {number[][]} grid
 * @return {number}
 */

var orangesRotting = function (grid) {
  const [m, n] = [grid[0].length, grid.length];
  const q = [];
  const orange = [];
  const check = [];
  for (let i = 0; i < n; i++) {
    check.push(new Array(m).fill(false));
  }

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (grid[i][j] !== 0) {
        orange.push([i, j]);
        if (grid[i][j] === 2) {
          q.push([i, j, 0]);
          check[i][j] = true;
        }
      }
    }
  }

  const checkAllRotten = () => {
    for (let i = 0; i < orange.length; i++) {
      let [x, y] = orange[i];
      if (!check[x][y]) return false;
    }
    return true;
  };
  const dir = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
  ];

  while (q.length) {
    let [x, y, time] = q.shift();

    for (let i = 0; i < 4; i++) {
      let [nx, ny] = [x + dir[i][0], y + dir[i][1]];

      if (
        nx >= 0 &&
        nx < n &&
        ny >= 0 &&
        ny < m &&
        grid[nx][ny] === 1 &&
        !check[nx][ny]
      ) {
        check[nx][ny] = true;
        if (checkAllRotten()) {
          return time + 1;
        }
        q.push([nx, ny, time + 1]);
      }
    }
  }

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (grid[i][j] === 1) {
        return -1;
      }
    }
  }

  return 0;
};
