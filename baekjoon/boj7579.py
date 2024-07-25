n, m = map(int, input().split())

mem = list(map(int, input().split()))
cost = list(map(int, input().split()))

info =[(0, 0)]

for i in range(n):
    info.append((mem[i], cost[i]))

INF = 1e10
s = sum(cost)
dp = [[0 for _ in range(s+1)] for _ in range(n+1)]

answer= INF

for i in range(1, n+1):
    for j in range(0, s+1):
        curMem, cost = info[i]
        if j-cost>=0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost] + curMem)
        else:
            dp[i][j] = max(dp[i][j], dp[i-1][j])
        
        if dp[i][j] >=m:
            answer= min(answer, j)

print(answer)
