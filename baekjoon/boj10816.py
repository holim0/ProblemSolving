import sys
input = sys.stdin.readline
n = int(input())

card = []


card = list(map(int, input().split()))
    
m = int(input())

target = list(map(int, input().split()))


dict = {}

for c in card:
    if c not in dict:
        dict[c] = 1
    else:
        dict[c] +=1

answer = []

for t in target:
    if t not in dict:
        answer.append(str(0))
    else:
        answer.append(str(dict[t]))

real_answer= " ".join(answer)

print(real_answer)