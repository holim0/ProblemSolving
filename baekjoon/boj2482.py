n = int(input())
k = int(input())

MOD = 1000000003

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(0, n+1):
    dp[i][1] = i
    dp[i][0] = 1


for i in range(2, n+1):
    for j in range(2, k+1):
        dp[i][j] = (dp[i-2][j-1] + dp[i-1][j])%MOD

answer = (dp[n-1][k] + dp[n-3][k-1]) %MOD
print(answer)