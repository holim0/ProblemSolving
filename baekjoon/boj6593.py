from collections import deque

while True:

    l, r, c = map(int, input().split())

    if l== 0 and r==0 and c==0:
        break

    mapp = []
    visited = [[[False for _ in range(c)] for _ in range(r)] for _ in range(l)]
    dir = [(0, 0, 1), (0, 1, 0), (0, -1, 0), (0, 0, -1), (1, 0, 0), (-1, 0, 0)]

    sz, sx, sy = 0, 0, 0
    ez, ex, ey = 0, 0, 0
    for i in range(l):
        cur_mapp = []
        for _ in range(r):
            row = list(input().rstrip())            
            cur_mapp.append(row)
        mapp.append(cur_mapp)
        input()

  
    for k in range(l):
        for i in range(r):
            for j in range(c):
                if mapp[k][i][j] == "S":
                    sz, sx, sy = k, i, j
                if mapp[k][i][j] == "E":
                    ez, ex, ey = k, i, j
    q = deque([])

    visited[sz][sx][sy] = True

    q.append((sz, sx, sy, 0))
    isDone = False
    while q:
        cz, cx, cy, time = q.popleft()
        
        if cz==ez and cx == ex and cy==ey:
            isDone = True
            print("Escaped in " + str(time) + " minute(s).")
            break

        for alpha, beta, comma in dir:
            nz, nx, ny = cz+alpha, cx+beta, cy+comma
            
            if 0<=nz<l and 0<=nx<r and 0<=ny<c and mapp[nz][nx][ny] != "#" and not visited[nz][nx][ny]:
                visited[nz][nx][ny] = True
                q.append((nz, nx, ny, time+1))
        


    
    if not isDone:
        print("Trapped!")
    
        

