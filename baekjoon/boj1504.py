import sys, heapq as hq
input = sys.stdin.readline

n, e = map(int, input().split())

g = {}

INF = 1e10
answer = 0


for _ in range(e):
    a, b, c = map(int, input().split())
    if a not in g:
        g[a] = [(c, b)]
    else:
        g[a].append((c, b))

    if b not in g:
        g[b] = [(c, a)]
    else:
        g[b].append((c, a))


v1, v2 = map(int, input().split())

def find(start, to):
    dist = [INF for _ in range(n+1)]

    dist[start] = 0

    q = []

    hq.heappush(q, (0, start))

    while q:
        cur_dist, cur = hq.heappop(q)

        if cur_dist>dist[cur]: continue

        if cur not in g: continue

        for d, nxt in g[cur]:
            if dist[nxt]> d+cur_dist:
                dist[nxt] = d+cur_dist
                hq.heappush(q, (dist[nxt], nxt))
    
    return dist[to]

onetoV1 = find(1, v1)
onetoV2 = find(1, v2)


v1tov2 = find(v1, v2)

v1toN = find(v1, n)
v2toN = find(v2, n)

route1 = onetoV1 + v1tov2 + v2toN
route2 = onetoV2 + v1tov2 + v1toN

answer= min(route1, route2)
if answer >=INF:
    print(-1)
else:
    print(answer)