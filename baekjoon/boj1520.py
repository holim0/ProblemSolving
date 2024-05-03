from collections import deque

m, n = map(int, input().split())

answer = 0
mapp =[]
for _ in range(m):
    row = list(map(int, input().split()))
    mapp.append(row)


def find(x, y, visited):
    global answer
    
    if x == m-1 and y == n-1:
        answer+=1
        return 
    

    for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nx, ny = x+a, y+b

        if 0<=nx<m and 0<=ny<n and not visited[nx][ny] and mapp[nx][ny]<mapp[x][y]:
            visited[nx][ny] = True
            find(nx, ny, visited)
            visited[nx][ny] = False

visited = [[False for _ in range(n)] for _ in range(m)]

find(0, 0, visited)

print(answer)