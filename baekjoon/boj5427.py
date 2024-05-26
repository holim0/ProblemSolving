from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
mapp = []

def fire(w, h, visited):

    
    for i in range(h):
        for j in range(w):
            if mapp[i][j] == "*":
                for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    nx, ny = i+a, j+b
                    if 0<=nx<h and 0<=ny<w and mapp[nx][ny] !="#" and not visited[nx][ny]:
                        visited[nx][ny] = True





for _ in range(t):
    mapp = []

    w, h = map(int, input().split())

    for _ in range(h):
        row = list(input())
        mapp.append(row)

    sx, sy = 0, 0
    visited = [[False] * w for _ in range(h)]
    q = deque([])
    for i in range(h):
        for j in range(w):
            if mapp[i][j] == "@":
                sx, sy = i, j
            elif mapp[i][j] == "*":
                visited[i][j] = True
                q.append((i, j, 0, True))
    
    

    visited[sx][sy] = True
    
    q.append((sx, sy, 0, False))
    isDone = False
    while q:
        cx, cy, time, isFire = q.popleft()
        
        if cx>=h or cx<0 or cy>=w or cy<0:
            if not isFire:
                isDone = True
                print(time)
                break

        
        for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx, ny = cx+a, cy+b
            
            if 0<=nx<h and 0<=ny<w:
                if isFire:
                    if not visited[nx][ny] and mapp[nx][ny] != "#":
                        visited[nx][ny] = True
                        q.append((nx, ny, 0, isFire))
                else:
                    if not visited[nx][ny] and mapp[nx][ny] == ".":
                        visited[nx][ny] = True
                        q.append((nx, ny, time+1, isFire))

            else:
                
                if not isFire:
                    q.append((nx, ny, time+1, isFire))

    if not isDone:
        print("IMPOSSIBLE")   



