from collections import deque
import sys
input = sys.stdin.readline
n, k = map(int, input().split())

mapp = []

for _ in range(n):
    row = list(map(int, input().split()))
    mapp.append(row)

s,x,y = map(int, input().split())

check = [[0] * n for _ in range(n)]

q= []

for i in range(n):
    for j in range(n):
        if mapp[i][j] !=0:
            q.append((mapp[i][j], i,j, 0))
            check[i][j] = mapp[i][j]

q.sort()

q = deque(q)

while q:
    curValue, cx, cy, curTime = q.popleft()
    if curTime == s:
        break
    for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nx, ny = cx+a, cy+b

        if 0<=nx<n and 0<=ny<n and check[nx][ny] ==0:
            check[nx][ny] = curValue
            q.append((curValue, nx, ny, curTime+1))


print(check[x-1][y-1])
