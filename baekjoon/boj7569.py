from collections import deque
import sys
dir = [(0, 0, 1), (0, 1, 0), (0, 0, -1), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]

m, n, h = map(int, input().split())

mapp =[]

check = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]

for i in range(h):
    row =[]

    for _ in range(n):
        rrow = list(map(int, input().split()))
        row.append(rrow)
    
    mapp.append(row)

q = deque([])

totalTomato = 0

for i in range(h):
    for a in range(n):
        for b in range(m):
            if mapp[i][a][b]==1 or mapp[i][a][b]==0:
                totalTomato+=1
            if mapp[i][a][b] ==1:
                q.append((0, i, a, b))
                check[i][a][b] = True

curCnt = 0
while q:
    day, curh, curi, cury = q.popleft()

    curCnt+=1
    if curCnt== totalTomato:
        print(day)
        sys.exit()

    for a, b, c in dir:
        nh, nx, ny = curh+a, curi+b, cury+c

        if 0<=nh<h and 0<=nx<n and 0<=ny<m and not check[nh][nx][ny] and mapp[nh][nx][ny]==0:
            check[nh][nx][ny] = True
            mapp[nh][nx][ny] = 1
            q.append((day+1, nh, nx, ny))



print(-1)
