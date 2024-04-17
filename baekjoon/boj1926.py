import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

mapp =[]

for _ in range(n):
    l = list(map(int, input().split()))
    mapp.append(l)
size = 0
count = 0
visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        value = mapp[i][j]
        if value == 0 : continue
        if visited[i][j]: continue

        q = deque([])
        visited[i][j] = True
        q.append((i, j))
        cur_size = 0

        while q: 
            x, y = q.popleft()
            cur_size+=1

            for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nx, ny = x+a, y+b
                if 0<=nx<n and 0<=ny<m and mapp[nx][ny] ==1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny)) 

        count+=1
        size = max(size, cur_size)

print(count)
print(size)