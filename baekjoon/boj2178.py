import sys
from collections import deque

n, m = map(int, input().split())

miro = []
visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    item = input()
    item = list(map(int, list(item)))
    miro.append(item)


visited[0][0] = True

q = deque([])
q.append((0, 0, 1))


while q != 0:
    cx, cy, cnt = q.popleft()

    if cx == n-1 and cy == m-1:
        print(cnt)
        break

    for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = cx+i, cy+j

        if 0<=nx<n and 0<=ny<m:
            if not visited[nx][ny] and miro[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny, cnt+1))




