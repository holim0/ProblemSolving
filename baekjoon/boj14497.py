import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

x1, y1, x2, y2 = map(int, input().split())

mapp =[]

for _ in range(n):
    row = list(input())
    row.pop()
    mapp.append(row)

x1-=1
y1-=1
x2-=1
y2-=1
cnt = 0
while True:

    q = deque([])
    check = [[False for _ in range(m)] for _ in range(n)]
    check[x1][y1] = True
    q.append((x1, y1))
    cnt+=1
    while q:
        cx, cy = q.popleft()
        if cx== x2 and cy==y2:
            print(cnt)
            sys.exit()
        for a, b in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = cx+a, cy+b
            if 0<=nx<n and 0<=ny<m and not check[nx][ny]:
                check[nx][ny] = True
                if mapp[nx][ny] == "0" or mapp[nx][ny] == "#":
                    q.append((nx, ny))
                elif mapp[nx][ny] == "1":
                    
                    mapp[nx][ny] = "0"
    

