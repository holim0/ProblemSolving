import heapq

n, m, x = map(int, input().split())

g = {}

for _ in range(m):
    a, b, t = map(int, input().split())

    if a not in g:
        g[a] = [(t, b)]
    else:
        g[a].append((t, b))

answer = 0

INF = 1e10

for i in range(1, n+1):

    q = []
    dist = [INF for _ in range(n+1)]
    heapq.heappush(q, (0, i))
    dist[i] = 0
    answerDist = 0
    while q:
        curdist, cur = heapq.heappop(q)

        if curdist > dist[cur]: continue
        if cur not in g: continue

        for nxtDist, nxt in g[cur]:
            if dist[nxt] > curdist + nxtDist:
                dist[nxt] = curdist + nxtDist
                heapq.heappush(q, (dist[nxt], nxt)) 
                
    answerDist+=dist[x]    
    q = []
    dist = [INF for _ in range(n+1)]
    dist[x] = 0
    heapq.heappush(q, (0, x))
    while q:
        curdist, cur = heapq.heappop(q)

        if curdist > dist[cur]: continue
        if cur not in g: continue

        for nxtDist, nxt in g[cur]:
            if dist[nxt] > curdist + nxtDist:
                dist[nxt] = curdist + nxtDist
                heapq.heappush(q, (dist[nxt], nxt)) 

    answerDist+=dist[i]
    answer =max(answer, answerDist)

print(answer)