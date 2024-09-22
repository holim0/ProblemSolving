import sys
input = sys.stdin.readline

n = int(input())
pos = []

total = 0
for _ in range(n):
    x, a = map(int, input().split())
    pos.append((x, a))
    total+=a

pos.sort()

cnt = 0

for x, a in pos:
    cnt+=a

    if cnt >= total/2:
        print(x)
        break


