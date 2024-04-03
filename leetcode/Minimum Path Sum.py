class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])

        if h ==1: return sum(grid[0])

        INF = 1e10

        dp = [[INF for _ in range(w)] for _ in range(h)]

        dp[0][0] = grid[0][0]

        for i in range(h):
            for j in range(w):
                if i ==0 and j == 0 : continue

                if i-1>=0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + grid[i][j])
                
                if j-1>=0:
                    dp[i][j] = min(dp[i][j], dp[i][j-1] + grid[i][j])

        return dp[h-1][w-1]        

        