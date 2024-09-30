import sys

input = sys.stdin.readline


t = int(input())

for _ in range(t):
    n = int(input())

    mapp ={}
    phone =[]

    for _ in range(n):
        curNumber = input().rstrip()
        mapp[curNumber] = True
        phone.append(curNumber)
    
    isBreak = False
    for p in phone:
        cur = ""
        for nn in list(p):
            cur+=nn
            if cur in mapp and cur != p:
                isBreak = True
                print("NO")
                break
        if isBreak: break
    
    if not isBreak:
        print("YES")
