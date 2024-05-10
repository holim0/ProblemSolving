from collections import deque
import sys

m, n = map(int, input().split())

mapp = []

for _ in range(n):
    row = list(map(int, input().split()))
    mapp.append(row)

visited = [[False for _ in range(m)] for _ in range(n)]


day = 0
tomato =deque([])
for i in range(n):
    for j in range(m):
        if mapp[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            tomato.append((i, j, 0))

answerDay = 0
while tomato:
    cx, cy, day = tomato.popleft()

    answeDay = day

    for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nx, ny = cx+a, cy+b

        if 0<=nx<n and 0<=ny<m and mapp[nx][ny] == 0 and not visited[nx][ny]:
            visited[nx][ny] = True
            mapp[nx][ny] = 1
            tomato.append((nx, ny, day+1))


for i in range(n):
    for j in range(m):
        if mapp[i][j] ==0:
            print(-1)
            sys.exit()

print(day)
            


