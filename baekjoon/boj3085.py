n = int(input())

mapp =[]

for _ in range(n):
    row = list(input())
    mapp.append(row)

answer =1


def getMax():
    global answer
    curCnt = 1
    
    for i in range(n):
        curCnt = 1
        for j in range(1, n):
            cur = mapp[i][j]
            prev = mapp[i][j-1]
            if cur==prev:
                curCnt+=1
                answer = max(answer, curCnt)
            else:
                answer = max(answer, curCnt)
                curCnt = 1
    
    
    for j in range(n):
        curCnt = 1
        for i in range(1, n):
            cur = mapp[i][j]
            prev =mapp[i-1][j]

            if cur==prev:
                curCnt+=1
                answer =max(answer, curCnt)
            else:
                answer =max(answer, curCnt)
                curCnt = 1

getMax()

for i in range(n):
    for j in range(n):
        if i+1<n and mapp[i+1][j] != mapp[i][j]:
            mapp[i+1][j], mapp[i][j] = mapp[i][j], mapp[i+1][j]
            getMax()
            mapp[i+1][j], mapp[i][j] = mapp[i][j], mapp[i+1][j]
        if i-1>=0 and mapp[i-1] != mapp[i][j]:
            mapp[i-1][j], mapp[i][j] = mapp[i][j], mapp[i-1][j]
            getMax()
            mapp[i-1][j], mapp[i][j] = mapp[i][j], mapp[i-1][j]



    
for j in range(n):
    for i in range(n):
        if j-1>=0 and mapp[i][j] != mapp[i][j-1]:
            mapp[i][j], mapp[i][j-1] = mapp[i][j-1], mapp[i][j]
            getMax()
            mapp[i][j], mapp[i][j-1] = mapp[i][j-1], mapp[i][j]
        if j+1<n and mapp[i][j] != mapp[i][j+1]:
            mapp[i][j], mapp[i][j+1] = mapp[i][j+1], mapp[i][j]
            getMax()
            mapp[i][j], mapp[i][j+1] = mapp[i][j+1], mapp[i][j]


print(answer)