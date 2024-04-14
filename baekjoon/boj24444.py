from collections import deque
g = {}
n, m, r = map(int, input().split())

for _ in range(m):
    a, b = map(int, input().split())
    
    if a not in g:
        g[a] = [b]
    else:
        g[a].append(b)
    
    if b not in g:
        g[b] = [a]
    else:
        g[b].append(a)

for key in g:
    g[key] = sorted(g[key])



visited = [False for _ in range(n+1)]

visited[r] = True

answer =[0 for _ in range(n+1)]



q = deque([r])


cur_order = 1
answer[r] = cur_order
while q:
    cur = q.popleft()
    
    if cur not in g: continue
    
    for nxt in g[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            q.append(nxt)
            answer[nxt] = cur_order +1
            cur_order +=1

for i in range(1, n+1):
    print(answer[i])





    
