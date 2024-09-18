import sys
input = sys.stdin.readline
n, m = map(int, input().split())

mapp =[ ]
answer = 0
check = [[False for _ in range(m)] for _ in range(n)]
for _ in range(n):
    row = list(map(int, input().split()))
    mapp.append(row)


def getSol(x, y, cnt, sum):
    global check
    global answer
    if cnt==4:
        answer = max(answer, sum)
        return


    for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nx, ny = x+a, y+b
        if 0<=nx<n and 0<=ny<m and not check[nx][ny]:
            check[nx][ny] = True
            getSol(nx, ny, cnt+1, sum+mapp[nx][ny])
            check[nx][ny] = False

def getSol2(x, y):
    global answer
    baseSum = mapp[x][y]

    for a, b in [(0, 1), (1, 0), (-1, 0)]:
        nx, ny = x+a, y+b
        if 0<=nx<n and 0<=ny<m:
            baseSum+=mapp[nx][ny]
        else:
            baseSum = mapp[x][y]
            break
    answer = max(answer, baseSum)
    baseSum = mapp[x][y]
    for a, b in [(0, 1), (1, 0), (0, -1)]:
        nx, ny = x+a, y+b
        if 0<=nx<n and 0<=ny<m:
            baseSum+=mapp[nx][ny]
        else:
            baseSum = mapp[x][y]
            break
    answer = max(answer, baseSum)
    baseSum = mapp[x][y]
    for a, b in [(1, 0), (-1, 0), (0, -1)]:
        nx, ny = x+a, y+b
        if 0<=nx<n and 0<=ny<m:
            baseSum+=mapp[nx][ny]
        else:
            baseSum = mapp[x][y]
            break
    answer = max(answer, baseSum)
    baseSum = mapp[x][y]
    for a, b in [(0, 1), (-1, 0), (0, -1)]:
        nx, ny = x+a, y+b
        if 0<=nx<n and 0<=ny<m:
            baseSum+=mapp[nx][ny]
        else:
            baseSum = mapp[x][y]
            break
    answer = max(answer, baseSum)


for i in range(n):
    for j in range(m):
        check[i][j] = True
        getSol(i, j, 1, mapp[i][j])
        check[i][j] = False
        getSol2(i, j)
    

print(answer)