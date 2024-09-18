
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s)==1: return 1
        answer = 1
        max_frequency = 0
        l = 0
        cnt = {}

        for r in range(len(s)):
            cur = s[r]
            cnt[cur] = cnt.get(s[r], 0) +1
            
            while r-l+1-max(cnt.values()) > k:
                cnt[s[l]]-=1
                l+=1

            
            answer = max(answer, r-l+1)
            


        return answer