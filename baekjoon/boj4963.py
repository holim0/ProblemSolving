import sys
from collections import deque
input = sys.stdin.readline

while True:

    w, h = map(int, input().split())
    if w==0 and h==0: break

    mapp =[]

    for _ in range(h):
        row = list(map(int, input().split()))
        mapp.append(row)
    
    visit = [[False]*w for _ in range(h)]
    q = deque([])
    answer = 0
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    for i in range(h):
        for j in range(w):
            if mapp[i][j]!=1 or visit[i][j]: continue
            
            visit[i][j] = True
            answer+=1

            q.append(([i, j]))

            while q:
                cx, cy = q.popleft()

                
                for a, b in dir:
                    nx, ny = cx+a, cy+b

                    if 0<=nx<h and 0<=ny<w and mapp[nx][ny] ==1 and not visit[nx][ny]:
                        visit[nx][ny] = True
                        q.append((nx, ny))

    print(answer)