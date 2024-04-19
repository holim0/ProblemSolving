from collections import deque
import sys

a, b = map(int, input().split())

visited = {}


visited[a] = True

q = deque([])
q.append((a, 0))

while q:
    cur, cnt = q.popleft()

    if cur == b:
        print(cnt+1)
        sys.exit()

    nxt = cur * 2

    if nxt <=b and nxt not in visited:
        visited[nxt] = True
        q.append((nxt, cnt+1))

    nxt = int(str(cur) + "1")

    if nxt <=b and nxt not in visited:
        visited[nxt] = True
        q.append((nxt, cnt+1))




print(-1)