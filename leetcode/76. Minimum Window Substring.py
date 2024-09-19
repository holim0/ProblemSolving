class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        tCnt = {}
        
        answer = ""
        minLen = 1e10
        for tt in t:
            tCnt[tt] = tCnt.get(tt, 0)+1

        p1 = 0
        def checkUnderZero():
            for key in tCnt:
                if tCnt[key]>0: return False
            return True


        for p2 in range(len(s)):
            cur = s[p2]
            
            if cur in tCnt:
                tCnt[cur]-=1
            
            while p1<=p2:
                leftValue = s[p1]
                if leftValue in tCnt:
                    tCnt[leftValue]+=1
                    if tCnt[leftValue]>0:
                        tCnt[leftValue]-=1
                        break
                p1+=1


            if checkUnderZero():
                if minLen> p2-p1+1:
                    answer = s[p1:p2+1]
                    minLen = p2-p1+1
                
    
        return answer

            

            
            
