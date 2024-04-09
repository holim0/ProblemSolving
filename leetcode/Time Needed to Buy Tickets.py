from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque([])

        time = 0 

        for i in range(len(tickets)):
            q.append((tickets[i], i))

        while q:
            buyCnt, curIdx = q.popleft()

            if buyCnt == 0: continue
            time+=1
            if buyCnt-1 == 0 and curIdx == k: break
            q.append((buyCnt-1, curIdx))


        return time