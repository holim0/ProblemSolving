from collections import deque
n, m, k = map(int, input().split())

candy = list(map(int, input().split()))
candy.insert(0, 0)
group = []

g = {}

for _ in range(m):
    a, b = map(int, input().split())

    if a not in g:
        g[a] = [b]
    else:
        g[a].append(b)

    if b not in g:
        g[b]= [a]
    else:
        g[b].append(a)

visited = [False for _ in range(n+1)]

for i in range(1, n+1):

    if not visited[i]:
        curValue = 0
        cnt = 0
        q = deque([])

        visited[i] = True

        q.append((i, candy[i]))

        while q:
            cur, curCandy = q.popleft()

            curValue+=curCandy
            cnt+=1
            if cur not in g: continue

            for nxt in g[cur]:
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append((nxt, candy[nxt]))
        
        group.append((curValue, cnt))

gSize = len(group)
group.insert(0, 0)
dp = [[0 for _ in range(k+1)] for _ in range(gSize+1)]

for i in range(1, gSize+1):
    for j in range(1, k+1):
        value, cnt = group[i]
        if j>=cnt:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cnt] + value)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[gSize][k-1])