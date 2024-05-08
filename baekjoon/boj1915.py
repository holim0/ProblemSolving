n, m = map(int, input().split())

mapp =[]

for _ in range(n):
    row = input()
    row = list(row)
    mapp.append(row)

dp = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if mapp[i][j] == "1":
            dp[i][j] = 1


for i in range(n):
    for j in range(m):
        size = max(i, j) + 1
        if dp[i][j]!=0 and i>=1 and j-1>=0:
            if dp[i-1][j-1] !=0 and dp[i-1][j-1] !=0 and dp[i][j-1] !=0:
                dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1])) +1

answer = 0
for row in dp:
    answer = max(answer, max(row))

print(answer * answer)