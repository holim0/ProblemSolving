import heapq as hp

n = int(input())
m = int(input())

INF = 1e10

dist = [INF] * (n+1)

g = {}

for _ in range(m):
    f, t, c = map(int, input().split())
    
    if f not in g:
        g[f] = [(c, t)]
    else:
        g[f].append((c, t))

start, to = map(int, input().split())

dist[start] = 0

q = []

hp.heappush(q, (0, start))

while q:
    curCost, cur = hp.heappop(q)

    if dist[cur]< curCost: continue
    if cur not in g: continue
    
    for nxtCost, nxt in g[cur]:
        nxtDist = curCost + nxtCost

        if nxtDist< dist[nxt]:
            dist[nxt]= nxtDist
            hp.heappush(q, (nxtDist, nxt))

print(dist[to])