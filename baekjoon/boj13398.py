n = int(input())

number = list(map(int, input().split()))
INF = 1e10
dp = [[-INF] * 2 for _ in range(n)]

sum = 0

dp[0][0] = number[0]
dp[0][1] = number[0]
answer = max(dp[0][0], dp[0][1])
for i in range(1, n):
    
    dp[i][0] = max(dp[i-1][0]+number[i], number[i])
    dp[i][1] = max(dp[i-1][0], dp[i-1][1]+number[i])

    answer= max(answer, max(dp[i][0], dp[i][1]))




print(answer)

