from collections import deque

island = []

answer = 1e10


n = int(input())

mapp = []

for _ in range(n):
    row = list(map(int, input().split()))
    mapp.append(row)

check = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if mapp[i][j]==0 or check[i][j]: continue

        q = deque([(i, j)])
        curIsLand = []
        
        check[i][j] = True

        while q:
            cx, cy = q.popleft()
            curIsLand.append((cx, cy))
            
            for a, b in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = cx+a, cy+b

                if 0<=nx<n and 0<=ny<n and not check[nx][ny] and mapp[nx][ny] == 1:
                    check[nx][ny] = True
                    q.append((nx, ny))


        island.append(curIsLand)


for i in range(len(island)-1):
    curIsLand  = island[i]
    for j in range(i+1, len(island)):
        nextIsLand = island[j]

        for a in range(len(curIsLand)):
            fx, fy = curIsLand[a]
            for b in range(len(nextIsLand)):
                ex, ey = nextIsLand[b]
                
                answer = min(answer, abs(fx-ex)+abs(fy-ey))

print(answer-1)