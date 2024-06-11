from collections import deque
import sys
n, k = map(int, input().split())

number = list(input().split())
sortedNumber = sorted(number)
number = "".join(number)
targetValue = "".join(sortedNumber)
answer = 1e10


check = {}

check[number] = True

q = deque([(number, 0)])

while q:
    cur, cnt = q.popleft()
    
    if cur == targetValue:
        print(cnt)
        sys.exit()
        
    for i in range(n-k+1):
        target = cur[i:i+k]
        nxt = cur[:i] + target[::-1] + cur[i+k:]
        
        if nxt not in check:
            check[nxt] = True
            q.append((nxt, cnt+1))

print(-1)