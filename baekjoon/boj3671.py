import sys
from itertools import permutations
MAX = 10000000
input = sys.stdin.readline

sosu = [i for i in range(1, MAX+1)]

for i in range(2, MAX):
    if sosu[i] == 0: continue
    for j in range(2*i, MAX, i):
        if j < MAX:
            sosu[j] = 0

real_sosu = []
for i in range(2, MAX):
    if sosu[i] !=0:
        real_sosu.append(i)


c = int(input())
sosu[1] = 0
sosu[0] = 0
for _ in range(c):
    number = input().rstrip()
    answer = 0
    total = set()

    for i in range(1, len(number)+1):
        per = list(permutations(number, i))
        for p in per:
            p = "".join(p)
            total.add(int(p))

    total = list(total)

    for t in total:
        if sosu[t] !=0:
            answer+=1

    print(answer)