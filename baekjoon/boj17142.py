import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

mapp =[]

pos =[]
empty= []


for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 2:
            pos.append((i, j))
        if row[j] == 0:
            empty.append((i, j))
    mapp.append(row)

def checkDone(check):

    for i in range(n):
        for j in range(n):
            if mapp[i][j] ==0 and check[i][j]==-1: return False

    return True

def getSol(curPos):
    
    q = deque([])
    check = [[-1 for _ in range(n)] for _ in range(n)]

    for x, y in curPos:
        check[x][y] = 0
        q.append((x, y, 0))
    
    curEmpty =[]
    curTime = 0
    while q:
        cx, cy, time = q.popleft()
        if(len(curEmpty) == len(empty)):
            return curTime
        for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx, ny = cx+a, cy+b

            if 0<=nx<n and 0<=ny<n and mapp[nx][ny] !=1 and check[nx][ny]==-1:
                check[nx][ny] = time+1
                curTime =max(curTime, time+1)
                if mapp[nx][ny] == 0:
                    curEmpty.append((nx,ny))
                q.append((nx, ny, time+1))
    
    return 1e10

answer = 1e10

def selectPos(cur, idx):
    global answer

    if len(cur) == m:
        curTime = getSol(cur)
        answer= min(answer, curTime)
        return 
    

    for i in range(idx, len(pos)):
        cur.append(pos[i])
        selectPos(cur, i+1)
        cur.pop()

selectPos([], 0)

if answer == 1e10:
    print(-1)
else:
    print(answer)