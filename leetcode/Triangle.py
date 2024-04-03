class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        h = len(triangle)
        max_w = len(triangle[-1])
        if h == 1: return triangle[0][0]

        INF = 1e10
        
        sum_dp = [[INF for _ in range(max_w)] for _ in range(h)]

        sum_dp[0][0] = triangle[0][0]

        for i in range(1, h):
            for j in range(len(triangle[i])):
                if j == 0:
                    sum_dp[i][j] = min(sum_dp[i][j], sum_dp[i-1][0] + triangle[i][j])
                elif j == len(triangle[i])-1:
                    sum_dp[i][j] = min(sum_dp[i][j], sum_dp[i-1][j-1] + triangle[i][j])

                else:
                    sum_dp[i][j] = min(sum_dp[i][j], sum_dp[i-1][j] + triangle[i][j])
                    sum_dp[i][j] = min(sum_dp[i][j], sum_dp[i-1][j-1] + triangle[i][j])


        return min(sum_dp[-1])


