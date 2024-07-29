from collections import deque

n, m = map(int, input().split())

g = {}
s, e = 1e10, 0
for _ in range(m):
    a, b, c = map(int, input().split())
    s = min(c, s)
    e = max(c, e)
    if a not in g:
        g[a] = [(b, c)]
    else:
        g[a].append((b, c))
    
    if b not in g:
        g[b] = [(a, c)]
    else:
        g[b].append((a, c))

start, end = map(int, input().split())

answer = 0

def isGo(w):

    q = deque([])

    visit = [False for _ in range(n+1)]

    visit[start] = True

    q.append(start)

    while q:
        cur = q.popleft()
        if cur == end:
            return True
        for nxt, curw in g[cur]:
            if curw>=w and not visit[nxt]:
                visit[nxt] = True
                q.append(nxt)

    return False

while s<=e:
    mid = (s+e)//2

    if(isGo(mid)):
        s= mid+1
        answer = max(answer, mid)
    else:
        e= mid-1

print(answer)

