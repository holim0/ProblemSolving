import sys
import heapq as hp
input = sys.stdin.readline

n, m, x = map(int, input().split())

g = {}

for _ in range(m):
    a, b, c = map(int, input().split())
    if a not in g:
        g[a] = [(c, b)]
    else:
        g[a].append((c, b))

INF = 1e10
dist = [INF for _ in range(n+1)]
dist[x] = 0 

answer = 0


goComeDist = 0
q = []
dist = [INF for _ in range(n+1)]
dist[x] = 0
hp.heappush(q, (0, x))

goComeDist = [0 for _ in range(n+1)]

while q:
    curdist, cur = hp.heappop(q)

    if dist[cur]<curdist: continue

    if cur not in g: continue

    for nxtDist,nxt in g[cur]:
        if dist[nxt]>curdist+nxtDist:
            dist[nxt] = curdist+nxtDist
            hp.heappush(q, (dist[nxt], nxt))

for i in range(1, n+1):
    goComeDist[i]+=dist[i]

for i in range(1, n+1):
    dist = [INF for _ in range(n+1)]
    dist[i] = 0

    hp.heappush(q, (0, i))

    while q:
        curdist, cur = hp.heappop(q)

        if dist[cur]<curdist: continue

        if cur not in g: continue

        for nxtDist,nxt in g[cur]:
            if dist[nxt]>curdist+nxtDist:
                dist[nxt] = curdist+nxtDist
                hp.heappush(q, (dist[nxt], nxt))
    
    goComeDist[i]+=dist[x]


print(max(goComeDist))