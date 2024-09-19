from collections import deque
import sys
INF = 1e10
n, m = map(int, input().split())

mapp =[]

check = [[False for _ in range(m)] for _ in range(n)]

for _ in range(n):
    row = list(map(int, input().split()))
    mapp.append(row)



isLand = []

def isInRange(x, y):
    global n
    global m
    if 0<=x<n and 0<=y<m: return True
    return False


label = 1
for i in range(n):
    for j in range(m):
        if check[i][j] or mapp[i][j] == 0: continue

        q = deque([])
        check[i][j] = True
        q.append((i, j))
        curIsLand = []
        while q:
            cx, cy = q.popleft()
            curIsLand.append((cx, cy))

            for a, b in [(0,1), (1, 0), (-1, 0), (0, -1)]:
                nx, ny = cx+a, cy+b

                if isInRange(nx, ny) and mapp[nx][ny] == 1 and not check[nx][ny]:
                    check[nx][ny] = True
                    q.append((nx, ny))
        
        for x, y in curIsLand:
            mapp[x][y] = label
        label+=1
        isLand.append(curIsLand)

distList = []
totalDist = 0

isLink = [[False for _ in range(10)] for _ in range(10)]

for i in range(len(isLand)-1):
    fromIsLand = isLand[i]
    for j in range(i+1, len(isLand)):
        if isLink[i+1][j+1] or isLink[j+1][i+1]: continue
        targetIsLand = isLand[j]
        dist = INF
        
        for sx, sy in fromIsLand:
            q = deque([])
            q.append((sx, sy, -1, ""))
            while q:
                cx, cy, moveCnt, dir = q.popleft()
                if (cx, cy) in targetIsLand:
                    if moveCnt ==1: continue
                    
                    dist = min(dist, moveCnt)
                    continue

                if dir == "":
                    for a, b in [(1, 0), (0, 1), (-1,0), (0, -1)]:
                        nx, ny = cx+a, cy+b

                        if isInRange(nx, ny) and (mapp[nx][ny] == 0 or mapp[nx][ny] == j+1):
                            q.append((nx, ny, moveCnt+1, (a, b)))
                        
                else:
                    nx, ny = cx+dir[0], cy+dir[1]
                    if isInRange(nx, ny) and (mapp[nx][ny] == 0 or mapp[nx][ny] == j+1):
                        q.append((nx, ny, moveCnt+1, dir))

        if dist != INF:
            distList.append((dist, i+1, j+1))
            isLink[i+1][j+1] = True
            isLink[j+1][i+1] = True
            totalDist+=dist

distList.sort(key = lambda x: x[0])
parent = [i for i in range(len(isLand)+1)]
answer = 0
def find(x):
    if parent[x] == x:
        return x
    
    return find(parent[x])

def merge(x, y):
    x = find(x)
    y = find(y)

    if x>y:
        parent[x] = y
    else:
        parent[y] = x

link = 0

for curDist, i, j in distList:
    
    if find(i) != find(j):
        merge(i, j)
        link+=1
        answer+=curDist
        

if link == len(isLand)-1:
    print(answer)
else:
    print(-1)


