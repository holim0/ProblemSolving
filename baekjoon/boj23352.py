from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

mapp = []

for _ in range(n):
    row = list(map(int, input().split()))
    mapp.append(row)


maxDist = 0
value = 0

for i in range(n):
    for j in range(m):
        if mapp[i][j] == 0: continue
        
        q = deque([])
        check = [[False] * m for _ in range(n)]
        check[i][j] = True
        q.append((i, j, 0))
        baseValue = mapp[i][j]

        while q: 
            cx, cy, curDist = q.popleft()

            if curDist > maxDist:
                maxDist = curDist
                value = baseValue + mapp[cx][cy]
            elif curDist == maxDist:
                value = max(value, baseValue + mapp[cx][cy])
            

            for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nx, ny = cx+a, cy+b

                if 0<=nx<n and 0<=ny<m and mapp[nx][ny] !=0 and not check[nx][ny]:
                    check[nx][ny] = True
                    q.append((nx, ny, curDist+1))

print(value)