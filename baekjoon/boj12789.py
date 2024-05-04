from collections import deque
import sys
n = int(input())

number = list(map(int, input().split()))

q = deque(number)
stack = []
curIdx = 1

while q and curIdx<=n:
    first = q.popleft()
    if curIdx != first:
        while stack and stack[-1] == curIdx:
            stack.pop()
            curIdx+=1
            

        if curIdx != first:
            stack.append(first)
        else:
            curIdx+=1
    else:
        curIdx+=1

if len(stack) ==0:
    print("Nice")
    sys.exit()

else:
    while stack:
        if stack[-1] == curIdx:
            stack.pop()
            curIdx+=1
        else:
            print("Sad")
            sys.exit()

print("Nice")

