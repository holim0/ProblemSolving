from collections import deque

n = int(input())


mapp =[]
check = [[1e10] * n for _ in range(n)]

for _ in range(n):
    row = list(map(int, input()))
    mapp.append(row)

q = deque([])

q.append((0, 0, 0))
check[0][0] = 0

while q:
    cx, cy, breakCnt = q.popleft()


    for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nx, ny = cx+a, cy+b

        if 0<=nx<n and 0<=ny<n:
            if mapp[nx][ny] == 0:
                if check[nx][ny] > breakCnt+1:
                    check[nx][ny] = breakCnt+1
                    q.append((nx, ny, breakCnt+1))
            else:
                if check[nx][ny] > breakCnt:
                    check[nx][ny] = breakCnt
                    q.append((nx, ny, breakCnt))


print(check[n-1][n-1])