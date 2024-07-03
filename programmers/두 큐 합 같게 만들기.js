from collections import deque

def isSwap(q2, originQ1):
    
    for i in range(len(q2)):
        if q2[i] != originQ1[i]: return False
    return True

def solution(queue1, queue2):
    answer = 0
    
    q1Sum = sum(queue1)
    q2Sum = sum(queue2)

    q1 = deque(queue1)
    q2 = deque(queue2)
    
    if ((q1Sum+q2Sum)%2!=0):
        return -1
    while q1Sum!=q2Sum:
        if len(q1)==0 or len(q2)==0:
            return -1
        
        if answer>=len(queue1) *4:
            return -1
        
        if q1Sum>q2Sum:
            cur = q1.popleft()
            q1Sum-=cur
            q2.append(cur)
            q2Sum+=cur
            answer+=1
        else:
            cur = q2.popleft()
            q2Sum-=cur
            q1.append(cur)
            q1Sum+=cur
            answer+=1
        
    
    
    return answer