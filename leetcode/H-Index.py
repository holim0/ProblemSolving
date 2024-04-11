class Solution:
    def hIndex(self, citations: List[int]) -> int:
        c = sorted(citations)
        answer = 0
        
        s, e = 0, len(c)

        while s<=e:

            mid = (s+e)//2

            cnt = 0

            for value in c:
                if mid<=value:
                    cnt+=1
            
            if mid<=cnt:
                s = mid+1
            else:
                e = mid-1
        
        return e



