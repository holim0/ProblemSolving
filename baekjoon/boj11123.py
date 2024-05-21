from collections import deque

t = int(input())

for _ in range(t):
    h, w = map(int, input().split())

    mapp = []

    for _ in range(h):
        row = list(input())
        mapp.append(row)
    
    visited = [[False for _ in range(w)] for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if mapp[i][j] == "#" and not visited[i][j]:
                visited[i][j] = True

                q = deque([])

                q.append((i, j))

                while q:
                    cx, cy = q.popleft()

                    for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        nx, ny = cx+a, cy+b

                        if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and mapp[nx][ny] == "#":
                            visited[nx][ny] = True
                            q.append((nx, ny))
                
                cnt+=1
        
    print(cnt)

