from collections import deque
import sys
n = int(input())

q = deque([])

for i in range(0, 10):
    q.append(i)

cnt = -1

while(cnt!=n and q):
    cur = q.popleft()
    cnt+=1
    if cnt == n:
        print(cur)
        sys.exit()
    
    stringCur = str(cur)
    for i in range(0, int(stringCur[-1])):
        nxt = stringCur + str(i)
        q.append(int(nxt))

print(-1)
