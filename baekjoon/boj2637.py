from collections import deque

n = int(input())
m = int(input())

rel = []
link = [0 for _ in range(n+1)]

g = {}

for _ in range(m):
    x, y, k = map(int, input().split())
    link[x]+=1

    if y not in g:
        g[y] = [(x, k)]
    else:
        g[y].append((x, k))

cntInfo = [[0] * (n+1) for _ in range(n+1)]

base =[]

for i in range(1, n+1):
    if link[i] ==0:
        base.append(i)
        cntInfo[i][i] = 1
q = deque(base)

while q:
    cur = q.popleft()

    if cur not in g: continue

    for nxt, needCnt in g[cur]:
        link[nxt]-=1
        for b in base:
            cntInfo[nxt][b]+=cntInfo[cur][b] * needCnt
        if link[nxt]==0:
            q.append(nxt)

answer = []
for b in base:
    answer.append((b, cntInfo[n][b]))

answer.sort()

for a, b in answer:
    print(a, b)

