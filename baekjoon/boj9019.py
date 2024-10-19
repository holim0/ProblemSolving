from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    check ={}

    check[a] = True
    
    q = deque([])
    q.append((a, ""))

    while q:
        qlen = len(q)
        isBreak = False
        for i in range(qlen):
            cur, orderString = q.popleft()

            if cur == b:
                print(orderString)
                isBreak = True
                break

            nextValue = (2 * cur) % 10000

            if nextValue not in check:
                check[nextValue] = True
                q.append((nextValue, orderString + "D"))

            nextValue = cur-1
            if nextValue == -1:
                nextValue = 9999
            
            if nextValue not in check:
                check[nextValue] = True
                q.append((nextValue, orderString+"S"))

            nextValue = str(cur)
            while len(nextValue)<4:
                nextValue = "0" + nextValue

            nextValue = nextValue[1:] + nextValue[0]
            nextValue = int(nextValue)
            
            
            if nextValue not in check:
                check[nextValue] = True
                q.append((nextValue, orderString +"L"))
            

            nextValue = str(cur)
            while len(nextValue)<4:
                nextValue = "0" + nextValue

            
            nextValue = nextValue[-1] + nextValue[:-1]
            nextValue = int(nextValue)
        
            if nextValue not in check:
                check[nextValue] = True
                q.append((nextValue, orderString +"R"))
        
        if isBreak:
            break

