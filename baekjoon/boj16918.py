r, c, n = map(int, input().split())

mapp =[]

for _ in range(r):
    row = list(input())
    mapp.append(row)

bombTime = [[-1 for _ in range(c)] for _ in range(r)]

for i in range(r):
    for j in range(c):
        if mapp[i][j] == "O":
            bombTime[i][j] = 0


def plant(plantTime):
    global bombTime
    for i in range(r):
        for j in range(c):
            if mapp[i][j]== "." and  bombTime[i][j] == -1:
                mapp[i][j] = "O"
                bombTime[i][j] = plantTime


    
def explosion(curTime):
    global bombTime
    explosionList = []
    for i in range(r):
        for j in range(c):
            if mapp[i][j] =="O" and curTime - bombTime[i][j] ==3:
                explosionList.append((i, j))

                for a, b in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nx, ny = i+a, j+b
                    if 0<=nx<r and 0<=ny<c:
                        explosionList.append((nx, ny))
    for a, b in explosionList:
        mapp[a][b] = "."
        bombTime[a][b] = -1

for curTime in range(2, n+1):
    
    if curTime%2==0:
        plant(curTime)
    if curTime%2==1:
        explosion(curTime)




for i in range(r):
    print("".join(mapp[i]))