n, m = map(int, input().split())
k = int(input())


no = []
for _ in range(k):
    a, b, c, d = map(int, input().split())
    no.append((a, b, c, d))


dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

dp[0][0] = 1

for i in range(m+1):
    for j in range(n+1):
        if i==0 and j==0: continue

        for a, b in [(-1, 0), (0, -1)]:
            nx, ny = i+a, j+b

            if 0<=nx and 0<=ny and ((ny, nx, j, i) not in no and (j,i, ny, nx) not in no):
                dp[i][j] += dp[nx][ny]
            


print(dp[m][n])
            
            
