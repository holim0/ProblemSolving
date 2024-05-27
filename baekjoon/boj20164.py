n = input()

minAnswer = 1e10
maxAnswer = 1

def check(cur, value):
    global minAnswer
    global maxAnswer
    
    if len(cur)==1:
        if int(cur)%2==1:
            value+=1
        minAnswer = min(minAnswer, value)
        maxAnswer = max(maxAnswer, value)
        return
    
    curValue = value
    for c in cur:
        if int(c)%2==1:
            curValue+=1
    
    if len(cur)==2:
        newCur = int(cur[0]) + int(cur[1])
        check(str(newCur), curValue)
    
    elif len(cur)>=3:
        newCur = 0
        
        for i in range(1, len(cur)-1):
            for j in range(i+1, len(cur)):
                v1, v2, v3 = int(cur[:i]), int(cur[i:j]), int(cur[j:])
                newCur = str(v1+v2+v3)
                
                check(newCur, curValue)








check(n, 0)

print(minAnswer, maxAnswer)