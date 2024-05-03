from collections import deque
n, m = map(int, input().split())

mapp = []

for _ in range(n):
    row = list(map(int, input().split()))
    mapp.append(row)


visited = [[False for _ in range(m)] for _ in range(n)]

def checkValid(i, j):
    global mapp

    for a, b in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
        nx, ny = i+a, j+b

        if 0<=nx<n and 0<=ny<m:
            if mapp[nx][ny] > mapp[i][j] :
                return False

    return True

answer = 0 

for i in range(n):
    for j in range(m):
        if not visited[i][j] and mapp[i][j] != 0 and checkValid(i, j):
            visited[i][j] = True
            q = deque([])
            q.append((i, j))
            cur = mapp[i][j]
            isHigh = True
            while q:
                cx, cy = q.popleft()

                if not checkValid(cx, cy):
        
                    isHigh = False
                    break

                for a, b in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
                    nx, ny = cx+a, cy+b

                    if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and mapp[nx][ny] == cur and mapp[nx][ny] !=0:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        
            
            if isHigh:
                answer+=1

print(answer)
                

        
