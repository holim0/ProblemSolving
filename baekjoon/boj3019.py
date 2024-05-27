c, p = map(int, input().split())

mapp = list(map(int, input().split()))


def getAnswer(shape):
    answer = 0

    if shape ==1:
        answer+=c

        for i in range(c-3):
            if mapp[i] == mapp[i+1] and mapp[i+1] == mapp[i+2] and mapp[i+2] == mapp[i+3]:
                answer+=1
        
        return answer
    
    if shape==2:
        for i in range(c-1):
            if mapp[i] == mapp[i+1]:
                answer+=1

        return answer

    if shape==3:

        for i in range(c-1):
            if mapp[i] - mapp[i+1]==1:
                answer+=1
        
        for i in range(c-2):
            if mapp[i] == mapp[i+1] and mapp[i+2] - mapp[i+1] ==1:
                answer+=1
        
        return answer

    if shape==4:
        
        for i in range(c-2):
            if mapp[i] - mapp[i+1] ==1 and mapp[i+1] == mapp[i+2]:
                answer+=1
        
        for i in range(c-1):
            if mapp[i+1]-mapp[i]==1:
                answer+=1

        return answer

    if shape==5:
        for i in range(c-2):
            if mapp[i] == mapp[i+1] and mapp[i+1] == mapp[i+2]:
                answer+=1
            
            if mapp[i]-mapp[i+1] ==1 and mapp[i+2]-mapp[i+1] == 1:
                answer+=1
        
        for i in range(c-1):
            if mapp[i+1]-mapp[i] ==1:
                answer+=1
            if mapp[i]- mapp[i+1] ==1:
                answer+=1
        
        return answer

    if shape==6:
        for i in range(c-2):
            if mapp[i]==mapp[i+1] and mapp[i+1] == mapp[i+2]:
                answer+=1

            if mapp[i+1]-mapp[i] ==1 and mapp[i+1]== mapp[i+2]:
                answer+=1

        for i in range(c-1):
            if mapp[i] == mapp[i+1]:
                answer+=1

            if mapp[i] - mapp[i+1] ==2:
                answer+=1

        return answer
    
    if shape==7:
        for i in range(c-2):
            if mapp[i] == mapp[i+1] and mapp[i+1] == mapp[i+2]:
                answer+=1

            if mapp[i] == mapp[i+1] and mapp[i+1] -mapp[i+2] ==1:
                answer+=1

        for i in range(c-1):
            if mapp[i+1]-mapp[i]==2:
                answer+=1
            if mapp[i] == mapp[i+1]:
                answer+=1
        
        return answer
            

print(getAnswer(p))