n = int(input())

info = []

for _ in range(n):
    s, e = map(int, input().split())
    info.append((s, e))

info.sort(key=lambda x: (x[1], x[0]))

curEnd = 0

answer = 0

for s, e in info:
    if s>=curEnd:
        answer+=1
        curEnd = e

print(answer)