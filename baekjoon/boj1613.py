from collections import deque

n, k = map(int, input().split())

order =[]

link = [0 for _ in range(n+1)]

g = {}

for _ in range(k):
    a, b = map(int, input().split())
    if a not in g:
        g[a] = [b]
    else:
        g[a].append(b)
    link[b]+=1

q = deque([])

for i in range(1, n+1):
    if link[i] == 0:
        q.append(i)

orderInfo = [0 for _ in range(n+1)]

while q:
    cur = q.popleft()
    curOrder = orderInfo[cur]

    if cur not in g: continue
    for nxt in g[cur]:
        link[nxt]-=1
        if link[nxt]==0:
            q.append(nxt)
            orderInfo[nxt] = curOrder+1


s = int(input())
isLink = [[False for _ in range(n+1)] for _ in range(n+1)]

def linking(start):
    global g
    global n
    q = deque([])
    check = [False for _ in range(n+1)]

    check[start] = True
    q.append(start)

    while q:
        cur = q.popleft()
        if cur not in g: continue

        for nxt in g[cur]:
            if not check[nxt]:
                check[nxt] = True
                isLink[start][nxt] = True
                q.append(nxt)

for i in range(1, n+1):
    linking(i)


for _ in range(s):
    a, b = map(int, input().split())
    if not isLink[a][b] and not isLink[b][a]:
        print(0)
        continue

    if orderInfo[a] == orderInfo[b]:
        print(0)
    elif orderInfo[a] < orderInfo[b]:
        print(-1)
    else:
        print(1)




