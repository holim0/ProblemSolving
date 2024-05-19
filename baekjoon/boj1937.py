import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
n = int(input())


mapp =[]

for _ in range(n):
    row = list(map(int, input().split()))
    mapp.append(row)
answer = 0

dp = [[-1 for _ in range(n)] for _ in range(n)]

def find(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 1

    for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nx, ny = x+a, y+b
        if 0<=nx<n and 0<=ny<n and mapp[nx][ny] > mapp[x][y]:
            dp[x][y] = max(dp[x][y], find(nx, ny) +1)
    
    return dp[x][y]
    


for i in range(n):
    for j in range(n):
        answer = max(find(i, j), answer)

print(answer)