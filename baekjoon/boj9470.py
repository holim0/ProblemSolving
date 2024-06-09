from collections import deque
t = int(input())
num = 1
for _ in range(t):

    k, m, p = map(int,input().split())
    
    dist = [0 for _ in range(m+1)]
    g = {}
    for _ in range(p):
        a, b = map(int, input().split())
        if a not in g:
            g[a] = [b]
        else:
            g[a].append(b)
        dist[b]+=1
        
    
    curOrder = [0 for _ in range(m+1)]

    inRiverInfo ={

    }
    q = deque([])

    for i in range(1, m+1):
        if dist[i] ==0:
            curOrder[i] = 1
            q.append(i)

    while q:
        cur = q.popleft()

        if cur not in g: continue

        for nxt in g[cur]:
            dist[nxt]-=1
            if nxt not in inRiverInfo:
                inRiverInfo[nxt] = (curOrder[cur], 1)
            else:
                curLiverOrder = curOrder[cur]

                inRiverToNxtOrder, cnt = inRiverInfo[nxt]

                if curLiverOrder == inRiverToNxtOrder:
                    inRiverInfo[nxt] = (curLiverOrder, cnt+1)
                
                elif curLiverOrder > inRiverToNxtOrder:
                    inRiverInfo[nxt] = (curLiverOrder, 1)

            if dist[nxt]==0:
                
                inRiverToNxtOrder, cnt = inRiverInfo[nxt]
                if cnt==1:
                    curOrder[nxt] = inRiverToNxtOrder
                elif cnt>1:
                    curOrder[nxt] = inRiverToNxtOrder+1
                q.append(nxt)

    
    print(num, curOrder[m])
    num+=1