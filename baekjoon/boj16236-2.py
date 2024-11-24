from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

mapp = []

for _ in range(n):
    row = list(map(int, input().split()))
    mapp.append(row)


def findCanEat(sx, sy, curSize):
    global n, mapp
    canEatList = []

    q = deque([])
    check = [[False] * n for _ in range(n)]
    
    check[sx][sy] = True
    q.append((sx, sy, 0))

    while q: 
        cx, cy, dist = q.popleft()

        if mapp[cx][cy] !=0 and mapp[cx][cy] !=9 and mapp[cx][cy]<curSize:
            canEatList.append((dist, cx, cy))
            continue


        for a, b in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = cx+a, cy+b

            if 0<=nx<n and 0<=ny<n and not check[nx][ny] and mapp[nx][ny] != 9 and mapp[nx][ny]<=curSize:
                q.append((nx, ny, dist+1))
                check[nx][ny] = True 

    return canEatList



time = 0

curSize = 2
eatCnt = 0
cx, cy = 0, 0

for i in range(n):
    for j in range(n):
        if mapp[i][j] == 9: 
            cx=i
            cy=j
            break

while True:

    canEatList = findCanEat(cx, cy, curSize)
    
    if len(canEatList)==0:
        print(time)
        break

    canEatList.sort()
    tdist, tx, ty = canEatList[0]
    mapp[cx][cy] = 0
    cx, cy = tx, ty
    mapp[tx][ty] = 9
    eatCnt+=1

    if eatCnt == curSize:
        curSize+=1
        eatCnt = 0
    time+=tdist
    