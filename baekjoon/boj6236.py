n, m = map(int, input().split())

cost = []

for _ in range(n):
    c = int(input())
    cost.append(c)

def getCnt(cur):

    cnt = 1
    curMoney = cur
    for c in cost:
        if c<=curMoney:
            curMoney-=c
        else:
            curMoney = cur
            cnt+=1
            if curMoney<c:
                return -1
            curMoney-=c

    return cnt
    
s, e = 1, sum(cost)
answer= 1e10
while s<=e:

    mid = (s+e)//2

    curCnt = getCnt(mid)

    if curCnt == -1:
        s = mid+1
        continue

    if curCnt>m:
        
        s = mid+1
    else:
        answer = min(answer, mid)
        e = mid-1

print(answer)
