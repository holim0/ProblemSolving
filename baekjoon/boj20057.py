n = int(input())

mapp =[]

for _ in range(n):
    row = list(map(int, input().split()))
    mapp.append(row)


answer = 0

dir = {
    0: (0, -1),
    1: (1, 0),
    2: (0, 1),
    3: (-1, 0)
}

sandMap = {
    0: [(-2, 0, 2), (-1, -1, 10),(-1, 0, 7), (-1, 1, 1), (0, -2, 5), (2, 0, 2), (1, -1, 10), (1, 0, 7), (1, 1, 1)],
    1: [(-1, -1, 1), (-1, 1, 1), (0, -2, 2), (0, -1, 7), (0, 1, 7),(0, 2, 2), (1, -1, 10), (1, 1, 10), (2, 0, 5) ],
    2: [(-2, 0, 2), (-1, -1, 1), (-1, 0, 7), (-1, 1, 10), (0, 2, 5), (2, 0, 2), (1, -1, 1), (1, 0, 7), (1, 1, 10)],
    3: [(-2, 0, 5), (-1, -1, 10), (-1, 1, 10), (0, -2, 2),(0, -1, 7), (0, 1, 7), (0, 2, 2), (1, -1, 1), (1, 1, 1)]
}

def moveAndGetSand(cx, cy, curdir):
    global mapp
    global answer
    dira, dirb = dir[curdir]
    sandMapList = sandMap[curdir]

    curSand = mapp[cx][cy]
    movex, movey = cx+dira, cy+dirb

    minusSand = 0
    for a, b, ratio in sandMapList:
        
        nx, ny = cx+a, cy+b
        
        if 0<=nx<n and 0<=ny<n:
            mapp[nx][ny] += ((curSand * ratio)//100)
            minusSand += (curSand * ratio)//100
        else:
            answer+=((curSand * ratio)//100)
            minusSand += (curSand * ratio)//100

    if 0<=movex<n and 0<=movey<n:
        mapp[movex][movey]+= (curSand - minusSand)
    else:
        answer+= (curSand - minusSand)
    
        
    mapp[cx][cy] = 0



curx, cury = n//2, n//2

cnt = 0
def moveTone():
    global curx, cury
    a, b = dir[cnt%4]

    moveValue = cnt//2 + 1
    for _ in range(moveValue):
        curx, cury = curx+a, cury+b
        if curx<0 or cury<0:
            return True
        moveAndGetSand(curx, cury, cnt%4)

    return False

while True:

    if curx ==0 and cury ==0: 
        break
    
    if(moveTone()): break

    cnt+=1
    
    


print(answer)

