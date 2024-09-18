from collections import deque
import sys

q = deque([])

n, m = map(int, input().split())

mapp =[]

for _ in range(n):
    row = list(map(int, input()))
    mapp.append(row)

check = [[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]

check[0][0][0] = True
check[0][0][1] = True

q.append((0, 0, 1, False))

while q:
    cx, cy, cnt, isBreak = q.popleft()

    if cx==n-1 and cy==m-1:
        print(cnt)
        sys.exit()

    
    for a, b in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = cx+a, cy+b

        if 0<=nx<n and 0<=ny<m:
            if mapp[nx][ny] == 0 and not check[nx][ny][isBreak]:
                check[nx][ny][isBreak] = True
                q.append((nx, ny, cnt+1, isBreak))
            
            elif mapp[nx][ny] == 1 and not check[nx][ny][1] and not isBreak:
                check[nx][ny][1] = True
                q.append((nx, ny, cnt+1, True))


print(-1)
