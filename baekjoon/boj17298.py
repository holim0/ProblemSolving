import sys
input = sys.stdin.readline
n = int(input())

number = list(map(int, input().split()))
stack = []
answer= [0 for _ in range(n)]

for i in range(n):
    if len(stack) ==0:
        stack.append((i, number[i]))
    else:
        while stack and stack[-1][1] < number[i]:
            idx, value = stack.pop()
            answer[idx] = number[i]
        
        stack.append((i, number[i]))


while stack:
    idx, value = stack.pop()
    answer[idx] = -1

print(" ".join(str(a) for a in answer))
