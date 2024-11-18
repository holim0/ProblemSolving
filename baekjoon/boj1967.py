import sys
sys.setrecursionlimit(10**5)

n = int(input())
if n==1:
    print(0)
    sys.exit()

leaf = []
dist = [0] * (n+1)
g ={}
linkCnt = [0] * (n+1)
for _ in range(n-1):
    a, b, c = map(int, input().split())
    linkCnt[a]+=1
    linkCnt[b]+=1
    g[a] = g.get(a, [])
    g[a].append((c, b))

    g[b] = g.get(b, [])
    g[b].append((c, a))

for i in range(1, n+1):
    if linkCnt[i]==1:
        leaf.append(i)

for key in g:
    g[key] = sorted(g[key], reverse=True)


maxDist = 0
check = [False] * (n+1)
def find(cur, curDist):
    global maxDist, check

    for d, nxt in g[cur]:
        if not check[nxt]:
            check[nxt] = True
            dist[nxt] = curDist + d
            maxDist = max(maxDist, dist[nxt])
            find(nxt, curDist+d)

def getDist(start):
    global maxDist, check
    check = [False] * (n+1)

    check[start] = True
    maxDist = 0
    find(start, 0)
    
    return maxDist


curDist = getDist(1)

start = -1

for i in range(1, n+1):
    if curDist == dist[i]:
        start = i
        break


answer= getDist(start)
print(answer)