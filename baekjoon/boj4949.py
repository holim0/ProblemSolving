while True:

    
        s = list(input())
        if s[0] == ".": break

        stack = []

        for i in range(len(s)):
            cur = s[i]

            if cur == "(" or cur== "[":
                stack.append(cur)
            
            elif cur == ")":
                if len(stack) >0 and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(cur)
            
            elif cur == "]":
                if len(stack) > 0 and stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(cur)


        
        if len(stack) ==0:
            print("yes")
        else:
            print("no")

    