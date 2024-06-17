import heapq as hp
from collections import deque
n, a, b = map(int, input().split())

INF = 1e10

g = {}

link =[]

for _ in range(n-1):
    fromm, to, d = map(int, input().split())
    if fromm not in g:
        g[fromm] = [(d, to)]
    else:
        g[fromm].append((d, to))
    
    if to not in g:
        g[to] = [(d, fromm)]
    else:
        g[to].append((d, fromm))



def getDist(start):
    global g
    global b
    q = deque([])
    
    check = [False for _ in range(n+1)]

    check[start] = True

    q.append((start, 0, 0))

    while q:
        cur, totalDist, curmax = q.popleft()

        if cur == b:
            print(totalDist-curmax)
            break
    
        for nxtDist, nxt in g[cur]:
            if not check[nxt]:
                check[nxt] = True
                q.append((nxt, totalDist+nxtDist, max(curmax, nxtDist)))

getDist(a)  


    
