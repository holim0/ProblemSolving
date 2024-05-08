import sys
n = int(input())

answer = 0
INF = 1e10
dp = [INF for _ in range(n+1)]

if n>=3:
    dp[3] = 1

if n>=5:

    dp[5] = 1

    for i in range(6, n+1):
        dp[i] = min(dp[3] + dp[i-3], dp[5]+ dp[i-5])

if dp[n] >= INF:
    print(-1)
else:
    print(dp[n])