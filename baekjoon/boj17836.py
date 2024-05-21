from collections import deque
n, m, t = map(int, input().split())

mapp = []

for _ in range(n):
    row = list(map(int, input().split()))
    mapp.append(row)


check = [[[False for _ in range(n)] for _ in range(m)] for _ in range(n)]

q = deque([])

check[0][0][0] = True

q.append((0, 0, 0))

answer = 1e10
while q:
    cx, cy, time = q.popleft()
    
    if cx==n-1 and cy==m-1:
        answer = min(time, answer)

    for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nx, ny = cx+a, cy+b
        
        if 0<=nx<n and 0<=ny<m:
            if mapp[nx][ny] == 2 and not check[nx][ny][1]:
                check[nx][ny][1] = True
                q.append((nx, ny, time+1))
            
            elif mapp[nx][ny] ==1 and check[cx][cy][1] and not check[nx][ny][1]:
                check[nx][ny][1] = True
                q.append((nx, ny, time+1))
            
            elif mapp[nx][ny] == 0:
                if check[cx][cy][1] and not check[nx][ny][1]:
                    check[nx][ny][1] = True
                    q.append((nx, ny, time+1))
                
                if check[cx][cy][0] and not check[nx][ny][0]:
                    check[nx][ny][0] = True
                    q.append((nx, ny, time+1))

if answer <=t:
    print(answer)
else:
    print("Fail")