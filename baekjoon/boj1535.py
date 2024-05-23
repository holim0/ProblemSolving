n = int(input())

hp = list(map(int, input().split()))
happy = list(map(int, input().split()))
hp.insert(0, 0)
happy.insert(0, 0)
dp = [[0] * 101 for _ in range(n + 1)]


for i in range(1, n+1):
    for j in range(1, 100):
        if j>=hp[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-hp[i]] + happy[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][99])