from collections import deque

W, B = 0, 0

n, m = map(int, input().split())

visited = [[False for _ in range(n)] for _ in range(m)]

mapp = []

for _ in range(m):
    row = list(input())
    mapp.append(row)


for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            
            cur = mapp[i][j]

            cnt = 0

            q = deque([])
            q.append((i, j))

            while q:
                cx, cy = q.popleft()
                cnt+=1

                for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    nx, ny = cx+a, cy+b

                    if 0<=nx<m and 0<=ny<n and mapp[nx][ny] == cur and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))
            
            if cur == "W":
                W+= (cnt**2)
            else:
                B += (cnt**2)

print(W, B)






            