from collections import deque
import sys
n, m = map(int, input().split())

mapp = []

for _ in range(n):
    row = list(map(int, input()))
    mapp.append(row)

q = deque([])


visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(2)]

visited[0][0][0] = True
visited[1][0][0] = True

q.append((0, 0, 0, 1))

while q:
    cx, cy, isBreak, dist = q.popleft()

    if cx == n-1 and cy==m-1:
        print(dist)
        sys.exit()

    for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nx, ny = cx+a, cy+b

        if 0<=nx<n and 0<=ny<m:
            if mapp[nx][ny] == 0 and not visited[isBreak][nx][ny]:
                visited[isBreak][nx][ny] = True
                q.append((nx, ny, isBreak, dist+1))
            elif mapp[nx][ny] == 1:
                if isBreak == 0 and not visited[1][nx][ny]:
                    visited[1][nx][ny] = True
                    q.append((nx, ny, 1, dist+1))


print(-1)

