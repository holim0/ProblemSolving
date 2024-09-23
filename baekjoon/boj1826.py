import heapq as hp
import sys
n = int(input())

pos = []

for _ in range(n):
    a, b = map(int, input().split())
    pos.append((a, b))

l, p = map(int, input().split())
pos.append((l, 0))
pos.sort()

q = []

curLocaion = 0
curP = p
i = 0
cnt = 0

while curP < l:
    while i < n and curP>= pos[i][0]:
        hp.heappush(q, -pos[i][1])
        i+=1
    

    if not q:
        print(-1)
        sys.exit()

    curP+= (-hp.heappop(q))
    cnt+=1

print(cnt)

