import sys
n, m = map(int, input().split())

mapp =[]

for _ in range(n):
    row = list(map(int, input().split()))
    mapp.append(row)

dp = [[-1 for _ in range(m)] for _ in range(n)]

def find(x, y):
    global dp

    if x==n-1 and y==m-1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    route= 0
    for a, b in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = x+a, y+b
        
        if 0<=nx<n and 0<=ny<m and mapp[nx][ny]<mapp[x][y]:
            route +=find(nx, ny)
    
    dp[x][y] = route
    return dp[x][y]


print(find(0, 0))