import sys
n, k = map(int, input().split())

a = list(map(int, input().split()))

accum = []
answer =0
for i in range(len(a)):
    
    if accum[i] == k:
        answer +=1

        