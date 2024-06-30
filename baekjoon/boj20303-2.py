from collections import deque
n, m, k = map(int, input().split())

candy = list(map(int, input().split()))
candy.insert(0, -1)


g = {}

group =[]

for _ in range(m):
    a, b = map(int, input().split())
    if a not in g:
        g[a] = [b]
    else:
        g[a].append(b)

    if b not in g:
        g[b] = [a]
    else:
        g[b].append(a)

check = [False] * (n+1)
for i in range(1, n+1):
    if not check[i]:
        check[i] = True

        q = deque([])
        cnt = 1
        candyCnt = candy[i]

        q.append(i)

        while q:
            cur = q.popleft()

            if cur not in g: continue

            for nxt in g[cur]:
                if not check[nxt]:
                    check[nxt] = True
                    q.append(nxt)
                    cnt+=1
                    candyCnt+= candy[nxt]
        
        group.append((cnt, candyCnt))

dp = [[0 for _ in range(k+1)] for _ in range(len(group))]


for i in range(len(group)):
    for j in range(1, k):
        w, v = group[i]
        if j-w>=0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[len(group)-1][k-1])

