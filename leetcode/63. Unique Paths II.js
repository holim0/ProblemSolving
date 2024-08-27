/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */
var uniquePathsWithObstacles = function (obstacleGrid) {
  if (obstacleGrid[0][0] === 1) return 0;
  const m = obstacleGrid[0].length;
  const n = obstacleGrid.length;

  const dp = [];
  for (let i = 0; i < n; i++) {
    dp.push(new Array(m).fill(0));
  }

  let dir = [
    [0, 1],
    [1, 0],
  ];
  const getSol = (cx, cy) => {
    if (cx === n - 1 && cy === m - 1 && obstacleGrid[cx][cy] === 0) return 1;
    if (dp[cx][cy] !== 0) return dp[cx][cy];
    for (let i = 0; i < 2; i++) {
      const [nx, ny] = [cx + dir[i][0], cy + dir[i][1]];
      if (
        nx >= 0 &&
        nx < n &&
        ny >= 0 &&
        ny < m &&
        obstacleGrid[nx][ny] === 0
      ) {
        dp[cx][cy] += getSol(nx, ny);
      }
    }

    return dp[cx][cy];
  };

  answer = getSol(0, 0);

  return answer;
};
