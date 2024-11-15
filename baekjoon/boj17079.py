import sys
n = int(input())

mapp =[]

for _ in range(n):
    row = list(map(int, input().split()))
    mapp.append(row)

check = [[[-1] * 4 for _ in range(n)] for _ in range(n)]

if mapp[n-1][n-1] == 1:
    print(0)
    sys.exit(0)

def getDir(sx, sy, ex, ey):

    if sx==ex: return 1

    if sy==ey: return 2

    return 3

def isValidPos(x, y):

    global mapp

    if 0<=x<n and 0<=y<n and mapp[x][y] == 0: return True

    return False

def move(sx, sy, ex, ey):
    global check
    dir = getDir(sx, sy, ex, ey)
    if check[ex][ey][dir] > 0:
        return check[ex][ey][dir]
    
    if ex==n-1 and ey==n-1:
        return 1
    
    

    check[ex][ey][dir] = 0
    if getDir(sx, sy, ex, ey) == 1:
        if isValidPos(ex, ey+1):
            check[ex][ey][dir]+=move(ex, ey, ex, ey+1)
            
        
        if isValidPos(ex+1, ey+1) and isValidPos(ex, ey+1) and isValidPos(ex+1, ey):
            
            check[ex][ey][dir]+=move(ex, ey, ex+1, ey+1)
            
            

    elif getDir(sx, sy, ex, ey) == 2:
        if isValidPos(ex+1, ey):
    
            check[ex][ey][dir]+=move(ex, ey, ex+1, ey)
            

        if isValidPos(ex+1, ey+1) and isValidPos(ex, ey+1) and isValidPos(ex+1, ey):
            
            check[ex][ey][dir]+=move(ex, ey, ex+1, ey+1)
            

    else:
        if isValidPos(ex, ey+1):
            
            check[ex][ey][dir]+=move(ex, ey, ex, ey+1)
            

        if isValidPos(ex+1, ey):
            
            check[ex][ey][dir]+=move(ex, ey, ex+1, ey)
            

        if isValidPos(ex+1, ey+1) and isValidPos(ex, ey+1) and isValidPos(ex+1, ey):
            
            check[ex][ey][dir]+=move(ex, ey, ex+1, ey+1)
            

    return check[ex][ey][dir]


print(move(0, 0, 0, 1))