from collections import deque

n, m = map(int, input().split())

mapp =[]

for _ in range(n):
    row = input()
    mapp.append(list(row))

check = [[False] * m for _ in range(n)]

q = deque([])

def findMe():
    global q, mapp, check
    for i in range(n):
        for j in range(m):
            if mapp[i][j] == "I":
                check[i][j] = True
                q.append((i, j))
                return
            
findMe()

answer = 0

while q:
    cx, cy = q.popleft()
    
    if mapp[cx][cy] == "P":
        answer+=1
    

    for a, b in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
        nx, ny = cx+a, cy+b

        if 0<=nx<n and 0<=ny<m and not check[nx][ny] and mapp[nx][ny] != "X":
            q.append((nx, ny))
            check[nx][ny] = True

if answer==0:
    print("TT")
else:
    print(answer)

