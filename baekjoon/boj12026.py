
n = int(input())
path = list(input())
INF = 1e10
dp = [1e10 for _ in range(n)]


dp[0] = 0

for i in range(1, n):
    for j in range(0, i):
        if path[i] == "J" and path[j] == "O":
            dp[i] = min(dp[i], dp[j]+pow(i-j, 2))
        elif path[i] == "O" and path[j] == "B":
            dp[i] = min(dp[i], dp[j]+pow(i-j, 2))
        elif path[i] == "B" and path[j] == "J":
            dp[i] = min(dp[i], dp[j]+pow(i-j, 2))

if dp[n-1] == INF:
    print(-1)
else:
    print(dp[n-1])
