n = int(input())

INF = 1e10
dp = [INF for _ in range(n+1)]

for i in range(1, n+1):
    if i*i <=n:
        dp[i*i] = 1

for i in range(1, n+1):
    for j in range(0, i):
        if j*j <=i:
            dp[i] = min(dp[i], dp[i-(j*j)] + dp[j*j])
        else:
            break

print(dp[n])