n, m = map(int, input().split())

byte = list(map(int, input().split()))
cost = list(map(int, input().split()))

info = []

for i in range(n):
    info.append((byte[i], cost[i]))

cost_sum = sum(cost)

answer = 1e10

dp = [[0 for _ in range(cost_sum+1)] for _ in range(len(cost))]

for i in range(len(cost)):
    c = cost[i]
    for j in range(cost_sum+1):
        if j-c>=0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-c]+byte[i])
        else:
            dp[i][j] = dp[i-1][j]

for i in range(len(cost)):
    for j in range(cost_sum+1):
        if dp[i][j] >=m:
            answer = min(answer, j)

print(answer)

