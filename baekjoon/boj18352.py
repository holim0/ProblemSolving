from collections import deque

n, m, k, x = map(int, input().split())

answer = []

q = deque([])

g = {}

visited = [False for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())

    if a not in g:
        g[a] = [b]
    else:
        g[a].append(b)

visited[x] = True

q.append((x, 0))

while q: 
    cur, dist = q.popleft()

    if dist == k:
        answer.append(cur)

    if cur not in g: continue

    
    for nxt in g[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            q.append((nxt, dist+1))



if len(answer) == 0:
    print(-1)
else:
    answer = sorted(answer)
    for a in answer:
        print(a)