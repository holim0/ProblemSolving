class Solution:
    def countSubstrings(self, s: str) -> int:
        l = len(s)
        if l==1: return 1
        if l==2:
            if s[0] == s[1]:
                return 3
            else:
                return 2
        answer = 0
        dp = [[False for _ in range(l)] for _ in range(l)]

        for i in range(l):
            answer+=1
            dp[i][i] = True
        for i in range(l-1):
            if s[i]== s[i+1]:
                answer+=1
                dp[i][i+1] = True

        for size in range(3, l+1):
            for i in range(l-size+1):
                left = i
                right = i+size-1
                if s[left] == s[right] and dp[left+1][right-1]:
                    dp[left][right] = True
                    answer+=1
        
        return answer        
        

        