from collections import deque
n = int(input())

inCar = []

for _ in range(n):
    name = input()
    inCar.append(name)

answer = 0
already_out = []
idx = 0
for _ in range(n):
    outCar = input()

    curInCar= inCar[idx]
    
    while inCar[idx] in already_out:
        idx+=1


    curInCar = inCar[idx]

    if outCar != curInCar:
        answer+=1
        already_out.append(outCar)
    else:
        idx+=1
    
print(answer)