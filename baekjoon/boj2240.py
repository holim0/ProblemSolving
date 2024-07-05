t, w = map(int, input().split())

info =[0]

for _ in range(t):
    n = int(input())
    info.append(n)

answer = 0

dp =[[[0] * (w+1) for _ in range(t+2)] for _ in range(3)]


for i in range(1, t+1):
    dropPos = info[i]
    for j in range(w+1):
        if j==0:
            if dropPos ==1:
                dp[1][i][j] = dp[1][i-1][j]+1
                dp[2][i][j] = dp[2][i-1][j]
            else:
                if i==1: continue
                dp[1][i][j] = dp[1][i-1][j]
                dp[2][i][j] = dp[2][i-1][j]+1
        else:
            if dropPos ==1:
                dp[1][i][j] = max(dp[1][i-1][j]+1, dp[2][i-1][j-1]+1)
                dp[2][i][j] = max(dp[2][i-1][j], dp[1][i-1][j-1])
            else:
                dp[1][i][j] = max(dp[1][i-1][j], dp[2][i-1][j-1])
                dp[2][i][j] = max(dp[2][i-1][j]+1, dp[1][i-1][j-1]+1)

answer =0
for i in range(w+1):
    answer = max(answer, dp[1][t][i])
    answer = max(answer, dp[2][t][i])

print(answer)