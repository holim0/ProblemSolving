class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = [i+1 for i in range(0, len(s))]
        
        map = {}

        for d in dictionary:
            map[d] = True


        for i in range(len(s)):
            for j in range(i+1):
                if j==i:
                    left = s[:i+1]
                    if left in dictionary:
                        dp[i] = 0
                    else:
                        dp[i] = min(dp[i], dp[i-1] + 1)
                else:
                   right = s[j+1:i+1]
                   if map.get(right, False) == True:
                        dp[i] = min(dp[i], dp[j])
                   else:
                        dp[i] = min(dp[i], dp[j] + len(right))
        
        return dp[len(s)-1]

