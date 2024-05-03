n = int(input())

answer = 0
stack =[]
for i in range(n):
    x, y = map(int, input().split())
    
    if len(stack) ==0:
        stack.append(y)

    else:
        
        while len(stack)>0 and stack[-1] > y:
            stack.pop()
            answer+=1
            
            
        if y not in stack:
            stack.append(y)

while stack:
    if stack[-1] > 0:
        answer += 1
    stack.pop()

print(answer)   

    

