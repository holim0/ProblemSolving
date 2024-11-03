import sys
from collections import deque
n = int(input())

f = list(map(int, input().split()))
kind = 0

check = [0] * 10

for ff in f:
    if check[ff] ==0:
        kind+=1
    check[ff]+=1

if kind<=2:
    print(len(f))
    sys.exit(0)

check = [0] * 10

l, r = 0, 1
answer = 0
check[f[0]]+=1
curKind = 1

while r<len(f):
    
    r_value = f[r]

    check[r_value]+=1

    if check[r_value]==1: curKind+=1

    
    while l<r and curKind>2:
        check[f[l]]-=1
        if check[f[l]]==0:
            curKind-=1
        l+=1
    
    answer = max(answer, r-l+1)
    r+=1





print(answer)