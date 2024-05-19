from collections import deque
import sys

n = int(input())

a, b = map(int, input().split())

g = {}

m = int(input())

for _ in range(m):
    x, y = map(int, input().split())

    if x not in g:
        g[x] = [y]
    else:
        g[x].append(y)

    if y not in g:
        g[y] = [x]
    else:
        g[y].append(x)

visited = [False for _ in range(n+1)]

visited[a] = True

q = deque([])

q.append((a, 0))

while q:
    cur, cnt = q.popleft()

    if cur == b:
        print(cnt)
        sys.exit()
    
    if cur not in g: continue

    for nxt in g[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            q.append((nxt, cnt+1))
    

print(-1)