from collections import deque
import sys

n = int(input())

mapp = list(map(int, input().split()))

visit = [False for _ in range(n)]

q = deque([(0, 0)])

visit[0] = True

while q:
    cur, cnt = q.popleft()

    if cur == n-1:
        print(cnt)
        sys.exit(0)
    
    for i in range(mapp[cur]+1):
        nxt = cur+i

        if nxt<n and not visit[nxt]:
            visit[nxt] = True
            q.append((nxt, cnt+1))

print(-1)