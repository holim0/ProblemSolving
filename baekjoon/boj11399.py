n = int(input())

lis = list(map(int, input().split()))

lis.sort()

accum = []

accum.append(lis[0])

for i in range(1, len(lis)):
    accum.append(accum[-1] + lis[i])

print(sum(accum))