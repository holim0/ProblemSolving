import sys
from collections import deque
import heapq as hp
input = sys.stdin.readline

t = int(input())
answer = 0


for _ in range(t):
    n, k = map(int, input().split())
    tmpTime = list(map(int, input().split()))
    
    time = [0, ]
    time+=tmpTime
    linkCnt = [0 for _ in range(n+1)]
    g = {}
    for _ in range(k):
        fromm, to = map(int, input().split())
        linkCnt[to]+=1
        if fromm not in g:
            g[fromm] = [to]
        else:
            g[fromm].append(to)
    w = int(input())
    q =[]
    for i in range(1, n+1):
        if linkCnt[i] ==0:
            hp.heappush(q, (time[i], i))

    while q:
        buildTime, cur = hp.heappop(q)
       
        if cur==w:
            print(buildTime)
            break

        if cur not in g:
            continue

        for nxt in g[cur]:
            linkCnt[nxt]-=1
            if linkCnt[nxt]==0:
                hp.heappush(q, ((buildTime + time[nxt]), nxt))
    


        


    


