import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
mapp =[]

for _ in range(n):
    like = list(map(int, input().split()))
    mapp.append(like)

answer = 0

number = [i for i in range(m)]

combi = list(combinations(number, 3))

for com in combi:
    a, b, c = com
    curSum = 0

    for i in range(n):
        value = max(mapp[i][a], max(mapp[i][b], mapp[i][c]))
        curSum+=value

    answer =max(answer, curSum)    


print(answer)
