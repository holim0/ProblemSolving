class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        t1Len = len(text1)
        t2Len = len(text2)
        text1 = " " + text1
        text2 = " " + text2
        dp = [[0 for _ in range(t2Len+1)] for _ in range(t1Len+1)]


        for i in range(1, t1Len+1):
            for j in range(1, t2Len+1):
                if text1[i] == text2[j] :
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        
        return dp[t1Len][t2Len]