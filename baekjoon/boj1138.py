import sys
n = int(input())

memory = list(map(int, input().split()))

order =[i for i in range(1, n+1)]


check = [False for _ in range(n+1)]

def getOrder(curOrder):
    
    if len(curOrder) == n:
        if(checkAnswer(curOrder)):
            print(" ".join(str(num) for num in curOrder))
            sys.exit()
        return 


    for o in order:
        
        if not check[o]:
            check[o] = True
            curOrder.append(o)
            getOrder(curOrder)
            curOrder.pop()
            check[o] = False





def checkAnswer(curOrder):

    curMemory = [0 for _ in range(n)]
    
    for i in range(len(curOrder)):
        curOrderValue = curOrder[i]
        curOrderValue = int(curOrderValue)
        if i==0:
            curMemory[curOrderValue-1] = 0
        else:
            cnt = 0

            for j in range(i):
                if int(curOrder[j])>curOrderValue:
                    cnt+=1
            
            curMemory[curOrderValue-1] = cnt
    
   
    for i in range(n):
        if curMemory[i] != memory[i]: return False
    
    return True


getOrder([])


