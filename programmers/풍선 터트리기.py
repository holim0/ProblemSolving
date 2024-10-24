def solution(a):
    answer = 0
    if len(a) ==1 or len(a) ==2: return len(a)
    
    
    rightMin = [1e10] * len(a)
    leftMin = [1e10] * len(a)
    curMin = a[-1]
    for i in range(len(a)-1, -1, -1):
        curMin = min(curMin, a[i])
        rightMin[i] = curMin
    
    curMin = a[0]
    
    for i in range(len(a)):
        curMin = min(curMin, a[i])
        leftMin[i] = curMin
    
    for i in range(1, len(a)-1):
        cur = a[i]
        leftMinValue = leftMin[i-1]
        rightMinValue = rightMin[i+1]
        
        if cur<leftMinValue or cur<rightMinValue:
            answer+=1
        
        
        
    return answer+2