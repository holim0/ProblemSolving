n, m, l = map(int, input().split())

pos = list(map(int, input().split()))

pos.sort()
pos.insert(0, 0)
pos.append(l)
check = {}
answer = l

left, right = 1, l


def insertRest(curGap):

    curCnt = 0
    
    for i in range(len(pos)-1):
        gap = pos[i+1]-pos[i]-1
        
        if gap>=curGap:
            curCnt+= (gap//curGap)
    
    return curCnt

    

while left<=right:

    mid = (left+right)//2
    
    if insertRest(mid)>m:
        left = mid+1
    else:
        answer = min(answer, mid)
        right = mid-1
    
print(answer)