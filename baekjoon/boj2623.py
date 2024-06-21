from collections import deque
n, m = map(int, input().split())

link = [0] * (n+1)

g ={}
for _ in range(m):
    row = list(map(int, input().split()))
    if len(row)==2: continue
    for i in range(1, len(row)-1):
        fromm, to = row[i], row[i+1]
        link[to]+=1
        if fromm not in g:
            g[fromm] = [to]
        else:
            g[fromm].append(to)


answer = []  
q = deque([])

for i in range(1, n+1):
    if link[i]==0:
        q.append(i)

while q:
    cur = q.popleft()
    answer.append(cur)
    if cur not in g:
        continue

    for nxt in g[cur]:
        link[nxt]-=1
        if link[nxt] ==0:
            q.append(nxt)



if len(answer) != n:
    print(0)
else:
    for a in answer:
        print(a)