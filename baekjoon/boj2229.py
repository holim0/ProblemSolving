n = int(input())
score = list(map(int, input().split()))

dp =[0] * n

dp[0] = 0

dp[1] = abs(score[0] - score[1])

for i in range(2, n):

    for j in range(i):
        dp[i] = max(dp[i], dp[j] + abs(min(score[j+1:i+1])-max(score[j+1:i+1])))

print(dp[n-1])