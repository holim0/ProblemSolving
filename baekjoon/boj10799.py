import sys
input = sys.stdin.readline
info = input().rstrip()


stack = []
mak = 0
answer = 0 
for i in range(len(info)):
    cur = info[i]
    if cur == "(":
        stack.append((cur, i))
        mak+=1
    else:
        top, topidx = stack[-1]
        if topidx+1 == i and top == "(":
            mak-=1
            answer+=mak
            stack.pop()
            continue
            
        if top == "(":
            stack.pop()
            answer+=1
            mak-=1

print(answer)
        
        
