from collections import deque

n, m = map(int, input().split())

mapp =[]

for _ in range(n):
    row = list(input())
    mapp.append(row)


cnt = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        mapp[i][j] = int(mapp[i][j])
        if mapp[i][j] ==0:
            cnt[i][j] = 1

check = [[False] * m for _ in range(n)]
group = {}
groupNumber = 0
for i in range(n):
    for j in range(m):
        if mapp[i][j] ==0 and not check[i][j]:
            check[i][j] = True
            q = deque([])
            curCnt = 0

            q.append((i, j))
            visit = []
            while q:
                cx, cy = q.popleft()
                visit.append((cx, cy))
                curCnt+=1
                
                for a, b in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nx, ny = cx+a, cy+b

                    if 0<=nx<n and 0<=ny<m and not check[nx][ny] and mapp[nx][ny]==0:
                        check[nx][ny] = True
                        q.append((nx, ny))

            for cx, cy in visit:
                cnt[cx][cy] = curCnt
                group[(cx, cy)] = groupNumber
            groupNumber+=1

groupCheck = {}
answer = [[0] *m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if mapp[i][j] ==1:
            groupCheck = {}
            answer[i][j] = 1
            for a, b in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nx, ny = i+a, j+b
                    if 0<=nx<n and 0<=ny<m and mapp[nx][ny]==0:
                        curGroupNumber = group[(nx, ny)]
                        if curGroupNumber not in groupCheck:
                            groupCheck[curGroupNumber] = True
                            answer[i][j]+=cnt[nx][ny]
            answer[i][j]%=10

for row in answer:
    print("".join(str(r) for r in row))


            

