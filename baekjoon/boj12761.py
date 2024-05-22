from collections import deque

a, b, n, m = map(int, input().split())
MAX = 100000
visited = [False for _ in range(MAX+1)]

visited[n] = True

q = deque([])

q.append((n, 0))

while q:
    cur, cnt = q.popleft()
    
    if cur==m:
        print(cnt)
        break

    for value in [1, -1, a, b, -a, -b]:
        nxt = cur + value

        if 0<=nxt<=MAX and not visited[nxt]:
            q.append((nxt, cnt+1))
            visited[nxt] = True

    nxt = cur * a
    if 0<=nxt<=MAX and not visited[nxt]:
        q.append((nxt, cnt+1))
        visited[nxt] = True
    
    nxt = cur * b
    if 0<=nxt<=MAX and not visited[nxt]:
        q.append((nxt, cnt+1))
        visited[nxt] = True
    