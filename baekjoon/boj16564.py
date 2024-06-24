n, k = map(int, input().split())

level = []

for _ in range(n):
    l = int(input())
    level.append(l)

level.sort()

s, e = level[0], level[-1] + k


def getLevel(goal):

    cnt = 0

    for l in level:
        if l<goal:
            cnt+= (goal-l)

    return cnt

while s<=e:

    mid = (s+e)//2

    curCnt = getLevel(mid)

    if curCnt<=k:
        s = mid+1
    else:
        e = mid-1
print(e)