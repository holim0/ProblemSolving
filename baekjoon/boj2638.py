from collections import deque

n, m = map(int, input().split())
mapp = []

for _ in range(n):
    row = list(map(int, input().split()))
    mapp.append(row)

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def checkRange(x, y):

    if 0<=x<n and 0<=y<m:
        return True
    return False

isAir = [[False] * m for _ in range(n)]

def checkOverAir(x, y):

    cnt = 0

    for a, b in dir:
        nx, ny = x+a, y+b

        if checkRange(nx, ny) and isAir[nx][ny]:
            cnt+=1
    
    if cnt>=2:
        return True
    return False


time = 0

cheeze =[]

for i in range(n):
    for j in range(m):
        if mapp[i][j] ==1:
            cheeze.append((i, j))


def getAir():
    q = deque([])
    check = [[False for _ in range(m)] for _ in range(n)]

    q.append((0, 0))

    check[0][0] = True
    while q:
        cx, cy = q.popleft()
        isAir[cx][cy] = True
        for a, b in dir:
            nx, ny = cx+a, cy+b
        
            if checkRange(nx, ny) and not check[nx][ny] and mapp[nx][ny] == 0:
                check[nx][ny] = True
                q.append((nx, ny))



while len(cheeze):

    getAir()

    newCheeze = []

    for a, b in cheeze:
        if checkOverAir(a, b):
            mapp[a][b] = 0
        else:
            newCheeze.append((a, b))
    
    cheeze = newCheeze
    time+=1



print(time)
