from collections import deque
t = int(input())

INF = 1e10

def plusZero(cur):

    while len(cur)<4:
        cur = "0" + cur
    
    return cur


q = deque([])
check = [False] * 10000

def checkTrue(cur, nxtOrder):
    global q, check
    if not check[int(cur)]:
        
        check[int(cur)] = True
        q.append((cur, nxtOrder))


for _ in range(t):
    a, b = input().split()

    check = [False] * 10000

    check[int(a)] = True

    q = deque([])
    q.append((a, ""))

    while q:
        
        cur, order = q.popleft()
        
        cur = plusZero(cur)
        
        if int(cur) == int(b):
            print(order)
            break
        
        nxt = (2 * int(cur)) % 10000
        
        checkTrue(str(nxt), order+"D")
        
        nxt = int(cur)-1
        
        if nxt ==-1:
            nxt = 9999
        
        checkTrue(str(nxt), order+"S")

        nxt = cur[1:] + cur[0]
        
        checkTrue(str(nxt), order+"L")        

        nxt = cur[-1] + cur[:3]
        
        checkTrue(str(nxt), order+"R")  
    