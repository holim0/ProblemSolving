import sys
input = sys.stdin.readline

s, c = map(int, input().split())

pa = []

for _ in range(s):
    p = int(input())
    pa.append(p)

s, e = 1, max(pa)

while s<=e:

    mid = (s+e)//2

    cnt = 0

    for p in pa:
        cnt += (p//mid)

    if cnt>=c:
        s = mid+1
    else:
        e = mid-1


paSum = sum(pa)
inputSum = e * c

print(paSum-inputSum)











