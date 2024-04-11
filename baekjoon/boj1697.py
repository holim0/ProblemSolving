import sys
from collections import deque

n, k = map(int, input().split())

MAX = 100000

visited = [False for _ in range(MAX+1)]


visited[n] = True

q = deque([(n, 0)])

while q:
    cur, time = q.popleft()

    if cur == k:
        print(time)
        break    
    for nxt in [cur-1, cur+1, 2*cur]:
        if 0<=nxt <= MAX and not visited[nxt] :
            visited[nxt] = True
            q.append((nxt, time+1))