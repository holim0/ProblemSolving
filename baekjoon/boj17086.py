from collections import deque
n, m = map(int, input().split())

mapp = []

for _ in range(n):
    row = list(map(int, input().split()))
    mapp.append(row)



maxSafe = -1

for i in range(n):
    for j in range(m):
        if mapp[i][j] == 1: continue

        q = deque([])
        check = [[False] * m for _ in range(n)]
        q.append((i, j, 0))
        check[i][j] = True

        while q:
            cx, cy, cnt = q.popleft()
            
            if mapp[cx][cy] ==1:
                maxSafe = max(maxSafe, cnt)
                break

            for a, b in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (-1, -1) ,(1, -1)]:
                nx, ny = cx+a, cy+b

                if 0<=nx<n and 0<=ny<m and not check[nx][ny]:
                    check[nx][ny] = True
                    q.append((nx, ny, cnt+1))

print(maxSafe)