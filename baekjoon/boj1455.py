from collections import deque


n, m = map(int, input().split())

mapp = []

for _ in range(n):
    row = list(map(int, input()))
    mapp.append(row)

answer = 0

def checkDone():
    global mapp
    for i in range(n):
        for j in range(m):
            if mapp[i][j] == 1: return False

    return True

switch = {
    1: 0,
    0: 1
}


while not checkDone():
    
    backList =[]
    for i in range(n):
        for j in range(m):
            if mapp[i][j] ==1:
                backList.append((i, j))

    cx, cy = backList[-1]
    
    for i in range(cx+1):
        for j in range(cy+1):
            switchValue = switch[mapp[i][j]]
            mapp[i][j] = switchValue
    
    answer+=1

print(answer)