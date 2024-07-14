w, h = map(int, input().split())


dist = [[[[-1] * 3 for _ in range(3)] for _ in range(w+1)] for _ in range(h+1)]
mod = 100000

# 0이 북, 1이 동
def getAnswer(cx, cy, curdir, isChangeDir):

    if cx==h and cy==w:
        return 1
    
    if dist[cx][cy][curdir][isChangeDir] != -1:
        return dist[cx][cy][curdir][isChangeDir]

    dist[cx][cy][curdir][isChangeDir] = 0
    curCnt = 0
    

    if cx+1<=h:
        if curdir == 0 or curdir == -1:
            curCnt+= getAnswer(cx+1, cy, 0, 0)
        elif curdir == 1:
            if isChangeDir ==0:
                curCnt +=getAnswer(cx+1, cy, 0, 1)
        
    if cy+1<=w:
        if curdir == 1 or curdir == -1:
            curCnt+= getAnswer(cx, cy+1, 1, 0)
        elif curdir == 0:
            if isChangeDir == 0:
                curCnt +=getAnswer(cx, cy+1, 1, 1)

    
    dist[cx][cy][curdir][isChangeDir] = curCnt % mod
    return dist[cx][cy][curdir][isChangeDir]


print(getAnswer(1, 1, -1, 0) % 100000)