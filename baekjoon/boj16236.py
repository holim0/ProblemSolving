from collections import deque

n = int(input())

link = []

parent = [-1] * (n+1)
check = [False] * (n+1)
parent[1] = 0
check[1] = True
g = {}

for _ in range(n-1):
    a, b = map(int, input().split())
    g[a] = g.get(a, [])
    g[b] = g.get(b, [])
    g[a].append(b)
    g[b].append(a)

q = deque([])
q.append(1)

while q:
    cur = q.popleft()

    if cur not in g: continue
    for child in g[cur]:
        if not check[child]:
            parent[child] = cur
            check[child] = True
            q.append(child)

for i in range(2, n+1):
    print(parent[i])