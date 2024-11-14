import sys
n = int(input())

a = list(map(int, input().split()))

m = int(input())

b = list(map(int, input().split()))



maxValue = 0

answer =[ ]
while a and b:
    curMaxValue = 0
    
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]==b[j]:
                curMaxValue = max(curMaxValue, a[i])
    
    if curMaxValue ==0: break
    for i in range(len(a)):
        if a[i] == curMaxValue:
            a = a[i+1:]
            break

    for j in range(len(b)):
        if b[j] == curMaxValue:
            b = b[j+1:]
            break
        
    
    answer.append(curMaxValue)
print(len(answer))
if answer:
    for aa in answer:
        print(aa, end=" ")

