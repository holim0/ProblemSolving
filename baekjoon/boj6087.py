from collections import deque
import sys
input = sys.stdin.readline
import copy

w, h = map(int, input().split())

mapp = []

for _ in range(h):
    row = list(input())
    mapp.append(row)

point = []

for i in range(h):
    for j in range(w):
        if mapp[i][j] == "C":
            point.append((i, j))

sx, sy = point[0]
ex, ey = point[1]

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
INF = 1e10
visited = [[[INF for _ in range(4)]for _ in range(w)] for _ in range(h)]

q = deque([])
visited[sx][sy][0] = 0
visited[sx][sy][1] = 0
visited[sx][sy][2] = 0
visited[sx][sy][3] = 0
q.append((sx, sy, 0))
q.append((sx, sy, 1))
q.append((sx, sy, 2))
q.append((sx, sy, 3))

answer = 1e10
while q:
    cx, cy, curDir = q.popleft()
    
    if cx==ex and cy==ey:
        
        answer = min(answer, visited[cx][cy][curDir])
        continue


    for i in range(0, 4):
        
        nx, ny = cx+dir[i][0], cy+dir[i][1]
        
        if 0<=nx<h and 0<=ny<w and mapp[nx][ny] !="*":
            
            if curDir == i:
                if visited[cx][cy][curDir] < visited[nx][ny][i]:
                    visited[nx][ny][i] = visited[cx][cy][curDir]
                    q.append((nx, ny, curDir))
            else:
                if visited[cx][cy][curDir] +1 < visited[nx][ny][i]:
                    visited[nx][ny][i] = visited[cx][cy][curDir] +1
                    q.append((nx, ny, i))

            

print(answer)
