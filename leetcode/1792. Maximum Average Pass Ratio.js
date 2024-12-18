import heapq as hp
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
        size = len(classes)
        q = []
        sum =0

        def getIncreaseFactor(p, t):
            return (p+1) / (t+1) - p/t

        for c in classes:
            p, t = c
            sum+=p/t

            hp.heappush(q, (-getIncreaseFactor(p, t), p, t))

        while extraStudents:
            increaseFactor, p, t = hp.heappop(q)

            sum-=(p/t)

            p+=1
            t+=1
            sum+=(p/t)

            hp.heappush(q, (-getIncreaseFactor(p, t), p, t))

            extraStudents-=1

        

        return sum/size