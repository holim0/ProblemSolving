class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1: return s
        if len(s) == 2:
            if s[0] == s[1]: return s
            else: return s[0]

        maxLeft = 0
        maxRight = 0    
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                maxLeft = i
                maxRight = i+1
                dp[i][i+1] = True
            
        for l in range(3, len(s)+1):
            for i in range(0, len(s)-l+1):
                left = i
                right = i+l-1
                
                if dp[left+1][right-1] and s[left]==s[right]:
                    dp[left][right] = True
                    if l>maxRight-maxLeft+1:
                        maxLeft = left
                        maxRight = i+l-1

        return s[maxLeft:maxRight+1]