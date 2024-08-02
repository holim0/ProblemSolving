from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

mapp = []

for _ in range(n):
    row = list(map(int, input().split()))
    mapp.append(row)

h, w, sx, sy, ex, ey = map(int, input().split())
sx, sy, ex, ey = sx-1, sy-1, ex-1, ey-1

check = [[False for _ in range(m)] for _ in range(n)]

q = deque([])

check[sx][sy] = True

q.append((sx, sy, 0))


def getPoint(baseX, baseY):
    return [(baseX, baseY), (baseX+h-1, baseY), (baseX, baseY+w-1), (baseX+h-1, baseY+w-1)]

def isBlock(a, b, group):

    if a==1 and b==0:
        sx, sy = group[1]
        for i in range(sy, sy+w):
            curValue = mapp[sx][i]
            if curValue == 1: return True

    elif a== -1 and b==0:
        sx, sy = group[0]
        for i in range(sy, sy+w):
            curValue = mapp[sx][i]
            if curValue == 1: return True


    elif a==0 and b==1:
        sx, sy = group[2]
        for i in range(sx, sx+h):
            curValue = mapp[i][sy]
            if curValue ==1: return True

    elif a==0 and b==-1:
        sx, sy = group[0]
        for i in range(sx, sx+h):
            curValue = mapp[i][sy]
            if curValue ==1: return True

    return False

def checkRange(group):

    for x, y in group:
        if 0<=x<n and 0<=y<m:
            continue
        else: 
            return False
    
    return True

while q:
    cx, cy, cnt = q.popleft()
    
    if cx==ex and cy ==ey:
        print(cnt)
        sys.exit()

    
    for a, b in [(1, 0), (0,1), (-1, 0), (0, -1)]:
        
        nx, ny = cx+a, cy+b

        nxtPos = getPoint(nx, ny)

        if not checkRange(nxtPos): continue
        
        if check[nx][ny]: continue
        
        if isBlock(a, b, nxtPos): continue
        
        check[nx][ny] = True
        q.append((nx, ny, cnt+1))


print(-1)