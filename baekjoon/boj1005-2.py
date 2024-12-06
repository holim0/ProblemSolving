from collections import deque

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    originTime = list(map(int, input().split()))
    originTime.insert(0, 0)
    
    time = []

    for ot in originTime:
        time.append(ot)

    degree = [0] * (n+1)
    g = {}
    for _ in range(k):
        x, y = map(int, input().split())
        degree[y]+=1

        g[x] = g.get(x, [])
        g[x].append(y)

    target = int(input())
    q = deque([])

    for i in range(1, n+1):
        if degree[i] ==0:
            q.append(i)
        
    while q:
        cur = q.popleft()

        if cur not in g: continue

        for nxt in g[cur]:
            degree[nxt]-=1
            time[nxt] = max(time[nxt], originTime[nxt] + time[cur])

            if degree[nxt]==0:
                q.append(nxt)
    
    print(time[target])