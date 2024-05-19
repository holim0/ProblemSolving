from collections import deque
import sys
m1 = []
m2 = []


n, m = map(int, input().split())

visited = [[False for _ in range(m)] for _ in range(n)]

for _ in range(n):
    row = list(map(int, input().split()))
    m1.append(row)

for _ in range(n):
    row = list(map(int, input().split()))
    m2.append(row)


isbreak = False
for i in range(n):
    if isbreak: break
    for j in range(m):
        if m1[i][j] != m2[i][j]:
            targetValue = m2[i][j]

            visited[i][j] = True
            
            q = deque([])
            q.append((i, j))

            while q:
                cx, cy = q.popleft()

                for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    nx, ny = cx+a, cy+b

                    if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and m1[nx][ny] == m1[i][j]:
                        visited[nx][ny] = True
                        m1[nx][ny] = targetValue
                        q.append((nx, ny))                

            m1[i][j] = targetValue

            isbreak = True
            break
    
for i in range(n):
    for j in range(m):
        if m1[i][j] != m2[i][j]:
            print("NO")
            sys.exit()

print("YES")
