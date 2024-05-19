n = int(input())

info = []
popul = 0
for _ in range(n):
    x, a = map(int, input().split())
    info.append((x, a))
    popul+=a

info.sort()

mid = popul/2
cur = 0
for i in info:
    x, a = i

    cur+=a
    if cur>=mid:
        print(x)
        break

