import copy
n, m, d = map(int, input().split())

mapp = []

for _ in range(n):
    row = list(map(int, input().split()))
    mapp.append(row)


arrow = []
enemy = []
arrowPosCheck = [False for _ in range(m)]

for i in range(n):
    for j in range(m):
        if mapp[i][j] == 1:
            enemy.append((i, j))

enemy.sort(key=lambda x: (-x[0], x[1]))

def checkDone(curEnemy):

    if len(curEnemy) !=0: return False
    return True

def move(curEnemy):
    newEnemy = []
    for i in range(len(curEnemy)):
        x, y = curEnemy[i]
        if x+1<n:
            newEnemy.append((x+1, y))
    return newEnemy

def removeDead(curEnemy, dead):

    newCurEnemy = []

    for x, y in curEnemy:
        if (x, y) not in dead:
            newCurEnemy.append((x, y))

    return newCurEnemy

def findEnemy(curx, cury, curEnemy):

    minDist = 1e10
    target = []
    for ex, ey in curEnemy:
        dist = abs(curx-ex) + abs(cury-ey)
        if dist<=d:
            if minDist > dist:
                minDist = dist
                target = [(ex, ey)]
            elif minDist == dist:
                target.append((ex, ey))
    
    if len(target) == 0:
        return (-1, -1)
    target.sort(key=lambda x: (x[1]))
    return target[0]

answer = 0
def find(curIdx):
    global answer

    if len(arrow) ==3:
        deadCnt = 0
        curEnemy = copy.deepcopy(enemy)
        
        curEnemy.sort(key=lambda x: (-x[0], x[1]))

        while not checkDone(curEnemy):
            dead = []
            for arrowy in arrow:
                for ex, ey in curEnemy:
                    if 0<=ex<n and 0<=ey<m:
                        targetx, targety = findEnemy(n, arrowy, curEnemy)
                        if targetx == -1 and targety==-1: continue
                        if (targetx, targety) not in dead:
                        
                            deadCnt+=1
                            dead.append((targetx, targety))
                        break


            curEnemy = removeDead(curEnemy, dead)
            
            curEnemy = move(curEnemy)
            
            curEnemy.sort(key=lambda x: (-x[0], x[1]))
        answer = max(answer, deadCnt)




    for i in range(curIdx+1, m):
        arrow.append(i)
        find(i)
        arrow.pop()




for i in range(m-2):
    arrow.append(i)
    find(i)
    arrow.pop()

print(answer)