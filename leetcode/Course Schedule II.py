from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        degree = [0 for _ in range(numCourses)]

        graph = {}

        for a, b in prerequisites:
            if b not in graph:
                graph[b] = [a]
            else:
                graph[b].append(a)
            degree[a] +=1
        
        q = deque([])
        order = []
        cnt = 0

        for i in range(numCourses):
            if degree[i] ==0:
                cnt+=1
                q.append(i)

        while q:
            cur = q.popleft()

            order.append(cur)
            if cur not in graph: continue
            for nxt in graph[cur]:
                degree[nxt] -=1
                if degree[nxt] ==0:
                    cnt+=1
                    q.append(nxt)


        return order if cnt == numCourses else []