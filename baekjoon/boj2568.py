n = int(input())

g = []
MAX = 0
mapp = {}
for _ in range(n):
    a, b = map(int, input().split())
    g.append((a, b))
    mapp[b] = a
    MAX = max(MAX, max(a, b))

tmp = [-1] * (MAX+1)

for a, b in g:
    tmp[a] = b

link = []

for value in tmp:
    if value !=-1:
        link.append(value)

posStore = [-1] * n
lis = [link[0]]

posStore[0] = 0

for i in range(1, n):
    
    curValue = link[i]
    

    if curValue>lis[-1]:
        lis.append(curValue)
        posStore[i] = len(lis)-1
        continue

    l, r = 0, len(lis)-1

    while l<=r:
        mid = (l+r)//2

        if lis[mid]>curValue:
            r = mid-1
        else:
            l = mid+1
    
    posStore[i] = l
    lis[l] = curValue


curIdx = len(lis)-1
increaseListIdx = []
for i in range(n-1, -1, -1):
    if posStore[i] == curIdx:
        increaseListIdx.append(i)
        curIdx-=1

increaseListIdx.sort()

check = {}

for idx in increaseListIdx:
    value = link[idx]
    mappingValue = mapp[value]
    check[mappingValue] = True

answer= []

for a, b in g:
    if a not in check:
        answer.append(a)

answer.sort()



print(n-len(lis))

for a in answer:
    print(a)


