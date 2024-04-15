import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
brid = list(map(int, input().split()))
start, end = map(int, input().split())

LIMIT = 10000
visited = [False for _ in range(10000)]

q = deque([(start-1, brid[start-1], 0)])

visited[start-1] = True

while q:
    curIdx, value, cnt = q.popleft()

    if curIdx == end-1:
        print(cnt)
        sys.exit()
    
    nxtIdx = curIdx + value
    while nxtIdx < n:
        if not visited[nxtIdx]:
            visited[nxtIdx] = True
            q.append((nxtIdx, brid[nxtIdx], cnt+1))
        nxtIdx += value
    
    nxtIdx = curIdx - value
    while nxtIdx >=0:
        if not visited[nxtIdx]:
            visited[nxtIdx] = True
            q.append((nxtIdx, brid[nxtIdx], cnt+1))
        nxtIdx -= value

    
    

print(-1)