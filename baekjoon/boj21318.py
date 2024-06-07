import sys
input = sys.stdin.readline
n = int(input())

paper = list(map(int, input().split()))

q = int(input())

acc =[]

for i in range(n):
    if i==0:
        acc.append(0)
    else:
        if paper[i]<paper[i-1]:
            acc.append(acc[-1]+1)
        else:
            acc.append(acc[-1])

for _ in range(q):
    x, y = map(int, input().split())
    x, y = x-1, y-1

    if x==y:
        print(0)
    else:
        print(acc[y]-acc[x])