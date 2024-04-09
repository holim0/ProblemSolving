import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())

INF = 1e10

dist = [INF for _ in range(v+1)]

mapp = {}

for _ in range(e):
    start, to, w = map(int, input().split())
    if start not in mapp:
        mapp[start] = [(w, to)]
    else:
        mapp[start].append((w, to))

dist[k] = 0

q = [(0, k)]

while q:
    curw, cur = heapq.heappop(q)

    if dist[cur] < curw: continue
    
    if cur not in mapp: continue
    for nxw, nxt in mapp[cur]:
    
        if dist[nxt] > curw + nxw:
            dist[nxt] = curw + nxw
            heapq.heappush(q, (curw + nxw, nxt))

for i in range(1, v+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])