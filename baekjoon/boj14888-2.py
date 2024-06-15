n = int(input())

number = list(map(int, input().split()))

plus, minus, mul, div = map(int, input().split())

maxAnswer = -1e10
minAnswer = 1e10

def getSol(idx, curPlus, curMinus, curMul, curDiv, value):
    global maxAnswer
    global minAnswer
    if idx==n-1:
        
        maxAnswer = max(maxAnswer, value)
        minAnswer = min(minAnswer, value)
        return 
    

    if curPlus >0:
        getSol(idx+1, curPlus-1, curMinus, curMul, curDiv, value+number[idx+1])

    if curMinus>0:
        getSol(idx+1, curPlus, curMinus-1, curMul, curDiv, value-number[idx+1])
    if curMul>0:
        getSol(idx+1, curPlus, curMinus, curMul-1, curDiv, value*number[idx+1])
    if curDiv>0:
        curValue = value
        nxtValue = 0
        if curValue<0:
            curValue*=-1
            nxtValue = curValue//number[idx+1]
            nxtValue *=-1

        else:
            nxtValue = curValue//number[idx+1]
        
        getSol(idx+1, curPlus, curMinus, curMul, curDiv-1, nxtValue)


getSol(0, plus, minus, mul, div, number[0])

print(maxAnswer)
print(minAnswer)

