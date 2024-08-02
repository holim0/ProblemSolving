n, h = map(int, input().split())


up =[]
down = []


minBreak= 1e10
cnt = 0

hCnt = [0 for _ in range(h+1)]

for i in range(1, n+1):
    cur = int(input())
    if i%2==0:
        up.append(cur)
    else:
        down.append(cur)

up.sort()
down.sort()


def getCnt(h, isUp):


    s = 0
    curList = up if isUp else down
    e = len(up)-1 if isUp else len(down)-1
    
    while s<=e:

        mid = (s+e)//2

        if curList[mid]>=h:
            e = mid-1
        else:
            s = mid+1
    
    curCnt = len(curList) - (e+1)

    return curCnt


for i in range(1, h+1):
    curBreakCnt = getCnt(i, True) + getCnt(h-i+1, False)
    
    if curBreakCnt < minBreak:
        minBreak = curBreakCnt
        cnt = 1
    elif minBreak == curBreakCnt:
        cnt+=1

print(minBreak, cnt)