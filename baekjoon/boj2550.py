import sys
input = sys.stdin.readline
n = int(input())

fromm = list(map(int, input().split()))
to = list(map(int, input().split()))

toDict = {}

for i in range(n):
    toDict[to[i]] = i

g = {}

idxList = []
for i in range(n):
    value = fromm[i]
    toIdx = toDict[value]
    idxList.append(toIdx)


lis = [idxList[0]]
record = [(-1, -1) for _ in range(n)]
record[0] = (to[idxList[0]], 0)

for i in range(1, n):
    curIdxValue = idxList[i]
    if lis[-1]<curIdxValue:
        lis.append(curIdxValue)
        record[i] = (to[curIdxValue], len(lis)-1)
        continue
    l, r = 0, len(lis)-1
    
    while l<=r:

        mid = (l+r)//2

        midValue = lis[mid]

        if midValue>curIdxValue:
            r = mid-1
        else:
            l = mid+1
    
    
    lis[l] = curIdxValue
    record[i] = (to[curIdxValue], l)
    
curLen = len(lis)-1
answer =[ ]

for i in range(len(record)-1, -1, -1):
    value, idx = record[i]
    if idx==curLen:
        answer.append(str(value))
        curLen-=1
    if curLen<0:
        break
    
answer.sort()

print(len(lis))
print(" ".join(answer))





