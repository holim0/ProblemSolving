n = int(input())

a = list(map(int, input().split()))

up_dp = [1 for _ in range(n)]
down_dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            up_dp[i] = max(up_dp[i], up_dp[j]+1)


a.reverse()

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            down_dp[i] = max(down_dp[i], down_dp[j]+1)

down_dp.reverse()

answer = 0


for i in range(n):
    answer = max(answer, up_dp[i] + down_dp[i])

print(answer-1)