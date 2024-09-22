from collections import deque
import sys

r, c = map(int, input().split())
mapp =[]

for _ in range(r):
    row = list(input())
    mapp.append(row)

def isBoundary(x, y):
    if x==0 or x==r-1 or y==0 or y==c-1: return True
    return False

check= [[False for _ in range(c)] for _ in range(r)]

q = deque([])
fireQ = deque([])

for i in range(r):
    for j in range(c):
        if mapp[i][j] == "J":
            q.append((i, j, 0))
            check[i][j]  = True
        
        if mapp[i][j] == "F":
            fireQ.append((i, j))


dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def isInRange(x, y):
    global r
    global c

    if 0<=x<r and 0<=y<c: return True
    return False

def moveFire():

    curFireLen = len(fireQ)

    for _ in range(curFireLen):
        cx, cy = fireQ.popleft()
        for a, b in dir:
            nx, ny = cx+a, cy+b
            if isInRange(nx, ny) and (mapp[nx][ny] == "." or mapp[nx][ny] =="J"):
                mapp[nx][ny] = "F"
                fireQ.append((nx, ny))


while q:
    qLen = len(q)


    moveFire()
    for _ in range(qLen):
        cx, cy, cnt = q.popleft()
        if isBoundary(cx, cy):
            print(cnt+1)
            sys.exit()

        for a, b in dir:
            nx, ny = cx+a, cy+b
            if isInRange(nx, ny) and not check[nx][ny] and mapp[nx][ny] == ".":
                check[nx][ny] = True
                q.append((nx, ny, cnt+1))

print("IMPOSSIBLE")

