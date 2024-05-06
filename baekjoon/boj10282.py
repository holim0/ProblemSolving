import heapq
t = int(input())

INF = 1e10
for _ in range(t):
    n, d, c = map(int, input().split())

    time = [INF for _ in range(n+1)]
    time[c] = 0
    g = {}
    for _ in range(d):
        a, b, s = map(int, input().split())
        if b not in g:
            g[b] = [(s, a)]
        else:
            g[b].append((s, a))

    q = []
    heapq.heappush(q, (0, c))
    cnt = 1
    visit = [c]
    while q:
        curtime, cur = heapq.heappop(q)
        if curtime > time[cur]: continue
        
        if cur not in g:
            continue

        for nxtTime, nxt in g[cur]:
            if time[nxt] > nxtTime + curtime:
                time[nxt] = nxtTime + curtime
                heapq.heappush(q, (time[nxt], nxt))
                if nxt not in visit:
                    visit.append(nxt)
    
    answer_time = 0
    for t in time:
        if t != INF:
            answer_time = max(answer_time, t)
    print(len(visit), answer_time)
            