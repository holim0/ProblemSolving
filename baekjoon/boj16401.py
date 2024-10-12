m, n = map(int, input().split())

candyLen = list(map(int, input().split()))


l, r = 1, max(candyLen)


def isOk(curCandyLen):

    cnt = 0
    
    for c in candyLen:
        cnt+= (c//curCandyLen)

    return cnt>=m

answer = 0
while l<=r:
    mid = (l+r)//2

    if isOk(mid):
        answer = max(answer, mid)
        l = mid+1
    else:
        r = mid-1
    

print(answer)