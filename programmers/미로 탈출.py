from collections import deque
def solution(maps):
    answer = 0
    
    for i in range(len(maps)):
        maps[i] = list(maps[i])
        
    sx, sy, ex, ey = 0, 0, 0, 0
    
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 'S':
                sx, sy = i, j
                
            if maps[i][j] == "E":
                ex, ey = i, j
                
    
    visited = [[[False] *2 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    visited[sx][sy][0] = True
    
    q= deque([])
    q.append((sx, sy, 0, False))
    
    while q:
        cx, cy, time, islabber = q.popleft()
        
        
        if cx==ex and cy==ey and islabber:
            return time
        
        
        for a, b in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = cx+a, cy+b
            
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]) and maps[nx][ny] !="X":
                if maps[nx][ny] == "L":
                    if not visited[nx][ny][1]:
                        visited[nx][ny][1] = True
                        q.append((nx, ny, time+1, True))
                        continue
                
                if islabber:
                    if not visited[nx][ny][1]:
                        visited[nx][ny][1] = True
                        q.append((nx, ny, time+1, islabber))
                    
                else:
                    if not visited[nx][ny][0]:
                        visited[nx][ny][0] = True
                        q.append((nx, ny, time+1, islabber))
                    
    
    return -1