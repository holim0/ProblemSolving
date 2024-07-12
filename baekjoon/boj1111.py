import sys
n = int(input())
number = list(map(int, input().split()))

answer = []


if len(number) ==1 :
    print("A")
    sys.exit()

def isAnswer(cura, curb):
    for i in range(1, len(number)):
        curNumber = number[i]
        preNumber = number[i-1]
        if(curNumber != (preNumber * cura) + curb):
            return
    
    value = number[-1] *cura + curb
    if value not in answer: 
        answer.append(value)

for a in range(-200, 201):

    cura = a
    curb = number[1] - number[0] * a

    isAnswer(cura, curb)

if len(answer) ==0:
    print("B")

elif len(answer) > 1:
    print("A")
else:
    print(answer[0])




