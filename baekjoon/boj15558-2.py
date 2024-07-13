from collections import deque
import sys
input = sys.stdin.readline

n, k =map(int, input().split())

mapp = []

check = [[False for _ in range(n)] for _ in range(2)]

for _ in range(2):
    row = list(map(int, input().rstrip()))
    mapp.append(row)


q = deque([])

q.append((0, 0, 0))
check[0][0] = True

switch = {
    0: 1,
    1: 0
}

while q:
    cx, cy, time = q.popleft()
    if cy+1>=n or cy+k>=n:
        print(1)
        sys.exit()
    
    nx, ny = cx, cy+1

    if ny<n and not check[nx][ny] and mapp[nx][ny] !=0:
        check[nx][ny] = True
        q.append((nx, ny, time+1))
    
    
    nx, ny = switch[cx], cy+k

    if ny<n and not check[nx][ny] and mapp[nx][ny] !=0:
        check[nx][ny] = True
        q.append((nx, ny, time+1))
    
    nx, ny = cx, cy-1
    if ny>=0 and ny<n and not check[nx][ny] and mapp[nx][ny] !=0 and time<ny:
        check[nx][ny] = True
        q.append((nx, ny, time+1))


print(0)




