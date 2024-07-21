n = int(input())

lazer = list(map(int, input().split()))

stack = []

lazerWithIdx =[]
answer =[]
for i in range(len(lazer)):
    cur, idx = lazer[i], i+1

    if len(stack) ==0:
        stack.append((cur, idx))
        answer.append(0)
    else:

        while stack and stack[-1][0] < cur:
            stack.pop()
    

        if stack and stack[-1][0] > cur:
            answer.append(stack[-1][1])
            stack.append((cur, idx))
        else:
            answer.append(0)
            stack.append((cur, idx))
real_answer = " ".join(str(a) for a in answer)

print(real_answer)



