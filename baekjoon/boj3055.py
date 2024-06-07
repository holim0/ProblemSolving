from collections import deque
import sys
r, c = map(int, input().split())

check = [[False]*c for _ in range(r)]

mapp = []

for _ in range(r):
    row = input()
    row = list(row)
    mapp.append(row)

ex, ey = 0, 0
sx, sy = 0, 0

q = deque([])

for i in range(r):
    for j in range(c):
        if mapp[i][j] == "*":
            q.append((i, j, -1))
            check[i][j] = True
        
        if mapp[i][j] == "D":
            ex, ey = i, j
        if mapp[i][j] == "S":
            sx, sy = i, j

check[sx][sy] = True

q.append((sx, sy, 0))

while q:
    cx, cy, time = q.popleft()

    if time != -1 and cx==ex and cy==ey:
        print(time)
        sys.exit()

    
    for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nx, ny = cx+a, cy+b
        
        if 0<=nx<r and 0<=ny<c and not check[nx][ny]:
            if time== -1 and mapp[nx][ny] == "D": continue
            
            if mapp[nx][ny] !="X":
                check[nx][ny] = True
                if time == -1:
                    q.append((nx, ny, time))
                else:
                    q.append((nx, ny, time+1))





print("KAKTUS")