n = int(input())
k = int(input())

sensor = list(map(int, input().split()))

sensor = sorted(sensor)

gap = []

for i in range(len(sensor)-1):
    gap.append(sensor[i+1] - sensor[i])

gap = sorted(gap, reverse=True)

answer = sum(gap[k-1:])

print(answer)