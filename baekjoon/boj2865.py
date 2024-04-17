import sys
from itertools import combinations
input = sys.stdin.readline

n, m, k = map(int, input().split())
answer = 0
pick = 0

check = [False for _ in range(n+1)]

pair = []

for i in range(m):
    ab = list(input().split())
    
    for j in range(0, len(ab), 2):
        number = int(ab[j])
        value = float(ab[j+1])
        pair.append((value, number))

pair = sorted(pair, reverse=True)



for p in pair:
    score, number = p
    if pick == k: break

    if not check[number]:
        check[number] = True
        answer+=score
        pick+=1

print(round(answer, 1))