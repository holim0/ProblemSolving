import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
INF = 1e10
dist = [INF for _ in range(200000+1)]

q = []

dist[n] = 0

heapq.heappush(q, (0, n))

while q:
    cost, cur = heapq.heappop(q)

    if dist[cur]<cost: continue

    for nxt in [cur-1, cur+1]:
        if nxt <0 or nxt > 100000: continue
        newDist = cost + 1
        if newDist < dist[nxt]:
            dist[nxt] = newDist
            heapq.heappush(q, (newDist, nxt))
    
    if 2*cur < 100001 and cost < dist[2*cur]:
        dist[2*cur] = cost
        heapq.heappush(q, (cost, 2*cur))

print(dist[k])



