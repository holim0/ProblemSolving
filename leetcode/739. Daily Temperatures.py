class Solution:
    def dailyTemperatures(self, temper: List[int]) -> List[int]:
        s = []
        answer = [0 for _ in range(len(temper))]
        for i in range(len(temper)):
            if len(s) == 0:
                s.append((i, temper[i]))
                continue

            while s and s[-1][1]<temper[i]:
                topIdx, topTemper = s.pop()
                answer[topIdx] = i-topIdx
            
            s.append((i, temper[i]))
        
        return answer