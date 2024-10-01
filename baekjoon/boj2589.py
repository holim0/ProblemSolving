from collections import deque

l, w = map(int, input().split())

mapp =[]

for _ in range(l):
    row = list(input())
    mapp.append(row)

answer = 0

for i in range(l):
    for j in range(w):
        if mapp[i][j] == "W": continue

        q = deque([])
        check = [[False for _ in range(w)] for _ in range(l)]
        check[i][j] = True
        q.append((i, j, 0))
        curDist = 0
        while q:
            cx, cy, dist = q.popleft()
            
            answer =max(answer, dist)
            for a, b in [(1, 0),(0, 1), (-1, 0), (0, -1)]:
                nx, ny = cx+a, cy+b

                if 0<=nx<l and 0<=ny<w and mapp[nx][ny] == "L" and not check[nx][ny]:
                    check[nx][ny] = True
                    q.append((nx, ny, dist+1))
        

print(answer)