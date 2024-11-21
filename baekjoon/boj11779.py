import heapq as hp

n = int(input())
m = int(input())

g = {}
INF = 1e10

dist = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    
    g[a] = g.get(a, [])
    g[a].append((c, b))

start, end = map(int, input().split())


q = []

hp.heappush(q, (0, start, str(start)))

pathStore = ""

while q:
    cost, cur, path = hp.heappop(q)

    if dist[cur] < cost: continue
    if cur not in g: continue

    for nxtCost, nxt in g[cur]:
        
        if dist[nxt] > nxtCost+cost:
            dist[nxt] = nxtCost+cost
            if nxt == end:
                pathStore = path+","+str(nxt)
            hp.heappush(q, (dist[nxt], nxt, path+","+str(nxt)))

print(dist[end])
print(len(pathStore.split(",")))
print(pathStore.replace(",", " "))