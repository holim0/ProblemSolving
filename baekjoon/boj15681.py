import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, r, q = map(int, input().split())

g = {} 
linkCnt = [0] * (n+1)
for _ in range(n-1):
    a, b = map(int, input().split())
    
    g[a] = g.get(a, [])
    g[a].append(b)

    g[b] = g.get(b, [])
    g[b].append(a)
    linkCnt[a]+=1
    linkCnt[b]+=1

subCnt = [1] * (n+1)
visit = [False] * (n+1)


def getDepth(cur):
    global visit

    if linkCnt[cur] ==1 and cur != r:
        return 1
    

    for nxt in g[cur]:
        if not visit[nxt]:
            visit[nxt] = True
            subCnt[cur]+=getDepth(nxt)

    return subCnt[cur]

visit[r] = True

getDepth(r)

for _ in range(q):
    u = int(input())
    print(subCnt[u])