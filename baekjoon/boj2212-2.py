n = int(input())
k = int(input())

pos = list(map(int, input().split()))
pos.sort()

gap = []

for i in range(0,n-1):
    gap.append(pos[i+1] - pos[i])

gap = sorted(gap, reverse=True)

answer = sum(gap[k-1:])

print(answer)