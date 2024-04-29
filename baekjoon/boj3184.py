from collections import deque
r, c = map(int, input().split())

mapp = []

for _ in range(r):
    row = list(input())
    mapp.append(row)

visited = [[False for _ in range(c)] for _ in range(r)]

sheep, wolf = 0, 0

for i in range(r):
    for j in range(c):
        if visited[i][j] or mapp[i][j] == "#": continue

        cur_sheep, cur_wolf = 0, 0

        

        visited[i][j] = True
        q = deque([(i, j)])

        while q:
            cx, cy = q.popleft()

            if mapp[cx][cy] == "o": cur_sheep+=1
            if mapp[cx][cy] == "v": cur_wolf+=1

            for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nx, ny = cx+a, cy+b
                
                if 0<=nx<r and 0<=ny<c and not visited[nx][ny] and mapp[nx][ny] != "#":
                    visited[nx][ny] = True
                    q.append((nx, ny))
        

        if cur_sheep >cur_wolf:
            sheep+=cur_sheep
        else:
            wolf+=cur_wolf

print(sheep, wolf)




