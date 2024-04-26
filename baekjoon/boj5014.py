from collections import deque
import sys

totalSize, cur, starlink, u, d  = map(int, input().split())

q = deque([])

visited = [False for _ in range(totalSize+1)]

visited[cur] = True

q.append((cur, 0))

while q: 
    cur, cnt = q.popleft()

    if cur == starlink:
        print(cnt)
        sys.exit()


    if cur+u<=totalSize and not visited[cur+u]:
        visited[cur+u] = True
        q.append((cur+u, cnt+1))


    if cur-d>=1 and not visited[cur-d]:
        visited[cur-d] = True
        q.append((cur-d, cnt+1))


print("use the stairs")