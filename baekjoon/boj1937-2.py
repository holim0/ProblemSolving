import sys
sys.setrecursionlimit(10000)
n = int(input())
mapp = []
answer = 1
for _ in range(n):
    row = list(map(int, input().split()))
    mapp.append(row)

dp =[[-1 for _ in range(n)] for _ in range(n)]


def getSol(cx, cy):

    if dp[cx][cy] != -1:
        return dp[cx][cy]
    

    dp[cx][cy] = 1
    maxCnt = 0
    for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nx, ny = cx+a, cy+b
        if 0<=nx<n and 0<=ny<n and mapp[cx][cy] < mapp[nx][ny]:
            cnt = getSol(nx, ny)
            maxCnt = max(cnt, maxCnt)
    
    dp[cx][cy] += maxCnt
    return dp[cx][cy]



for i in range(0, n):
    for j in range(0, n):
        value = getSol(i, j)
        answer = max(answer, value)

print(answer)