class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size == 1: return s
        if size == 2 and s[0] == s[1]: return s
        max_len = 1
        ai, aj = 0, 0

        dp = [[False for _ in range(size)] for _ in range(size)]

        for i in range(size):
            for j in range(size):
                if i==j: dp[i][j] = True


            
        for k in range(1, size):
            for i in range(size-k):
                if s[i] == s[i+k]:
                    if k == 1: 
                        dp[i][i+k] = True
                        if k+1 > max_len:
                            max_len = k+1
                            ai, aj = i, i+k
                        continue
                    if dp[i+1][i+k-1] == True:
                        dp[i][i+k] = True
                        if k+1 > max_len:
                            max_len = k+1
                            ai, aj = i, i+k
        
        return s[ai:aj+1]
