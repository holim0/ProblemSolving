class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        h = len(obstacleGrid)
        w = len(obstacleGrid[0])

        dp = [[0 for _ in range(w)] for _ in range(h)]

        if obstacleGrid[0][0] != 1:
            dp[0][0] = 1

        for i in range(h):
            for j in range(w):
                if (i==0 and j == 0) or obstacleGrid[i][j] ==1: continue

                ux, uy = i-1, j
                rx, ry = i, j-1

                if 0<=ux<h and 0<=uy<w and obstacleGrid[ux][uy] ==0:
                    dp[i][j] += dp[ux][uy]

                if 0<=rx<h and 0<=ry<w and obstacleGrid[rx][ry] ==0:
                    dp[i][j] += dp[rx][ry]




        return dp[h-1][w-1]