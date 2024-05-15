from collections import deque

n = int(input())
answer = 1

mapp =[]
max_height = 0
min_height = 200
for _ in range(n):
    row = list(map(int, input().split()))
    max_height = max(max_height, max(row))
    min_height = min(min_height, min(row))
    
    mapp.append(row)


for k in range(min_height, max_height):

    check = [[False for _ in range(n)] for _ in range(n)]
    
    curh = k
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not check[i][j] and mapp[i][j]>curh:
                check[i][j] = True

                q = deque([])
                q.append((i, j))

                while q:
                    cx, cy = q.popleft()
                    
                    for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        nx, ny = cx+a, cy+b

                        if 0<=nx<n and 0<=ny<n and not check[nx][ny] and mapp[nx][ny] > curh:
                            check[nx][ny] = True
                            q.append((nx, ny))


                cnt+=1

    answer = max(answer, cnt)

print(answer)
