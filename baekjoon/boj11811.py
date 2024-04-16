import sys
input = sys.stdin.readline

n = int(input())

number = [["0" for _ in range(31)] for _ in range(n+1)]
mapp = []

answer = [0 for _ in range(n+1)]
for _ in range(n):
    row = list(map(int, input().split()))
    mapp.append(row)

def numTobin(number):
    binString =  format(number, "b")
    return binString[::-1]



for i in range(n):
    for j in range(n):
        if mapp[i][j] == 0: continue
        binString = numTobin(mapp[i][j])
        for k in range(len(binString)):
        
            if int(binString[k]) == 1:
                number[i+1][k] = "1"
                number[j+1][k] = "1"
answer = []
for i in range(1, n+1):
    value = "".join(number[i])
    value = "0b" + value[::-1]
    value = int(value, 2)
    answer.append(str(value))

print(" ".join(answer))
