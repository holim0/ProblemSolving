n,targetS = map(int, input().split())

value = list(map(int, input().split()))

acc = [value[0]]

for i in range(1, len(value)):
    acc.append(acc[-1]+ value[i])

minLen = 1e10
s, e = 0, 0

while s<=e and e<n:

    curSum = 0

    if s==0:
        curSum = acc[e]
    else:
        curSum = acc[e] - acc[s-1]

    if curSum >=targetS:
        minLen = min(minLen, e-s+1)
        s+=1
    else:
        e+=1


if minLen == 1e10:
    print(0)
else:
    print(minLen)