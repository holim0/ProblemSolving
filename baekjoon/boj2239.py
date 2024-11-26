import sys
mapp =[]

for _ in range(9):
    row = list(input())
    mapp.append(row)

for i in range(9):
    for j in range(9):
        mapp[i][j] = int(mapp[i][j])

emptyPos = []

for i in range(9):
    for j in range(9):
        if mapp[i][j] == 0:
            emptyPos.append((i, j))

startPos = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]

def isCanInsert(x, y, curMapp, value):
    
    for j in range(9):
        curValue = curMapp[x][j]
        if curValue ==0 :continue
        if curValue == value: return False

    for i in range(9):
        curValue = curMapp[i][y]
        if curValue ==0 :continue
        if curValue == value: return False

    sx, sy = (x//3) *3,  (y//3) * 3 

    for i in range(sx, sx+3):
        for j in range(sy, sy+3):
            curValue = curMapp[i][j]
            if curValue ==0 :continue
            if curValue == value: return False

    return True

def solve(idx):
    global mapp, emptyPos
    
    if idx == len(emptyPos):
        for i in range(9):
            print("".join(str(s) for s in mapp[i]))
        sys.exit()
    

    cx, cy = emptyPos[idx]
    
    for value in range(1, 10):
        if(isCanInsert(cx, cy, mapp, value)):
            mapp[cx][cy] = value
            solve(idx+1)
            mapp[cx][cy] = 0

solve(0)

