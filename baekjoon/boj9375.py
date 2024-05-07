import sys
from itertools import combinations
input = sys.stdin.readline
t = int(input())

    

for _ in range(t):
    mapp = {}
    n = int(input())
    answer = 1
    for _ in range(n):
        name, kind = input().split()
        if kind not in mapp:
            mapp[kind] = [name]
        else:
            mapp[kind].append(name)

    for key in mapp:
        answer *= (len(mapp[key])+1)
    answer-=1
    
    

    print(answer)
    
