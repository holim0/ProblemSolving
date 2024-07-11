from collections import deque

n = int(input())

value = list(map(int, input().split()))

answer =[]

q = deque([])

for i in range(len(value)):
    q.append((i+1, value[i]))


while q:
    idx, cur = q.popleft()
    answer.append(idx)

    if cur>0:
        while q and cur>1:
            nxt = q.popleft()
            q.append(nxt)
            cur-=1
    else:
        while q and cur<0:
            nxt = q.pop()
            q.appendleft(nxt)
            cur+=1

print(" ".join(str(a) for a in answer))