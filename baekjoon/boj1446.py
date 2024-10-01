import heapq as hp

n, d = map(int, input().split())

info = []
g = {}
q = []
for i in range(0, d):
    g[i] = [(1, i+1)]

for _ in range(n):
    s, e, dist = map(int, input().split())

    if e>d: continue

    if s not in g:
        g[s] = [(dist, e)]
    else:
        g[s].append((dist, e))



dist = [1e10 for _ in range(d+1)]


hp.heappush(q, (0, 0))
dist[0] = 0
while q:
    curDist, cur = hp.heappop(q)

    if dist[cur] < curDist: continue

    if cur not in g: continue
    for nxtDist, nxt in g[cur]:
        if nxt>d: continue
        if dist[nxt] > curDist + nxtDist:
            dist[nxt] = curDist + nxtDist
            hp.heappush(q, (dist[nxt], nxt))
            
    
print(dist[d])