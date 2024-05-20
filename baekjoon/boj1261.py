from collections import deque

m, n = map(int, input().split())

mapp = []

for _ in range(n):
    row = list(map(int, input()))
    mapp.append(row)

cnt = [[[1e10 for _ in range(2)] for _ in range(m)] for _ in range(n)]

q = deque([])


q.append((0, 0, 0))
cnt[0][0][0] = 0
cnt[0][0][1] = 0

answer = 1e10
while q:
    cx, cy, breakCnt = q.popleft()

    if cx==n-1 and cy==m-1:
        answer = min(answer, breakCnt)
        continue

    for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nx, ny = cx+a, cy+b
        
        if 0<=nx<n and 0<=ny<m:
            if mapp[nx][ny]==0:
                if cnt[nx][ny][0] > breakCnt:
                    cnt[nx][ny][0] = breakCnt
                    q.append((nx, ny, breakCnt))
            else:
                if cnt[nx][ny][1] > breakCnt+1:
                    cnt[nx][ny][1] = breakCnt +1
                    q.append((nx, ny, breakCnt+1))

print(answer)


