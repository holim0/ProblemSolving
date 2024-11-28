t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a_acc = [0, a[0]]
b_acc = [0, b[0]]

aSumMap = {}
bSumMap = {}

for i in range(1, n):
    a_acc.append(a_acc[-1]+a[i])

for i in range(1, m):
    b_acc.append(b_acc[-1] + b[i])

for i in range(1, n+1):
    for j in range(i, n+1):
        curSum = a_acc[j] - a_acc[i-1]
        aSumMap[curSum] = aSumMap.get(curSum, 0)
        aSumMap[curSum]+=1

for i in range(1, m+1):
    for j in range(i, m+1):
        curSum = b_acc[j] - b_acc[i-1]
        bSumMap[curSum] = bSumMap.get(curSum, 0)
        bSumMap[curSum]+=1

answer = 0

for key in aSumMap:
    sumValue = key
    sumCnt = aSumMap[key]

    targetSum = t - sumValue

    targetSumCnt = bSumMap.get(targetSum, 0)

    answer+= (sumCnt * targetSumCnt)

print(answer)
    