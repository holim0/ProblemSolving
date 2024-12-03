from collections import deque

n, m = map(int, input().split())

mapp =[]

for _ in range(n):
    row = list(input())
    mapp.append(row)

answer = 0

dir = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}

check = [[-1] * m for _ in range(n)]

curCheckValue = 1

for i in range(n):
    for j in range(m):
        if check[i][j] == -1:
            check[i][j] = curCheckValue

            q = deque([])
            q.append((i, j))


            while q:
                x, y = q.popleft()

                curDir = dir[mapp[x][y]]

                nx, ny = x+curDir[0], y+curDir[1]
                
                if check[nx][ny] ==-1:
                    check[nx][ny] = curCheckValue
                    q.append((nx, ny))
                else:
                    if check[nx][ny] == curCheckValue:
                        answer+=1
                        break

                    if check[nx][ny]< curCheckValue:
                        break

            curCheckValue+=1


print(answer)