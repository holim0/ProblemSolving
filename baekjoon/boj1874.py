target = []

n = int(input())

for _ in range(n):
    cur = int(input())
    target.append(cur)

stack =[]

cur = 1
answer =[]
idx = 0
for i in range(1, n+1):
    stack.append(i)
    answer.append("+")
    
    while stack:
        if stack[-1] == target[idx]:
            stack.pop()
            answer.append("-")
            idx+=1
        else:
            break

if len(stack) ==0:
    for a in answer:
        print(a)
else:
    print("NO")
