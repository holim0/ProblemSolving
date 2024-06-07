from collections import deque

mapp =[]
answer = 1e10
w, h = map(int, input().split())

lazer = []

for _ in range(h):
    row = list(input())
    mapp.append(row)

for i in range(h):
    for j in range(w):
        if mapp[i][j] == "C":
            lazer.append((i, j))

sx, sy = lazer[0]
ex, ey = lazer[1]

check = [[[1e10]*4 for _ in range(w)] for _ in range(h)]

check[sx][sy][0] = 0
check[sx][sy][1] = 0
check[sx][sy][2] = 0
check[sx][sy][3] = 0


q = deque([])

q.append((sx, sy, 0))
q.append((sx, sy, 1))
q.append((sx, sy, 2))
q.append((sx, sy, 3))

dir = {
    0: (0, 1),
    1: (1, 0),
    2: (-1, 0),
    3: (0, -1)
}

dirValue = [(0, 1), (1, 0), (-1, 0), (0, -1)]

while q:
    cx, cy, curDirNum = q.popleft()

    if cx==ex and cy==ey:
        answer = min(answer, check[cx][cy][curDirNum])
        continue


    for i in range(4) :
        a, b = dirValue[i]
        nx, ny = cx+a, cy+b

        if 0<=nx<h and 0<=ny<w and mapp[nx][ny] !="*":
            if curDirNum == i:
                if check[nx][ny][curDirNum] > check[cx][cy][curDirNum]:
                    check[nx][ny][curDirNum] = check[cx][cy][curDirNum]
                    q.append((nx, ny, curDirNum))
            else:
                if check[cx][cy][curDirNum] +1 < check[nx][ny][i]:
                    check[nx][ny][i] = check[cx][cy][curDirNum] +1
                    q.append((nx, ny, i))

    

    




print(answer)