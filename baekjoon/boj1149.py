n = int(input())

costMap =[[0]]

for _ in range(n):
    curCost = list(map(int, input().split()))
    costMap.append(curCost)

INF = 1e10
dp = [[INF for _ in range(3)] for _ in range(n+1)]

dp[1][0] = costMap[1][0]
dp[1][1] = costMap[1][1]
dp[1][2] = costMap[1][2]

for i in range(2, n+1):
    dp[i][0] = min(dp[i][0], min(dp[i-1][1], dp[i-1][2]) + costMap[i][0])

    dp[i][1] = min(dp[i][1], min(dp[i-1][0], dp[i-1][2]) + costMap[i][1])

    dp[i][2] = min(dp[i][2], min(dp[i-1][0], dp[i-1][1]) + costMap[i][2])


print(min(dp[n]))