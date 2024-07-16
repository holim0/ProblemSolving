n = int(input())

stair = [-1, ]

for _ in range(n):
    s = int(input())
    stair.append(s)

dp = [[0 for _ in range(2)] for _ in range(n+1)]

dp[1][0] = stair[1]

for i in range(2, n+1):

    dp[i][0] = max(dp[i][0], max(dp[i-2][0], dp[i-2][1]) + stair[i])

    dp[i][1] = max(dp[i-1][0] + stair[i], dp[i][1])

print(max(dp[n][0], dp[n][1]))