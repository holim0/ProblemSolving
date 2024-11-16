import heapq as hp

n, e = map(int, input().split())

g = {}

for _ in range(e):
    a, b, c  = map(int, input().split())
    
    if a not in g:
        g[a] = [(c, b)]
    else:
        g[a].append((c, b))
    
    if b not in g:
        g[b] = [(c, a)]
    else:
        g[b].append((c, a))

u, v = map(int, input().split())

INF = 1e10

def getMinDist(fromm, to):

    dist = [INF] * (n+1)

    dist[fromm] = 0

    q = []

    hp.heappush(q, (0, fromm))

    while q:
        curDist, cur = hp.heappop(q)

        if curDist> dist[cur]: continue
        if cur not in g: continue

        for nxtDist, nxt in g[cur]:
            
            if dist[nxt]> curDist + nxtDist:
                dist[nxt] = curDist + nxtDist
                hp.heappush(q, (dist[nxt], nxt))
        
    return dist[to]





route1 = getMinDist(1, u) + getMinDist(u, v) + getMinDist(v, n)
route2 = getMinDist(1, v) + getMinDist(v, u) + getMinDist(u, n)

answer = min(route1, route2)

if answer >= INF:
    print(-1)
else:
    print(answer)