import heapq

n, m = map(int, input().split())

g = {}

degree = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    degree[b]+=1

    if a not in g:
        g[a] = [b]
    else:
        g[a].append(b)

answer = []

q =[]

for i in range(1, n+1):
    if degree[i] ==0:
        heapq.heappush(q, i)


while q:
    cur = heapq.heappop(q)

    answer.append(cur)

    if cur not in g: continue

    for nxt in g[cur]:
        degree[nxt]-=1
        if degree[nxt] ==0:
            heapq.heappush(q, nxt)

print(" ".join(str(a) for a in answer))








