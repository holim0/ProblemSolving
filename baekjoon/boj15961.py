import sys
from collections import deque

input = sys.stdin.readline

n, d, k, c = map(int, input().split())

belt = []

for _ in range(n):
    cur = int(input())
    belt.append(cur)

answer = 0

s, e = 0, k-1

cnt = [0 for _ in range(d+1)]

curkind = 0
for i in range(s, e+1):
    value = belt[i]
    cnt[value]+=1
    if cnt[value]==1:
        curkind+=1

answer = max(answer, curkind)


while s<n-1:
    
    startValue = belt[s]
    nextValue = belt[(e+1)%n]

    cnt[startValue]-=1
    if cnt[startValue] == 0:
        curkind-=1
    cnt[nextValue]+=1


    if cnt[nextValue] ==1:
        curkind+=1

    if cnt[c]==0:
        answer = max(answer, curkind+1)
    else:
        answer = max(answer, curkind)
    
    s+=1
    e+=1

    
print(answer)

