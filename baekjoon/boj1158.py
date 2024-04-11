from collections import deque 
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

number = [i for i in range(1, n+1)]

q = deque(number)
answer = []
cnt = 0
while q:

    cnt+=1
    cur = q.popleft()
    if cnt == k:
        answer.append(cur)
        cnt = 0
    else:
        q.append(cur)

answer_s = "<"

for value in answer:
    answer_s+= str(value) + ", "

answer_s = answer_s[:-2]
answer_s +=">"
print(answer_s)