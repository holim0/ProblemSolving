import sys
input = sys.stdin.readline

m, n = map(int, input().split())

mapp = []

distCnt = [[-1]* n for _ in range(m)]

for _ in range(m):
    row = list(map(int, input().split()))
    mapp.append(row)


def getRoute(x, y):

    
    if x==m-1 and y==n-1:
        return 1
    
    if distCnt[x][y] !=-1:
        return distCnt[x][y]
    
    distCnt[x][y] = 0

    for a, b in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x+a, y+b

        if 0<=nx<m and 0<=ny<n and mapp[nx][ny]<mapp[x][y]:
            distCnt[x][y]+=getRoute(nx, ny)
    
    return distCnt[x][y]

print(getRoute(0, 0))