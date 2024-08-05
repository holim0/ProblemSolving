import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n= int(input())
    info= []
    answer = 0
    for _ in range(n):
        a, b = map(int, input().split())
        info.append((a, b))
    
    info.sort()
    minValue = 1e10
    
    for i in range(len(info)):
        a, b = info[i]
        if minValue>b:
            minValue = b
            answer+=1
    
    print(answer)

