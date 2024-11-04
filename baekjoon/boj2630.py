n = int(input())
mapp = []

for _ in range(n):
    row = list(map(int, input().split()))
    mapp.append(row)

white, blue = 0, 0 

def checkAllSame(sx, sy, curSize):
    global mapp
    
    if curSize==1: return True
    value = mapp[sx][sy]

    for i in range(sx, sx+curSize):
        for j in range(sy, sy+curSize):
            if mapp[i][j] != value: return False
    
    return True


def getSol(sx, sy, curSize):
    global blue
    global white
    if checkAllSame(sx, sy, curSize):
        if mapp[sx][sy] == 0: white+=1
        else: blue+=1

    else:
        half = curSize//2
        getSol(sx, sy, half)
        getSol(sx, sy+half, half)
        getSol(sx+half, sy, half)
        getSol(sx+half, sy+half, half)





getSol(0, 0, n)

print(white)
print(blue)