s = input()

stack = []
answer = 0


for i in range(len(s)):
    if s[i] != ")":
        if s[i] == "(":
            stack.append(s[i])
            continue
        if i== len(s)-1:
            stack.append(1)
            continue
        if s[i] != "(":
            if s[i+1] == "(":
                stack.append(int(s[i]))
            else:
                stack.append(1)
    
    else:
        tmpLen = 0
        while stack and stack[-1] !="(":
            curLen = stack.pop()
            tmpLen+=curLen

        stack.pop() 
        mulCnt = stack.pop()
        stack.append(mulCnt*tmpLen)
    
    
    
while stack:
    curLen = stack.pop()
    answer+=curLen

print(answer)

