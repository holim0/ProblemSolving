import sys
input = sys.stdin.readline
s = input()

q = int(input())

cntMap = {}

for i in range(len(s)):
    cur  = s[i]

    if cur not in cntMap:
        cntMap[cur] = [i]
    else:
        cntMap[cur].append(i)


for _ in range(q):
    a, l, r = input().split()
    l, r = int(l), int(r)
    if a not in cntMap:
        print(0)
        continue

    start, end = 0, len(cntMap[a])-1
    
    while start<=end:

        mid = (start+end)//2

        if l<=cntMap[a][mid]:
            end = mid-1
        else:
            start = mid+1

    lower = start
    
    startnew, endnew = 0, len(cntMap[a])-1
    while startnew<=endnew:

        mid = (startnew+endnew)//2
        if r>=cntMap[a][mid]:
            startnew = mid+1
        else:
            endnew = mid-1
    
    upper = endnew
    print(upper-lower+1)