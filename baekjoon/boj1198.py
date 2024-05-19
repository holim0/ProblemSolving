from itertools import combinations

n = int(input())

pos = []
answer = 0
for _ in range(n):
    x, y = map(int, input().split())
    pos.append((x, y))


def getSize(c):
    global answer
    x1, y1 = c[0]
    x2, y2 = c[1]
    x3, y3 = c[2]

    cal1 = x1 * y2 + x2 * y3 + x3 * y1
    cal2 = x2 * y1 + x3 * y2 + x1 * y3

    size = abs(cal1-cal2)/2
    answer = max(answer, size)

combi = list(combinations(pos, 3))

for c in combi:
    getSize(c)

print(answer)