slen, plen = map(int, input().split())

s = input()

cnt = list(map(int, input().split()))

indexMap = {
    "A": 0,
    "C": 1,
    "G": 2,
    "T": 3
}

curCnt = [0, 0, 0, 0]

p1, p2 = 0, plen-1

for i in range(p1, p2+1):
    sIdx = indexMap[s[i]]
    curCnt[sIdx]+=1


def isOver():
    global cnt
    global curCnt

    for i in range(4):
        if curCnt[i]<cnt[i]: return False
    
    return True

answer = 0
while p2<slen:


    if(isOver()): answer+=1

    p1Alpha = s[p1]
    idx = indexMap[p1Alpha]
    curCnt[idx]-=1
    
    if p2+1<slen:
        p2NextAlpha = s[p2+1]
        idx = indexMap[p2NextAlpha]
        curCnt[idx]+=1
    else:
        break

    p1+=1
    p2+=1

print(answer)