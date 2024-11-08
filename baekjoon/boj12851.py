from collections import deque

n, k = map(int, input().split())


check = [1e10] * 100001


check[n] = 0

q = deque([])
q.append((n, 0))
minTime = 1e10
cnt = 0
while q:
    cur, time = q.popleft()

    if cur==k:
        if minTime>time:
            minTime= time
            cnt = 1
        elif minTime==time:
            cnt+=1
        
        continue

    for a in [1, -1, cur]:
        next = cur+a

        if 0<=next<=100000 and check[next]>=time+1:
            check[next] = time+1
            q.append((next, time+1))

print(minTime)
print(cnt)