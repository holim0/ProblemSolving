from collections import deque
n, m = map(int, input().split())

degree = [0 for _ in range(n+1)]

g = {}

for _ in range(m):
    a, b = map(int, input().split())
    if a not in g:
        g[a] = [b]
    else:
        g[a].append(b)
    degree[b]+=1

first = []

for i in range(1, n+1):
    if degree[i] == 0:
        first.append(i)

answer = []
for value in first:
   
    q = deque([])
    q.append(value)
    answer.append(value)
    while q:
        cur = q.popleft()

        if cur not in g: continue

        for nxt in g[cur]:
            degree[nxt]-=1
            if degree[nxt] ==0:
                answer.append(nxt)
                q.append(nxt)

print(" ".join(str(a) for a in answer))


