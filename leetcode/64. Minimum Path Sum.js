/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function (grid) {
  const m = grid[0].length;
  const n = grid.length;

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (i == 0) {
        if (j == 0) continue;
        grid[i][j] += grid[i][j - 1];
      } else {
        if (j == 0) {
          grid[i][j] += grid[i - 1][j];
        } else {
          grid[i][j] += Math.min(grid[i - 1][j], grid[i][j - 1]);
        }
      }
    }
  }

  return grid[n - 1][m - 1];
};
