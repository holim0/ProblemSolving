n, m = map(int, input().split())

time =[]

for _ in range(n):
    t = int(input())
    time.append(t)

time.sort()

startTime = 1
endTime = time[-1] * m

answer = endTime


def getAvaliableCnt(curTime):

    cnt = 0

    for t in time:
        cnt+= (curTime//t)

    return cnt


while startTime<=endTime:

    midTime = (startTime+endTime)//2


    curAvaliableCnt = getAvaliableCnt(midTime)

    if curAvaliableCnt>=m:
        answer = min(answer, midTime)
        endTime = midTime-1
    else:
        startTime = midTime+1

print(answer)